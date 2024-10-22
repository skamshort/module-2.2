first = 11
print(first)
second = 16
print(second)
third = 16
print(third)
if first == second and second == third and first == third:
    print(3)
elif first == second or second== third or first==third:
    print(2)
elif first != second and second != third and first!=third:
    print(0)