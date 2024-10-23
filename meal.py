def main():
    time = input("What time is it?")
    new_time = convert(time)
    if 7 <= new_time <= 8:
        print("breakfast time")
    elif 12 <= new_time <= 13:
        print("lunch time")
    elif 18 <= new_time <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    minutes = float(minutes) / 60
    hours = float(hours)
    new_time = hours + minutes
    return new_time


if __name__ == "__main__":
    main()
