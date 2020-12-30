# x-vault
simple primitive secret management experiment using openssl asymmetric encryption glued with python scripting

## Required
To test out this x requires:
- pip & python3
- openssl
- make

## Usage
### Initializing
Vault requires a public and private RSA key pair. If you dont have one, you can generate one with openssl:
```sh
$ make init
```

### Baking and unbaking vault
> **To bake the vault you only need public key. To unbake you need private key.**

Baking and unbaking vault are as simple as:
```sh
# unbake default vault file
$ make unbake
unbaking...
done

# see unbaked vault file (or update it as you want)
$ cat vault.conf
[vault]
samantha = mysql://localhost:3306/organizer?user=root&password=root
meta = mysql://localhost:3306/organizer?user=root&password=root
corona = mysql://localhost:3306/organizer?user=root&password=root
afala = mysql://localhost:3306/organizer?user=root&password=root
core = 37a31642-7d70-40d9-a754-499a6ff0806f
subcore = 9b229056-8e83-42fe-ba08-3eafe477ac09

# rebake vault.conf file
$ make bake
baking...
done
```


## References
- https://www.czeskis.com/random/openssl-encrypt-file.html