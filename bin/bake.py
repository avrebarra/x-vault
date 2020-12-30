import os
import sys
import glob
import re
import toml

# =========================================
#                 PREBAKE
# =========================================

# ensure public key
if not os.path.isfile('keys/rsa.key.pub'):
    print('prebake/bake skipped: public key not found')
    sys.exit(1)

# check for vault file
if os.path.isfile('vault.conf'):
    print('vault.conf file found!')
    vault_data = toml.load("vault.conf")

    # join data
    data = toml.load(f"vault.conf")['vault']
    for k in data:
        print("baking", k)

        # write new file
        fname = f"./vault/{k}.tmp"
        f = open(fname, "w")
        f.write(data[k])
        f.close()

        # generate encryption key
        os.system("openssl rand -base64 128 > vault/rawkey.tmp")
        os.system(
            f"openssl rsautl -encrypt -inkey ./keys/rsa.key.pub -pubin -in vault/rawkey.tmp -out vault/{k}.key")

        # encrypt all files
        os.system(
            f"openssl enc -aes-256-cbc -salt -in {fname} -out vault/{k} -pass file:vault/rawkey.tmp")

        # clean file
        os.remove(fname)

    # clean source file
    os.system("rm vault.conf")


# clean all tmp
for file in glob.glob('*/*.tmp'):
    os.remove(file)
