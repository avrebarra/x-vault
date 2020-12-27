import os
import sys
import glob
import re
import toml

# =========================================
#                 PREBAKE
# =========================================

# ensure public key
if not os.path.isfile('keys/rsa.pub.pem.key'):
    print('prebake/bake skipped: public key not found')
    sys.exit(1)

# check for cauldron config file
cauldron_files = glob.glob('cauldron/*.conf')
if len(cauldron_files) >= 1 :
    print('conf files found in cauldron!')

    # encrypt all files
    for file in cauldron_files:
        print(f'prebaking: encrypting conf file {file}!')

        # generate encryption key
        os.system(f"openssl rand -base64 128 > {file}.rawkey.tmp")
        os.system(f"openssl rsautl -encrypt -inkey ./keys/rsa.pub.pem.key -pubin -in {file}.rawkey.tmp -out {file}.key.prebake")

        # encrypt all files
        os.system(f"openssl enc -aes-256-cbc -salt -in {file} -out {file}.prebake -pass file:{file}.rawkey.tmp")


# =========================================
#                  BAKE
# =========================================

def merge_copy(d1, d2): return {k: merge_copy(d1[k], d2[k]) if k in d1 and isinstance(d1[k], dict) and isinstance(d2[k], dict) else d2[k] for k in d2}

# ensure private key
if not os.path.isfile('keys/rsa.pem.key'):
    print('bake skipped: private key not found')
    sys.exit(0)

# check for prebaked cauldron files
prebaked_files = glob.glob('cauldron/*.conf.prebake')
if len(prebaked_files) >= 1 :
    print('prebaked files found in cauldron!')

    # unbake vault for concatenation
    os.system("make unbake")
    vault_data = toml.load("vault.conf")

    # decrypt all files
    for file in prebaked_files:
        print(f'prebaking: decrypting file {file}!')

        origfilename = re.sub('\.prebake$', '', file)

        # decrypt all files
        os.system(f"openssl rsautl -decrypt -inkey keys/rsa.pem.key -in {origfilename}.key.prebake -out {origfilename}.rawkey.tmp")
        os.system(f"openssl enc -d -aes-256-cbc -in {origfilename}.prebake -out {origfilename} -pass file:{origfilename}.rawkey.tmp")

        data = toml.load(f"{origfilename}")
        vault_data = merge_copy(vault_data,data)

    # update vault.conf
    f = open("vault.conf", "w")
    f.write(toml.dumps(vault_data))
    f.close()

# check for vault file
if os.path.isfile('vault.conf') :
    print('vault.conf file found!')
    vault_data = toml.load("vault.conf")

    # generate encryption key
    os.system("openssl rand -base64 128 > rawkey.tmp")
    os.system("openssl rsautl -encrypt -inkey ./keys/rsa.pub.pem.key -pubin -in rawkey.tmp -out vault/key")

    # encrypt all files
    os.system("openssl enc -aes-256-cbc -salt -in vault.conf -out vault/vault -pass file:rawkey.tmp")

    # clean source file
    os.system("rm rawkey.tmp")
    os.system("rm vault.conf")