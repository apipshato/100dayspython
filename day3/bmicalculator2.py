# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi=round(weight/height ** 2)
if bmi < 18.5:
    print("they are under wight")
elif bmi > 18.5  and bmi < 25:
    print(f"your bmi{bmi}, they are normal weight")
elif bmi >25 and bmi < 30:
    print(f"your bmi {bmi} ,they are overweight")
elif bmi > 30 and bmi < 35:
    print(f"your bmi {bmi} ,they are obess")
elif bmi > 35:
        print(f"your bmi {bmi}, they are clinicaly obess")
else:
    print(f"your bmi {bmi}, your clinically obese danger ")
