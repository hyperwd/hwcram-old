#!/bin/bash            
fun_uwsgi(){
    a=$(netstat -lnpt|grep uwsgi |awk  '{print $7 }'|awk -F '/' '{print $2}')
    if  [ "$a" = 'uwsgi' ];then
        exit 0 
    else
        /usr/local/bin/uwsgi --ini /opt/hwcram/web/hostinfo/hostinfo_uwsgi.ini -d /var/log/hostinfo/uwsgi.log
    fi
}

for((i=1;i<=6;i++));do
    fun_uwsgi
    sleep 10                
done                   
