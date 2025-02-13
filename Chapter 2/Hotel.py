bill_amount = float(input("Enter bill amount : "))
no_person = int(input("Enter no. of persons : "))
tip_per = float(input("Enter % of tip you want to pay : "))
tip_amount = bill_amount*(tip_per/100)
total_amount = bill_amount+tip_amount
contri = total_amount/no_person
print(f"Contribution per head : {round(contri,2)}")