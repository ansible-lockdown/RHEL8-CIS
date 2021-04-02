RHEL 8 CIS
================

![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL8-CIS/CommunityToDevel?label=Devel%20Build%20Status&style=plastic)
![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL8-CIS/DevelToMain?label=Main%20Build%20Status&style=plastic)
![Release](https://img.shields.io/github/v/release/ansible-lockdown/RHEL8-CIS?style=plastic)


Configure RHEL/Centos 8 machine to be [CIS](https://www.cisecurity.org/cis-benchmarks/) compliant

Based on [CIS RedHat Enterprise Linux 8 Benchmark v1.0.0 - 09-30-2019 ](https://www.cisecurity.org/cis-benchmarks/)

Caution(s)
-------
This role **will make changes to the system** which may have unintended concequences. This is not an auditing tool but rather a remediation tool to be used after an audit has been conducted.

This role was developed against a clean install of the Operating System. If you are implimenting to an existing system please review this role for any site specific changes that are needed.

To use release version please point to main branch

Documentation
-------------
[Getting Started](https://www.lockdownenterprise.com/docs/getting-started-with-lockdown)<br>
[Customizing Roles](https://www.lockdownenterprise.com/docs/customizing-lockdown-enterprise)<br>
[Per-Host Configuration](https://www.lockdownenterprise.com/docs/per-host-lockdown-enterprise-configuration)<br>
[Getting the Most Out of the Role](https://www.lockdownenterprise.com/docs/get-the-most-out-of-lockdown-enterprise)<br>
[Wiki](https://github.com/ansible-lockdown/RHEL8-CIS/wiki)<br>
[Repo GitHub Page](https://ansible-lockdown.github.io/RHEL8-CIS/)<br>

Auditing (new)
--------------

This can be turned on or off within the defaults/main.yml file with the variable rhel8cis_run_audit. The value is false by default, please refer to the wiki for more details.

This is a much quicker, very lightweight, checking (where possible) config compliance and live/running settings.

A new form of auditing has been develeoped, by using a small (12MB) go binary called [goss](https://github.com/aelsabbahy/goss) along with the relevant configurations to check. Without the need for infrastructure or other tooling.
This audit will not only check the config has the correct setting but aims to capture if it is running with that configuration also trying to remove [false positives](https://www.mindpointgroup.com/blog/is-compliance-scanning-still-relevant/) in the process.

Refer to [RHEL8-CIS-Audit](https://github.com/ansible-lockdown/RHEL8-CIS-Audit).


Requirements
------------

RHEL 8 or CentOS 8 - Other versions are not supported.
Access to download or add the goss binary and content to the system if using auditing. options are available on how to get the content to the system.

**General:**
- Basic knowledge of Ansible, below are some links to the Ansible documentation to help get started if you are unfamiliar with Ansible
  - [Main Ansible documentation page](https://docs.ansible.com)
  - [Ansible Getting Started](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html)
  - [Tower User Guide](https://docs.ansible.com/ansible-tower/latest/html/userguide/index.html)
  - [Ansible Community Info](https://docs.ansible.com/ansible/latest/community/index.html)
- Functioning Ansible and/or Tower Installed, configured, and running. This includes all of the base Ansible/Tower configurations, needed packages installed, and infrastructure setup. 
- Please read through the tasks in this role to gain an understanding of what each control is doing. Some of the tasks are disruptive and can have unintended consiquences in a live production system. Also familiarize yourself with the variables in the defaults/main.yml file or the [Main Variables Wiki Page](https://github.com/ansible-lockdown/RHEL8-CIS/wiki/Main-Variables).

Dependencies
------------
- Python3
- Ansible 2.9+
- python-def (should be included in RHEL/CentOS 8)
- libselinux-python

Role Variables
--------------
This role is designed that the end user should not have to edit the tasks themselves. All customizing should be done via the defaults/main.yml file or with extra vars within the project, job, workflow, etc. These variables can be found [here](https://github.com/ansible-lockdown/RHEL8-CIS/wiki/Main-Variables) in the Main Variables Wiki page. All variables are listed there along with descriptions.


Tags
----
There are many tags available for added control precision. Each control has it's own set of tags noting what level, if it's scored/notscored, what OS element it relates to, if it's a patch or audit, and the rule number. 

Below is an example of the tag section from a control within this role. Using this example if you set your run to skip all controls with the tag services, this task will be skipped. The opposite can also happen where you run only controls tagged with services. 
```
      tags:
      - level1-server
      - level1-workstation
      - scored
      - avahi
      - services
      - patch
      - rule_2.2.4
```

Example Audit Summary
---------------------

This is based on a vagrant image with selections enabled. e.g. No Gui or firewall.
Note: More tests are run during audit as we check config and running state.
````
ok: [default] => {
    "msg": [
        "The pre remediation results are: ['Total Duration: 5.454s', 'Count: 338, Failed: 47, Skipped: 5'].",
        "The post remediation results are: ['Total Duration: 5.007s', 'Count: 338, Failed: 46, Skipped: 5'].",
        "Full breakdown can be found in /var/tmp",
        ""
    ]
}

PLAY RECAP *******************************************************************************************************************************************
default                    : ok=270  changed=23   unreachable=0    failed=0    skipped=140  rescued=0    ignored=0  
````
Branches
-------
**devel** - This is the default branch and the working development branch. Community pull requests will pull into this branch<br>
**main** - This is the release branch<br>
**reports** - This is a protected branch for our scoring reports, no code should ever go here<br>
**all other branches** - Individual community member branches<br>

Community Contribution
----------------------

We encourage you (the community) to contribute to this role. Please read the rules below. 
- Your work is done in your own individual branch. Make sure to Signed-off and GPG sign all commits you intend to merge.
- All community Pull Requests are pulled into the devel branch
- Pull Requests into devel will confirm your commits have a GPG signature, Signed-off, and a functional test before being approved
- Once your changes are merged and a more detailed review is complete, an authorized member will merge your changes into the main branch for a new release
