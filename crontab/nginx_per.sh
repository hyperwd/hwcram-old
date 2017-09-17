#!/bin/bash            
fun_nginx(){
    a=$(netstat -lnpt |grep nginx|awk -F ' ' {'print $7'}|awk -F '/' {'print $2'})
    if  [ "$a" = 'nginx' ];then
        exit 0 
    else
        /usr/sbin/nginx 
    fi
}

for((i=1;i<=6;i++));do
    fun_nginx
    sleep 10                
done                   
