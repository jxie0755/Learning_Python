#!/usr/bin/python
# -*- coding: utf-8 -*-
from unicodedata import name, lookup

print(name('A'))
# >>> LATIN CAPITAL LETTER A

print(lookup('WHITE SMILING FACE'))
# >>>

print(lookup('BABY').encode())
# >>> b'\xf0\x9f\x91\xb6'
