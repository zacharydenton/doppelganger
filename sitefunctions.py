#!/usr/bin/env python
import random
import urllib.request

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/534.52.7 (KHTML, like Gecko) Version/5.1.2 Safari/534.52.7',
    'Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
]

sites = []

def site(fn):
    sites.append(fn)
    return fn

@site
def twitter(email, password):
    data = urllib.parse.urlencode({
        'session[username_or_email]': email,
        'session[password]': password
    }).encode('utf-8')
    request = urllib.request.Request('https://twitter.com/sessions', data)
    request.add_header('User-Agent', random.choice(USER_AGENTS))
    request.add_header('Referer', 'http://twitter.com')
    request.timeout = 5
    return 'login' not in urllib.request.HTTPSHandler().https_open(request).read().decode('utf-8')

