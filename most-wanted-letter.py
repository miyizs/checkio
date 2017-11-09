import string
from operator import itemgetter, attrgetter
def checkio(text):
    text = text.lower()
    countArr= [(text.count(ch), ch) for ch in string.ascii_lowercase]
    sortedArr = sorted(countArr,key=itemgetter(1), reverse=True)
    tempCount = 0
    tempStr = ''
    for item in sortedArr:
        if item[0]>=tempCount:
            tempCount = item[0]
            tempStr = item[1]

    return tempStr
