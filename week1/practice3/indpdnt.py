#task1
def is_alive(health):
    if health==0 or health<0:
        print("False")
    else:
        print("True")
is_alive(int(input()))
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
season_events(int(input("enter the month")))
#task3
