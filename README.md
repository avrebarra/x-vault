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
$ rm ./vault/*
```

### Baking and unbaking vault
> **To bake the vault you need public key (`rsa.key.pub`)**

> **To unbake you need private key (`rsa.key`).**

Baking and unbaking vault are as simple as:
```sh
# test with sample vault file
$ cp vault.conf.sample vault.conf
$ cat vault.conf
[vault]
afala = "mysql://localhost:3306/organizer?user=root&password=root"
meta = "mysql://localhost:3306/organizer?user=root&password=root"
subcore = "9b229056-8e83-42fe-ba08-3eafe477ac09"
samantha = "mysql://localhost:3306/organizer?user=root&password=root"
corona = "mysql://localhost:3306/organizer?user=root&password=root"
core = "37a31642-7d70-40d9-a754-499a6ff0806f"

# bake vault
$ make bake
vault.conf file found!
baking afala
baking meta
baking subcore
baking samantha
baking corona
baking core
done

# unbake vault file
$ make unbake
afala
meta
subcore
samantha
corona
core
done
```

### Updating only one key
> **Again, to update a key you need the public key (`rsa.key.pub`)**

You can update a key by adding the specified key to vault.conf file:
```sh
$ nano vault.conf
$ cat vault.conf
[vault]
core = "updated_value"

$ make bake
vault.conf file found!
baking core
done

$ make unbake
afala
meta
subcore
samantha
corona
core
done

$ cat vault.conf
[vault]
afala = "mysql://localhost:3306/organizer?user=root&password=root"
meta = "mysql://localhost:3306/organizer?user=root&password=root"
subcore = "9b229056-8e83-42fe-ba08-3eafe477ac09"
samantha = "mysql://localhost:3306/organizer?user=root&password=root"
corona = "mysql://localhost:3306/organizer?user=root&password=root"
core = "updated_value"

```


## References
- https://www.czeskis.com/random/openssl-encrypt-file.html