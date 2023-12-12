#!/usr/bin/env bash 

# if any command fails exit
set -e

# A list of packges to install based on the linux distro
pk=("python" "python-pip" "pipx")
pkg=("python" "python-pip" "python-pipx")
pkgs=("python3" "python3-pip" "pipx")

# Varriable for distro ID 
fedora_ID=$(grep ID=fedora /etc/os-release)
Arch_ID=$(grep ID=arch /etc/os-release)
deb_ID=$(grep ID=debian /etc/os-release)


# if the Distro ID equals ID=fedora then install the fedora array
if [ "$fedora_ID" == ID=fedora  ]; then 
        sudo dnf install "${pk[@]}"
        exit 0


fi 

# if the distro ID equals ID=arch then install the Arch array
if [ "$Arch_ID" == ID=arch ]; then
        sudo pacman -S "${pkg[@]}"
        exit 0
fi

# if the distro ID equals ID=debian then install array
if [ "$deb_ID" == ID=debian ]; then 
        sudo apt-get install "${pkgs[@]}"
        exit 0

else
        echo "Error: Your Distro is not found"
        exit 1


fi 

