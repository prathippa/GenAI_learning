# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

a = [1,2,3,4,5,6,7,8]
t = 15

for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        for k in range(i+1,len(a)):
            if a[i]+ a[j] + a[k]== 15:
                print(a[i],a[j],a[k])