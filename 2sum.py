#two sum
num=[2,7,11,15]
tar=13
for i in range(len(num)-1):
    for j in range(i+1,len(num)):
        if num[i]+num[j]==tar:
            print ([i,j])

