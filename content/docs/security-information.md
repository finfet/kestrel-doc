+++
title = "Security Information"
description = "Overview of Kestrel's security properies"
[extra]
nav_page = "security-information"
+++

# Security Information

## Overview

Kestrel uses a simple combination of the Noise Protocol and a
chunked file encryption scheme.

The noise protocol (Noise_X_25519_ChaChaPoly_SHA256) is used to encrypt a
payload key. This payload key is then used to derived a key for
ChaCha20-Poly1305 file encryption. Files are split into encrypted and
authenticated chunks, ensuring that unauthenticated data is never written to disk.

Users can also use a password instead of public keys. This password is used
with scrypt to derive a symmetric key for file encryption.


## Public Key Encryption

The X pattern of a noise protocol handshake is used to perform public key
authenticated encryption between sender and recipient.

In order to send a message, senders are required to obtain a legitimate copy
of the recipient's public key.

### Security Properties

**Overview**

- When you successfully decrypt a file, you know that the file hasn't been
  modified and that it came from a specific, known public key.
- Deniability. If you send a message and your recipient reveals it and tries
  to claim that you sent it, you can deny it because the recipient has the
  ability to forge received messages.
- If your private key gets compromised later, the attacker can't read the
  messages that you've sent. The only way to decrypt the messages is to
  compromise your recipient's private key.
- If your private key gets compromised, the attacker can pretend to be you.
  You need to get a new key pair and be able to communicate the new public key
  to your contacts.
- Messages can be replayed. Replay prevention is out of scope for this
  application. However, replay is considered benign in this context. Imagine
  sending your encrypted tax files to an accountant. The attacker can resend
  your encrypted file to the accountant, but the accountant will end up with a
  benign, redundant copy.
- The encryption is meant to work as you would expect it to. If you get a file,
  you know who it came from, and that it hasn't been read or tampered with.
  When you send a file, only the person that you sent it to can read it.

**Guarantees from the noise protocol**

Each payload is assigned a "source" property regarding the degree of
authentication of the sender provided to the recipient, and a "destination"
property regarding the degree of confidentiality provided to the sender.

_Source properties_

Sender authentication vulnerable to key-compromise impersonation (KCI).
The sender authentication is based on a static-static DH ("ss") involving both
parties' static key pairs. If the recipient's long-term private key has been
compromised, this authentication can be forged.

_Destination Properties_

Encryption to a known recipient, forward secrecy for sender compromise only,
vulnerable to replay. This payload is encrypted based only on DHs involving the
recipient's static key pair. If the recipient's static private key is
compromised, even at a later date, this payload can be decrypted. This message
can also be replayed, since there's no ephemeral contribution from the
recipient.

### Encryption Steps

1. A fresh 256 bit symmetric key is generated from a CSPRNG. This is the
   payload key.
2. A noise handshake is performed between the sender and recipient with the
   payload key included as the noise payload. The result is a noise handshake
   message that includes the encrypted payload key and the encrypted sender
   public key.
3. The plaintext is encrypted using the chunked encryption format with a key
   derived from the payload key.

### Decryption Steps

1. The recipient must choose to decrypt using the same key that the sender
   chose as the recipient key. Because the ciphertext contains no identifying
   information from either the sender or recipient, the recipient must choose
   the correct key pair from which to attempt decryption. If the recipient has,
   for example, a work key pair, and a personal key pair, the recipient must
   know to decrypt with either the work key or the personal key. Obviously
   decryption could be attempted with both keys if the recipient is unsure.
2. The recipient decrypts the noise handshake message. If successful, this
   results in the decrypted payload key and sender's public key.
3. The ciphertext is decrypted using the chunked encryption format with a
   key derived from the payload key. The sender's public key is displayed upon
   successful decryption.


## Password Encryption

Scrypt is used to derive a symmetric key from a password which is then used
with the chunked file encryption format.

### Security Properties

Files are encrypted and authenticated. After a successful decryption, you can
be certain that the file was not modified and that it came from the person in
possession of the shared password.

### Encryption and Decryption Steps

1. A symmetric key is derived from a password using the scrypt parameters
   N = 15, r = 8, and p = 1.
2. The file is encrypted or decrypted using the derived key and the chunked
   encryption format.

## Chunked File Format

Files may be too large to fit entirely into memory, so they are split into
into encrypted and authenticated chunks.

Each chunk has a chunk number starting from zero and incrementing
sequentially (0, 1, 2, 3, ...).

The chunk number is also used as the nonce for the encryption function. Keys
are fresh for each message ensure that the nonce does not repeat.

Chunks are 65,536 bytes (64k) in size.

The last chunk has an authenticated last chunk indicator signifying that this
is the last chunk in the message. The chunk number MUST increase sequentially
and MUST contain only a single last chunk indicator.

This design ensures that chunks in a message CANNOT be re-ordered, modified, removed, duplicated, or truncated.

Messages CANNOT be modified or truncated without detection.
