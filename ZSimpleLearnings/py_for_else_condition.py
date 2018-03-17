# https://stackoverflow.com/a/9980752/8435726
print()

# Using the Python for...else construct you have
def process(x):
    pass

mylist = [1,2,3,4]
theflag = 3

print('Example A1:')
for i in mylist:
    if i == theflag:
        break
    process(i)
else:
    print("List argument missing terminal flag.\n")
print('Bypassed else condition\n')

# once for loop is break, else is bypassed
# compare to:
print('Example A2:')
theflag = 5
for i in mylist:
    if i == theflag:
        break
    process(i)
else:
    print("List argument missing terminal flag.\n")


# Compare this to a method that does not use this syntactic sugar:
print('Example B1:')
theflag = 3
flagfound = False
for i in mylist:
    if i == theflag:
        flagfound = True
        break
    process(i)

if not flagfound:
    print("List argument missing terminal flag.\n")
print('Bypassed else condition\n')

print('Example B2:')
theflag = 5
flagfound = False
for i in mylist:
    if i == theflag:
        flagfound = True
        break
    process(i)

if not flagfound:
    print("List argument missing terminal flag.\n")
