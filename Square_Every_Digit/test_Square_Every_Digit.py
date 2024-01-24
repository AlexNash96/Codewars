def square_digits(num):
    
    string = str(num)
    out = ''
    length = len(string)

    for i in range(length):
        out += str(int(string[i])*int(string[i]))
    return int(out)

def test_answer():
    assert square_digits(7825) == 4964425
    assert type(square_digits(781234)) is int