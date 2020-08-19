#   1.


#   2.

#   3.
# for i in range(100,1000):
#     if i==(i//100)**3+((i//10)%10)**3+(i%10)**3:
#         print(i)

#   4.
# list=[]
# for __ in range(10):
#     list.append(int(input("随意输入一个数字")))
# for i in range(0,len(list)-1):
#     for c in range(i+1,len(list)):
#         if list[i]>list[c]:
#             list[i],list[c]=list[c],list[i]
# print(list)

#   5.
# list=[4,35,7,64,7,35]
# for i in range(0,len(list)-1):
#     for c in range(i+1,len(list)):
#         if list[i]==list[c]:
#            del list[c]
# print(list)

#   6.
s="ABCACDBEFD"
s1=list(s)

for c in range(0,len(s1)-1):
    s2.remove(s1[c])
    s2 = s1.copy()
    if s1[c] not in s2:
        print(s1[c])
        break



