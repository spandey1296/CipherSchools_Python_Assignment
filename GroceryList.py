# This loop will go on until the budget is integer or float
while True:
    try:
        bg = float(input("Enter your budget : "))
        # if budget is integer or float it will be stored
        # temporarily in variable 's'
        s = bg
    except ValueError:
        print("PRINT NUMBER AS A AMOUNT")
        continue
    else:
        break



a = {"name": [], "quantity": [], "price": []}
b = list(a.values())
na = b[0]
qu = b[1]
pr = b[2]

# This loop terminates when user select 2.EXIT option when asked
# in try it will ask user for an option as an integer (1 or 2)
# if correct then proceed else continue asking options
while True:
    try:
        ch = int(input("1.ADD\n2.EXIT\nEnter your choice : "))
    except ValueError:
        print("\nERROR: Choose only digits from the given option")
        continue
    else:
        # check the budget is greater than zero and option selected
        # by user is 1 i.e. to add an item
        if ch == 1 and s > 0:

            pn = input("Enter product name : ")

            q = input("Enter quantity : ")

            p = float(input("Enter price of the product : "))

            if p > s:
                # checks if price is less than budget
                print("\nCAN,T BUT THE PRODUCT")
                continue

            else:
                # checks if product name already in list
                if pn in na:
                    # find the index of that product
                    ind = na.index(pn)

                    # remove quantity from "quant" index of the product
                    qu.remove(qu[ind])

                    pr.remove(pr[ind])

                    qu.insert(ind, q)

                    pr.insert(ind, p)
                    s = bg - sum(pr)

                    print("\namount left", s)
                else:
                    # append value of in "name", "quantity", "price"
                    na.append(pn)
                    qu.append(q)
                    pr.append(p)
                    s = bg - sum(pr)

                    print("\namount left", s)

        # if budget goes zero print "NO BUDGET"
        elif s <= 0:
            print("\nNO BUDGET")
        else:
            break

# will print amount left in variable 's'
print("\nAmount left : Rs.", s)

# if the amount left equals to any amount in price list
if s in pr:
    print("\nAmount left can buy you a", na[pr.index(s)])

print("\n\n\nGROCERY LIST")

# print final grocery list
for i in range(len(na)):
    print(na[i], qu[i], pr[i])
