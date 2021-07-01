name= input('Name')
if name == "Kuddus":
    print('Hi')
age = int(input('Age'))
if age > 12 and age < 18: 
    print(f"{name} you are teen age")
elif age > 18 and age < 35:
    print(f"{name} You are young")
elif age > 35 and age < 50 :
    print(f"{name} You are middle aged")
elif age > 50 and age < 100:
    print(f"{name} You are old")
