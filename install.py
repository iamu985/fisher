import distro
import os
from time import sleep
from python.tools import utility as util


def install_npm():
    if distro.id() == "ubuntu":
        os.system("sudo apt-get install npm")
    elif distro.id() == "debian":
        os.system("sudo apt-get install npm")
    elif distro.id() == "fedora":
        os.system("sudo dnf install npm")
    elif distro.id() == "arch":
        os.system("sudo pacman -S npm")
    elif distro.id() == "centos":
        os.system("sudo yum install npm")
    elif distro.id() == "gentoo":
        os.system("sudo emerge -av npm")
    elif distro.id() == "sabayon":
        os.system("sudo eix-install npm")
    elif distro.id() == "rhel":
        os.system("sudo yum install npm")
    
    elif distro.id() == "opensuse":
        os.system("sudo zypper install npm")
    elif distro.id() == "sles":
        os.system("sudo zypper install npm")
    elif distro.id() == "linuxmint":
        os.system("sudo apt-get install npm")
    elif distro.id() == "garuda":
        os.system("sudo pacman - S npm")

def install_mpv():
    if distro.id() == "ubuntu":
        os.system("sudo apt-get install mpv")
    elif distro.id() == "debian":
        os.system("sudo apt-get install mpv")
    elif distro.id() == "fedora":
        os.system("sudo dnf install mpv")
    elif distro.id() == "arch":
        os.system("sudo pacman -S mpv")
    elif distro.id() == "centos":
        os.system("sudo yum install mpv")
    elif distro.id() == "gentoo":
        os.system("sudo emerge -av mpv")
    elif distro.id() == "sabayon":
        os.system("sudo eix-install mpv")
    elif distro.id() == "rhel":
        os.system("sudo yum install mpv")
    
    elif distro.id() == "opensuse":
        os.system("sudo zypper install mpv")
    elif distro.id() == "sles":
        os.system("sudo zypper install mpv")
    elif distro.id() == "linuxmint":
        os.system("sudo apt-get install mpv")
    elif distro.id() == "garuda":
        os.system("sudo pacman - S mpv")

def check_dependencies():
    #check of npm is installed
    if os.system("which npm") != 0:
        install_npm()
    # installing peerflix
    util.clrscr()
    print("Installing peerflix...")
    os.system("npm install -g peerflix")
    print('peerflix installed...')
    util.clrscr()

    # check if mpv is installed
    if os.system("which mpv") != 0:
        install_mpv()
        print('mpv installed...')

if __name__ == '__main__':
    check_dependencies()
