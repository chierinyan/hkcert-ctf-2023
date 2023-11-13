import requests

base_url = 'http://chal-a.hkcert23.pwnable.hk:28231/encrypt'

c = requests.get(base_url+'/flag/').json()['ciphertext']
c = [int(c[i:i+16], 16) for i in range(0, len(c), 16)]

m = []
for i in range(1, len(c)):
    ciXc0 = (c[i] ^ c[0]).to_bytes(8, 'big').hex()
    miXci_1 = requests.get(base_url+'/?m='+ciXc0).json()['ciphertext'][16:32]
    m.append(int(miXci_1, 16) ^ c[i-1])

print(''.join(map(lambda x: x.to_bytes(8, 'big').decode(), m)))
