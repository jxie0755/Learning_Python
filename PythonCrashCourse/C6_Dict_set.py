favorite_languages = { 'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
for name in favorite_languages.keys():     # 可以不写keys,默认也是寻找keys
    print(name.title())
print()

for language in favorite_languages.values():  # value必须要标明
    print(language.title())   # 这样会出现重复的language, 可以使用set
print()
    # set跟list很像,但是要求每个item不能重复
for language in set(favorite_languages.values()):
    print(language.title())
print()

for name in sorted(favorite_languages.keys()):    # sorted临时排序
    print(name.title() + ", thank you for taking the poll.")
