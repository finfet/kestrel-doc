+++
title = "Kestrel Releases"
description = "Download a release of Kestrel"
[extra]
nav_page = "releases"
css_file = "releases.css"
+++

# Download Kestrel

## Relase v1.0.0

28 Dec 23

### Changes

- The file format is now stable. All Kestrel files encrypted with this version
  will be able to be decrypted with future Kestrel versions. Kestrel is ready
  for production.
- Output files are no longer overwritten during a failed decryption attempt.
- Improved error messages when decrypting unsupported files.
- Added check to ensure the input and output file locations differ.

### Download

- **[.deb x86_64](/releases/v1.0.0/kestrel_1.0.0-1_amd64.deb)**
- **[.rpm x86_64](/releases/v1.0.0/kestrel-1.0.0-1.x86_64.rpm)**
- **[Windows Installer](/releases/v1.0.0/kestrel-cli-setup-v1.0.0-x64.exe)**
- **[Source Code](/releases/v1.0.0/kestrel-1.0.0.tar.gz)**
- **[SHA256SUMS.txt](/releases/v1.0.0/SHA256SUMS.txt)**
- [kestrel-1.0.0-1.aarch64.rpm](/releases/v1.0.0/kestrel-1.0.0-1.aarch64.rpm)
- [kestrel-linux-v1.0.0-amd64.tar.gz](/releases/v1.0.0/kestrel-linux-v1.0.0-amd64.tar.gz)
- [kestrel-linux-v1.0.0-arm64.tar.gz](/releases/v1.0.0/kestrel-linux-v1.0.0-arm64.tar.gz)
- [kestrel-macos-v1.0.0-amd64.tar.gz](/releases/v1.0.0/kestrel-macos-v1.0.0-amd64.tar.gz)
- [kestrel-macos-v1.0.0-arm64.tar.gz](/releases/v1.0.0/kestrel-macos-v1.0.0-arm64.tar.gz)
- [kestrel-windows-v1.0.0-x64.zip](/releases/v1.0.0/kestrel-windows-v1.0.0-x64.zip)
- [kestrel_1.0.0-1_arm64.deb](/releases/v1.0.0/kestrel_1.0.0-1_arm64.deb)

**Homebrew**

`brew tap finfet/kestrel`  
`brew install kestrel-cli`

**Arch Linux**

