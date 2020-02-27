NFT
=========

This role watches the Custom Resource and provides the initial configuration for the Linux Router.
Its reconcilaton also provide garbage collection for the svc role 

Requirements
------------

This role does not have any specific ansible requirements however the base operator container has been
updated to include ssh so targets outside of the cluster can be configured

Role Variables
--------------

Role variables are contained in the cr.yml.  It also uses variable found in the metallb configmap

Dependencies
------------

This role is designed to work in conjunction with the other operator role svc.

Example Playbook
----------------

The role is run by the ansible operator

License
-------

Apache 2

Author Information
------------------

Adam Dunstan  adam@acnodal.com
