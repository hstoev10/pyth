# broqch s funciq - kolko malki i kolko glavni bukvi ima
x = 0
y = 0
# za da jiveqt x,y, trqbva da sa v koda v def...ako sa taka izvun nego, moje chrez vuvejdane na global
# vutre v koda....global x ; global y

def count_upper_lower_chars(input_str):
    lower = 0
    upper = 0

    for char in input_str:
        if char.islower():
            lower += 1
        else:
            upper += 1

    print("The number of lowercase characters is:", lower)
    print("The number of uppercase characters is:", upper)

my_string = "MyStringHere"
count_upper_lower_chars(my_string)

