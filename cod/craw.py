#!/usr/bin/env python
#upload gist
#
# -*- coding:utf8 -*-   

#handle cmd parameter
import sys
import re
import traceback
import curl
import pycurl
import json
import urllib
from StringIO import StringIO
pycurl.version.split(' ')[0][8:]
try: 
    a = open('../../psword/oauth_git.txt')
    oauth =  '?access_token='+a.read().strip()
except IOError:
    print "Don't have this file,Please edit path or \
      get personal-oauth from https://github.com"
    exit(1)

'''
Note that:
  create a personal gist:  $python craw.py gistP -A gist-name
  delete a personal gist:  $python craw.py gistP -C gist-name
  ……
  _dict_gistformat as Gist-Post-Type
  Please read complete doc
  .../doc/USER.doc


'''

#need edit
_description = ''
_gist_opt = ''
_file = ''
_content = ''

### fault
_dict_gistformat = {
      "description": _description,
        "public": _gist_opt,
          "files": {
                _file : {
                        "content": _content
                            }
                  }
          }

#public or private choosen
_o_ption = ('false','true')
#z.setopt(z.WRITEFUNCTION,a.write)
#Post-method
#crl.setopt(crl.POSTFIELDS,  urllib.urlencode(post_data_dic))

#api-lst

'''try: 
    _api_lst = open('api.lst').read()
except IOError:
    print "API.lst Not Exist!"
    exit(1)
'''

#get user-oauth

def _read_gistfile(path):
    '''
      translate file to POST-DATA
    '''
    try: 
        _gist_file = open(path)
        _gistname = _gist_file.readline().strip()
        _description = _gist_file.readline().strip()
        #file third-line is 0 ,choose Private-Gist,_o_ption[0]='False'
        _option = _o_ption[_gist_file.readline().strip()]
        _content = _gist_file.read()
    except IOError:
        print "Don't have this gist-file"
        exit(1)
    return (_gistname,_description,_option,_content)

def _option_error(errortype):
    '''
      1 is null option or null parameter
    '''
    if errortype == 1:
        print "Need More Parameter"
        exit(1)


'''def _get_userinfo(oauth,user=None,password=None,filepath=None):
    _curl = pycurl.Curl()
    if oauth is not None:
        _access_token = access_token + oauth
        _curl.setopt(URL,_api_url+_access_token)
        _curl.perfom()
    elif (user is not None) and (password is not None):
        _str_oauth = '%s:%s' % (user,password)
        _curl.setopt(_curl.USERPWD, _str_oauth)
        _curl.setopt(_curl.URL,'https://api.github.com/user')
        _data = _curl.perfom()
        _json_data_fm = json.load(_data)
'''

def _create_user_Ggist(gist_name):
    '''
      mode:
      _dict_gistformat = {
      "description": _description,
        "public": _gist_opt,
          "files": {
                _file : {
                        "content": _content
                            }
                  }
          }'''

    _curl = pycurl.Curl()
    _curl.setopt(_curl.URL,'https://api.github.com/gists'+oauth)
    _curl.setopt(_curl.POST,1)

def _delete_user_Ggist(gist_name):

def _create_user_Pgist(gist_name):

def _delete_user_Pgist(gist_name):


def _search_keyword_from_publicgist(keyword,gistnum = 5):
    '''
       exist issues
    '''
    _curl = pycurl.Curl()
    _buffer = StringIO()
    _curl.setopt(_curl.URL,'https://api.github.com/gists/public')
    _curl.setopt(_curl.WRITEFUNCTION,_buffer.write)
    _t_data = _buffer.getvalue()
    _pattern = re.compile(r'$"raw_url":"\w[4,5]\W?\w?$"')
    _result = _pattern.match(_t_data)
    print _result

def handle():
  '''
    handle cli-parameter
  '''
    _list_agv = sys.argv
    if _list_agv[1] == 'gistS':
        try:
            _keyword = _list_agv[2]
            try:
                _gistnum = _list_agv[3]
                _search_keyword_from_publicgist(_keyword,_gistnum)
            except:
                _search_keyword_from_publicgist(_keyword)  
        except:        
            _option_error(1) 

    if _list_agv[1] == 'gistP': 
        if _list_agv[2] == '-A':
            try:
                _gist_name = _list_agv[3]
            except:
                _option_error(1)              
            _create_user_Pgist(_gist_name)
        elif _list_agv[2] == '-D':
            try:
                _gist_name = _list_agv[3]
            except:
                _option_error(1)              
            _delete_user_Pgist(_gist_name)

    if _list_agv[1] == 'gistG':
        if _list_agv[2] == '-A':
            try:
                _gist_name = _list_agv[3]
            except:
                _option_error(1)              
            _create_user_Ggist(_gist_name)
        elif _list_agv[2] == '-D':
            try:
                _gist_name = _list_agv[3]
            except:
                _option_error(1)              
            _delete_user_Ggist(_gist_name)



if __name__ == '__main__':
    handle()
        

    
