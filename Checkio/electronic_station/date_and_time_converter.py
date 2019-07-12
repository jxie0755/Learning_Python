# Computer date and time format consists only of numbers, for example: 21.05.2018 16:30
# Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes
import datetime

# NB: words "hour" and "minute" are used only when time is 01:mm (1 hour) or hh:01 (1 minute).
# In other cases it should be used "hours" and "minutes".

def date_time(time: str) -> str:
    date_n = str(int(time[0:2]))
    month_n = time[3:5]
    year_n = time[6:10]
    hour_n = str(int(time[11:13]))
    minute_n = str(int(time[14:16]))

    month_trans = {"01": "January", "02": "February", "03": "March", "04": "April",
                   "05": "May", "06": "June", "07": "July", "08": "August",
                   "09": "September", "10": "October", "11": "November", "12": "December"}

    hour_str = " hour " if hour_n == "1" else " hours "
    minute_str = " minute" if minute_n == "1" else " minutes"


    return date_n + " " + month_trans[month_n] + " " + year_n + " year " + hour_n + hour_str + minute_n + minute_str


if __name__ == "__main__":
    print("Example:")
    print(date_time("01.01.2000 00:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click "Check" to earn cool rewards!")
