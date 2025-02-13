p=input("Enter your password : ")


def check_number(p):
    if any(p.isdigit()):
        return True
    else:
        return False


def check_alpha(p):
   if any(p.isalpha()):
       return True
   else :
       return False
number_check=check_number(p)
alpha_check=check_alpha(p)

if len(p)<8 and len(p)>16:
    print("Invalid password !")
else :
    if number_check==True and alpha_check==True:
        print("Your password is valid : ")
    else:
        print("Invalid password!")








