# Create a class called Integer.
# Upon initialization, it should receive a single parameter value (int).
# It should have 3 additional methods:
# • fom_float(float_value)- creates a new instance by flooring the provided floating
# number. If the value is not a float, return the message "value is not value"
# • fom_roman(value)- creates a new instance by converting the roman number (as string) to
# an int
# • from_string(value)- creates a new instance by converting the string to an int(if the value
# cannot be converted, return a message "wrong type")
# TEST CODE:
# first_num = Integer (10)
# print (first_num.value)
# second_num = Integer.from_roman("IV")
# print(second_num.value)
# print(Integer.from_float("2.6"))
# print(Integer.from_string("2.6"))
# OUTPUT:
# 10
# 4
# "value is not a float"
# "wrong type"

class Integer:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            raise ValueError("Value is not an integer")

    @classmethod
    def from_float(cls, float_value):
        if isinstance(float_value, float):
            return cls(int(float_value))
        else:
            return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for i in range(len(value)):
            if i > 0 and roman_dict[value[i]] > roman_dict[value[i - 1]]:
                result += roman_dict[value[i]] - 2 * roman_dict[value[i - 1]]
            else:
                result += roman_dict[value[i]]

        return cls(result)

    @classmethod
    def from_string(cls, value):
        try:
            return cls(int(value))
        except ValueError:
            return "wrong type"

# Test code
first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float(2.6))
print(Integer.from_string("2.6"))
