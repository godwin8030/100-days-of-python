weight = float(input("Please enter your weight in kg: "))
height = float(input("Please enter your height in metre: "))
             
bmi = weight/(height**2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight") 
    