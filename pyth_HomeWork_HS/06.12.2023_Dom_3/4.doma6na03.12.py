#Напишете конзолна програма, която чете ден от седмицата (str) – въведен от потребителя и
#принтира на конзолата цената на билет за кино според деня от седмицата, както е показано на
#таблицата:
day_of_week = input("Enter day of week:")
match day_of_week:
    case "Monday":
        print("12")
    case "Tuesday":
        print("12")
    case "Wednesday":
        print("14")
    case "Thursday":
        print("14")
    case "Friday":
        print("12")
    case "Saturday":
        print("16")
    case "Sunday":
        print("16")        
    case _:
        print("Invalid day of week")
