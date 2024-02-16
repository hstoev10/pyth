#5*. Напишете програма, която чете N дни от седмицата като текст
#● където N e число прочетено от конзолата
#● прави проверка дали въведения текст е правилен ден от седмицата
#● ако не е принтира подходящо съобщение и приключва изпъление
#● ако е верен сумира колко пъти е въведен съотвения ден
#● след като се въведат N дни, програмата принтира кой ден колко пъти е въведен и приключва
#Примерен изход:
#Monday - 3 times
#Sunday - 1 time
#Saturday - 2 times

days = ["monday": 0, "tuesday": 0, "wednesday": 0, "thursday": 0, "friday": 0, "saturday": 0, "sunday": 0,]
for i in range(number_of_days):
    current_day = input("Enter day of week:").loaer_()
    days[current_day] += 1
    print(f"(day1): (count1)")