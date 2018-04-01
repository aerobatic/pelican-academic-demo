#!/usr/bin/env python3

# https://gist.github.com/saschwarz/8eff30f5ea5d468f0b86bd0bb149a186
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

import sys
from livereload import Server, shell
from pelican import Pelican
from pelican.settings import read_settings


settings = read_settings('pelicanconf.py')
p = Pelican(settings)

def compile():
    try:
        p.run()
    except SystemExit as e:
        pass

server = Server()
server.watch(p.settings['PATH'], compile)
server.watch(p.settings['THEME'], compile)
server.watch('templates', compile)
server.watch('./pelicanconf.py', compile)

# localhost_url = p.settings.get('SITEURL') or 'http://localhost:' sys.argv[0]
# details = urlparse(localhost_url)
# host = 'localhost'
# port = sys.argv[2]
# host, port = details[1].split(':')

server.serve(host='localhost', port=sys.argv[1], root=settings['OUTPUT_PATH'])
