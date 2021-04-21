# Changes to rhel8CIS



## v1.2.1

- bootloader and default variables
- empty strings lint updates

### 87

- rule 6.1.1 - audit only - outputs file discrepancies to {{ rhel8cis_rpm_audit_file }}

### 88

- checkmode_improvements added to relevant tasks

### PR #96 

- crypto policy idempotency



## v1.2.0

### 86

- Adding on the goss auditing tool
- remove deprecated warnings
- format and layout
- general improvements
- readme updates
- use ansible package_facts

### 90

- cis fix - nfs-server not nfs
  - Thanks to danderemer
