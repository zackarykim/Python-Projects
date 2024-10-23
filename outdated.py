months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date_entered = input("Date: ").strip()
    try:
        month, day, year = date_entered.split("/")
        if (int(month)<=12 and int(month)>=1) and (int(day)<=31 and int(day)>=1):
            break
    except:
        try:
            string_month, old_day, year = date_entered.split(" ")
            for i in range(len(months)):
                if string_month == months[i]:
                    month = i + 1
            if "," in old_day:
                day = old_day.replace(",","")
                if ( 1<=int(month)<=12 and 1<=int(day)<=31):
                    break
        except:
            print()
            pass



print(f"{year}-{int(month):02}-{int(day):02}")


