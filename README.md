lxc-pywizard
============

python wrapper script to launch lxc container

Information
============
- This is a Work in progress so i take no responsibility if your system(s) break
- At the moment you can create a cache and update it
- you can launch debian Squeeze and Wheezy containers and they work ;)
- You can select the arch you want example 32-bit or 64-bit
- It creates containers using lvm to isolate your containers on their own partitions
- you can easily add packages you want to your initial cache in the script
- Added option to define filesystem of choice example ext3/ext4/xfs etc..

Future Additions (wish list)
============================
- possibility to add profiles which can create finalized containers example web server etc...
- possibility to use ssh key to connect to container
- add some serious error checking to lxc-pywizard
- add option so container has his hostname defined based on fqdn
- add option to configure static ip from command line

Example Usage
=============
create a cache for containers to use.
lxc-pywizard --create

Update the cache
lxc-pywizard -u or --update

launch a container by defining some basics
./lxc-pywizard -cont --fqdn=test4.sklav --ram=512 --size=4G --fs=ext3
