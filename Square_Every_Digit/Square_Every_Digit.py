def square_digits(num):
    
    string = str(num)
    out = ''
    length = len(string)

    for i in range(length):
        out += str(int(string[i])*int(string[i]))
    return int(out)