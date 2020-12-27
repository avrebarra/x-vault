import os

# generate encryption key
os.system("openssl rand -base64 128 > rawkey.tmp")
os.system("openssl rsautl -encrypt -inkey ./keys/rsa.pub.pem.key -pubin -in rawkey.tmp -out vault/key")

# encrypt all files
os.system("openssl enc -aes-256-cbc -salt -in vault.conf -out vault/vault -pass file:rawkey.tmp")
