# Ali Sayedsalehi

p = False
q = True

def negation (p):
    if p == True:
        return False
    elif p == False:
        return True
    else:
        print("data not boolean")


def conjunction(p,q):
    if (p == True and q == True):
        return True
    elif (p == False and q == False):
        return False
    elif (p == True and q == False):
        return False
    elif (p == False and q == True):
        return False
    else:
        print("data not boolean")


def disjunction(p, q):
    if (p == True and q == True):
        return True
    elif (p == False and q == False):
        return False
    elif (p == True and q == False):
        return True
    elif (p == False and q == True):
        return True
    else:
        print("data not boolean")


def implication (p, q):
    if (p == True and q == True):
        return True
    elif (p == False and q == False):
        return True
    elif (p == True and q == False):
        return False
    elif (p == False and q == True):
        return True
    else:
        print("data not boolean")

def biconditional (p, q):
    if (p == True and q == True):
        return True
    elif (p == False and q == False):
        return True
    elif (p == True and q == False):
        return False
    elif (p == False and q == True):
        return False
    else:
        print("data not boolean")

