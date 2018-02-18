# Learning plotting by using an external library (pylab)
import pylab as plt

# reference the method by calling plt.<procName>

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

# mySamples is the X value, the rest can be used as the Y value

# linear plotting
plt.plot(mySamples, myLinear)  # ensure both list has the same length
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)
plt.show()  # this is to generate a window to show the plotting








