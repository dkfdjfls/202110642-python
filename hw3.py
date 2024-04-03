
def get_fixed_price(rate, sale_price):
    net_price = sale_price / (1 - rate / 100)
    return net_price

rate = int(input('할인율은? '))
a_sale_price = int(input('A 상품의 할인된 가격은? '))
b_sale_price = int(input('B 상품의 할인된 가격은? '))

print('A 상품의 정가는', int(get_fixed_price(rate, a_sale_price)), '원')
print('B 상품의 정가는', int(get_fixed_price(rate, b_sale_price)), '원')
