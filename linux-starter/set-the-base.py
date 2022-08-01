
from struct import pack
import subprocess


# choose distro

input_distro = input("Choose distro family: \n1. Debian \n2. Arch \n3. RedHat \n")


if input_distro == "1":

    print("Debian")
    update = input("Update? (y/n) ")
    nala = input("install Nala? (y/n) ")
    dev_pack = input("install devel packages? (y/n) ")

elif input_distro == "2":

    update = input("Update? (y/n) ")
    yay = input("Install yay? (y/n) ")
    dev_pack = input("Install devel packages? (y/n) ")

    # update arch
    if update == "y":
        subprocess.call(["sudo", "pacman", "-Syu"])
        print("Arch updated")
    if dev_pack == "y":
        subprocess.call(["sudo", "pacman", "-S", "base-devel", "git", "vim", "tmux", "neovim"])
        print("Base packages installed")
    if yay == "y":
        subprocess.call(["git", "clone", "https://aur.archlinux.org/yay.git"])
        subprocess.call(["cd", "yay"])
        subprocess.call(["makepkg", "-si"])
        subprocess.call(["cd", ".."])
        print("yay installed")

elif input_distro == "3":

    update = input("Update? (y/n) ")
    rpm = input("Enable RPM Fusion repo? (y/n) ")
    dev_pack = input("Install devel packages? (y/n) ")

else:
    print("Invalid input")
