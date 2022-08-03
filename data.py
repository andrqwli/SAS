import random
from tests import *
# generates a valid date string
def generateValidDateString():
    return generateValidDate() + 'T' + generateValidTime() + generateValidTimeZone()

# generate valid date
def generateValidDate():
    return generateValidYear() + '-' + generateValidMonth() + '-' + generateValidDay()

# generate valid year
def generateValidYear():
    yearValue = str(random.randint(0, 9999))
    while len(yearValue) < 4:
        yearValue = '0' + yearValue
    return yearValue


# generate valid month
def generateValidMonth():
    monthValue = str(random.randint(1, 12))
    return monthValue if len(monthValue) == 2 else '0' + monthValue

# generate valid day
def generateValidDay():
    dayValue = str(random.randint(1, 31))
    return dayValue if len(dayValue) == 2 else '0' + dayValue

# generate valid time
def generateValidTime():
    return generateValidHours() + ':' + generateValidMinutesSeconds() + ':' +generateValidMinutesSeconds()

# generate valid hours
def generateValidHours():
    hourValue = str(random.randint(0, 23))
    return hourValue if len(hourValue) == 2 else '0' + hourValue

# generate valid minutes or seconds
def generateValidMinutesSeconds():
    minuteValue = str(random.randint(0, 59))
    return minuteValue if len(minuteValue) == 2 else '0' + minuteValue



# generate valid time zone
def generateValidTimeZone():
    if random.randint(0, 19) == 0:
        return 'Z'

    sign = random.choice(['+', '-'])
    time = generateValidHours() + ':' + generateValidMinutesSeconds()
    return sign + time

# generate a list of length n of distinct valid date strings
def generateValidDateStringList(n):
    dateSet = set()
    while len(dateSet) < n:
        dateSet.add(generateValidDateString())
    return list(dateSet)

# generate a list of valid dates with duplicates
def generateValidListWithDuplicates(numDistinctDates, numDuplicates):
    dateSet = set()
    while len(dateSet) < numDistinctDates:
        dateSet.add(generateValidDateString())
    
    dateList = list(dateSet)
    while len(dateList) < numDistinctDates + numDuplicates:
        index = random.randint(1,numDistinctDates) - 1
        dateList.append(dateList[index])
    return dateList


validList10 = generateValidDateStringList(10)
validList100 = generateValidDateStringList(100)
validList1000 = generateValidDateStringList(1000)
validList5000 = generateValidDateStringList(5000)

