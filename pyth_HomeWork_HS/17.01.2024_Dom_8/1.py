# # 1. Create a class called Calculator that has the following static methods:
# 1. Create a class called Calculator that has the following static methods:
# • add (*args) - sums all the arguments passed to the function and returns the result
# •multiply (*args)  - multiplies all the numbers and returns the result
# • divide(*args)- divides all the numbers (starting from the first one) and returns the result
# • subtract(*args)- subtracts all the numbers (starting from the first one) and returns the result
# TEST CODE:
# print ( Calculator.add(5,10,14))
# print ( Calculator.multiply(1,2,3,5))
# print ( Calculator.divide(100,2))
# print ( Calculator.subtract(90,20,-50,43,7))
# OUTPUT:
# 19
# 30
# 50.0
# 70

class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for num in args[1:]:
            result /= num
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for num in args[1:]:
            result -= num
        return result

# Test code
print(Calculator.add(5, 10, 14))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
