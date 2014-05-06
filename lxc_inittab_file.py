inittab = """
    id:3:initdefault:
    si::sysinit:/etc/init.d/rcS
    l0:0:wait:/etc/init.d/rc 0
    l1:1:wait:/etc/init.d/rc 1
    l2:2:wait:/etc/init.d/rc 2
    l3:3:wait:/etc/init.d/rc 3
    l4:4:wait:/etc/init.d/rc 4
    l5:5:wait:/etc/init.d/rc 5
    l6:6:wait:/etc/init.d/rc 6
    # Normally not reached, but fallthrough in case of emergency.
    z6:6:respawn:/sbin/sulogin
    1:2345:respawn:/sbin/getty 38400 console
    c1:12345:respawn:/sbin/getty 38400 tty1 linux
    #c2:12345:respawn:/sbin/getty 38400 tty2 linux
    #c3:12345:respawn:/sbin/getty 38400 tty3 linux
    #c4:12345:respawn:/sbin/getty 38400 tty4 linux
    """

def lxc_inittab_file(fqdn):
    "This generates an inittab config for lxc containers"
    filename = '/var/lib/lxc/{fqdn}/rootfs/etc/inittab'.format(fqdn=fqdn)
    with open(filename, 'a') as f:
        f.write(inittab.format(fqdn=fqdn))

#def lxc_inittab_file(fqdn):
#    "This generates a generic lxc config for containers"
#    inittab_file = open('/var/lib/lxc/'+args.fqdn+'/rootfs/etc/inittab','w')
#    print >>inittab_file, "id:3:initdefault:"
#    print >>inittab_file, "si::sysinit:/etc/init.d/rcS"
#    print >>inittab_file, "l0:0:wait:/etc/init.d/rc 0"
#    print >>inittab_file, "l1:1:wait:/etc/init.d/rc 1"
#    print >>inittab_file, "l2:2:wait:/etc/init.d/rc 2"
#    print >>inittab_file, "l3:3:wait:/etc/init.d/rc 3"
#    print >>inittab_file, "l4:4:wait:/etc/init.d/rc 4"
#    print >>inittab_file, "l5:5:wait:/etc/init.d/rc 5"
#    print >>inittab_file, "l6:6:wait:/etc/init.d/rc 6"
#    print >>inittab_file, "# Normally not reached, but fallthrough in case of emergency."
#    print >>inittab_file, "z6:6:respawn:/sbin/sulogin"
#    print >>inittab_file, "1:2345:respawn:/sbin/getty 38400 console"
#    print >>inittab_file, "c1:12345:respawn:/sbin/getty 38400 tty1 linux"
#    print >>inittab_file, "#c2:12345:respawn:/sbin/getty 38400 tty2 linux"
#    print >>inittab_file, "#c3:12345:respawn:/sbin/getty 38400 tty3 linux"
#    print >>inittab_file, "#c4:12345:respawn:/sbin/getty 38400 tty4 linux"
#    inittab_file.close()
