# 这里是介绍普通的引入模块问题,但是涉及到一个python的更新改动
# python3.5和以前的版本: 字典的键值配对是无序的,不保持添加的顺序
# 自python3.6开始, 这个问题得到了改善, 字典会保持添加时的配对顺序.
# 这同时也是的collections里面的OrderedDict方法不再有存在的意义

from collections import OrderedDict

favorite_languages = OrderedDict()
favorite_languages2 = {}

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print()

favorite_languages2['jen'] = 'python'
favorite_languages2['sarah'] = 'c'
favorite_languages2['edward'] = 'ruby'
favorite_languages2['phil'] = 'python'

for name, language in favorite_languages2.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
