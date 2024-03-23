#Test Program
#Number=1 return 1
#Number=2 return 1+4
#Number=3 return 1+4+9


def squaredNum(number):
    total=0
    for num in range(1,number+1):
        total=total+num**2
    return total

print(squaredNum(70))
