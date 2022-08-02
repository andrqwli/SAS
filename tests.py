from data import *
# check if each list element in a list of dates is of type string
def checkAllDates(dateArray):
    if hasNoDuplicates(dateArray) != True:
        print('Date array has duplicates as follows: ')
        print(hasNoDuplicates(dateArray))
        return False

    for date in dateArray:
        if not isValidDateString(date):
            return False
    
    return True

# check if list of dates includes any duplicate values
def hasNoDuplicates(dateArray):
    dateSet = set(dateArray)
    if len(dateSet) == len(dateArray):
        return True
    else:
        out = []
        for date in dateSet:
            if dateArray.count(date) > 1:
                out.append((date, dateArray.count(date)))
        return out

# check if a single date string is in valid format "YYYY-MM-DDThh:mm:ssTZD"
def isValidDateString(dateString):
    if not isinstance(dateString, str):
        print("Date input value is of type {}, should be of type string".format(type(dateString)))
        return False

    if dateString.find('T') == -1:
        # change this to an exception
        print('Invalid number of \'T\' delimiters between date and time ({}), should be 1'.format(dateString.find('T')))
        return False
    else:
        [date, time] = dateString.split("T")

    if not isDateValid(date):
        print('Date portion is not valid')
        return False
    
    if not isTimeValid(time):
        print('Time portion is not valid')
        return False

    return True

# check if date portion of date string is valid
def isDateValid(date):
    if len(date) != 10:
        print('Invalid date length of {}, should be 10'.format(len(date)))
        return False
    if date.count('-') != 2:
        print('Invalid \'-\' delimiter count of {}, should be 2'.format(date.count('-')))
        return False
    
    [year, month, day] = date.split('-')
    
    if not isYearValid(year):
        print('Year portion is not valid')
        return False
    
    if not isMonthValid(month):
        print('Month portion is not valid')
        return False
    
    if not isDayValid(day):
        print("Day portion is not valid")
        return False
    
    return True

# check if 'YYYY' portion is valid
def isYearValid(year):
    if len(year) != 4:
        print('Invalid year length of {}, should be 4'.format(len(year)))
        return False
    
    try:
        yearInt = int(year)
    except:
        print('Year contains nonnumerical characters')
        return False
    
    return True

# check if 'MM' portion is valid
def isMonthValid(month):
    if len(month) != 2:
        print('Invalid month length of {}, should be 2'.format(len(month)))
        return False
    
    try:
        monthInt = int(month)
    except:
        print('Month contains nonnumerical characters')
        return False
    
    if monthInt <= 12 and monthInt >= 1:
        return True
    else:
        print('Month is not in range [01, 12]')
        return False

def isDayValid(day):
    if len(day) != 2:
        print('Invalid day length of {}, should be 2'.format(len(day)))
        return False
    
    try:
        dayInt = int(day)
    except:
        print('Day contains nonnumerical characters')
        return False
    
    if dayInt <= 31 and dayInt >= 1:
        return True
    else:
        print('Day is not in range [01, 12]')
        return False



# check if time portion of date string is valid
def isTimeValid(time):
    if len(time) <= 8:
        print("Invalid time length of {}, should be at least 9".format(len(time)))
        return False
    clockTime = time[:8]
    timeZone = time[8:]

    if not isClockTimeValid(clockTime):
        print('Invalid clock time')
        return False
    
    if not isTimeZoneValid(timeZone):
        print('Invalid time zone')
        return False

    return True

# check if 'hh:mm:ss' portion is valid
def isClockTimeValid(clockTime):
    if clockTime.count(':') != 2:
        print('Invalid \':\' delimiter count of {}, should be 2'.format(clockTime.count(':')))
        return False
    [hours, minutes, seconds] = clockTime.split(':')
    
    if not isHoursValid(hours):
        print('Hours not valid')
        return False
    if not isMinutesOrSecondsValid(minutes):
        print('Minutes not valid')
        return False
    if not isMinutesOrSecondsValid(seconds):
        print('Seconds not valid')
        return False

    return True

# check if 'hh' is valid
def isHoursValid(hours):
    if len(hours) != 2:
       print('Hours of length {}, should have length 2'.format(len(hours)))
       return False

    try:
        hoursInt = int(hours)
    except:
        print("Hours contains nonnumerical characters")
        return False 
    
    if not (hoursInt <=23 and hoursInt >= 0):
        print('Hours value is {}, should be in range [00-23]'.format(hoursInt))
        return False
    
    return True

#check if 'mm' or 'ss' is valid as they share the same format
def isMinutesOrSecondsValid(minutes):
    if len(minutes) != 2:
       print('Minutes/seconds of length {}, should have length 2'.format(len(minutes)))
       return False

    try:
        minutesInt = int(minutes)
    except:
        print("Minutes/seconds contains nonnumerical characters")
        return False 
    
    if not (minutesInt <=59 and minutesInt >= 0):
        print('Minutes/seconds value is {}, should be in range [00-23]'.format(minutesInt))
        return False
    
    return True 

# check if time zone is valid 'Z' or '+hh:mm' or '-hh:mm'
def isTimeZoneValid(timeZone):
    # the case where TZD value is 'Z'
    if len(timeZone) == 1:
        if timeZone == 'Z':
            return True
        else:
            print('Time zone is of length one but is {}, should be \'Z\''.format(timeZone))
            return False
    # the case where TZD value is of format '+hh:mm' or '-hh:mm'
    if len(timeZone) != 6:
        print('Time zone has length {}, should have length 6 if not \'Z\''.format(len(timeZone)))
        return False
    
    firstChar = timeZone[0]

    if not (firstChar == '+' or firstChar == '-'):
        print('First character of time zone is {}, should be \'+\' or \'-\''.format(firstChar))

    time = timeZone[1:]
    if time.count(':') != 1:
        print('Time zone has {} \':\' delimiters, should have 1'.format(time.count(':')))
    
    [hours, minutes] = time.split(':')

    if not isHoursValid(hours):
        print('Time zone hours not valid')
        return False
    if not isMinutesOrSecondsValid(minutes):
        print('Time zone minutes not valid')
        return False

    return True


print(isValidDateString("9999-02-31T12:34:56+12:34"))