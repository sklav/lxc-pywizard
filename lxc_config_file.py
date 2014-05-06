###########################################
def lxc_config_file(fqdn, ram):
    "This generates a generic lxc config for containers"
    filename = '/var/lib/lxc/{fqdn}/config'.format(fqdn=fqdn)
    with open(filename, 'a') as f:
        f.write(lxc_config.format(fqdn=fqdn, ram=ram))

lxc_config = """
    lxc.utsname = {fqdn}
    lxc.network.type = veth
    lxc.network.flags = up
    lxc.network.link = br0
    #lxc.network.hwaddr = xx:xx:xx:xx:xx:xx
    #lxc.network.ipv4 = 192.168.1.x
    #lxc.network.veth.pair = veth-{fqdn}
    lxc.tty = 1
    lxc.pts = 1024
    #Memory
    lxc.cgroup.memory.limit_in_bytes = {ram}M
    lxc.cgroup.memory.memsw.limit_in_bytes = {ram}M
    lxc.cgroup.blkio.weight = 100
    # Lxc isolation
    #lxc.cap.drop = sys_module mac_admin mac_override sys_time sys_admin
    lxc.rootfs = /var/lib/lxc/{fqdn}/rootfs
    lxc.cgroup.devices.deny = a
    # /dev/null and zero
    lxc.cgroup.devices.allow = c 1:3 rwm
    lxc.cgroup.devices.allow = c 1:5 rwm
    # consoles
    lxc.cgroup.devices.allow = c 5:1 rwm
    lxc.cgroup.devices.allow = c 5:0 rwm
    lxc.cgroup.devices.allow = c 4:0 rwm
    lxc.cgroup.devices.allow = c 4:1 rwm
    # /dev/urandom
    lxc.cgroup.devices.allow = c 1:9 rwm
    lxc.cgroup.devices.allow = c 1:8 rwm
    lxc.cgroup.devices.allow = c 136:* rwm
    lxc.cgroup.devices.allow = c 5:2 rwm
    # rtc
    lxc.cgroup.devices.allow = c 254:0 rwm
    # mounts point
    lxc.mount.entry=proc /var/lib/lxc/{fqdn}/rootfs/proc proc nodev,noexec,nosuid 0 0
    lxc.mount.entry=devpts /var/lib/lxc/{fqdn}/rootfs/dev/pts devpts defaults 0 0
    lxc.mount.entry=sysfs /var/lib/lxc/{fqdn}/rootfs/sys sysfs defaults  0 0
    lxc.mount.entry=/etc/hostname /var/lib/lxc/{fqdn}/rootfs/etc/host none ro,bind 0 0
    """
