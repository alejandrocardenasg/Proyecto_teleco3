# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.define :balancer do |balancer|
    balancer.vm.box = "bento/centos-7.9"
    balancer.vm.network :private_network, ip: "192.168.80.2"
    balancer.vm.hostname = "balancer"
  end
  
  config.vm.define :master do |master|
    master.vm.box = "bento/centos-7.9"
    master.vm.network :private_network, ip: "192.168.80.3"
    master.vm.hostname = "master"
  end

  config.vm.define :slave1 do |slave1|
    slave1.vm.box = "bento/centos-7.9"
    slave1.vm.network :private_network, ip: "192.168.80.4"
    slave1.vm.hostname = "slave1"
  end

  config.vm.define :slave2 do |slave2|
    slave2.vm.box = "bento/centos-7.9"
    slave2.vm.network :private_network, ip: "192.168.80.5"
    slave2.vm.hostname = "slave2"
  end

end
