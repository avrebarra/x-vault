import glob
import os
import toml
import re

current_vault = {}

# read all key files
for file in glob.glob('vault/*.key'):
    name = re.sub('\.key$', '', file)
    name = re.sub('^vault/', '', name)
    print(name)

    # decrypt
    os.system(
        f"openssl rsautl -decrypt -inkey keys/rsa.key -in vault/{name}.key -out vault/{name}.rawkey.tmp")
    os.system(
        f"openssl enc -d -aes-256-cbc -in vault/{name} -out vault/{name}.raw.tmp -pass file:vault/{name}.rawkey.tmp")

    # read value to vault obj
    value = ""
    with open(f"vault/{name}.raw.tmp", 'r') as file:
        value = file.read().replace('\n', '')

    current_vault[name] = value


# write to vault.conf
f = open("vault.conf", "w")
f.write(toml.dumps({'vault': current_vault}))
f.close()

# clean all tmp
for file in glob.glob('*/*.tmp'):
    os.remove(file)
