import hmac
import hashlib
from pwn import *
import itertools


def sign_message(key_client: bytes, key_server: bytes, message: str) -> bytes:
    key_combined = xor(key_client, key_server)

    signature = hmac.new(key_combined, message.encode(), hashlib.sha256).digest()
    return signature

def sign(r, key_client: bytes, message: str):
    r.sendlineafter('🎬 '.encode(), b'sign')
    r.sendlineafter('🔑 '.encode(), key_client.hex().encode())
    r.sendlineafter('💬 '.encode(), message.encode())
    r.recvuntil('📝 '.encode())
    return bytes.fromhex(r.recvline().decode().strip())

def get_flag(r, key_server: bytes):
    signature = sign_message(b'\0'*16, key_server, 'gib flag pls')

    r.sendlineafter('🎬 '.encode(), b'verify')
    r.sendlineafter('💬 '.encode(), b'gib flag pls')
    r.sendlineafter('📝 '.encode(), signature.hex().encode())


if __name__ == '__main__':
    r = remote('chal.hkcert23.pwnable.hk', 28029)

    key_server = b''

    for i in range(2, 18, 2):
        s = sign(r, b'\0'*(i), 'testing')

        for guess in range(256*256):
            key_server_guess = key_server + int.to_bytes(guess, 2, 'big')
            if sign_message(b'\0'*(i), key_server_guess, 'testing') != s: continue
            key_server = key_server_guess
            break
        print(f'{key_server = }')

    get_flag(r, key_server)

    r.interactive()
