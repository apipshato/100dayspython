import random
name_string=input("give me everybody name, separeted by comma")
names=name_string.split(", ")
numes_item=len(names)
random_choice=random.randint(0, numes_item -1)
print(random_choice)

