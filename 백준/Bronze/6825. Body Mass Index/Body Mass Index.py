W = float(input())
H = float(input())

BMI = W / (H ** 2)

if BMI >= 25:
    print("Overweight")
elif BMI < 18.5:
    print("Underweight")
else:
    print("Normal weight")