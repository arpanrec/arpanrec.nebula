## [5.2.4](https://github.com/arpanrec/arpanrec.nebula/compare/5.2.3...5.2.4) (2024-05-04)


### Bug Fixes

* Updated CI ([313074e](https://github.com/arpanrec/arpanrec.nebula/commit/313074ea55973cf396c6d1c702647b66b9f55064))

## [5.2.3](https://github.com/arpanrec/arpanrec.nebula/compare/5.2.2...5.2.3) (2024-05-01)


### Bug Fixes

* Update semantic-release version in release.yml workflow ([00fea4c](https://github.com/arpanrec/arpanrec.nebula/commit/00fea4c82a491e9dfbab4670576b3b7a2dddc7ee))
* Update semantic-release version in release.yml workflow ([bc45a7b](https://github.com/arpanrec/arpanrec.nebula/commit/bc45a7be9c51f1aca1477369c92de13821c0e2c7))
* Update semantic-release version in release.yml workflow ([cdd7dd3](https://github.com/arpanrec/arpanrec.nebula/commit/cdd7dd316c4bc3dedeffe4c72a1874ce10094cb9))
* Update settings.json to enable single quotes in GitHub Actions workflow ([9f7ac20](https://github.com/arpanrec/arpanrec.nebula/commit/9f7ac2095375d4c5972910c9ab026353f9560084))

## [5.2.2](https://github.com/arpanrec/arpanrec.nebula/compare/5.2.1...5.2.2) (2024-05-01)


### Bug Fixes

* added ms-python.mypy-type-checker ([0c2d1be](https://github.com/arpanrec/arpanrec.nebula/commit/0c2d1befb94eeb76f35dd26a57046c2bdfb6ed31))

## [5.2.1](https://github.com/arpanrec/arpanrec.nebula/compare/5.2.0...5.2.1) (2024-04-30)


### Bug Fixes

* Update Docker role to geerlingguy.docker in cloudinit.yml playbook ([8bd6aa0](https://github.com/arpanrec/arpanrec.nebula/commit/8bd6aa040c6fb6a4a7d5552d0671f39cc842ec24))

# [5.2.0](https://github.com/arpanrec/arpanrec.nebula/compare/5.1.0...5.2.0) (2024-04-30)


### Features

* remove docker ([fc9e645](https://github.com/arpanrec/arpanrec.nebula/commit/fc9e645a98d1b5fe142b63bbc5c354af6dbe9972))

# [5.1.0](https://github.com/arpanrec/arpanrec.nebula/compare/5.0.2...5.1.0) (2024-04-30)


### Features

* Change variable names ([20c289f](https://github.com/arpanrec/arpanrec.nebula/commit/20c289f3f7b36c69cae4ad1ac6ccad6f10f8e673))

## [5.0.2](https://github.com/arpanrec/arpanrec.nebula/compare/5.0.1...5.0.2) (2024-04-30)


### Bug Fixes

* Cloudintit docs added ([#17](https://github.com/arpanrec/arpanrec.nebula/issues/17)) ([f28e71f](https://github.com/arpanrec/arpanrec.nebula/commit/f28e71f247e7809ff9ee8527bb10d47e514b7555))

## [5.0.1](https://github.com/arpanrec/arpanrec.nebula/compare/5.0.0...5.0.1) (2024-04-29)


### Bug Fixes

* fix docs to readme to telegram ([#16](https://github.com/arpanrec/arpanrec.nebula/issues/16)) ([b218658](https://github.com/arpanrec/arpanrec.nebula/commit/b218658503865e9c31415abbde4e884e5c1e55ab))

# [5.0.0](https://github.com/arpanrec/arpanrec.nebula/compare/4.4.4...5.0.0) (2024-04-29)


### Features

* cloudinit ([#15](https://github.com/arpanrec/arpanrec.nebula/issues/15)) ([21ab0ff](https://github.com/arpanrec/arpanrec.nebula/commit/21ab0ffb7da093e9af18b517ce179aede3c6fc56))


### BREAKING CHANGES

* docker added

* Fix network configuration and environment variables in linux_patching tasks

* Fix environment variable PATH in ssh_hardening tasks

* Update user_add role to handle empty ssh access public key list

* Update server_workspace playbook to enable Bitwarden CLI and Node JS roles

* Update cloudinit.yml playbook to use include_role instead of import_role

* remove bw

* telegram_desktop

* Update molecule.yml to use debian_role_telegram_desktop_default instead of debian_role_telegram_default

## [4.4.4](https://github.com/arpanrec/arpanrec.nebula/compare/4.4.3...4.4.4) (2024-04-29)


### Bug Fixes

* no become ([9d1dbbc](https://github.com/arpanrec/arpanrec.nebula/commit/9d1dbbc98d6c54cc14d04e80342a4b8b98150e2a))

## [4.4.3](https://github.com/arpanrec/arpanrec.nebula/compare/4.4.2...4.4.3) (2024-04-29)


### Bug Fixes

* update apt cache ([3849d29](https://github.com/arpanrec/arpanrec.nebula/commit/3849d29b6cb45649f478bf68e98ed62a1043e830))

## [4.4.2](https://github.com/arpanrec/arpanrec.nebula/compare/4.4.1...4.4.2) (2024-04-29)


### Bug Fixes

* don't reboot if ansible connection is local ([a90dc37](https://github.com/arpanrec/arpanrec.nebula/commit/a90dc377490cf37371ade6e8a71a0ebb42f81bd7))

## [4.4.1](https://github.com/arpanrec/arpanrec.nebula/compare/4.4.0...4.4.1) (2024-04-29)


### Bug Fixes

* cloudinit ([addbf57](https://github.com/arpanrec/arpanrec.nebula/commit/addbf57c31bf7758dbb14f4a8672497d25884e73))

# [4.4.0](https://github.com/arpanrec/arpanrec.nebula/compare/4.3.6...4.4.0) (2024-04-29)


### Features

* cloundinit ([6cd813a](https://github.com/arpanrec/arpanrec.nebula/commit/6cd813a8c1c30ca1bb087fcb0a61edfbe324ef51))

## [4.3.6](https://github.com/arpanrec/arpanrec.nebula/compare/4.3.5...4.3.6) (2024-04-29)


### Bug Fixes

* hostname line in network.yml has one space ([2034606](https://github.com/arpanrec/arpanrec.nebula/commit/2034606bd3a403d3f8821feeb6bee0f3811347c2))
* Merge branch 'main' of github.com:arpanrec/arpanrec.nebula ([4bd72b4](https://github.com/arpanrec/arpanrec.nebula/commit/4bd72b45d1dc07ac7593d4915d0c74c765860cd4))

## [4.3.5](https://github.com/arpanrec/arpanrec.nebula/compare/4.3.4...4.3.5) (2024-04-29)


### Bug Fixes

* add domain in hostname ([2977492](https://github.com/arpanrec/arpanrec.nebula/commit/297749265f567851d069edcef7d13057a80adda9))

## [4.3.4](https://github.com/arpanrec/arpanrec.nebula/compare/4.3.3...4.3.4) (2024-04-29)


### Bug Fixes

* python3-pip,venv moved to dev ([300eef2](https://github.com/arpanrec/arpanrec.nebula/commit/300eef294f81c212f838373e725a7384354c2ba9))

## [4.3.3](https://github.com/arpanrec/arpanrec.nebula/compare/4.3.2...4.3.3) (2024-04-29)


### Bug Fixes

* add log for packages ([9b70a43](https://github.com/arpanrec/arpanrec.nebula/commit/9b70a4318d825e6d9c7b12aa76a2cdb672268f62))

## [4.3.2](https://github.com/arpanrec/arpanrec.nebula/compare/4.3.1...4.3.2) (2024-04-29)


### Bug Fixes

* Debug msg for dev machine ([db5c75e](https://github.com/arpanrec/arpanrec.nebula/commit/db5c75e5b1c9bc65635364d387b3b60c3030d1b7))

## [4.3.1](https://github.com/arpanrec/arpanrec.nebula/compare/4.3.0...4.3.1) (2024-04-29)


### Bug Fixes

* Refactor assert statements in cloudinit.yml, user_add.yml, arch_aur_helper.yml, downloan_archive.yml, and tlscert.yml to use simplified syntax ([ee1cf8f](https://github.com/arpanrec/arpanrec.nebula/commit/ee1cf8fd685648ec842c435e6dd2412432877773))

# [4.3.0](https://github.com/arpanrec/arpanrec.nebula/compare/4.2.1...4.3.0) (2024-04-29)


### Features

* pv_cloud_is_dev_machine is mandatory variable now ([125c475](https://github.com/arpanrec/arpanrec.nebula/commit/125c4751e246f246355e92f988a03dba35682a40))

## [4.2.1](https://github.com/arpanrec/arpanrec.nebula/compare/4.2.0...4.2.1) (2024-04-29)


### Bug Fixes

* Application User | Checking essential variables ([0e30a69](https://github.com/arpanrec/arpanrec.nebula/commit/0e30a693ffb3e9c11221cadb08075bdcb37ccb32))

# [4.2.0](https://github.com/arpanrec/arpanrec.nebula/compare/4.1.4...4.2.0) (2024-04-29)


### Features

* Add development packages ([39db575](https://github.com/arpanrec/arpanrec.nebula/commit/39db5754892f365649bcd9836f3964c2cd452616))
* Merge branch 'main' of github.com:arpanrec/arpanrec.nebula ([1b76286](https://github.com/arpanrec/arpanrec.nebula/commit/1b762862cf498b5a157990ad27a4f5f80567c3b2))

## [4.1.4](https://github.com/arpanrec/arpanrec.nebula/compare/4.1.3...4.1.4) (2024-04-29)


### Bug Fixes

* Refactor Linux Patching task to use noninteractive mode for apt-get commands ([e3d1487](https://github.com/arpanrec/arpanrec.nebula/commit/e3d1487e79ee960035c6adbadb7bddd60cd1d3bf))

## [4.1.3](https://github.com/arpanrec/arpanrec.nebula/compare/4.1.2...4.1.3) (2024-04-28)


### Bug Fixes

* Add issues link to galaxy.yml ([701e2df](https://github.com/arpanrec/arpanrec.nebula/commit/701e2dfe0b4fc587cc3d5309e96ac56636254e8c))

## [4.1.2](https://github.com/arpanrec/arpanrec.nebula/compare/4.1.1...4.1.2) (2024-04-28)


### Bug Fixes

* Update release.config.cjs to include poetry lock file in assets ([5029d4b](https://github.com/arpanrec/arpanrec.nebula/commit/5029d4bb594163dd8f80f6c7544a0d3cc67376b0))

## [4.1.1](https://github.com/arpanrec/arpanrec.nebula/compare/4.1.0...4.1.1) (2024-04-28)


### Bug Fixes

* Refactor dependencies in pyproject.toml file ([fb1dbac](https://github.com/arpanrec/arpanrec.nebula/commit/fb1dbac4433221e9f09fd75909663658fa34cde8))
* Refactor release.config.cjs to remove unnecessary code ([c8b2b44](https://github.com/arpanrec/arpanrec.nebula/commit/c8b2b448fbc2253759ae1c78d87139a52aa3fd71))

# [4.1.0](https://github.com/arpanrec/arpanrec.nebula/compare/4.0.0...4.1.0) (2024-04-28)


### Features

* Refactor split_certificates function to support Python 3 in split_certificates.py ([bdc3fce](https://github.com/arpanrec/arpanrec.nebula/commit/bdc3fcea6266aa7c936fcb546fd811b7e710e875))

# [4.0.0](https://github.com/arpanrec/arpanrec.nebula/compare/3.4.4...4.0.0) (2024-04-28)


### Features

* Change License ([#14](https://github.com/arpanrec/arpanrec.nebula/issues/14)) ([18b71f7](https://github.com/arpanrec/arpanrec.nebula/commit/18b71f7403290c89d699992ccc5079767679b54d))


### BREAKING CHANGES

* Changed the license to GLWTS

## [3.4.4](https://github.com/arpanrec/arpanrec.nebula/compare/3.4.3...3.4.4) (2024-04-28)


### Bug Fixes

* Update galaxy.yml to remove unnecessary files from build_ignore ([03917c9](https://github.com/arpanrec/arpanrec.nebula/commit/03917c9b93589f910e39ac550ca61f4433d498a2))

## [3.4.3](https://github.com/arpanrec/arpanrec.nebula/compare/3.4.2...3.4.3) (2024-04-28)


### Bug Fixes

* Merge branch 'main' of github.com:arpanrec/arpanrec.nebula ([53eb869](https://github.com/arpanrec/arpanrec.nebula/commit/53eb8694fcbb745cf85a203aa69ad5b903f37487))
* Update release.config.js and galaxy.yml files with new changes ([eba8680](https://github.com/arpanrec/arpanrec.nebula/commit/eba8680bd9df1bd20918e54812455643d389f5eb))

## [3.4.2](https://github.com/arpanrec/arpanrec.nebula/compare/3.4.1...3.4.2) (2024-04-28)


### Bug Fixes

* Update release.config.js and galaxy.yml files with new changes ([c692fd5](https://github.com/arpanrec/arpanrec.nebula/commit/c692fd56995b4b16b77dac942bf72d1af208fd00))

## [3.4.1](https://github.com/arpanrec/arpanrec.nebula/compare/3.4.0...3.4.1) (2024-04-28)


### Bug Fixes

* Update network.yml to include a newline character in the content of the copy task ([20a9b97](https://github.com/arpanrec/arpanrec.nebula/commit/20a9b97824dfe03ce90c49ccfd3861d2b0fdfde1))

# [3.4.0](https://github.com/arpanrec/arpanrec.nebula/compare/3.3.1...3.4.0) (2024-04-28)


### Features

* Feature/fail2ban ([#12](https://github.com/arpanrec/arpanrec.nebula/issues/12)) ([b246c31](https://github.com/arpanrec/arpanrec.nebula/commit/b246c313c9419085f38297f216e8d8560831934e))

## [3.3.1](https://github.com/arpanrec/arpanrec.nebula/compare/3.3.0...3.3.1) (2024-04-28)


### Bug Fixes

* Cleanup ([#11](https://github.com/arpanrec/arpanrec.nebula/issues/11)) ([c3be5a5](https://github.com/arpanrec/arpanrec.nebula/commit/c3be5a5bbd7d1ae4c270eebfb7f48acf5d6be9be))

# [3.3.0](https://github.com/arpanrec/arpanrec.nebula/compare/3.2.3...3.3.0) (2024-04-28)


### Features

* disable themes by default ([#10](https://github.com/arpanrec/arpanrec.nebula/issues/10)) ([617e896](https://github.com/arpanrec/arpanrec.nebula/commit/617e89633b94b3535cc6a5a1f43636061bb263f9))

## [3.2.3](https://github.com/arpanrec/arpanrec.nebula/compare/3.2.2...3.2.3) (2024-04-27)


### Bug Fixes

* Update hvac package version to 2.2.0 ([2119814](https://github.com/arpanrec/arpanrec.nebula/commit/2119814363c48f6fc8476ba89b35f152cdff5792))

## [3.2.2](https://github.com/arpanrec/arpanrec.nebula/compare/3.2.1...3.2.2) (2024-04-27)


### Bug Fixes

* Update default packages in linux_patching role ([#9](https://github.com/arpanrec/arpanrec.nebula/issues/9)) ([e000295](https://github.com/arpanrec/arpanrec.nebula/commit/e000295b7836fc32537e068e8c658e6dc200930c))

## [3.2.1](https://github.com/arpanrec/arpanrec.nebula/compare/3.2.0...3.2.1) (2024-04-27)


### Bug Fixes

* maintenance ([#8](https://github.com/arpanrec/arpanrec.nebula/issues/8)) ([8242115](https://github.com/arpanrec/arpanrec.nebula/commit/8242115ac73a7e8599618f21ebbf7e1d33e83270))

# [3.2.0](https://github.com/arpanrec/arpanrec.nebula/compare/3.1.0...3.2.0) (2024-03-25)


### Features

* python3 toolchain ([2d27279](https://github.com/arpanrec/arpanrec.nebula/commit/2d27279e56911e6f62ef090e4a4596b4c26fc2ee))

# [3.1.0](https://github.com/arpanrec/arpanrec.nebula/compare/3.0.0...3.1.0) (2024-03-23)


### Features

* 2024.2.1 bw cli ([a77db9b](https://github.com/arpanrec/arpanrec.nebula/commit/a77db9bb6184526f8fca849b79ab105a7e5b4d48))

# [3.0.0](https://github.com/arpanrec/arpanrec.nebula/compare/2.0.3...3.0.0) (2024-02-20)


### Features

* Add WTFPL license ([c0d0053](https://github.com/arpanrec/arpanrec.nebula/commit/c0d00531794af7ae90878780f72cedae5650ce8e))


### BREAKING CHANGES

* Adding build ignore and copying changes

## [2.0.3](https://github.com/arpanrec/arpanrec.nebula/compare/2.0.2...2.0.3) (2024-02-20)


### Bug Fixes

* remove neovim ([84dc4d6](https://github.com/arpanrec/arpanrec.nebula/commit/84dc4d6d13e9677f25a346a064e3be2338337ca7))

## [2.0.2](https://github.com/arpanrec/nebula/compare/2.0.1...2.0.2) (2024-02-16)


### Bug Fixes

* Refactor dotfiles tasks and templates ([ab41987](https://github.com/arpanrec/nebula/commit/ab419874e5b0d3614b804724ac8fc1e994304173))

## [2.0.1](https://github.com/arpanrec/nebula/compare/2.0.0...2.0.1) (2024-02-15)


### Bug Fixes

* docs remove KDE konsave ([d88bf51](https://github.com/arpanrec/nebula/commit/d88bf51f54415a24e645aadc40e10dad7778db85))

# [2.0.0](https://github.com/arpanrec/nebula/compare/1.0.5...2.0.0) (2024-02-15)


### Features

* Remove KDE-related files and configurations ([#7](https://github.com/arpanrec/nebula/issues/7)) ([a7c0b14](https://github.com/arpanrec/nebula/commit/a7c0b14b22024235b9499ae4ed5b2b1299de51d9))


### BREAKING CHANGES

* * Remove KDE-related files and configurations

* Remove molecule_test_role_kde from ansible_molecule.yml

* Add import statement for requests module

* Update semantic-release dependencies

## [1.0.5](https://github.com/arpanrec/nebula/compare/1.0.4...1.0.5) (2024-01-30)


### Bug Fixes

* 4 spaces for yaml ([#6](https://github.com/arpanrec/nebula/issues/6)) ([2f8edac](https://github.com/arpanrec/nebula/commit/2f8edac11796f8b33ff2de26a63a42f32ecfb996))

## [1.0.4](https://github.com/arpanrec/nebula/compare/1.0.3...1.0.4) (2024-01-14)


### Bug Fixes

* Update author email in pyproject.toml ([ff1623d](https://github.com/arpanrec/nebula/commit/ff1623de34f639670bf3bc5e8db415282bb82629))

## [1.0.3](https://github.com/arpanrec/nebula/compare/1.0.2...1.0.3) (2024-01-14)


### Bug Fixes

* Update release.config.js to include pyproject.toml ([e1ff9f5](https://github.com/arpanrec/nebula/commit/e1ff9f5c94f3be898528dd8af7b079c10e8bb6cd))

## [1.0.2](https://github.com/arpanrec/nebula/compare/1.0.1...1.0.2) (2024-01-14)


### Bug Fixes

* Update release workflow to remove unnecessary command ([c6f1954](https://github.com/arpanrec/nebula/commit/c6f195429f51d8b0d3b0d635c357a4cceb741a5f))

## [1.0.1](https://github.com/arpanrec/nebula/compare/1.0.0...1.0.1) (2024-01-14)


### Bug Fixes

* Add ignored files to build_ignore list ([df1c2e2](https://github.com/arpanrec/nebula/commit/df1c2e2b7930edd1bdfaefbd1eec43a53d38b68b))
* Update version number in pyproject.toml ([37b6aff](https://github.com/arpanrec/nebula/commit/37b6aff3b226120b7f2feed8208672f916020b4a))

# 1.0.0 (2024-01-13)


### Features

* bring in the code ([b98147d](https://github.com/arpanrec/nebula/commit/b98147d5ea654645651bdb46db46b8c79f547851))
* bring in the code ([7320ad5](https://github.com/arpanrec/nebula/commit/7320ad5f32d8c129b3956d5b424218c8286dd909))


### BREAKING CHANGES

* first commit
* first commit

# 1.0.0 (2024-01-13)


### Bug Fixes

* delegate_to: localhost ([#84](https://github.com/arpanrec/nebula/issues/84)) ([ad15a42](https://github.com/arpanrec/nebula/commit/ad15a42a1e2e65ae8a3d514150e6a2ff28d8b21d))
* Download Check ([44ac233](https://github.com/arpanrec/nebula/commit/44ac233494dbc02a19e997ab1b0ce7ca9afca3c5))
* release exe ([4f8d4aa](https://github.com/arpanrec/nebula/commit/4f8d4aa592f217ef5c5be8c476c9b930afaf4f91))
* requirements.txt to reduce vulnerabilities ([#103](https://github.com/arpanrec/nebula/issues/103)) ([98ca6c6](https://github.com/arpanrec/nebula/commit/98ca6c6dda28f049ab53f2df6ccc07e1d6837c13))
* requirements.txt to reduce vulnerabilities ([#104](https://github.com/arpanrec/nebula/issues/104)) ([60e8bb5](https://github.com/arpanrec/nebula/commit/60e8bb530064351bd6934024e5bc869514113490))


### Feat

* Groovy, Patch, telegram ([acfc2b2](https://github.com/arpanrec/nebula/commit/acfc2b262404bdd0b8fef983c329a1cba796078c))


### Features

* add kotlin support ([bf1f654](https://github.com/arpanrec/nebula/commit/bf1f654a5f4435c4546ccec7350bcc9a45ff2ab0))
* added kotlin compile ([41d9220](https://github.com/arpanrec/nebula/commit/41d922045c096ef9d25898b36a8187d52b7c57e2))
* Ansible lint ([d7d348a](https://github.com/arpanrec/nebula/commit/d7d348ae4adf40639bc9504180f3fed44002fae8))
* auto release ([#3](https://github.com/arpanrec/nebula/issues/3)) ([fc77058](https://github.com/arpanrec/nebula/commit/fc770582fb11bab04976ed8c588141acd3293acb))
* Bitwarden Dynamic Version ([d5f471c](https://github.com/arpanrec/nebula/commit/d5f471c2f8dc9bf6e9d070c788c386c90418c610))
* Gather Facts ([5522998](https://github.com/arpanrec/nebula/commit/5522998223c3c0388c0d4fce0c26dce37fb4674f))
* Get Dynamic Latest version of java tools ([07018ea](https://github.com/arpanrec/nebula/commit/07018ea888dd23f2a3998b5de826c6980935d2b5))
* Golang Dynamic version ([#79](https://github.com/arpanrec/nebula/issues/79)) ([04882c0](https://github.com/arpanrec/nebula/commit/04882c08fc45a7a7f0ebc26037f054c351e6de44))
* moved to github arpanrec as user ([#102](https://github.com/arpanrec/nebula/issues/102)) ([9824866](https://github.com/arpanrec/nebula/commit/9824866f602deaebeb8b2f0b7b909f3c63e69dca))
* Update release branch to main and configure GPG signing ([#4](https://github.com/arpanrec/nebula/issues/4)) ([d482838](https://github.com/arpanrec/nebula/commit/d482838691a7dffcc63ba56ca0c92bf71ab0c394))


### BREAKING CHANGES

* Removed terraform cloud managed role, it's moved to plugin
* Added kotlin, and java env setup
* Added Groovy SDK, Bug Fixed to telegram unzip, Added XZ Utils to Linux patch
