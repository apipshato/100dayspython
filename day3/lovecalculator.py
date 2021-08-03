print("welcome to calcluator love")
name1=input("what is your name: \n")
name2=input("what is your second name: \n")

combine_string= name1 + name2
lower_case_string=combine_string.lower()
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")
true=t + r +u +e

l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love= l + o + v + e

love_score= str(true) + str(love)
print(love_score)

if (love_score < 10) or (love_score >90):
