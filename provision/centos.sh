#!/bin/bash

# Update packages
#sudo yum update -y

sudo yum install -y epel-release

# Install development tools
sudo yum install -y git gc

[ -e /vagrant/provision/install_python27.sh ] && /vagrant/provision/install_python27.sh
