+++
title = "Installation"
description = "Kestrel installation"
[extra]
nav_page = "installation"
+++

# Installation

Download a [release](@/releases.md)

Pick the file for your operating system.

Kestrel supports

- Linux on x86-64, arm64
- macOS on Apple Silicon (arm64), Intel
- Windows on x64 with a traditional installer or portable install.


## Linux

### Debian / Ubuntu / .deb

Install the .deb package. Example:
```
sudo apt install ./kestrel_1.0.0-1_amd64.deb
```

Bash completion and man pages are included and automatically installed.

### Uninstall

```
sudo apt remove kestrel
```

### Fedora / .rpm

Install the .rpm package. Example:
```
sudo dnf install ./kestrel-1.0.0-1.fc36.x86_64.rpm
```

Bash completion and man pages are included and automatically installed.

### Uninstall

```
sudo dnf remove kestrel
```

### Arch Linux

kestrel is available on the [AUR](https://aur.archlinux.org/packages/kestrel)

Follow the normal installation procedure for AUR packages.

### Static Binary

Extract the `.tar.gz`. The binary can be run from anywhere.

Example to place the binary on your `$PATH`:
```
sudo cp kestrel /usr/local/bin
kestrel --version
```

## macOS

### Homebrew

```
brew tap finfet/kestrel
brew install kestrel-cli
kestrel --version
```

Bash completion and man pages are included and automatically installed.

### Static binary

Extract the `.tar.gz`. The binary can be run from anywhere.

You may need to remove the macOS quarantine attribute that is added to files
downloaded from the internet.
```
xattr -d com.apple.quarantine kestrel
```

Example to place the binary on your `$PATH`:
```
sudo cp kestrel /usr/local/bin/
```

### Uninstall

Remove binary
```
brew remove kestrel-cli
```

Uninstall tap
```
brew untap finfet/kestrel
```

## Windows

### Windows Installer

Follow the instructions on the installer. You may need to click through the
SmartScreen warning.

After installation, Kestrel can be used from powershell or command prompt
using the command `kestrel`.

### Portable Install

Unzip the archive. `kestrel.exe` can be run from any location that you
would like.


## SHA-256 Checksums

It's a good idea to make sure that what you downloaded matches the expected
file hash.

The SHA-256 hashes of the release can be found in the file `SHA256SUMS.txt`

**Linux**

Use `sha256sum <archive-name.tar.gz>`

**macOS**

Use `shasum -a 256 <archive-name.tar.gz>`

**Windows Powershell**

Use `Get-FileHash <the-archive.zip>`
