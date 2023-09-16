weight = float(input("weight: "))
unit = input ("(K)g or (L)bs ")

if unit.upper() =="K":
    converted = weight / 2.205
    print (str(converted) + " weight in lbs: ")
elif unit.upper() =="L":
    converted = weight * 2.205
    print (str(converted) + " weight in kg: ")