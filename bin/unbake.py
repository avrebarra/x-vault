import os

os.system("openssl rsautl -decrypt -inkey keys/rsa.pem.key -in vault/key -out rawkey.tmp")
os.system("openssl enc -d -aes-256-cbc -in vault/vault -out vault.conf -pass file:rawkey.tmp")