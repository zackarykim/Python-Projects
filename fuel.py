tank = input("Fraction:")

try:
    value_split = tank.split("/")
    first_value = int(value_split[0])
    second_value = int(value_split[1])
    percentage = round(first_value/second_value*100)

    if second_value == 0:
        raise ZeroDivisionError()
    elif percentage <= 1:
        print("E", end="")
    elif percentage >= 99 and percentage <=100:
        print("F", end="")
    elif first_value <= second_value:
        print(f"{percentage}%", end="")
    else:
        raise ValueError()

except ValueError:
    tank = input("Fraction:")

except ZeroDivisionError:
    tank = input("Fraction:")
