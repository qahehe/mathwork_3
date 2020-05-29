#calculate Eurler's phi function
#@author:陈海龙
def Eurler(n):
    i=2
    count =n
    while(i*i<=n):
        if(n%i==0):
            count=count-count//i
            while(n%i==0):
                n=n//i
        i=i+1
    if(n>1):
        count=count -count//n
    return count

#测试案例
a=7
b=Eurler(a)
print(b)
