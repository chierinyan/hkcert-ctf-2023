with open('./readfile.asm') as srcf:
    src = srcf.readlines()

bol = "JMP {}\nJMP "
jmpscare = ''

for line in src:
    jmpscare += bol.format(hex( 0x400000 + len(jmpscare) + 17 )) + line

print(jmpscare)

## hkcert23{jump_1n70_m1dd13_0f_1n57ruc710n_1s_r34l1y_fun}
