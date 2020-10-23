RHEL 8 CIS
================

[![Build Status](https://gitlab.com/mindpointgroup/lockdown-enterprise/rhel-8-cis/badges/master/pipeline.svg)](https://gitlab.com/mindpointgroup/lockdown-enterprise/rhel-8-cis/commits/master)


Configure RHEL/Centos 8 machine to be [CIS](https://www.cisecurity.org/cis-benchmarks/) compliant. Level 1 and 2 findings will be corrected by default.

This role **will make changes to the system** that could break things. This is not an auditing tool but rather a remediation tool to be used after an audit has been conducted.

Based on [CIS RedHat Enterprise Linux 8 Benchmark v2.1.1 - 01-31-2017 ](https://community.cisecurity.org/collab/public/index.php).


Requirements
------------

You should carefully read through the tasks to make sure these changes will not break your systems before running this playbook.
If you want to do a dry run without changing anything, set the below sections (rhel8cis_section1-6) to false. 

Role Variables
--------------
There are many role variables defined in defaults/main.yml. This list shows the most important.

**rhel8cis_notauto**: Run CIS checks that we typically do NOT want to automate due to the high probability of breaking the system (Default: false)

**rhel8cis_section1**: CIS - General Settings (Section 1) (Default: true)

**rhel8cis_section2**: CIS - Services settings (Section 2) (Default: true)

**rhel8cis_section3**: CIS - Network settings (Section 3) (Default: true)

**rhel8cis_section4**: CIS - Logging and Auditing settings (Section 4) (Default: true)

**rhel8cis_section5**: CIS - Access, Authentication and Authorization settings (Section 5) (Default: true)

**rhel8cis_section6**: CIS - System Maintenance settings (Section 6) (Default: true)  

##### Disable all selinux functions
`rhel8cis_selinux_disable: false`

##### Service variables:
###### These control whether a server should or should not be allowed to continue to run these services

```
rhel8cis_avahi_server: false  
rhel8cis_cups_server: false  
rhel8cis_dhcp_server: false  
rhel8cis_ldap_server: false  
rhel8cis_telnet_server: false  
rhel8cis_nfs_server: false  
rhel8cis_rpc_server: false  
rhel8cis_ntalk_server: false  
rhel8cis_rsyncd_server: false  
rhel8cis_tftp_server: false  
rhel8cis_rsh_server: false  
rhel8cis_nis_server: false  
rhel8cis_snmp_server: false  
rhel8cis_squid_server: false  
rhel8cis_smb_server: false  
rhel8cis_dovecot_server: false  
rhel8cis_httpd_server: false  
rhel8cis_vsftpd_server: false  
rhel8cis_named_server: false  
rhel8cis_bind: false  
rhel8cis_vsftpd: false  
rhel8cis_httpd: false  
rhel8cis_dovecot: false  
rhel8cis_samba: false  
rhel8cis_squid: false  
rhel8cis_net_snmp: false  
```  

##### Designate server as a Mail server
`rhel8cis_is_mail_server: false`


##### System network parameters (host only OR host and router)
`rhel8cis_is_router: false`  


##### IPv6 required
`rhel8cis_ipv6_required: true`  


##### AIDE
`rhel8cis_config_aide: true`

###### AIDE cron settings
```
rhel8cis_aide_cron:
  cron_user: root
  cron_file: /etc/crontab
  aide_job: '/usr/sbin/aide --check'
  aide_minute: 0
  aide_hour: 5
  aide_day: '*'
  aide_month: '*'
  aide_weekday: '*'  
```

##### SELinux policy
`rhel8cis_selinux_pol: targeted` 


##### Set to 'true' if X Windows is needed in your environment
`rhel8cis_xwindows_required: no` 


##### Client application requirements
```
rhel8cis_openldap_clients_required: false 
rhel8cis_telnet_required: false 
rhel8cis_talk_required: false  
rhel8cis_rsh_required: false 
rhel8cis_ypbind_required: false 
```

##### Time Synchronization
```
rhel8cis_time_synchronization: chrony
rhel8cis_time_Synchronization: ntp

rhel8cis_time_synchronization_servers:
    - 0.pool.ntp.org
    - 1.pool.ntp.org
    - 2.pool.ntp.org
    - 3.pool.ntp.org  
```  
  
##### 3.4.2 | PATCH | Ensure /etc/hosts.allow is configured
```
rhel8cis_host_allow:
  - "10.0.0.0/255.0.0.0"  
  - "172.16.0.0/255.240.0.0"  
  - "192.168.0.0/255.255.0.0"    
```  

```
rhel8cis_firewall: firewalld
rhel8cis_firewall: iptables
``` 
  

Dependencies
------------

Ansible > 2.6.5

Example Playbook
-------------------------

This sample playbook should be run in a folder that is above the main RHEL8-CIS / RHEL8-CIS-devel folder.

```
- name: Harden Server
  hosts: servers
  become: yes

  roles:
    - RHEL8-CIS
```

Tags
----
Many tags are available for precise control of what is and is not changed.

Some examples of using tags:

```
    # Audit and patch the site
    ansible-playbook site.yml --tags="patch"
```
