print()
def whos_first(p11,p22):
    if(p11==p22):
        return "tie"
    elif (p11>p22):
        return "p2 is faster"
    else:
        return "p1 is faster"
p1="     Bang!"
p2="        Bang! "
p11 = len(p1) - len(p1.lstrip())
p22 = len(p2) - len(p2.lstrip())
print(whos_first(p11,p22))
