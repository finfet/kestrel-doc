# Getting Started

## Installation

[Download Kestrel](https://getkestrel.com/download/)


## Usage Examples

Generate a new private key
```
kestrel key gen -o keyring.txt
```

Encrypt a file
```
kestrel encrypt example.txt --to alice --from alice -k keyring.txt
```

Decrypt a file
```
kestrel decrypt example.txt.ktl -t alice
```

Encrypt a file using a password
```
kestrel pass enc example.txt
```


## Key Management

Keys are stored in a simple configuration file.

Here is an example
```
[Key]
Name = alice
PublicKey = 3663fiXFmDLOU6JBgD/XsLzopZ4NSbafwu/swCsKtDfn0tOV
PrivateKey = AAE+JlahluaAjaOg4U/V8g1HKZKmQ24J6bt0wE1u9BxnCoLOGaoMDxWOs5ncdp6LdYM7vs5j12El8FyLS8gU4JjO

[Key]
Name = bob
PublicKey = g4Yms3Wq9stLOCzCAA7LgFnoDahpKZIzvnqZFO4DD2kmfYpf

# Lines starting with # are ignored
```

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
