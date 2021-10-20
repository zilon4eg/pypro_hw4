import hashlib
import os


def md5(path):
    with open(os.path.join(os.getcwd(), path), encoding='utf-8') as file:
        for line in file:
            hash_object = hashlib.md5((line).encode())
            yield hash_object.hexdigest()


path = 'temp\countries_url.txt'
for hash in md5(path):
    print(hash)