try: 
    _api_lst = open('st')
    oauth = a.read()
    print oauth
except IOError:
    print "FAILED"
    exit(1)
