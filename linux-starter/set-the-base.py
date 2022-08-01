
from struct import pack
import subprocess


# choose distro

input_distro = input("Choose distro family: \n1. Debian \n2. Arch \n3. RedHat \n")


if input_distro == "1":

    print("Debian")
    update = input("Upgrade? (y/n) ")
    nala = input("Install Nala? (y/n) ")
    dev_pack = input("install devel packages? (y/n) ")

    if nala == "y":
        subprocess.call(["sudo", "apt-get", "update"])
        subprocess.call(["echo", '"deb https://deb.volian.org/volian/ scar main"', "|", "sudo", "tee", "/etc/apt/sources.list.d/volian-archive-scar-unstable.list"])
        subprocess.call(["wget", "-qO", "-", "https://deb.volian.org/volian/scar.key", "|", "sudo", "tee", "/etc/apt/trusted.gpg.d/volian-archive-scar-unstable.gpg", ">", "/dev/null"])
        subprocess.call(["sudo", "apt-get", "update"])
        subprocess.call(["sudo", "apt-get", "install", "nala", "-y"])

    if update == "y":
        if nala == "y":
            subprocess.call(["sudo", "nala", "upgrade", "-y"])
        else:
            subprocess.call(["sudo", "apt", "upgrade", "-y"])
    
    if dev_pack == "y":
        if nala == "y":
            subprocess.call(["sudo", "nala", "install", "build-essential", "git", "vim", "neovim", "tmux", "-y"])
        else:
            subprocess.call(["sudo", "apt", "install", "build-essential", "git", "vim", "neovim", "tmux", "-y"])
    
elif input_distro == "2":

    update = input("Update? (y/n) ")
    yay = input("Install yay? (y/n) ")
    dev_pack = input("Install devel packages? (y/n) ")

    # update arch
    if update == "y":
        subprocess.call(["sudo", "pacman", "-Syu"])
        print("Arch updated")
    if dev_pack == "y":
        subprocess.call(["sudo", "pacman", "-Sy", "base-devel", "git", "vim", "tmux", "neovim"])
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
