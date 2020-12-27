import os
import sys
import glob
import re
import toml
from deepmerge import always_merger

# =========================================
#                 PREBAKE
# =========================================

# ensure public key
if not os.path.isfile('keys/rsa.key.pub'):
    print('prebake/bake skipped: public key not found')
    sys.exit(1)

# check for cauldron file
cauldron_files = glob.glob('cauldron.conf')
if len(cauldron_files) >= 1 :
    print('found cauldron file!')

    # encrypt all files
    for file in cauldron_files:
        print(f'prebaking: encrypting conf file {file}!')

        # generate encryption key
        os.system(f"openssl rand -base64 128 > {file}.rawkey.tmp")
        os.system(f"openssl rsautl -encrypt -inkey ./keys/rsa.key.pub -pubin -in {file}.rawkey.tmp -out {file}.key.prebake")

        # encrypt all files
        os.system(f"openssl enc -aes-256-cbc -salt -in {file} -out {file}.prebake -pass file:{file}.rawkey.tmp")

        # clean tmp file
        print("removing", f"{file}.rawkey.tmp")
        os.remove(f"{file}.rawkey.tmp")


# =========================================
#                  BAKE
# =========================================

# ensure private key
if not os.path.isfile('keys/rsa.key'):
    print('bake skipped: private key not found')
    sys.exit(0)

# check for prebaked cauldron files
prebaked_files = glob.glob('cauldron.conf.prebake')
if len(prebaked_files) >= 1 :
    print('prebaked files found in cauldron!')

    # unbake vault for concatenation
    os.system("make unbake")
    vault_data = toml.load("vault.conf")

    # decrypt all files
    for file in prebaked_files:
        print(f'prebaking: decrypting file {file}!')

        origin_file = re.sub('\.prebake$', '', file)

        # decrypt all files
        os.system(f"openssl rsautl -decrypt -inkey keys/rsa.key -in {origin_file}.key.prebake -out {origin_file}.rawkey.tmp")
        os.system(f"openssl enc -d -aes-256-cbc -in {origin_file}.prebake -out {origin_file} -pass file:{origin_file}.rawkey.tmp")

        # join data
        data = toml.load(f"{origin_file}")
        vault_data = always_merger.merge(vault_data,data)

        # delete bake file
        os.remove(f"{origin_file}")
        os.remove(f"{origin_file}.prebake")
        os.remove(f"{origin_file}.key.prebake")
        os.remove(f"{origin_file}.rawkey.tmp")

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
    os.system("openssl rsautl -encrypt -inkey ./keys/rsa.key.pub -pubin -in rawkey.tmp -out vault/key")

    # encrypt all files
    os.system("openssl enc -aes-256-cbc -salt -in vault.conf -out vault/vault -pass file:rawkey.tmp")

    # clean source file
    os.system("rm rawkey.tmp")
    os.system("rm vault.conf")