[AUR](https://aur.archlinux.org/packages/kestrel)

- - - - -

## Release v0.11.0

25 Sep 23

### Changes

- Added the abilility to input and output data using unix pipes.
- Changed the format of private keys. The private key format's salt value has
  been increase from 16 to 32 bytes in order to give encrypted private keys
  the same security properties as password encrypted files.
- Changed the file format of key encrypted files. The noise handshake hash
  is now bound to the payload key for improved security.

**Note:**

**THIS IS A BREAKING RELEASE**

All files that were encrypted with versions prior to this will no longer
decrypt. You must decrypt any files with the previous version and then
re-encrypt them with the new version. All private keys must also be regenerated.

No changes to the file formats are expected after the 1.0.0 release.

### Download

- **[.deb x86_64](/releases/v0.11.0/kestrel_0.11.0-1_amd64.deb)**
- **[.rpm x86_64](/releases/v0.11.0/kestrel-0.11.0-1.x86_64.rpm)**
- **[Windows Installer](/releases/v0.11.0/kestrel-cli-setup-v0.11.0-x64.exe)**
- **[Source Code](/releases/v0.11.0/kestrel-0.11.0.tar.gz)**
- **[SHA256SUMS.txt](/releases/v0.11.0/SHA256SUMS.txt)**
- [kestrel-0.11.0-1.aarch64.rpm](/releases/v0.11.0/kestrel-0.11.0-1.aarch64.rpm)
- [kestrel-linux-v0.11.0-amd64.tar.gz](/releases/v0.11.0/kestrel-linux-v0.11.0-amd64.tar.gz)
- [kestrel-linux-v0.11.0-arm64.tar.gz](/releases/v0.11.0/kestrel-linux-v0.11.0-arm64.tar.gz)
- [kestrel-macos-v0.11.0-amd64.tar.gz](/releases/v0.11.0/kestrel-macos-v0.11.0-amd64.tar.gz)
- [kestrel-macos-v0.11.0-arm64.tar.gz](/releases/v0.11.0/kestrel-macos-v0.11.0-arm64.tar.gz)
- [kestrel-windows-v0.11.0-x64.zip](/releases/v0.11.0/kestrel-windows-v0.11.0-x64.zip)
- [kestrel_0.11.0-1_arm64.deb](/releases/v0.11.0/kestrel_0.11.0-1_arm64.deb)

**Homebrew**

`brew tap finfet/kestrel`  
`brew install kestrel-cli`

**Arch Linux**

[AUR](https://aur.archlinux.org/packages/kestrel)

- - - - -

## Release v0.10.1

20 Jan 23

### Changes

- Fixed a crash when running kestrel key
- Improved cli error message output

### Download

- **[.deb x86_64](/releases/v0.10.1/kestrel_0.10.1-1_amd64.deb)**
- **[.rpm x86_64](/releases/v0.10.1/kestrel-0.10.1-1.x86_64.rpm)**
- **[Windows Installer](/releases/v0.10.1/kestrel-cli-setup-v0.10.1-x64.exe)**
- **[Source Code](/releases/v0.10.1/kestrel-0.10.1.tar.gz)**
- **[SHA256SUMS.txt](/releases/v0.10.1/SHA256SUMS.txt)**
- [kestrel-0.10.1-1.aarch64.rpm](/releases/v0.10.1/kestrel-0.10.1-1.aarch64.rpm)
- [kestrel-linux-v0.10.1-amd64.tar.gz](/releases/v0.10.1/kestrel-linux-v0.10.1-amd64.tar.gz)
- [kestrel-linux-v0.10.1-arm64.tar.gz](/releases/v0.10.1/kestrel-linux-v0.10.1-arm64.tar.gz)
- [kestrel-macos-v0.10.1-amd64.tar.gz](/releases/v0.10.1/kestrel-macos-v0.10.1-amd64.tar.gz)
- [kestrel-macos-v0.10.1-arm64.tar.gz](/releases/v0.10.1/kestrel-macos-v0.10.1-arm64.tar.gz)
- [kestrel-windows-v0.10.1-x64.zip](/releases/v0.10.1/kestrel-windows-v0.10.1-x64.zip)
- [kestrel_0.10.1-1_arm64.deb](/releases/v0.10.1/kestrel_0.10.1-1_arm64.deb)

**Homebrew**

`brew tap finfet/kestrel`  
`brew install kestrel-cli`

**Arch Linux**

[AUR](https://aur.archlinux.org/packages/kestrel)

- - - - -

## Release v0.10.0

08 Aug 22

### Changes

- Native .deb, .rpm and homebrew packages.
- Bash completion and man pages for Linux and macOS.
- A warning is displayed if an empty password is used.
- Updated cryptography depdendency version.

### Download

- [kestrel_0.10.0-1_amd64.deb](/releases/v0.10.0/kestrel_0.10.0-1_amd64.deb)
- [kestrel_0.10.0-1_arm64.deb](/releases/v0.10.0/kestrel_0.10.0-1_arm64.deb)
- [kestrel-0.10.0-1.fc36.aarch64.rpm](/releases/v0.10.0/kestrel-0.10.0-1.fc36.aarch64.rpm)
- [kestrel-0.10.0-1.fc36.x86_64.rpm](/releases/v0.10.0/kestrel-0.10.0-1.fc36.x86_64.rpm)
- [kestrel-0.10.0.tar.gz](/releases/v0.10.0/kestrel-0.10.0.tar.gz)
- [kestrel-cli-setup-v0.10.0-x64.exe](/releases/v0.10.0/kestrel-cli-setup-v0.10.0-x64.exe)
- [kestrel-linux-v0.10.0-amd64.tar.gz](/releases/v0.10.0/kestrel-linux-v0.10.0-amd64.tar.gz)
- [kestrel-linux-v0.10.0-arm64.tar.gz](/releases/v0.10.0/kestrel-linux-v0.10.0-arm64.tar.gz)
- [kestrel-macos-v0.10.0-amd64.tar.gz](/releases/v0.10.0/kestrel-macos-v0.10.0-amd64.tar.gz)
- [kestrel-macos-v0.10.0-arm64.tar.gz](/releases/v0.10.0/kestrel-macos-v0.10.0-arm64.tar.gz)
- [kestrel-windows-v0.10.0-x64.zip](/releases/v0.10.0/kestrel-windows-v0.10.0-x64.zip)
- [SHA256SUMS.txt](/releases/v0.10.0/SHA256SUMS.txt)
