# x-vault
simple primitive secret management experiment using openssl asymmetric encryption glued with python scripting

## Required
To test out this x requires:
- openssl
- python
- make

## Usage
### Initializing
Vault requires rsa_id registered in `~/.ssh/id_rsa`. If it's not already exist, you can generate one for host machine with:
```sh
$ ssh-keygen
```

And setup vault project with:
```sh
$ make init # will setup keys folder
```

### Baking and unbaking vault
Baking and unbaking vault are as simple as:
```sh
# unbake default vault file
$ make unbake
unbaking...
done

# see unbaked vault file (or update it as you want)
$ cat vault.conf
[mysql_access]
samantha = mysql://localhost:3306/organizer?user=root&password=root
meta = mysql://localhost:3306/organizer?user=root&password=root
corona = mysql://localhost:3306/organizer?user=root&password=root
afala = mysql://localhost:3306/organizer?user=root&password=root

[redis_access]
core = 37a31642-7d70-40d9-a754-499a6ff0806f
subcore = 9b229056-8e83-42fe-ba08-3eafe477ac09

# rebake vault.conf file
$ make bake
baking...
done
```

## References
- https://www.czeskis.com/random/openssl-encrypt-file.html