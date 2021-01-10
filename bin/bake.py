import os
import sys
import glob

# =========================================
#                 PREBAKE
# =========================================

# parse args
args = sys.argv[1:]
key = args[0]
value = args[1]

print(f"baking value into {key}...")

# ensure public key
if not os.path.isfile('keys/rsa.key.pub'):
    print('prebake/bake skipped: public key not found')
    sys.exit(1)

# baking data
fname = f"./vault/{key}.tmp"
f = open(fname, "w")
f.write(value)
f.close()

# generate encryption key
os.system("openssl rand -base64 128 > vault/rawkey.tmp")
os.system(
    f"openssl rsautl -encrypt -inkey ./keys/rsa.key.pub -pubin -in vault/rawkey.tmp -out vault/{key}.key")

# encrypt all files
os.system(
    f"openssl enc -aes-256-cbc -salt -in {fname} -out vault/{key} -pass file:vault/rawkey.tmp")

# clean all tmp
for file in glob.glob('*/*.tmp'):
    os.remove(file)

print("done")
sys.exit(0)
