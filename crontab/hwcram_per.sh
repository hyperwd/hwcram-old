#!/bin/bash            
fun_hwcram(){
    hwcram_pid=$(ps -ef|grep hwcram.py|grep -v grep|awk  '{if($3 == 1) print $2}')
    if  [ "$hwcram_pid" -gt 0 ];then
        exit 0 
    else
        /bin/bash /opt/hwcram/utils/start.sh
    fi
}

for((i=1;i<=6;i++));do
    fun_hwcram
    sleep 10                
done                   
