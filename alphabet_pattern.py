# ---- shivant kumar pandey ----
# Program to print alphabet pattern as given in question
# ASCII VALUE OF A: 65 TO Z=97

for i in range(65, 70):
    k = i
    # Inner loop
    for j in range(65, i + 1):
        print(chr(k), end=" ")
        k = k + 1
    print()
