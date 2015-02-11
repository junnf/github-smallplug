#!/usr/bin/env python
#upload gist
#
# -*- coding:utf8 -*-   

#handle cmd parameter
import sys
import traceback
import curl
import pycurl
import json
from StringIO import StringIO

'''
Note that:
  create a personal gist:  $python craw.py gistP -A gist-name
  delete a personal gist:  $python craw.py gistP -C gist-name
  ……
  
  Please read complete doc
  .../doc/USER.doc

'''

pycurl.version.split(' ')[0][8:]
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


def _get_userinfo(oauth,user=None,password=None,filepath=None):
    _curl = pycurl.Curl()
    if oauth is not None:
        _access_token = access_token + oauth
        _curl.setopt(URL,_api_url+_access_token)
        #info to file-path
        _file_path
        _curl.perfom()
    elif (user is not None) and (password is not None):
        _str_oauth = '%s:%s' % (user,password)
        _curl.setopt(_curl.USERPWD, _str_oauth)
        _curl.setopt(_curl.URL,'https://api.github.com/user')
        _data = _curl.perfom()
        _json_data_fm = json.load(_data)

def _create_user_personal_gist(gist_name):
    pass

def _create_user_public_gist(gist_name):
    pass

def _search_keyword_from_publicgist(keyword,gistnum = 5):
    pass

def handle():
    
    _list_agv = sys.argv
    if _list_agv[1] == 'gistP' and _list_agv[2] == '-A':
        try:
            _gist_name = _list_agv[3]
        except:
            print "Add your gist name"
            exit(1)
        #call create-api
        try:
            _create_user_Pgist(_gist_name)
        except:
            print "Failed"
            exit(1)



if __name__ == '__main__':
    handle()
        

    
