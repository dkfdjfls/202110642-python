
def get_integer(prompt):
    total = int(input(prompt))
    return total

def exchange(total):
    n500 = total // 500
    remain = total % 500
    n100 = remain // 100
    remain %= 100
    n50 = remain // 50
    remain %= 50
    n10 = remain // 10
    print('500원 동전의 개수:', n500)
    print('100원 동전의 개수:', n100)
    print('50원 동전의 개수:', n50)
    print('10원 동전의 개수:', n10)

total = get_integer('동전으로 교환하고자 하는 금액은? ')
exchange(total)

    
