sandwich_orders = ['ham', 'tuckey', 'blt', 'veggie', 'pastrami', 'pastrami', 'pastrami']


print("Deli has ran out of pastrami!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
    