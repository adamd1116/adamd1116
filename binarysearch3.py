#Maybe a binary search I have no idea
#Took me 30 minutes to realise the algorithm was attempting to search through an unsorted list even though it was designed for a sorted list
import random

found = False
l = [9, 5, 4, 15, 2, 2246, 53 ,87, 13, 59, 12 ,69, 1039 ,5929, 235, 6837, 29]
t  = random.choice(l)
le = 0
r = len(l)-1
m = round((le+r)/2)
ll = len(l)-1
ll2 = len(l)
search = False

for j in range(0,ll2):
    check_for_swap = False
    for i in range(0,ll):
        if l[i] > l[i + 1]:
            swap = l[i]
            l[i] = l[i + 1]
            l[i + 1] = swap
            check_for_swap = True
    if check_for_swap == False:
        search = True
        break

print(f'\nSorted: ',l,'\n')

if search == True:
    while found == False:
        if t <= l[m]:
            if t < l[m]:
                print(f"\tTarget is less than middle")
                r = m
                m = (le+r)//2
                if t < le:
                    le-=1
                else:
                    pass
            elif t == l[m]:
                print(f"\n\tTarget found: {t}")
                found = True
                break
        if t >= l[m]:
            if t > l[m]:
                print(f"\tTarget is larger than middle")
                le = m
                m = (le+r)//2
                if t > r:
                    r+=1
                else:
                    pass
            elif t == l[m]:
                print(f"\n\tkTarget found: {t}")
                found = True
                break
    else:
        pass