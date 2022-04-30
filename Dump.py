# DECOMPILED BY QURESHI
# DONT MESS WITH ME
import os
import sys
import re
import time
import json
import requests
import random
import datetime
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from time import sleep
reload(sys)
sys.setdefaultencoding('utf-8')
H = '\x1b[1;90m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
T = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
ua_nokia = 'Mozilla/5.0 (NokiaC5-00)UC AppleWebkit(like Gecko) Safari/530'
ua_xiaomi = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36'
ua_samsung = 'Mozilla/5.0 (Linux; Android 9; SM-G960F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.11 Mobile Safari/537.36'
ua_macos = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_0_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
ua_vivo = 'Mozilla/5.0 (Linux; U; Android 6.0; en-US; vivo 1713 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/11.5.0.1015 Mobile Safari/537.36'
ua_oppo = 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'
ua_huawei = 'Mozilla/5.0 (Linux; Android 8.0.0; HUAWEI Y7 PRO) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36'
ua_redmi4a = 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36'
ua_vivoy12 = 'Mozilla/5.0 (Linux; Android 9; vivo 1904) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36'
ua_nokiax = 'NokiaX2-01/5.0 (07.10) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+'
ua_asus = 'Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36'
ua_galaxys10 = 'Mozilla/5.0 (Linux; Android 9; SM-G977N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.105 Mobile Safari/537.36'
ua_lenovo = 'Mozilla/5.0 (Linux; Android 9; Lenovo TB-8705F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136 Safari/537.36'
ua = random.choice([
    ua_nokia,
    ua_xiaomi,
    ua_samsung,
    ua_macos,
    ua_vivo,
    ua_oppo,
    ua_huawei,
    ua_redmi4a,
    ua_vivoy12,
    ua_nokiax,
    ua_asus,
    ua_galaxys10,
    ua_lenovo])
logo ="""
\x1b[1;97m{__        {__                    
\x1b[1;92m{__        {__                  {_
\x1b[1;97m{__   {_   {__   {__     {____    
\x1b[1;92m{__  {__   {__ {__  {__ {__    {__
\x1b[1;92m{__ {_ {__ {__{__   {__   {___ {__
\x1b[1;97m{_ {_    {____{__   {__     {__{__
\x1b[1;92m{__        {__  {__ {___{__ {__{__

\t\033[1;97m[\x1b[1;97m\x1b[1;92m Mr Wasi Qureshi\x1b[0m\x1b[1;97m]
\t\033[1;97m[\x1b[1;97m\x1b[1;92m Wellcome \x1b[0m\x1b[1;97m]
\t\033[1;97m[\x1b[1;97m\x1b[1;92m This Tool Is Only For File Making\x1b[0m\x1b[1;97m]"""

def haha():
    os.system('clear')
    print logo
    print '\x1b[1;97m-----------------------------------------------'
    time.sleep(0.2)
    print '\x1b[1;91m[\x1b[1;97m1\x1b[1;91m]\x1b[1;92m Make File'
    time.sleep(0.2)
    print '\x1b[1;91m[\x1b[1;97m2\x1b[1;91m]\x1b[1;92m Exit'
    time.sleep(0.2)
    print '\x1b[1;97m-----------------------------------------------'
    time.sleep(0.2)
    print ''
    time.sleep(0.2)
    ok = raw_input('\x1b[1;91m[\x1b[1;97m?\x1b[1;91m]\x1b[1;97m Select: \x1b[1;92m')
    if ok == '':
        print '\x1b[1;91m[\x1b[1;97m!\x1b[1;91m] \x1b[1;91mWrong Input'
        haha()
    elif ok == '1':
        login()
    elif ok == '2':
        print '\x1b[1;97m       SEE YOU AGAIN :)'
        sys.exit()


def login():
    os.system('clear')
    print logo
    print '\x1b[1;97m-----------------------------------------------'
    print '\x1b[1;92m          Use Bussiness Token (EAAB)  '
    print '\x1b[1;97m-----------------------------------------------'
    print ''
    
    try:
        ___token___ = raw_input('         %s[%s~%s]%s T O K E N  :%s ' % (B, P, B, P, K))
        if ___token___ in ('', ' '):
            exit('%s[%s!%s]%sYAAR TOKEN LAGAW ' % (P, M, P, M))
        xwx = requests.get('https://graph.facebook.com/me/?access_token=%s' % ___token___).json()
        print '%s[%s*%s]%s WelCome  %s %s' % (B, P, B, P, H, xwx['name'].lower())
        open('login.txt', 'w').write(___token___)
        menu()
    except ConnectionError:
        exit('%s[%s!%s]%s YOUR INTERNET CONNECTION IS LOL' % (P, K, P, K))



def menu():
    os.system('clear')
    
    try:
        ___token___ = open('login.txt', 'r').read()
    except IOError:
        print ''

    print logo
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;92m                 INPUT IDS'
    print '\x1b[1;97m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print '\x1b[1;92m[~~~~] After Put Ids Go And See Your File :) '
    print '\x1b[1;92mNote      : PaSt OnLy Uid Not Uid And Name'
    print '\x1b[1;92mExample: /sdcard/Wasi.txt'
    print ''
    file = raw_input('\x1b[1;97mFile Path: ')
    id1 = raw_input('\x1b[1;97mid: ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id1, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;91mNot Public'

    id2 = raw_input('\x1b[1;97mid: ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id2, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;91mNot Public'
        
        id3 = raw_input('\x1b[1;97mid: ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id2, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;91mNot Public'      
        
        id4 = raw_input('\x1b[1;97mid: ')
    
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id2, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;91mNot Public'      
    
    id5 = raw_input('\x1b[1;97mid: ')
    try:
        rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (id1, ___token___)).json()
        file1 = open(file, 'a')
        for a in rex['friends']['data']:
            file1.write(a['id'] + ' | ' + a['name'] + '\n')
    except KeyError:
        print '\x1b[1;91mNot Public'
        print '\x1b[1;96m DUMP COMPLETED'
    time.sleep(5)
    menu()
   
    
haha()