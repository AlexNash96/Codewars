def solution(number):
    sum = 0
    for i in range(number):
        if i%5 == 0:
            sum = sum+i
        elif i%3 == 0:
            sum = sum+i
    return sum

def test_answer():
    assert solution(10) == 23
    assert solution(100) == 2318
    assert solution(1000) == 233168
    assert solution(-1000) == 0
    assert solution(2) == 0
    assert solution(5) == 3
    assert solution(6) == 8