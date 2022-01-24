# Installation

Download a [release](https://getkestrel.com/releases/)

Pick the file for your operating system.

Kestrel supports

- Linux on x86-64, arm64
- macOS on Apple Silicon (arm64), Intel
- Windows on x64 with a traditional installer or portable install.


## Linux

Extract the archive. (Replace with the name of your archive)
```
tar -xf kestrel-linux-v0.9.0-amd64.tar.gz
```

Put the binary somewhere on your PATH
```
cd kestrel-linux-v0.9.0-amd64
sudo cp kestrel /usr/local/bin
```

## macOS

Extract the archive. (Replace with the name of your archive)
```
tar -xf kestrel-macos-v0.9.0-arm64.tar.gz
```

You may need to remove the macOS quarantine attribute that is added to files
downloaded from the internet.
```
cd kestrel-macos-v0.9.0-arm64
xattr -d com.apple.quarantine kestrel
```

Put the binary somewhere on your PATH
```
sudo cp kestrel /usr/local/bin/
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

Use `sha256sum <archive-name.tar.g>`

**macOS**

Use `shasum -a 256 <archive-name.tar.gz>`

**Windows Powershell**

Use `Get-FileHash <the-archive.zip>`
