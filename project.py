import functions

while True:
    p1 = input('Enter P1 (only True or False): ')
    if p1 == "True" or p1 == "False":
        p1 = bool(p1)
        break
    else:
        print("p1 type is wrong, enter only True or False\n")

while True:
    p2 = input('Enter P2 (only True or False): ')
    if p2 == "True" or p2 == "False":
        p2 = bool(p2)
        break
    else:
        print("p2 type is wrong, enter only True or False\n")

while True:
    p3 = input('Enter P3 (only True or False): ')
    if p3 == "True" or p3 == "False":
        p3 = bool(p3)
        break
    else:
        print("p3 type is wrong, enter only True or False\n")


a1 = functions.disjunction(p1, p2)
a2 = functions.conjunction(not p1, a1)
a3 = functions.implication(a2, p2)

b1 = functions.implication(p1, not p2)
b2 = functions.conjunction(p2, b1)
b3 = functions.implication(not p1, not p2)
b4 = functions.conjunction(b2, b3)

c1 = functions.implication(p2, p3)
c2 = functions.implication(p1, c1)
c3 = functions.implication(p1, p2)
c4 = functions.implication(c3, p3)
c5 = functions.implication(c2, c4)


f = open("result.txt", mode='w', encoding = 'utf-8')

f.write("\nResult for a: {}".format(a3))
f.write("\nResult for b: {}".format(b4))
f.write("\nResult for c: {}".format(c5))

list = [True, False]


##### Truth table for part a #############

f.write("\n\n\n\ntruth table for a:")
f.write("\np1\t\tp2\t\t(p1 \/ p2)\t\t(-p1 /\ (p1 \/ p2)\t\t\
    (-p1 /\ (p1 \/ p2) --> p2")

flag = True
counter = 0

for i in list:
    for j in list:
        p1 = i
        p2 = j

        a1 = functions.disjunction(p1, p2)
        a2 = functions.conjunction(not p1, a1)
        a3 = functions.implication(a2, p2)


        if (flag == True) and (counter > 0):
            if a3 != a3_prev:
                a_prop = "Contingency"
                flag = False
            else:
                if a3 == True:
                    a_prop = "Tautology"
                else:
                    a_prop = "Contradiction"

        a3_prev = a3
        counter += 1

        f.write("\n{}\t\t{}\t\t{}\t\t\t{}\t\t\t\t\t\t\t{}"\
            .format(p1, p2, a1, a2, a3))

f.write("\n\nThe propositions is a {}".format(a_prop))

###########################

##### Truth table for part b #############

f.write("\n\n\n\ntruth table for b:")
f.write("\np1\t\tp2\t\t(p1 --> -p2)\t\t(p2 /\ (p1 --> -p2)\t\t\
    (-p1 --> -p2)\t\t(p2 /\ (p1 --> -p2) /\ (-p1 --> -p2)")

flag = True
counter = 0

for i in list:
    for j in list:
        p1 = i
        p2 = j

        b1 = functions.implication(p1, not p2)
        b2 = functions.conjunction(p2, b1)
        b3 = functions.implication(not p1, not p2)
        b4 = functions.conjunction(b2, b3)


        if (flag == True) and (counter > 0):
            if b4 != b4_prev:
                b_prop = "Contingency"
                flag = False
            else:
                if b4 == True:
                    b_prop = "Tautology"
                else:
                    b_prop = "Contradiction"

        b4_prev = b4
        counter += 1
        
        f.write("\n{}\t\t{}\t\t{}\t\t\t\t{}\t\t\t\t\t\t{}\t\t\t\t\t{}"\
            .format(p1, p2, b1, b2, b3, b4))

f.write("\n\nThe propositions is a {}".format(b_prop))

############################

##### Truth table for part c #############

f.write("\n\n\n\ntruth table for c:")
f.write("\np1\t\tp2\t\tp3\t\t(p2 --> p3)\t\t(p1 -- > (p2 --> p3))\t\t\
    (p1 --> p2)\t\t((p1 --> p2) --> p3)\t\t\
    (p1 -- > (p2 --> p3)) --> ((p1 --> p2) --> p3)")

flag = True
counter = 0

for i in list:
    for j in list:
        for k in list:
            p1 = i
            p2 = j
            p3 = k

            c1 = functions.implication(p2, p3)
            c2 = functions.implication(p1, c1)
            c3 = functions.implication(p1, p2)
            c4 = functions.implication(c3, p3)
            c5 = functions.implication(c2, c4)


            if (flag == True) and (counter > 0):
                if c5 != c5_prev:
                    c_prop = "Contingency"
                    flag = False
                else:
                    if c5 == True:
                        c_prop = "Tautology"
                    else:
                        c_prop = "Contradiction"

            c5_prev = c5
            counter += 1

            f.write("\n{}\t\t{}\t\t{}\t\t{}\
                \t\t\t{}\t\t\t\t{}\t\t\t\t{}\t\t\t\t\t\t{}"\
                .format(p1, p2, p3, c1, c2, c3, c4, c5))

f.write("\n\nThe propositions is a {}".format(c_prop))

####################



f.close()

print("output printed to file result.txt!")
