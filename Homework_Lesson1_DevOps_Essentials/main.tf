
resource "virtualbox_server" "VM_without_image" {
    count     = 1
    name      = format("VM_without_image-%02d", count.index + 1)
    basedir = format("VM_without_image-%02d", count.index + 1)
    cpus      = 1
    memory    = 1000
    status = "poweroff"
    os_id = "Ubuntu"
    image = "/Users/selivonchik/Downloads/ubuntu-24.04.1-live-server-arm64.iso"

    network_adapter {
    type           = "hostonly"
    host_interface = "vboxnet1"
  }
}
