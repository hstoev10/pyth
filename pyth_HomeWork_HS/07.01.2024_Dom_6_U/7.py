# 
def shout(s, y=0) 
    s += 5
    if y:
        s += y + 1
        return s
    
result = shout(10)
print(result)
  
