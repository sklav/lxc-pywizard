###########################################
#FUNCTIONS#
def lxc_config_file():

    "This generates a generic lxc config for containers"
    config_file = open('/var/lib/lxc/'+args.fqdn+'/config','a')
    print >>config_file, "lxc.utsname = ", args.fqdn
    print >>config_file, "lxc.network.type = veth"
    print >>config_file, "lxc.network.flags = up"
    print >>config_file, "lxc.network.link = br0"
    print >>config_file, "#lxc.network.hwaddr = xx:xx:xx:xx:xx:xx"
    print >>config_file, "#lxc.network.ipv4 = 192.168.1.x"
    print >>config_file, "#lxc.network.veth.pair = veth-"+args.fqdn
    print >>config_file, "lxc.tty = 1"
    print >>config_file, "lxc.pts = 1024"
    print >>config_file, "#Memory"
    print >>config_file, "lxc.cgroup.memory.limit_in_bytes = " +args.ram+"M"
    print >>config_file, "lxc.cgroup.memory.memsw.limit_in_bytes = "+args.ram+"M"
    print >>config_file, "lxc.cgroup.blkio.weight = 100"
    print >>config_file, "# Lxc isolation"
    print >>config_file, "#lxc.cap.drop = sys_module mac_admin mac_override sys_time sys_admin"
    print >>config_file, "lxc.rootfs = /var/lib/lxc/"+args.fqdn+"/rootfs"
    print >>config_file, "lxc.cgroup.devices.deny = a"
    print >>config_file, "# /dev/null and zero"
    print >>config_file, "lxc.cgroup.devices.allow = c 1:3 rwm"
    print >>config_file, "lxc.cgroup.devices.allow = c 1:5 rwm"
    print >>config_file, "# consoles"
    print >>config_file, "lxc.cgroup.devices.allow = c 5:1 rwm"
    print >>config_file, "lxc.cgroup.devices.allow = c 5:0 rwm"
    print >>config_file, "lxc.cgroup.devices.allow = c 4:0 rwm"
    print >>config_file, "lxc.cgroup.devices.allow = c 4:1 rwm"
    print >>config_file, "# /dev/{,u}random"
    print >>config_file, "lxc.cgroup.devices.allow = c 1:9 rwm"
    print >>config_file, "lxc.cgroup.devices.allow = c 1:8 rwm"
    print >>config_file, "lxc.cgroup.devices.allow = c 136:* rwm"
    print >>config_file, "lxc.cgroup.devices.allow = c 5:2 rwm"
    print >>config_file, "# rtc"
    print >>config_file, "lxc.cgroup.devices.allow = c 254:0 rwm"
    print >>config_file, "# mounts point"
    print >>config_file, "lxc.mount.entry=proc /var/lib/lxc/"+args.fqdn+"/rootfs/proc proc nodev,noexec,nosuid 0 0"
    print >>config_file, "lxc.mount.entry=devpts /var/lib/lxc/"+args.fqdn+"/rootfs/dev/pts devpts defaults 0 0"
    print >>config_file, "lxc.mount.entry=sysfs /var/lib/lxc/"+args.fqdn+"/rootfs/sys sysfs defaults  0 0"
    print >>config_file, "lxc.mount.entry=/etc/hostname /var/lib/lxc/"+args.fqdn+"/rootfs/etc/host none ro,bind 0 0"
    config_file.close()
