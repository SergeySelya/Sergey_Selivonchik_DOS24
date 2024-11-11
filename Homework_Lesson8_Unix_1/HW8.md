## Задание:
RSYNC либо RCLONE
1. сделать синхронизацию с облачных хранилищем (S3, GCP Storage) c указанием NAME_SURNAME в имени папки
2. FDISK + LVM
3. *синхронизировать между собой две папки на двух разных вм-ках
4. *синхронизировать папки на двух вмках и ещё на GCP
____________________________________________
ссылки на GCP bucket
https://console.cloud.google.com/storage/browser/tms_123121419djscj_test
gs://tms_123121419djscj_test
## Решение

1. Настроим rsync на VM ubuntu.24.10:

```bash
# устанавливаем rsync
sudo apt-get install rsync  

# создаем конфигурационный файл /etc/rsyncd.conf
sudo nano /etc/rsyncd.conf
# записываем его, подставляя ip своей VM
uid = swift
gid = swift
log file = /var/log/rsyncd.log
pid file = /var/run/rsyncd.pid
address = 192.168.100.20
[account]
max connections = 2
path = /srv/node/
read only = false
lock file = /var/lock/account.lock
[container]
max connections = 2
path = /srv/node/
read only = false
lock file = /var/lock/container.lock
[object]
max connections = 2
path = /srv/node/
read only = false
lock file = /var/lock/object.lock

# запускаем rsync и ставим ему статус enable
sudo service rsync start
sudo systemctl enable rsync 
```