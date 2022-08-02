# check if each list element is of type string
def isTypeString(dateArray):
    out = []
    for idx, date in enumerate(dateArray):
        if not isinstance(date, str):
            out.append((i, date))
    
    return out if len(out) > 0 else True

