total = 50
acceptable_payment = [25, 10, 5]
while total > 0:
    print("Amount Due:", total)
    inserted_coin = int(input("Insert Coin:"))
    if inserted_coin in acceptable_payment:
        total -= inserted_coin
    if total < 0:
        total = abs(0 - total)
        break
print("Change Owed:", total)
