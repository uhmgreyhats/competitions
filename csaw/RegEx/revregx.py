#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rstr
import os
import re
from sh import nc
import socket


thefile = open('outfile.txt', 'w')

sock = socket.socket()
sock.connect(('misc.chal.csaw.io',8001))
buff = sock.recv(4096)
buff2 = '?'
while str(buff2) != '':

    buff2 = sock.recv(4096)
    print 'recv>>' + buff2
    thefile.write('recv>>' + buff2 + '\n')
    matched = rstr.xeger(buff2)
    #print 'match>>' + matched
    thefile.write('match>>' + matched + '\n')
    matched = re.sub('\n','\t',matched)
    print matched
    sock.send(matched)
    sock.send('\n')
thefile.close()
