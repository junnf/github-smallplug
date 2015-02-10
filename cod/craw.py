#!/usr/bin/env python
#upload gist
#

import traceback
import curl
import pycurl
import json
from StringIO import StringIO

_version = pycurl.version()
_api_url = 'https://api.github.com/user'
access_token = '?access_token='

#z.setopt(z.WRITEFUNCTION,a.write)
#

try: 
    a = open('../../psword/oauth_git.txt')
    oauth = a.read().strip()
    print oauth
except:
    exit(1)
    print "Open failed"


def get_userinfo(user=None,password=None,oauth,filepath=None):
    _curl = pycurl.Curl()
    if oauth is not None:
        _access_token = access_token + oauth
        _curl.setopt(URL,_api_url+_access_token)
        #info to file-path
        _file_path
        _curl.perfom()
    else if user is not None and password is not None:
        _str_oauth = '%s:%s' % (user,password)

        

    
