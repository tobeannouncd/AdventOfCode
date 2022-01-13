def getData(day = None, filename = None):   
    if day:
        filename = './input/' + f'day{day}.txt'
    with open(filename) as f:
        data = f.read()
    return data.splitlines()

