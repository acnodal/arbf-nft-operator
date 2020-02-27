SVC
=========

This role watches the kubeapi for services updates and updates firewall entries 
for LoadBalanced Services

Requirements
------------

This role does not have any specific ansible requirements however the base operator container has been
updated to include ssh so targets outside of the cluster can be configured

Role Variables
--------------

As the role variables found in the cr for nft and variables found in the metallb configmap

Dependencies
------------

This role is designed to work in conjunction with the other operator role nft

Example Playbook
----------------

The role is run by the ansible operator

License
-------

Apache 2

Author Information
------------------

Adam Dunstan adam@acnodal.com
