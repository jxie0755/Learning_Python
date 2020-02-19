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

# 解释:
# 如果pattern中没有分组, 它是会显示符合pattern的整个字段
# 如果pattern中没有分组, 它返回的不是符合整个pattern的字段,而是把pattern中的各个分组用Tuple装起来返回:
#   如果整个pattern中存在不彻底分组(有一部分分组了,其他没有): 则会忽略返回那些没有被分组的部分
#   如果整个pattern中每一个字段都被分组, 则会返回完整的字段, 但是需要结合成一个字段
