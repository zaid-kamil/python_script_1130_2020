def pythagoras(perpendicular,base):
    """
    the classic function for pythagoras
    perpendicular : should be a number  
    base : should be a number
    example

    h = pythagoras(3,4)  
    """
    from math import sqrt
    hyp = sqrt(perpendicular**2 + base**2)
    return hyp

h = pythagoras(3,5)
print(f'hypotenuse is {h}')




