weight_str = input('Enter weight in kilograms:')
height_str = input('Enter height in centimeters:')
weight = float(weight_str)
height = float(height_str)
mass_index = (weight / (height*height) * 10000)
print(f"BMI (body mass index) is : {mass_index: 6.1f}")


