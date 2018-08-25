
def answer():
    for  a in range(1,10):
        print(a)

def answer2():
    lis=[1,3,5,7,9,10,11]
    sum=0
    for num in lis:
        sum=sum+num
    print(sum)

def answer3():
    for x in range(1, 11):
        for y in range(1, 11):
            print '%d * %d = %d' % (x, y, x*y)


answer()
print("\n-------------------------------------------")
answer2()
print("\n-------------------------------------------")
answer3()
print("\n-------------------------------------------")
