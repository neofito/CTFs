#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
web1.py (v0.1)

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
import bs4

def main():
    """ Main Function """

    url = "http://ctf.navajanegra.com/WEB%201.php"
    headers = {'User-Agent':'Wget/1.13.4 (linux-gnu)'}

    print '-----------------------------------------------------'
    print '- #nn4ed CTF - Level: web1 (unclassified) -'
    print '-----------------------------------------------------'
    print '[*] Guetting WEB 1.php content...'
    req = requests.get(url, headers=headers)
    print '[*] Done!'
    print '[*] Analyzing the retrieved content...'
    soup = bs4.BeautifulSoup(req.text)
    print '[*] Done!'
    print '-----------------------------------------------------'
    for string in soup.strings:
        if "Password" in string:
            print string.replace('\n', '')

if __name__ == "__main__":
    main()

