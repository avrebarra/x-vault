# x-vault
simple primitive secret management experiment using openssl asymmetric encryption glued with python scripting

## Required
To test out this x requires:
- python3
- openssl

## Usage
### Initializing
Vault requires a public and private RSA key pair. If you dont have one, you can generate one with openssl:
```sh
# setup key
ssh-keygen -f keys/rsa.key
ssh-keygen -m pem -f keys/rsa.key
openssl rsa -in ./keys/rsa.key -pubout -outform pem > ./keys/rsa.key.pub

# remove placeholder
$ rm ./vault/*
```

### Baking variable to vault
> **To bake the vault you need public key (`rsa.key.pub`)**

Baking as simple as:
```sh
# bake vault
$ python3 bin/bake.py "afaladb" "mysql://localhost:3306/organizer?user=root&password=root"
baking value into afaladb...
done
```

### Yielding variable from vault
> **To yield/unbake you need private key (`rsa.key`).**

Unbaking key from vault:
```sh
# yield/unbake key from vault
$ python3 bin/yield.py "afaladb"
mysql://localhost:3306/organizer?user=root&password=root
```

## References
- https://www.czeskis.com/random/openssl-encrypt-file.html