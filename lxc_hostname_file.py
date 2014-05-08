###########################################
def lxc_hostname_file(fqdn):
    "This add the hostname to the container"
    filename = '/var/lib/lxc/{fqdn}/rootfs/etc/hostname'.format(fqdn=fqdn)
    with open(filename, 'w') as f:
        f.write(lxc_hostname.format(fqdn=fqdn))

lxc_hostname = """{fqdn}"""
