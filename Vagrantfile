# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|


  #
  # Centos
  #

  config.vm.define "centos-6.5" do |v|
    v.vm.box = "chef/centos-6.5"
    v.vm.box_url = "https://vagrantcloud.com/chef/centos-6.5"
    v.vm.hostname = "boundary-plugin-dev-centos-6-5"
    v.vm.provision "shell", :path => "provision/centos.sh"
    v.vm.post_up_message = "TO LOGIN: vagrant ssh centos-6.5"
  end

  config.vm.define "centos-7.0" do |v|
    v.vm.box = "chef/centos-7.0"
    v.vm.box_url = "https://vagrantcloud.com/chef/centos-7.0"
    v.vm.hostname = "boundary-plugin-dev-centos-7-0"
    v.vm.provision "shell", :path => "provision/centos.sh"
    v.vm.post_up_message = "TO LOGIN: vagrant ssh centos-7.0"
  end

  #
  # Ubuntu
  #
  config.vm.define "ubuntu-12.04" do |v|
    v.vm.box = "hashicorp/precise64"
    v.vm.hostname = "ubuntu-12.04"
    v.vm.provision "shell", :path => "provision/ubuntu.sh"
    v.vm.post_up_message = "Run vagrant ssh ubuntu-12.04 to login"
  end

  config.vm.define "ubuntu-14.04" do |v|
    v.vm.box = "ubuntu/trusty64"
    v.vm.hostname = "ubuntu-14.04"
    v.vm.provision "shell", :path => "provision/ubuntu.sh"
    v.vm.post_up_message = "Run vagrant ssh ubuntu-14.04 to login"
  end

end
