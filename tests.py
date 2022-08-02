# check if each list element is of type string
def isTypeString(dateArray):
    out = []
    for idx, date in enumerate(dateArray):
        if not isinstance(date, str):
            out.append((idx, date))
    
    return out if len(out) > 0 else True

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


