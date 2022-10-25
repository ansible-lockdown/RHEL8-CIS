# Changes to rhel8CIS

## 1.5.0

- Changed include_tasks to import_tasks to resolve using tags for levels
- #209 5.6.5 rewrite umask settings
- #220 tidy up and align variables
- #226 Thanks to Thulium-Drake
  -Extended the auditd config required value for auditd space left percentage (not part of CIS Benchmark but required fopr auditd to run correctly in some cases)

- #227 thanks to OscarElits
  - chrony files now RH expected locations
- #228 Thanks to benbulll 
  - audit binary copy var missing


## 1.4.0

- workflow improvements
- auditd alignment
  - tftp client
  - default locatoin moved from /var/tmp to /opt
- linting
  - new .ansiblelint
  - boolean standards
  - general linting improvements

## 1.3.9

- tidy up become statements

Improvements for idempotency

- update to auditd template
  - uses facts and template new variable
    - update_audit_template (default false)
- 3.4.1.5 discovery improvement
- 5.6.1.4 discovery improvement
- warning count added to summary at end of playbook
- Added support for Almalinux
- Added support for Rocky

## 1.3.8

Issues

- #185 thanks to @flwitten rsyslog and journald work
- #189
- #190 being addressed thanks to @ztmr - any feedback helpful on this one
- #196 #200 thanks to @Thulium-Drake
- #203 thanks to @scottdoane
- #204 thanks to @ccravens
- #206 flush handler tidy up

## improvements

- Dynamic UID discovery
- Several title updates and alignments
- Logic and idempotence improvement
- Tag updates and fixes
- Removed config no longer used
- Dynamic container discovery
- Update container variables and usage

## 1.3.7

Issues

- thanks to @ccravens
  - #160 & #183 - Please not this changes the variable for the aide cron job from /etc/crontab - manual tidy up maybe required.
- thanks to @flwitten
  - #180 - update to assert in main.yml and 1.4.1 conditional update
  - #181 - 1.8.5 typo resolved
  - #182 - 1.2.2 fixed variable and enhanced gpg check with vendor key

Improvements

- changed crypto to DEFAULT in defaults/main and updated as allowed option
- 3.4.1.2 - removed enabled option as errors if masked and enable option
- workflow added branch option to issues.

## 1.3.6

- Issues
  - #164
  - #165
  - #168
  - #176

## 1.3.5

- Update to V2.0.0
  - many changes inline with new benchamrk requirements please refer to official docs

## 1.3.4

- CentOS no longer supported due to moving to Stream updates
- Rocky and AlmaLinux tested and working
- #155 thanks to RayMcAdmin
- #156 thanks to Thulium-Drake

## 1.3.3

- update to audit script
  - variable for audit OS agnostic
  - removal of included library module (not required)

- Issues included
  - #135 - running levels - upadted tags
  - #138 - auditd immutable
  - #139 - 5.2.13 valus updated
  - #140
  - #141 - check mode update
  - #142
  - #143 - labels added
  - #144
  - #146 - undefined variable added
  - #147 - removed warn statement
  - #149 - shell timeout

## 1.3.2

- issues with crypto policies on ec2 - added skip for rules if system_is_ec2 variable
  - cis_1.10  ## Change crypto breaks installing products
  - cis_1.11  ## Change crypto breaks installing products

## 1.3.1

- CIS 1.0.1 updates
- Added Issue and PR templates
- Added better reboot logic
- Added options to ensure idempotence
- Enhanced flush handlers
- Typo fixes
- mount check improvements
- Linting fixes
- Added systemd tmp mount
- Added systemd tmpfs block
- #110 tmp.mount support
  - thanks to @erpadmin

## 1.3

- extentions to LE audit capability
- more lint and layout changes
- sugroup assertion added 5.7
- added extra logic variable to authselect/config section 5.3 related
- AlmaLinux and Rocky tested (comments in readme - also rsyslog installed at build or will fail)
- section 1.1 mount work has been rewritten and systemd tmp mount options added

## 1.2.3

- #117 sugroup enhancements
  - thanks to @ihotz
- #112 use of dnf module not shell
  - thanks to @wolskie

## 1.2.2

- #33 mkgrub missing variable issues - efi and bios path resolution
  - thanks to @mrampant & @mickey1928geo
- #102 2.2.2 xorg pkg removal extended
  - thanks to @RosarioVinoth
- #104 5.4.1 pwquality logic
  - thanks to @RosarioVinoth
- #107 Idempotence improvement for 4.1.1.3 and 4.1.1.4
  - thanks to @andreyzher
- lint changes and updates to sync with ansible-galaxy

## v1.2.1

- bootloader and default variables
- empty strings lint updates
- #87
- rule 6.1.1 - audit only - outputs file discrepancies to {{ rhel8cis_rpm_audit_file }}
- #88
- checkmode_improvements added to relevant tasks
- PR #96
- crypto policy idempotency

## v1.2.0

- #86
- Adding on the goss auditing tool
- remove deprecated warnings
- format and layout
- general improvements
- readme updates
- use ansible package_facts
- #90
- cis fix - nfs-server not nfs
  - Thanks to danderemer
