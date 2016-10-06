#!/bin/bash

nginx -c `pwd`/conf/ninjutsu.conf -p "`pwd`"
nginx -c `pwd`/conf/ninjutsu.1.conf -p "`pwd`"
nginx -c `pwd`/conf/ninjutsu.2.conf -p "`pwd`"
