
def read_single_digit(a):
    if a == 0 :
        return '영 '
    elif a == 1 :
        return '일 '
    elif a == 2 :
        return '이 '
    elif a == 3 :
        return '삼 '
    elif a == 4 :
        return '사 '
    elif a == 5 :
        return '오 '
    elif a == 6 :
        return '육 '
    elif a == 7 :
        return '칠 '
    elif a == 8 :
        return '팔 '
    else :
        return '구 '

def read_number(n):
    first = read_single_digit(n // 100)
    second = read_single_digit((n % 100) // 10)
    third = read_single_digit(n % 10)
    return first + second + third

number = int(input('세 자리 정수 입력: '))
print(read_number(number))
