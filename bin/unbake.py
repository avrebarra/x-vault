import os
import toml
from deepmerge import always_merger

# cache changes
current_vault = {}
if os.path.isfile('vault.conf'):
    current_vault = toml.load("vault.conf")

# decrypt
os.system("openssl rsautl -decrypt -inkey keys/rsa.pem.key -in vault/key -out rawkey.tmp")
os.system("openssl enc -d -aes-256-cbc -in vault/vault -out vault.conf -pass file:rawkey.tmp")
unbaked_vault = toml.load("vault.conf")

# update vault.conf
f = open("vault.conf", "w")
f.write(toml.dumps(always_merger.merge(unbaked_vault, current_vault)))
f.close()

# remove tmp file
os.remove(f"rawkey.tmp")