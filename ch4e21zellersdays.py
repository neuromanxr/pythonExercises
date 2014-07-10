year = eval(input("Enter year: "))
month = eval(input("Enter month, 1-12: "))
day = eval(input("Enter day of month, 1-31: "))

if month == 1:
    month = 13
    year = year - 1
elif month == 2:
    month = 14
    year = year - 1

day = day - 1
yearCent = year % 100 # k
century = year / 100 # j
twentySix = 26 * (month + 1) / 10

dayOfWeek = (day + twentySix + yearCent \
            + (yearCent / 4) + (century / 4) + (5 * century)) % 7

dayOfWeek = dayOfWeek // 1

if dayOfWeek == 0:
    print("Day is Saturday")
elif dayOfWeek == 1:
    print("Day is Sunday")
elif dayOfWeek == 2:
    print("Day is Monday")
elif dayOfWeek == 3:
    print("Day is Tuesday")
elif dayOfWeek == 4:
    print("Day is Wednesday")
elif dayOfWeek == 5:
    print("Day is Thursday")
elif dayOfWeek == 6:
    print("Day is Friday")


# print(dayOfWeek // 1)
