#!/usr/bin/env python
#upload gist
#

import traceback
import curl
import pycurl
import json
from StringIO import StringIO

pycurl.version.split(' ')[0].[8:]
_api_url = 'https://api.github.com/user'
access_token = '?access_token='

#z.setopt(z.WRITEFUNCTION,a.write)
#Post-method
#crl.setopt(crl.POSTFIELDS,  urllib.urlencode(post_data_dic))

#api-lst
try: 
    _api_lst = open('api.lst').read()
except IOError:
    print "API.lst Not Exist!"
    exit(1)

#get user-oauth
try: 
    a = open('../../psword/oauth_git.txt')
    oauth = a.read().strip()
    print oauth
except IOError:
    print "Don't have this file,Please edit path or \
      get personal-oauth from https://github.com"
    exit(1)


def get_userinfo(oauth,user=None,password=None,filepath=None):
    _curl = pycurl.Curl()
    if oauth is not None:
        _access_token = access_token + oauth
        _curl.setopt(URL,_api_url+_access_token)
        #info to file-path
        _file_path
        _curl.perfom()
    elif (user is not None) and (password is not None):
        _str_oauth = '%s:%s' % (user,password)

        

    
