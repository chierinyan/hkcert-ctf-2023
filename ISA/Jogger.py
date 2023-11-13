with open('./readfile.asm') as srcf:
    src = srcf.read()

hexstr = src.encode('utf-8').hex()
jogger = ['MOV R7, {base__}']

for i in range(0, len(hexstr), 8):
    word = hexstr[i:i+8]
    word = ''.join(reversed([word[j:j+2] for j in range(0, len(word), 2)]))
    word = word.ljust(8, '0')
    jogger.append(f'MOV [R7+{i//2}], 0x{word}')

jogger = '\n'.join(jogger)
print(jogger.format(base__=hex(len(jogger) + 0x400001)))

## hkcert23{m0v_1s_7ur1n9_c0mp1373_4nd_y0u_ju5t_v3r1fi3d_th4t_f0r_m3}
