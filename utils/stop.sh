#!/bin/bash
kill -9 $(ps -ef|grep hwcram.py|grep -v grep|awk  '{if($3 == 1) print $2}')
