# A simple example to use all the functions

# planning for retirement
# intend to save an amount m each month
# expect to earn a percentage r of income on investment each month
# want to explore how big a retirement fund will be compounded by time when retirement

import pylab as plt

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base += [i]
        savings += [savings[-1]*(1+mRate) + monthly]
    return base, savings
    # this generate two list


# Look at how much monthly deposit can impact
def displayRetireWMonthlies(monthlies, rate, terms):
    plt.figure("retireMonth")
    plt.clf()
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label="retire:" + str(monthly))
        plt.legend(loc="upper left")
    plt.show()

displayRetireWMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40*12)


# Look at how much rates can impact
def displayRetireWRates(monthly, rates, terms):
    plt.figure("retireRates")
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label="retire:" + str(monthly)+":" + str(int(rate*100)))
        plt.legend(loc="upper left")
    plt.show()

displayRetireWRates(800, [.03, .05, .07], 40*12)


# Look at both
def displayRetireWMonthsAndRates(monthlies, rates, terms):
    plt.figure("retireBoth")
    plt.clf()
    plt.xlim(30*12, 40*12)  # limit to high range
    for monthly in monthlies:
        for rate in rates:
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals,yvals, label="retire:"+str(monthly)+ ":" + str(int(rate*100)))
            plt.legend(loc="upper left")
    plt.show()

displayRetireWMonthsAndRates([500, 700, 900, 1100], [.03, .05, .07], 40*12)
# this does not show very well, can't distinguish each curve

def displayRetireWMonthsAndRates2(monthlies, rates, terms):
    plt.figure("retireBoth")
    plt.clf()
    plt.xlim(30*12, 40*12)  # limit to high range
    monthLabels = ["r", "b", "g", "k"]
    rateLabels = ["-", "o", "--"]
    for i in range(len(monthlies)):
        monthly = monthlies[i]
        monthLabel = monthLabels[i%len(monthLabels)]
        for j in range(len(rates)):
            rate = rates[j]
            rateLabel = rateLabels[j%len(rateLabels)]
            xvals, yvals = retire(monthly, rate, terms)
            plt.plot(xvals,yvals,
                     monthLabel+rateLabel,
                     label="retire:"+str(monthly) + ":" + str(int(rate*100)))
            plt.legend(loc="upper left")
    plt.show()

displayRetireWMonthsAndRates2([500, 700, 900, 1100], [.03, .05, .07], 40*12)
