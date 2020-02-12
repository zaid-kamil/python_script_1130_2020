def armstrong(number):
    temp = number
    total =  0
    while temp>0:
        r = temp%10
        total += r**3
        temp //= 10
    if number == total:
        return True
    else:
        return False

# called in loop
for i in range(100,500):
    if armstrong(i):
        print(i)
    
