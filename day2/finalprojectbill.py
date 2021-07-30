print("welcome to the tip calculator")
bill=float(input("what was the bill $"))
tip=int(input("how much you give tips  10, 13 or 15"))
people=int(input("how moany people split the bill"))
tip_as_percent=tip/100
total_tip_amount=bill * tip_as_percent
total_bill=bill + total_tip_amount
bill_per_person=total_bill / people
final_amount=round(bill_per_person, 2)
final_amount="{:.2f}".format(bill_per_person)
print(f"each person pay \n ${final_amount}" )