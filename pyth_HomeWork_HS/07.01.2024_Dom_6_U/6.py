# funkciq vuv funkciqta da polu4avat 2 parametura za iz4esklenie. purvata funciq *2, 

def outer_fun(a, b):
    square = a * 2
    def additime(a, b):
        return a + b 
    add = additime(a, b)
    return add + square 
result = outer_fun(5, 10)
print(result) 
