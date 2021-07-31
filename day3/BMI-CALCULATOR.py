height=float(input("enter your height in m: "))
weight=float(input("enter your weight in kg: "))

if weight <= 18.5:
    print("they are under wight")
    if weight >= 18.5  and weight <= 25:
        print("they are normal weight")
    elif weight >=25 and weight <= 30:
        print("they are overweight")
    elif weight >= 25:
        print("they are overweight")
    elif weight <= 30:
        print("they are overweight")
    
        