import hashlib

## http://chal.hkcert23.pwnable.hk:28301/js/app.38bf3c86.js
CHECKERS = (
    # 'checker: e => f(e.substr(0, 8)).startsWith("b08c89")',
    ('f', 10, 'ce45fd'),
    ('p', 12, '87b3c7'),
    ('p', 14, 'd0687a'),
    ('p', 16, 'cbe2c9'),
    ('p', 18, 'c25dd2'),
    ('p', 20, 'b72709'),
    ('f', 22, '8b035b'),
    ('p', 24, '40f34c'),
    ('p', 26, '7be965'),
    ('f', 28, '0b67cb'),
    ('f', 30, 'bf7eeb'),
    ('p', 32, 'f9f48b'),
    ('f', 34, '69260f'),
    ('p', 36, '7ef31a'),
    ('p', 38, 'e3c817'),
    ('f', 40, '8a9de8'),
    ('p', 42, 'e3c817'),
)

algorithms = {'p': hashlib.sha256, 'f': hashlib.sha224}
flag = b'hkcert23{'

for checker in CHECKERS:
    algorithm = algorithms[checker[0]]
    length = checker[1]
    hashstarts = checker[2]
    padding_length = length - len(flag)

    for padding_ascii_7 in range(1 << (padding_length * 7)):
        padding_ascii_8 = 0
        remaining = padding_ascii_7
        while remaining:
            padding_ascii_8 = (padding_ascii_8 << 8) + (remaining & 0x7f)
            remaining >>= 7

        result = flag + padding_ascii_8.to_bytes((padding_ascii_8.bit_length()+7)//8, 'big')
        if algorithm(result).hexdigest().startswith(hashstarts):
            flag = result
            print(flag.decode())
            break
    else:
        exit(233)
