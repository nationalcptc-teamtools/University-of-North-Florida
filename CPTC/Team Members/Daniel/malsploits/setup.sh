    sudo apt update -y
    sudo apt install -y git golang-go debootstrap rsync gpg squashfs-tools
    git clone https://github.com/lxc/distrobuilder
    cd distrobuilder
    make
    cd ..
    wget https://raw.githubusercontent.com/lxc/lxc-ci/master/images/alpine.yaml
    sudo $HOME/go/bin/distrobuilder build-incus alpine.yaml --type=split -o image.release=3.18
    cd ..