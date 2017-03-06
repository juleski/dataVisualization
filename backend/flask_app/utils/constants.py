import os

INDEX = 'exam'
ES_HOST = 'elastic:changeme@%s:9200' % (os.environ['ES_CONFIG'])