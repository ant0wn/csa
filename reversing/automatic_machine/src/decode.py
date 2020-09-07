import base64

with open('data/encoded.base64', 'rb') as encoded_file:
    decoded = base64.b64decode(encoded_file.readline()).decode()

print(f'{decoded}')
