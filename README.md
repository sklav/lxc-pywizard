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
- you can easily add packages you want to you initial cache in the script
- you can easily select what filesystem you want example ext4 and company

Future Additions (wish list)
============================
- possibility to add profiles which can create finalized containers example web server etc...
- possibility to use ssh key to connect to container
- possibility to specify filesystem type on the fly, hard coded to ext4 at the moment but can be easily modified for your needs.
