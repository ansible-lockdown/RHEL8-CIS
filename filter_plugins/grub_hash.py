#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2025, Jeffrey van Pelt <jeff@vanpelt.one>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

DOCUMENTATION = r"""
name: grub_hash
short_description: Generate a GRUB2 password hash
version_added: 1.0.0
author: Jeffrey van Pelt (@Thulium-Drake)
description:
  - Generate a GRUB2 password hash from the input
options:
  _input:
    description: The desired password for the GRUB bootloader
    type: string
    required: true
  salt:
    description: The salt used to generate the hash
    type: string
    required: false
  rounds:
    description: The amount of rounds to run the PBKDF2 function
    type: int
    required: false
"""

EXAMPLES = r"""
- name: 'Generate hash with defaults'
  ansible.builtin.debug:
    msg: "{{ 'mango123!' | grub_hash }}"

- name: 'Generate hash with custom rounds and salt'
  ansible.builtin.debug:
    msg: "{{ 'mango123!' | grub_hash(rounds=10001, salt='andpepper') }}"
    # Produces: grub.pbkdf2.sha512.10001.616E64706570706572.4C6AEA2A811B4059D4F47AEA36B77DB185B41E9F08ECC3C4C694427DB876C21B24E6CBA0319053E4F1431CDEE83076398C73B9AA8F50A7355E446229BC69A97C
"""

RETURN = r"""
_value:
  description: A GRUB2 password hash
  type: string
"""

from ansible.errors import AnsibleFilterError
import os
import base64
from passlib.hash import grub_pbkdf2_sha512

def grub_hash(password, rounds=10000, salt=None):
    if salt is None:
        # Generate 64-byte salt if not provided
        salt = os.urandom(64)

    # Check if the salt, when not generated, is a valid bytes value and attempt to convert if needed
    if not isinstance(salt, bytes):
        try:
            salt = salt.encode("utf-8")
        except AttributeError:
            raise TypeError("Salt must be a string, not int.")

    # Configure hash generator
    pbkdf2_generator = grub_pbkdf2_sha512.using(rounds=rounds, salt=salt)
    return pbkdf2_generator.hash(password)

class FilterModule(object):
    def filters(self):
        return {
            'grub_hash': grub_hash
        }
