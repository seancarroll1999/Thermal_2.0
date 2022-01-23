from datetime import datetime, date

def getSuffix(i):
    j = i % 10
    k = i % 100

    if(j == 1 and k != 11):
        return "st"

    if(j == 2 and k != 12):
        return "nd"

    if(j == 3 and k != 13):
        return "rd"

    return "th" 

def GetDate():
    today = datetime.now()
    date = int(today.strftime("%-d"))
    suffix = getSuffix(date)
    return "{day} - {date}{suffix}".format(date=date, suffix=suffix, day=today.strftime("%A"))
