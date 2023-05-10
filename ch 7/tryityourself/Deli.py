sandwich_orders = ['ham', 'tuckey', 'blt', 'veggie']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop()

    print(f"{current_order} is made.")
    finished_sandwiches.append(current_order)
print("\nThe following sandwichs have been move:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())