#task1
def is_alive(health):
    if health==0 or health<0:
        print("False")
    else:
        print("True")
is_alive(int(input("Enter health rate: ")))
#task2
def season_events(n):
    months=[[12,1,2],[3,4,5],[6,7,8],[9,10,11]]
    if n in months[0] :
        print ( "You were born in Winter. White snow fell outside the window" )
    elif n in months[1] :
        print ( "You were born in Spring. Birds sang beautiful songs" )
    elif n in months[2] :
        print ( "You were born in Summer. The sun shone brighter than ever" )
    elif n in months[3] :
        print ( "You were born in Autumn. The harvest was incredible" )
    else :
        print ( "You need to enter the real number of the month" )
season_events(int(input("enter the number of the month: ")))
#task3
def check_pass(pswd):
    ch = ['*', '-', '#']
    isPerfect = True
    if len(pswd)!=8:
        print('password has to be 8 characters')
        isPerfect=False
    if not any(char.isupper() for char in pswd):
        print('password has to have uppercase letters')
        isPerfect=False
    if not any(char.islower() for char in pswd):
        print('password has to have lowercase letters')
        isPerfect=False
    if not any(char.isdigit() for char in pswd):
        print('password has to have at least one number')
        isPerfect=False
    if not any(char in ch for char in pswd):
        print('password has to have symbols like *-#')
        isPerfect=False
    if isPerfect:
        print('The password is perfect')
password = input("enter your password:")
check_pass(password)
