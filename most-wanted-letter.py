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

# import string
#
# def checkio(text):
#     """
#     We iterate through latyn alphabet and count each letter in the text.
#     Then 'max' selects the most frequent letter.
#     For the case when we have several equal letter,
#     'max' selects the first from they.
#     """
#     text = text.lower()
#     return max(string.ascii_lowercase, key=text.count)
