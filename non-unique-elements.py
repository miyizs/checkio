def checkio(data):
    countResult = [(data.count(ch),ch) for ch in data]
    filtered = filter(lambda x: x[0] > 1, countResult)
    final = map(lambda x: x[1], filtered)
    return(list(final))

# def checkio(data):
#         return [i for i in data if data.count(i) > 1]
