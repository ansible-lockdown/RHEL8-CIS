# RHEL 8 CIS

![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL8-CIS/CommunityToDevel?label=Devel%20Build%20Status&style=plastic)
![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL8-CIS/DevelToMain?label=Main%20Build%20Status&style=plastic)
![Release](https://img.shields.io/github/v/release/ansible-lockdown/RHEL8-CIS?style=plastic)

Configure RHEL/Rocky/AlmaLinux machine to be [CIS](https://www.cisecurity.org/cis-benchmarks/) compliant

Based on [CIS RedHat Enterprise Linux 8 Benchmark v2.0.0 - 02-23-2022 ](https://www.cisecurity.org/cis-benchmarks/)

## Join us

On our [Discord Server](https://discord.io/ansible-lockdown) to ask questions, discuss features, or just chat with other Ansible-Lockdown users

## Caution(s)

This role **will make changes to the system** which may have unintended consequences. This is not an auditing tool but rather a remediation tool to be used after an audit has been conducted.

This role was developed against a clean install of the Operating System. If you are implementing to an existing system please review this role for any site specific changes that are needed.

To use release version please point to main branch

## Documentation

- [Getting Started](https://www.lockdownenterprise.com/docs/getting-started-with-lockdown)
- [Customizing Roles](https://www.lockdownenterprise.com/docs/customizing-lockdown-enterprise)
- [Per-Host Configuration](https://www.lockdownenterprise.com/docs/per-host-lockdown-enterprise-configuration)
- [Getting the Most Out of the Role](https://www.lockdownenterprise.com/docs/get-the-most-out-of-lockdown-enterprise)
- [Wiki](https://github.com/ansible-lockdown/RHEL8-CIS/wiki)
- [Repo GitHub Page](https://ansible-lockdown.github.io/RHEL8-CIS/)

### Running level1 or level2 only

While the defaults/main.yml has the options this is used for auditing purposes.
In order to run level(1|2)-server level(1|2)-workstation  This is carried out via tags.

e.g.

``` shell
ansible-playbook -l test-server -i test_inv site.yml -t level1-server

```

## Auditing (new)

This can be turned on or off within the defaults/main.yml file with the variable rhel8cis_run_audit. The value is false by default, please refer to the wiki for more details.

This is a much quicker, very lightweight, checking (where possible) config compliance and live/running settings.

A new form of auditing has been developed, by using a small (12MB) go binary called [goss](https://github.com/aelsabbahy/goss) along with the relevant configurations to check. Without the need for infrastructure or other tooling.
This audit will not only check the config has the correct setting but aims to capture if it is running with that configuration also trying to remove [false positives](https://www.mindpointgroup.com/blog/is-compliance-scanning-still-relevant/) in the process.

Refer to [RHEL8-CIS-Audit](https://github.com/ansible-lockdown/RHEL8-CIS-Audit).

## Requirements

RHEL/AlmaLinux/Rocky 8 - Other versions are not supported.

- AlmaLinux/Rocky Has been tested on 8.4(enabling crypto (sections 1.10&1.11) breaks updating or installs 01Jul2021
- Access to download or add the goss binary and content to the system if using auditing (other options are available on how to get the content to the system.)

## General

- Basic knowledge of Ansible, below are some links to the Ansible documentation to help get started if you are unfamiliar with Ansible
  - [Main Ansible documentation page](https://docs.ansible.com)
  - [Ansible Getting Started](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html)
  - [Tower User Guide](https://docs.ansible.com/ansible-tower/latest/html/userguide/index.html)
  - [Ansible Community Info](https://docs.ansible.com/ansible/latest/community/index.html)
- Functioning Ansible and/or Tower Installed, configured, and running. This includes all of the base Ansible/Tower configurations, needed packages installed, and infrastructure setup.
- Please read through the tasks in this role to gain an understanding of what each control is doing. Some of the tasks are disruptive and can have unintended consiquences in a live production system. Also familiarize yourself with the variables in the defaults/main.yml file or the [Main Variables Wiki Page](https://github.com/ansible-lockdown/RHEL8-CIS/wiki/Main-Variables).

## Dependencies

- Python3
- Ansible 2.9+
- python-def (should be included in RHEL 8)
- libselinux-python

## Role Variables

This role is designed that the end user should not have to edit the tasks themselves. All customizing should be done via the defaults/main.yml file or with extra vars within the project, job, workflow, etc. These variables can be found [here](https://github.com/ansible-lockdown/RHEL8-CIS/wiki/Main-Variables) in the Main Variables Wiki page. All variables are listed there along with descriptions.

## Tags

There are many tags available for added control precision. Each control has it's own set of tags noting what level, if it's scored/notscored, what OS element it relates to, if it's a patch or audit, and the rule number.

Below is an example of the tag section from a control within this role. Using this example if you set your run to skip all controls with the tag services, this task will be skipped. The opposite can also happen where you run only controls tagged with services.

```txt
      tags:
      - level1-server
      - level1-workstation
      - scored
      - avahi
      - services
      - patch
      - rule_2.2.4
```

## Example Audit Summary

This is based on a vagrant image with selections enabled. e.g. No Gui or firewall.
Note: More tests are run during audit as we check config and running state.

```txt

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
```

## Branches

- devel - This is the default branch and the working development branch. Community pull requests will pull into this branch
- main - This is the release branch
- reports - This is a protected branch for our scoring reports, no code should ever go here
- all other branches** - Individual community member branches

## Lifecycle of releases and branches

While Remediate and Audit are managed individually some of the content is linked. Ther are occasions where both need updating or just one of them.

As a general rule we try to abide to the following lifecycle process for branches and releases inclduing ansible-galaxy sync updates. Being community we do have direct customer requests
and requirements will take priority in releases.

- devel branch
  - Staging area for bug fixes PRs and new benchmarks.

    We aim to get the majority of PRs merged to devel in 2-4 weeks.

- Main branch
  - Merge of devel in to main.

    This is dependant on the severity and impact of issues closed. Normally a release alignment every 8-12 weeks (sometimes much quicker)

  - New benchmark version release.

    Once a new benchmark has been released by the provider we aim to get to a new tagged release in 2-4 weeks

  - This is also the where the releases are sourced and linked with ansible-galaxy.

## Community Contribution

We encourage you (the community) to contribute to this role. Please read the rules below.

- Your work is done in your own individual branch. Make sure to Signed-off and GPG sign all commits you intend to merge.
- All community Pull Requests are pulled into the devel branch
- Pull Requests into devel will confirm your commits have a GPG signature, Signed-off, and a functional test before being approved
- Once your changes are merged and a more detailed review is complete, an authorized member will merge your changes into the main branch for a new release

## Pipeline Testing

uses:

- ansible-core 2.12
- ansible collections - pulls in the latest version based on requirements file
- runs the audit using the devel branch
- This is an automated test that occurs on pull requests into devel

## known-issues

cloud0init - due to a bug this will stop working if noexec is added to /var.
rhel8cis_rule_1_1_3_3

[bug 1839899](https://bugs.launchpad.net/cloud-init/+bug/1839899)

## Support

This is a community project at its core and will be managed as such. Please provide as much information as possible and utilise the community [Discord Server](https://discord.io/ansible-lockdown).

Refer to linked below drop us a message for further information

- [Lockdown Enterprise](https://www.lockdownenterprise.com)
  - support for individual repository benchmarks
    - advice on how to use and adopt and priority issue adoption
- [Ansible Counselor](https://www.mindpointgroup.com/cybersecurity-products/ansible-counselor)
  - support for all available repos and enhanced support around ansible usage

Bespoke automation support - ansible and otrher products

- Please enquire for specific requirements
