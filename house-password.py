def checkio(data):
    return not data.isalpha() and not data.isdigit() and not data.islower() and not data.isupper() and len(data) >= 10

print(checkio('yzA2zzzzzz'))
