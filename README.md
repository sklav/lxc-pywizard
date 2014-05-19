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
- added option so container has his hostname defined based on fqdn on creation
- you can easily add packages you want to your initial cache in the script
- it creates a custom inittab file
- it creates a config file for your lxc container
- Added option to define filesystem of choice example ext3/ext4/xfs etc..
- Added some basic error checking to lxc-pywizard as promised.
- cache directory layout more versatile to arch changes and distro releases can now define based on release and arch example squeeze/wheezy/amd64/i386
- Version information has been added.
- Better Help messages added.
- Some sane defaults have been added to ram and fs options which now default to  ram=512M and fs=2G
- eliminated unnecessary hardcoded paths in script
- made lvm optional --lvm=yes Default or --lvm=no option was there but not usable
- Added error check if the cache directory is missing or not created when using the -c option

Future Additions (wish list)
============================
- possibility to add profiles which can create finalized containers example web server etc...
- make example usages in Readme more clear especially related to the features present and fix formating of readme
- possibility to use ssh key to connect to container
- add some serious error checking to lxc-pywizard
- add option to configure static ip from command line on creation
- possibility to make the scrip work with febootstrap, which would in theory add fedora and centos/rhel support to the script

Example Usage
=============
create a cache for containers to use.
-------------------------------------
lxc-pywizard --create | -cr

Update the cache
----------------
lxc-pywizard -u or --update

launch a container by defining some basics
------------------------------------------
lxc-pywizard --container | -cont --fqdn=test4.sklav --ram=512 --size=4G --fs=ext3

Create a container using defaults and no lvm partition
------------------------------------------------------
lxc-pywizard --container | -cont --fqdn=test4.sklav --lvm=no

Display version information
---------------------------
lxc-pywizard --version | -v | -V
