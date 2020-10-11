import random
import copy
numlist=[random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10)]
operators=['+','-','*','/']
print(numlist)
expression=[]
def opNum(n1,n2):
    division=0
    division2=0
    if n2>0:
        division=n1/n2
    if n1>0:
        division2=n2/n1
    return [
        [
            '('+str(n1)+'+'+str(n2)+')',
            '('+str(n1)+'-'+str(n2)+')',
            '('+str(n2)+'-'+str(n1)+')',
            '('+str(n1)+'*'+str(n2)+')',
            '('+str(n1)+'/'+str(n2)+')',
            '('+str(n2)+'/'+str(n1)+')'
        ],
        [n1+n2,n1-n2,n2-n1,n1*n2,division,division2]
        ]
result=[]

#运算顺序 n1+n2+n3+n4
#n1+(n2+n3+n4)
#n1+(n2+n3)+n4
#n1+n2+(n3+n4)
#(n1+n2+n3)+n4
for i in range(0,4):
    for j in range(i+1,4):
        list1=copy.copy(numlist)
        list2=[list1.pop(i),list1.pop(j-1)]
        result1=opNum(list1[0],list1[1])
        result2=opNum(list2[0],list2[1])
        
        for i2 in range(0,6):
            for j2 in range(0,6):
                resultArr=opNum(result1[1][i2],result2[1][j2])
                for k2 in range(0,6):
                    if resultArr[1][k2]==24:
                        print(result1[0][i2])
                        print(result2[0][j2])
                        print(resultArr[0][k2])
                        print('--------')
        for i2 in range(0,6):
            result3=opNum(result1[1][i2],list2[0])
            result4=opNum(result1[1][i2],list2[1])
            for j2 in range(0,6):
                resultArr1=opNum(result3[1][i2],list2[1])
                resultArr2=opNum(result4[1][i2],list2[0])
                for k2 in range(0,6):
                    if resultArr1[1][k2]==24:
                        # print(result1[0][i2])
                        # print(result2[0][j2])
                        print(resultArr1[0][k2])
                        print('--------')
                    if resultArr2[1][k2]==24:
                        # print(result1[0][i2])
                        # print(result2[0][j2])
                        print(resultArr2[0][k2])
                        print('--------')