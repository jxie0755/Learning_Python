"""体会圆括号的作用"""

import re

msg = "BbEDCbbGJLSbbbbVNbUYREWbEbbObbP"
# find the word that is in the "AAa" form

m = re.findall("[A-Z][A-Z][a-z]",msg)
k = re.findall("[A-Z]([A-Z])[a-z]",msg)
v = re.findall("([A-Z])[A-Z]([a-z])",msg)

print(m)  # >>> ["DCb", "LSb", "VNb", "EWb"]
print(k)  # >>> ["C", "S", "N", "W"]
print(v)  # >>> [("D", "b"), ("L", "b"), ("V", "b"), ("E", "b")]
