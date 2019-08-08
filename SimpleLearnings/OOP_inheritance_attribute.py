"""Investigation on default parameter in OOP"""

# two types of default parameter:
# 显性: D, 可以在创建实例时被更改
# 隐性: E, 不能在创建实例时被更改
class SuperC():
    def __init__(self, a, b, c, d="显性D what?"):
        self.A = a
        self.B = b
        self.C = c
        self.D = d
        self.E = "隐性E what?"

sup = SuperC("A0", "B0", "C0")
print(sup.A)  # >>> A0
print(sup.B)  # >>> B0
print(sup.C)  # >>> C0
print(sup.D)  # >>> 显性D what?
print(sup.E)  # >>> 隐性E what?

print()
# 免费继承默认值attribute
class SubC1(SuperC):
    def __init__(self, a, b, c, f):
        super().__init__(a, b, c)
        self.F = f

sub1 = SubC1("A1", "B1", "C1", "Y1")
print(sub1.A)  # >>> A1  # (无默认值设定情况下)Ａ, B, C被继承而且数值被刷新
print(sub1.B)  # >>> B1
print(sub1.C)  # >>> C1
print(sub1.D)  # >>> 显性D what?   # 此处虽然super()没有指定,class也没有设定,但是由于SuperC中有默认值,所以仍然被继承
print(sub1.E)  # >>> 隐性E what?   # 隐性默认值也是同上行为
print(sub1.F)  # >>> Y1      # 新属性 f 不受干扰

# 不论如何都可以后天更改显性和隐性属性
sub1.D = "更改显性D"
print(sub1.D)  # >>> 更改显性D
sub1.E = "更改隐性E"
print(sub1.E)  # >>> 更改隐性E

print()
# 如果想在生成实例时就自动继承/改变 默认属性值:
# 一个办法就是子类__init__和super()中都加入显性默认值的变量
class SubC2(SuperC):
    def __init__(self, a, b, c, f, d="D0"):  # 子类维持与父类相同的默认值
        super().__init__(a, b, c, d)  # super()中也添加d
                                    # 此处不能放置e,因为e不属于父类__init()方法创建时必须输入的参数

        #  super().__init__(a, b, c, d="XXX")
        #  此处如果super()中再次写入默认值,则会再度覆盖子类属性的赋值,除非生成实例后再改写
        # 理由是super().有更高的权利
        self.F = f

sub2 = SubC2("A2", "B2", "C2", "Y2", d="new d22")  # 此处不设定d,则维持同父类一致的默认值,但是同时又可以赋予实例新值
print(sub2.A)  # >>> A2  # Ａ, B, C被继承而且数值被刷新
print(sub2.B)  # >>> B2
print(sub2.C)  # >>> C2
print(sub2.D)  # >>> new d22     # 显性默认值不再强制父类数值,而是跟随新默认值,或者新实例设定值
print(sub2.E)  # >>> 隐性E what?  # 隐性默认值继续继承,而且无法被更改
print(sub2.F)  # >>> Y2

# 生成实例后再改写super()里的默认值,也还是可以的
sub2.D = "YYY"
print(sub2.D)

print()
# 另一个的方法就是在__init__()创建新属性self.变量
class SubC3(SuperC):
    def __init__(self, a, b, c, f, d="new D", e="new E"):
        super().__init__(a, b, c)  # 即使继续选择不继承d和e,但是下面写入新设定
        self.D = d  # 新属性D设定, 覆盖父类数值
        self.E = e  # 新属性E设定, 覆盖父类数值
        self.F = f

sub3 = SubC3("A3", "B3", "C3", "Y3", "new D again", "new E again")  # 此处完美继承
print(sub3.A)  # >>> A3  # Ａ, B, C被继承而且数值被刷新
print(sub3.B)  # >>> B3
print(sub3.C)  # >>> C3
print(sub3.D)  # >>> D3  # D和E都可以跟随新默认值,或者新实例设定值
print(sub3.E)  # >>> E3
print(sub3.F)  # >>> Y3


# STOF https://stackoverflow.com/q/48039361/8435726
# 总结,如果只是子类属性和父类属性的默认值不同,则根本不必创建子类
# 创建子类的原则是: 继承大部分父类属性,同时还要包含新属性,不然根本就无需建立子类
# 隐性默认值本来就不应该在子类中被改变,设置成隐性默认值就是为了子类中不能轻易改变其赋值
