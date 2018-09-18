Number = int(input("Enter your Number :"))

def evenodd(Number):
    if (Number % 2 == 0):
        return "even"
    else:
        return "odd"
print (evenodd(Number))
