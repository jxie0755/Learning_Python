__version__ = 0.2

mymodule = __import__("10_module4")

mymodule.say_hi()

print('Version', mymodule.__version__)
print('Version', __version__)

# 建议使用import命令，然后每次运行都使用module.function的方式，虽然麻烦，但是避免冲突
