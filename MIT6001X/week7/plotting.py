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


# the linear and quadratic is overlapped
# To generate seperately
plt.figure("lin")  # create a window named "lin"
plt.plot(mySamples, myLinear)
plt.figure("quad")
plt.plot(mySamples, myQuadratic)
plt.figure("cube")
plt.plot(mySamples, myCubic)
plt.figure("expo")
plt.plot(mySamples, myExponential)
plt.show()
# this will genreate 4 indivdiual window


# To add labels (x axis and y axis)
plt.figure("cube2")
plt.xlabel("days")
plt.ylabel("Peroxide Value")
plt.plot(mySamples, myCubic)
plt.show()

plt.figure("exponential2")
plt.plot(mySamples, myExponential)
# plt.show()  # can not show here, once show, then terminates the further editing

plt.figure("exponential2")  # reopen the figure and add labels
plt.xlabel("days")
plt.ylabel("free FFA")
plt.show()


# Adding titles
plt.figure("cube3")
plt.title("PV in project A")
plt.xlabel("days")
plt.ylabel("Peroxide Value")
plt.plot(mySamples, myCubic)
plt.show()


# clear a window
# plt.clf()


# Compare result
# limit axis scale
plt.figure("lin vs exp")
plt.ylim((0, 1000))  # limit y axis
plt.plot(mySamples, myLinear)
plt.plot(mySamples, myExponential)
plt.show()

plt.figure("cube vs exp")
plt.yscale("log")  # set changing of y scale
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponential)
plt.show()


# Add a lengend
plt.figure("quad vs cube")
plt.plot(mySamples, myQuadratic, label = "quad")
plt.plot(mySamples, myCubic, label="cube")
plt.legend(loc="upper left")  # plot legend by grouping labels, and define the location
# default is to let pylab to decide
plt.show()


# Control display paramenter
# change color and style
plt.figure("lin vs quad")

plt.plot(mySamples, myLinear, "b--", label="lin", linewidth=5.0)  # linewidth pixel
plt.plot(mySamples, myQuadratic, "r^", label="quad", linewidth=2.0)
# in plot: b - blue, r - red, g - green, k - black
# second letter is the style of the line: "-" is line, "--" is dash, "|" is triangle, "^" is triangle

plt.legend(loc="upper left")  # plot legend by grouping labels, and define the location
# default is to let pylab to decide
plt.show()


# Subplot (one figure to show multiple graphs)
plt.figure("subplot test")
plt.subplot(221)  # numbers of rows, number of columns
plt.title("1")
plt.plot(mySamples, myLinear, label="lin")
plt.plot(mySamples, myQuadratic, label="quad")

plt.subplot(222)  # numbers of rows, number of columns
plt.title("2")
plt.plot(mySamples, myLinear, label="lin")
plt.plot(mySamples, myQuadratic, label="quad")

# Subplot (one figure to show multiple graphs)
plt.subplot(223)  # numbers of rows, number of columns
plt.title("3")
plt.plot(mySamples, myLinear, label="lin")
plt.plot(mySamples, myQuadratic, label="quad")

plt.subplot(224)  # numbers of rows, number of columns
plt.title("4")
plt.plot(mySamples, myLinear, label="lin")
plt.plot(mySamples, myQuadratic, label="quad")

plt.show()
