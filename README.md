# Send HID data to device by pyusb.

## Environment prepare for Raspberry Pi

<br/>

### Make an install disk by macOS
##### Download Raspbian from <a href="https://www.raspberrypi.org/downloads/raspbian/">https://www.raspberrypi.org/downloads/raspbian/</a>
##### Find SD card disk
    $ diskutil list
##### Format disk
    $ diskutil eraseDisk FAT32 RPI [Micro SD mount location ex. /dev/disk2]
##### Unmount disk
    $ diskutil unmountDisk [Micro SD mount location]
##### Write Raspbian to disk
    // This step will spend some time.
    // Dont Interrupt and wait for "copied" or "transferred" message.<br/>
    $ sudo dd bs=1m if=[Raspbian image path] of=[Micro SD mount location]
##### Unmount disk again
    $diskutil unmount [Micro SD mount location]

<br/><br/>

### Configure Raspberry Pi
##### Login to Pi ( default user/password : pi/raspberry )
##### Change password
    $ sudo passwd [username]
##### Enable SSH
    $ sudo raspi-config
    // Then select "Advance Options" -> "SSH"
##### Add new user
    $ sudo adduser [username]
##### Add user to sudo
    $ sudo usermod -a -G sudo [username]
##### Set static eth0 ip
    $ cd /etc/network/interfaces.d
    $ sudo nano eth0
##### Input following setting to eth0 and save changed:
    auto eth0
    iface eth0 inet static
    address 192.168.2.11
    netmask 255.255.255.0
    gateway 192.168.2.254
##### Now can connect Pi by cable line from Mac.
    $ ssh [username]@192.168.2.11

<br/><br/>

### Install Python 2.7
    $ sudo apt-get update<br/>
    $ sudo apt-get install build-essential checkinstall<br/>
    $ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
    $ cd /usr/src<br/>
    $ sudo wget https://www.python.org/ftp/python/2.7.14/Python-2.7.14.tgz<br/>
    $ sudo tar xzf Python-2.7.14.tgz<br/>
    $ cd Python-2.7.14<br/>
    $ sudo ./configure --enable-optimizations<br/>
    $ sudo make altinstall<br/>
    $ python2.7 -V


### Install pip
    $ sudo apt-get update && sudo apt-get -y upgrade
    $ sudo apt-get install python-pip
    $ pip -V


### Install libusb
    $ sudo apt-get install libusb-1.0-0-dev


### Install Python usb library
    $ sudo pip install pyusb
    $ sudo pip install libusb1

### Run uat.py
    $ sudo -S python path-to/usb-automation-test/uat.py
