import glob
import sys
import os
import toml
import re

current_vault = {}

# parse args
args = sys.argv[1:]
key = args[0]
value = ""

# decrypt
name = key
fname = f"./vault/{name}"
keyfname = f"./vault/{name}.key"

os.system(
    f"openssl rsautl -decrypt -inkey keys/rsa.key -in vault/{name}.key -out vault/{name}.rawkey.tmp")

os.system(
    f"openssl enc -d -aes-256-cbc -in vault/{name} -out vault/{name}.raw.tmp -pass file:vault/{name}.rawkey.tmp")

# read value to vault obj
with open(f"vault/{name}.raw.tmp", 'r') as file:
    value = file.read().replace('\n', '')

# clean all tmp
for file in glob.glob('*/*.tmp'):
    os.remove(file)

# print value
print(value)
