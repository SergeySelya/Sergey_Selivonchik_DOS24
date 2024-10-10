terraform {
  required_providers {
    virtualbox = {
      source = "daria-barsukova/virtualbox"
      version = "0.0.2"
    }
  }
}

provider "virtualbox" {
    # Define a VirtualBox server resource for creating VMs with network configurations
    resource "virtualbox_server" "VM_network" {
        count   = 0
        name    = format("VM_network-%02d", count.index + 1)  # Name of the VM
        basedir = format("VM_network-%02d", count.index + 1)  # Base directory for VM files
        cpus    = 3                                           # Number of CPUs for the VM
        memory  = 500                                         # Amount of memory in MB for the VM

        # Network adapter configurations
        network_adapter {
            network_mode = "nat"                                # NAT mode for network adapter
            port_forwarding {
            name      = "rule1"
            hostip    = ""                                    # Host IP address for port forwarding
            hostport  = "80"                                  # Host port for port forwarding
            guestip   = ""                                    # Guest IP address for port forwarding
            guestport = "63222"                               # Guest port for port forwarding
            }
        }
        network_adapter {
            network_mode    = "nat"                             # NAT mode for network adapter
            nic_type        = "82540EM"                         # Type of network interface controller
            cable_connected = true                              # Whether the cable is connected
        }
        network_adapter {
            network_mode = "hostonly"                          # Host-only mode for network adapter
        }
        network_adapter {
            network_mode = "bridged"                            # Bridged mode for network adapter
            nic_type     = "virtio"                             # Type of network interface controller
        }

        status = "poweroff"                                   # Initial status of the VM
}
}