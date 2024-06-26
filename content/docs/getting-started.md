+++
title = "Getting Started"
description = "Get started with Kestrel"
[extra]
nav_page = "getting-started"
+++

# Getting Started

## Installation

Make sure that you have the application installed. See [installation](@/docs/installation.md)
for more.

## Generate a new key pair

Follow the prompts to give the key a name, and encrypt it with the
password you choose.

The name can be anything that helps you remember your key. A name, nickname,
or email are good ideas. In the example Alice is generating a key for herself.

```
kestrel key generate -o keyring.txt
```

The result is a file that looks like this:

```
[Key]
Name = alice
PublicKey = D7ZZstGYF6okKKEV2rwoUza/tK3iUa8IMY+l5tuirmzzkEog
PrivateKey = ZWdrMPEp09tKN3rAutCDQTshrNqoh0MLPnEERRCm5KFxvXcTo+s/Sf2ze0fKebVsQilImvLzfIHRcJuX8kGetyAQL1VchvzHR28vFhdKeq+NY2KT
```

This is an example key. Do not use this. Make sure to generate
your own.

A `[Key]` has three properties: `Name`, `PublicKey`, `PrivateKey`.

`Name` is a nickname for a `PublicKey`. It's short so that you don't have to
type the `PublicKey` each time. You'll use `Name` to refer to specific public
keys, so each name should be something unique that reminds you of the person
that owns that key. Remember that you are also a person with a `PublicKey` so
you can encrypt files for yourself.

`PublicKey` is the public identifier for a key. Your friends will use this
public key to send you files. You can post the `PublicKey` anywhere. Post it
on social media, e-mail it to your friends, whatever works. Just make sure
that they have a good copy of your public key.

`PrivateKey` must be kept secret. Never share it. To be able to decrypt
files that are sent to you, you'll need to know the private key
string and the password used to unlock it. If you lose your private key you
will no longer be able to decrypt files. Keep a backup of the private key
somewhere safe.


## Encrypt a file using a key

Let's encrypt an example file. Alice is using a file called `example.txt`. You
can use any file that you want. Grab a file from your computer and try it out.

Here Alice is encrypting a file **to** the key `alice` and **from** the key `alice`.

She is encrypting the file to herself. This is a great way to keep backups
secure from online storage providers.

When encrypting a file, think of it like addressing a letter. The destination
`--to` is a public key with a name. And the `--from` is the sender's key.

```
kestrel encrypt example.txt --to alice --from alice -o example.txt.ktl -k keyring.txt
```

This results in a file called `example.txt.ktl` that only Alice can read
and decrypt.

Kestrel also supports pipes, so you could do something like this:
```
cat example.txt | kestrel enc -t alice -f alice > example.txt.ktl -k keyring.txt
```

## Decrypt a file

To decrypt Alice uses

```
kestrel decrypt example.txt.ktl -t alice -o example.txt -k keyring.txt
```

The result is the decrypted example.txt that Alice can view. For the `--to`
option, Alice chose her key, because she knows that the key was sent to her.
Upon successful decryption, Alice she can see that the file was sent from
the `alice` key.

To decrypt a file, you'll need to know the key that the file was sent to.
If you only have one key pair, this will always be your only key. However, if
you have multiple keys, like for work and school, when trying to decrypt the
file you'll need to know if you should use the work key or the school key.

## Adding a Public Key

Alice just met Bob and got Bob's public key from social media.

Bob's public key is
```
g4Yms3Wq9stLOCzCAA7LgFnoDahpKZIzvnqZFO4DD2kmfYpf
```

Alice can add Bob's key by modifying `keyring.txt` and adding another `[Key]`
section.
```
[Key]
Name = bob
PublicKey = g4Yms3Wq9stLOCzCAA7LgFnoDahpKZIzvnqZFO4DD2kmfYpf
```

Name can be anything that helps Alice identify Bob.


Now Alice can encrypt a file for Bob using his key.
```
kestrel encrypt example.txt --to bob --from alice -k keyring.txt -o example.txt.ktl
```

The result is a file `example.txt.ktl` that only Bob will be able to decrypt.
Alice can then send this file to Bob through e-mail or some other means.


## Default Keyring

Instead of having to use the `-k` option each time in order to specify the
location of the list of keys, you can set a default keyring that will be
used automatically.

To do this, set the environment variable `KESTREL_KEYRING` to the location
of the key file that you would like to use.


## Password Encryption

Instead of using Public Keys, you can also encrypt and decrypt files using passwords.

```
kestrel password encrypt example.txt -o example.txt.ktl
```

```
kestrel password decrypt example.txt.ktl -o example.txt
```

## Key Management

Public and private keys are simple Base64 strings. Put your public
key somewhere that your friends will have access to. Post it to social
media, email it out, whatever works.

When you want to encrypt a file to a friend, just copy their public key and
add it to your list of keys.

Private keys are always encrypted with your password. Make sure to choose
a strong password. Although the private key is encrypted, it's still a
good idea to keep it hidden.

As long as you have access to your private key and the password used to
unlock it, you'll be able to access your data. However, if you lose access to
the private key and/or password, you won't be able to decrypt any files sent
to that key.

You can change the password of a private key
```
kestrel key change-pass <BASE64-PRIVATE-KEY>
```

You can view the public key for a private key
```
kestrel key extract-pub <BASE64-PUBLIC-KEY>
```

## Usage Help

View all of the usage options
```
kestrel --help
```

## Security Guarantees

If decryption of a file is successful, you know for certain that the file
hasn't been tampered with and that it came from a specific known key.

See more in [security information](@/docs/security-information.md)
