weight=int(input("Enter your weight in kg : "))
height=int(input("Enter your height meters : "))
body_mass_index=weight/(height**2)
print(f"Body mass index : {round(body_mass_index,2)}")
if body_mass_index>40:
    print("Pass")
else :
    print("Fail")