RHEL 8 CIS
================

![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL8-CIS/CommunityToDevel?label=Devel%20Build%20Status&style=plastic)


Configure RHEL/Centos 8 machine to be [CIS](https://www.cisecurity.org/cis-benchmarks/) compliant.

Based on [CIS RedHat Enterprise Linux 8 Benchmark v2.1.1 - 01-31-2017 ](https://community.cisecurity.org/collab/public/index.php).

This role **will make changes to the system** which may have unintended concequences. This is not an auditing tool but rather a remediation tool to be used after an audit has been conducted.

Documentation
-------------
[Getting Started](https://www.lockdownenterprise.com/docs/getting-started-with-lockdown)<br>
[Customizing Roles](https://www.lockdownenterprise.com/docs/customizing-lockdown-enterprise)<br>
[Per-Host Configuration](https://www.lockdownenterprise.com/docs/per-host-lockdown-enterprise-configuration)<br>
[Getting the Most Out of the Role](https://www.lockdownenterprise.com/docs/get-the-most-out-of-lockdown-enterprise)<br>
[Wiki](https://github.com/ansible-lockdown/RHEL8-CIS/wiki)<br>
[Repo GitHub Page](https://ansible-lockdown.github.io/RHEL8-CIS/)<br>


Requirements
------------

**General:**
- Basic knowledge of Ansible, below are some links to the Ansible documentation to help get started if you are unfamiliar with Ansible
  - [Main Ansible documentation page](https://docs.ansible.com)
- Ansible and/or Tower Installed, configured, and running. This includes all of the base Ansible/Tower configurations, infrastructure setup, and needed packages installed. 
- Please read through the tasks in this role to gain an understanding of what each control is doing. Some of the tasks are disruptive and can have unintended consiquences in live production systems. With this also familiarize yourself with the variables in the defaults/main.yml file.

**Technical Dependencies:**
- Running Ansible/Tower setup (this role is tested against Ansible version 2.9.1 and newer)
- Python3 Ansibl run environment
- python-def (should be included in RHEL/CentOS 8)
- libselinux-python

Role Variables
--------------
This role is designed that the end user should not have to edit the tasks themselves. All editing should happen via the defaults/main.yml file or with extra vars in the project, job, workflow, etc. These variables can be found [here](https://github.com/ansible-lockdown/RHEL8-CIS/wiki/Main-Variables) in the Main Variables Wiki page. All variables are listed there along with descriptions.


Tags
----
There are many tags available for precise control of what is and is not changed. Each control has it's own set of tags noting what level, if it's scored/notscored, what OS element it relates to, if it's a patch or audit, and the rule number. 

Below is an example of the tag section from a control. Using this example if you set your run to skip all controls related to services, this task will be skipped. The opposite can also happen where you run only tasks related to services. You can use any tag to control that level of precision role wide. 
```
      tags:
      - level1
      - scored
      - avahi
      - services
      - patch
      - rule_2.2.4
```
