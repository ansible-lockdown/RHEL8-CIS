# Changes to rhel8CIS

## 1.3

- CIS 1.0.1
- extentions to LE audit capability
- more lint and layout changes
- sugroup assertion added 5.7
- added extra logic variable to authselect/config section 5.3 related
- Rocky tested (comments in readme not rsyslog intsalled at build or will fail)
- section 1.1 mount work has been rewritten

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
