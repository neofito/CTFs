#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
extra.py (v0.1)

Created: 2014-09-28

Copyright (c) 2010: Vte J. Garcia Mayen  <neofito@gmail.com>
Copyright (c) 2010: Neo System Forensics http://neosysforensics.es

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 2 of the License, or (at your
option) any later version.  See http://www.gnu.org/copyleft/gpl.html for
the full text of the license.
"""
import requests
import urlparse
import bs4

def make_get_007(url, headers=False):
    """ Function doc """

    if headers:
        headers = {'User-Agent':'007'}
        req = requests.get(url,headers=headers)
    else:
        req = requests.get(url)

    soup = bs4.BeautifulSoup(req.text)
    for img in soup.find_all('img'):
        url  = "http://" + urlparse.urlparse(url).netloc
        img['src'] = url + "/" + img['src']

    return soup.prettify()

def make_post_buda(url):
    """ Function doc """

    payload = {'master':'BUDA'}
    headers = {'User-Agent':'007',
               'Accept':'*/*',
               'Content-Type':'application/x-www-form-urlencoded',
               'Content-Length':'11'}

    req = requests.post(url, data=payload, headers=headers)
    soup = bs4.BeautifulSoup(req.text)

    for link in soup.find_all('a'):
        if 'extra.php' in link.get('href'):
            link['href'] = url + link['href']
        else:
            url  = "http://" + urlparse.urlparse(url).netloc
            link['href'] = url + "/" + link['href']

    return soup.prettify()


def create_file(name, content):
    """ Function doc """

    hnd = open(name, 'w')
    hnd.write(content)
    hnd.close()

def main():
    """ Main Function """

    url = "http://ctf.navajanegra.com/extra.php"

    print '-----------------------------------------------------'
    print '- #nn4ed CTF - Level: extra (HTTP headers/requests) -'
    print '-----------------------------------------------------'
    print '[*] Guetting first stage on extra_1.html...'
    create_file('extra_1.html', make_get_007(url))
    print '[*] Done!'
    print '[*] Guetting second stage on extra_2.html...'
    create_file('extra_2.html', make_get_007(url, headers=True))
    print '[*] Done!'
    print '[*] Guetting third stage on extra_3.html...'
    create_file('extra_3.html', make_post_buda(url))
    print '[*] Done!'
    print '-----------------------------------------------------'

if __name__ == "__main__":
    main()

