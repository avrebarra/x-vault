import os

# generate public key
os.system("openssl rsa -in ~/.ssh/id_rsa -outform pem > ./keys/rsa.pem.key")
os.system("openssl rsa -in ./keys/rsa.pem.key -pubout -outform pem > ./keys/rsa.pub.pem.key")
