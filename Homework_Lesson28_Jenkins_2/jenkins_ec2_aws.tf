
provider "aws" {
  region     = "us-east-1"
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
}


resource "aws_security_group" "jenkins_sg" {
  name        = "jenkins_security_group_1"
  description = "Allow inbound traffic on port 8080 for Jenkins"
 
  # Разрешаем входящие соединения на порт 22 (SSH) для всех источников
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Разрешить доступ с любых IP
  }

  ingress {
    from_port   = 8080
    to_port     = 8080
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "jenkins_instance" {
  ami           = "ami-04b4f1a9cf54c11d0"  # Используем найденный AMI ID
  instance_type = "t2.medium"                # Укажите размер экземпляра
  key_name = "key"           # Укажите ваш SSH ключ для доступа

  security_groups = [aws_security_group.jenkins_sg.name]

  # Скрипт для автоматической установки и настройки
  user_data = <<-EOF
              #!/bin/bash
              # Устанавливаем Git
              apt-get update -y
              apt-get install -y git curl


              # Клонируем репозиторий
              git clone https://github.com/deng4/jenkins.git
              cd jenkins

              # Устанавливаем Docker
              curl -fsSL https://get.docker.com -o get-docker.sh
              chmod +x ./get-docker.sh
              ./get-docker.sh

              # Добавляем пользователя ubuntu в группу docker для доступа к сокету Docker
              usermod -aG docker ubuntu
              

              # Устанавливаем необходимую зависимость
              apt-get install -y uidmap
              sudo apt install -y docker-rootless-extras

              # Настройка Docker в режиме rootless
              dockerd-rootless-setuptool.sh install
              

              # Устанавливаем Docker Compose и запускаем контейнер
              curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
              chmod +x /usr/local/bin/docker-compose

              newgrp docker

              docker-compose up -d
              EOF
  connection {
    type        = "ssh"
    user        = "ubuntu"  # Default user for AWS Ubuntu AMIs
    host        = self.public_ip
    private_key = file("key.pem")
  }
  provisioner "remote-exec" {
    inline = [
      "echo 'Waiting for setup to finish...'",
      "until docker ps; do echo 'Waiting for Docker to be ready...'; sleep 7; done",
      "echo 'Docker is ready, continuing...'"
    ]
  }

  tags = {
    Name = "Jenkins"
  }

}

output "instance_public_ip" {
  value = aws_instance.jenkins_instance.public_ip
}
