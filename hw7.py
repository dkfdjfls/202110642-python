
shopping_bag = {}

print('[구입]')
while True:
    item = input('상품명? ')
    if item == '':
        break
    n = input('수량은? ')
    shopping_bag[item] = n
    print(f'장바구니에 {item} {n}개가 담겼습니다.\n')

print(f'\n>>> 장바구니 보기: {shopping_bag}')

print('\n[검색]')
find = input('장바구니에서 확인하고자 하는 상품은? ')

if find in shopping_bag:
    print(f'{find}은(는) {shopping_bag.get(find)}개 담겨 있습니다.')
else:
    print(f'{find}은(는) 장바구니에 담겨있지 않습니다.')
