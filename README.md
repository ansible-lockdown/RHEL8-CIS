# RHEL 8 CIS

## Configure a RHEL/Rocky/AlmaLinux 8 machine to be [CIS](https://www.cisecurity.org/cis-benchmarks/) compliant

### Based on [ CIS RedHat Enterprise Linux 8 Benchmark v2.0.0 - 02-23-2022 ](https://www.cisecurity.org/cis-benchmarks/)

---

![Org Stars](https://img.shields.io/github/stars/ansible-lockdown?label=Org%20Stars&style=social)
![Stars](https://img.shields.io/github/stars/ansible-lockdown/RHEL8-CIS?label=Repo%20Stars&style=social)
![Forks](https://img.shields.io/github/forks/ansible-lockdown/RHEL8-CIS?style=social)
![followers](https://img.shields.io/github/followers/ansible-lockdown?style=social)
[![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/AnsibleLockdown.svg?style=social&label=Follow%20%40AnsibleLockdown)](https://twitter.com/AnsibleLockdown)

![Ansible Galaxy Quality](https://img.shields.io/ansible/quality/56380?label=Quality&&logo=ansible)
![Discord Badge](https://img.shields.io/discord/925818806838919229?logo=discord)

![Devel Build Status](https://img.shields.io/github/actions/workflow/status/ansible-lockdown/RHEL8-CIS/linux_benchmark_testing.yml?label=Devel%20Build%20Status)
![Devel Commits](https://img.shields.io/github/commit-activity/m/ansible-lockdown/RHEL8-CIS/devel?color=dark%20green&label=Devel%20Branch%20commits)

![Release Branch](https://img.shields.io/badge/Release%20Branch-Main-brightgreen) 
![Main Build Status](https://img.shields.io/github/actions/workflow/status/ansible-lockdown/RHEL8-CIS/linux_benchmark_testing.yml?label=Build%20Status)
![Main Release Date](https://img.shields.io/github/release-date/ansible-lockdown/RHEL8-CIS?label=Release%20Date)
![Release Tag](https://img.shields.io/github/v/tag/ansible-lockdown/RHEL8-CIS?label=Release%20Tag&&color=success)

![Issues Open](https://img.shields.io/github/issues-raw/ansible-lockdown/RHEL8-CIS?label=Open%20Issues)
![Issues Closed](https://img.shields.io/github/issues-closed-raw/ansible-lockdown/RHEL8-CIS?label=Closed%20Issues&&color=success)
![Pull Requests](https://img.shields.io/github/issues-pr/ansible-lockdown/RHEL8-CIS?label=Pull%20Requests)

![License](https://img.shields.io/github/license/ansible-lockdown/RHEL8-CIS?label=License)

---

## Looking for support?

[Lockdown Enterprise](https://www.lockdownenterprise.com#GH_AL_RH8_cis)

[Ansible support](https://www.mindpointgroup.com/cybersecurity-products/ansible-counselor#GH_AL_RH8_cis)

### Community

Join us on our [Discord Server](https://discord.io/ansible-lockdown) to ask questions, discuss features, or just chat with other Ansible-Lockdown users.

---

## Caution(s)

This role **will make changes to the system** which may have unintended consequences. This is not an auditing tool but rather a remediation tool to be used after an audit has been conducted.

Check Mode is not supported! The role will complete in check mode without errors, but it is not supported and should be used with caution. The RHEL8-CIS-Audit role or a compliance scanner should be used for compliance checking over check mode.

This role was developed against a clean install of the Operating System. If you are implementing to an existing system please review this role for any site specific changes that are needed.

To use release version please point to main branch and relevant release for the cis benchmark you wish to work with.

---

## Matching a security Level for CIS

It is possible to to only run level 1 or level 2 controls for CIS.
This is managed using tags:

- level1_server
- level1_workstation
- level2_server
- level2_workstation

The control found in defaults main also need to reflect this as this control the testing thet takes place if you are using the audit component.

## Coming from a previous release

CIS release always contains changes, it is highly recommended to review the new references and available variables. This have changed significantly since ansible-lockdown initial release.
This is now compatible with python3 if it is found to be the default interpreter. This does come with pre-requisites which it configures the system accordingly.

Further details can be seen in the [Changelog](./ChangeLog.md)

## Auditing (new)

This can be turned on or off within the defaults/main.yml file with the variable rhel8cis_run_audit. The value is false by default, please refer to the wiki for more details. The defaults file also populates the goss checks to check only the controls that have been enabled in the ansible role.

This is a much quicker, very lightweight, checking (where possible) config compliance and live/running settings.

A new form of auditing has been developed, by using a small (12MB) go binary called [goss](https://github.com/goss-org/goss) along with the relevant configurations to check. Without the need for infrastructure or other tooling.
This audit will not only check the config has the correct setting but aims to capture if it is running with that configuration also trying to remove [false positives](https://www.mindpointgroup.com/blog/is-compliance-scanning-still-relevant/) in the process.

Refer to [RHEL8-CIS-Audit](https://github.com/ansible-lockdown/RHEL8-CIS-Audit).

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

## Documentation

- [Read The Docs](https://ansible-lockdown.readthedocs.io/en/latest/)
- [Getting Started](https://www.lockdownenterprise.com/docs/getting-started-with-lockdown#GH_AL_RH8_cis)
- [Customizing Roles](https://www.lockdownenterprise.com/docs/customizing-lockdown-enterprise#GH_AL_RH8_cis)
- [Per-Host Configuration](https://www.lockdownenterprise.com/docs/per-host-lockdown-enterprise-configuration#GH_AL_RH8_cis)
- [Getting the Most Out of the Role](https://www.lockdownenterprise.com/docs/get-the-most-out-of-lockdown-enterprise#GH_AL_RH8_cis)

## Requirements

**General:**

- Basic knowledge of Ansible, below are some links to the Ansible documentation to help get started if you are unfamiliar with Ansible

  - [Main Ansible documentation page](https://docs.ansible.com)
  - [Ansible Getting Started](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html)
  - [Tower User Guide](https://docs.ansible.com/ansible-tower/latest/html/userguide/index.html)
  - [Ansible Community Info](https://docs.ansible.com/ansible/latest/community/index.html)
- Functioning Ansible and/or Tower Installed, configured, and running. This includes all of the base Ansible/Tower configurations, needed packages installed, and infrastructure setup.
- Please read through the tasks in this role to gain an understanding of what each control is doing. Some of the tasks are disruptive and can have unintended consiquences in a live production system. Also familiarize yourself with the variables in the defaults/main.yml file.

**Technical Dependencies:**

RHEL/AlmaLinux/Rocky/Oracle 8 - Other versions are not supported.

- AlmaLinux/Rocky Has been tested on 8.4(enabling crypto (sections 1.10&1.11) breaks updating or installs : July 01 2021
- Access to download or add the goss binary and content to the system if using auditing 
(other options are available on how to get the content to the system.)
- Python3
- Ansible 2.9+
- python-def (should be included in RHEL 8)
- libselinux-python

## Role Variables

This role is designed that the end user should not have to edit the tasks themselves. All customizing should be done via the defaults/main.yml file or with extra vars within the project, job, workflow, etc.

## Tags

There are many tags available for added control precision. Each control has it's own set of tags noting what level, if it's scored/notscored, what OS element it relates to, if it's a patch or audit, and the rule number.

Below is an example of the tag section from a control within this role. Using this example if you set your run to skip all controls with the tag services, this task will be skipped. The opposite can also happen where you run only controls tagged with services.

```sh
      tags:
      - level1-server
      - level1-workstation
      - scored
      - avahi
      - services
      - patch
      - rule_2.2.4
```

## Community Contribution

We encourage you (the community) to contribute to this role. Please read the rules below.

- Your work is done in your own individual branch. Make sure to Signed-off and GPG sign all commits you intend to merge.
- All community Pull Requests are pulled into the devel branch
- Pull Requests into devel will confirm your commits have a GPG signature, Signed-off, and a functional test before being approved
- Once your changes are merged and a more detailed review is complete, an authorized member will merge your changes into the main branch for a new release

## Known Issues

cloud0init - due to a bug this will stop working if noexec is added to /var.
rhel8cis_rule_1_1_3_3

[bug 1839899](https://bugs.launchpad.net/cloud-init/+bug/1839899)

## Pipeline Testing

uses:

- ansible-core 2.12
- ansible collections - pulls in the latest version based on requirements file
- runs the audit using the devel branch
- This is an automated test that occurs on pull requests into devel

## Local Testing

Molecule can be used to work on this role and test in distinct _scenarios_.

**examples**

```bash
molecule test -s default
molecule converge -s wsl -- --check
molecule verify -s localhost
```

local testing uses:

- ansible 2.13.3
- molecule 4.0.1
- molecule-docker 2.0.0
- molecule-podman 2.0.2
- molecule-vagrant 1.0.0
- molecule-azure 0.5.0
