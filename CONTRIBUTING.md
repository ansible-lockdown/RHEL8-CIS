Contributing to Ansible-Lockdown Projects
==========================================

Who can raise a pull request
----------------------------

**Pull requests come from approved contributors, and we are happy to onboard anyone who would like to join them.**

We appreciate everyone who takes the time to contribute, and a great deal of what makes these roles useful has come from the community.

As the project has grown, we have found that contributions sometimes arrive that do not quite line up with the conventions shared across the Ansible-Lockdown roles, or that cover ground we are already working on ahead of the next release. That means rework on both sides, and it is a disappointing outcome for someone who has put real effort in. Talking it through with us first means we can tell you what is already in hand and point you at the right branch and conventions from the start, so your work lands the way you intended.

To become an approved contributor:

1) Join our [Discord Server](https://www.lockdownenterprise.com/discord)
2) Ask in the community channel for contributor access, and tell us what you would like to work on
3) A maintainer will confirm no one is already working on it, walk you through the conventions, and grant you access

**Issues are still open to everyone.** You do not need approval to raise a bug report, and a well described issue is a genuinely valuable contribution. Please include the branch you are on, your Ansible version, the control affected, and the actual against expected behaviour. If you have already worked out a fix, describe it in the issue and we will credit you in the changelog when it is applied.

Rules
-----

1) Pull requests are from approved contributors (see above)
2) All commits must be GPG signed and carry Signed-off-by (details in Signing section)
3) Work in your own branch or your own fork
4) Pull requests go into the devel branch. From a fork they go into a staging branch first, as our CI/CD needs information held in the repo
5) Be open and nice to each other

Workflow
--------

- Agree the change with a maintainer first, so you know what is already in hand
- Work in your own branch. GPG sign and Signed-off every commit
- Raise the pull request into devel. Automated checks cover signing, signoff and functional tests
- Once merged and reviewed, a maintainer merges to main for the next release

Signing your contribution
-------------------------

We've chosen to use the Developer's Certificate of Origin (DCO) method
that is employed by the Linux Kernel Project, which provides a simple
way to contribute to Ansible-Lockdown projects.

The process is to certify the below DCO 1.1 text:

    Developer's Certificate of Origin 1.1

    By making a contribution to this project, I certify that:

    (a) The contribution was created in whole or in part by me and I
        have the right to submit it under the open source license
        indicated in the file; or

    (b) The contribution is based upon previous work that, to the best
        of my knowledge, is covered under an appropriate open source
        license and I have the right under that license to submit that
        work with modifications, whether created in whole or in part
        by me, under the same open source license (unless I am
        permitted to submit under a different license), as indicated
        in the file; or

    (c) The contribution was provided directly to me by some other
        person who certified (a), (b) or (c) and I have not modified
        it.

    (d) I understand and agree that this project and the contribution
        are public and that a record of the contribution (including all
        personal information I submit with it, including my sign-off) is
        maintained indefinitely and may be redistributed consistent with
        this project or the open source license(s) involved.

Then, when it comes time to submit a contribution, include the following
text in your contribution commit message:

    Signed-off-by: Joan Doe <joan.doe@email.com>

This message can be entered manually, or if you have configured git
with the correct `user.name` and `user.email`, you can use the `-s`
option to `git commit` to automatically include the signoff message.
