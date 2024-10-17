output "name" {
  value = virtualbox_server.VM_without_image[0].name
}

output "basedir" {
  value = virtualbox_server.VM_without_image[0].basedir
}

output "cpus" {
 value = virtualbox_server.VM_without_image[0].cpus
}

output "memory" {
  value = virtualbox_server.VM_without_image[0].memory
}

output "status" {
  value = virtualbox_server.VM_without_image[0].status
}