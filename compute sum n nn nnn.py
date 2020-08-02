# Input an integer (n) and computes the value of n+nn+nnn
num = input('Enter an integer: ')
n = int('%s'%num)
# print(n, type(n))
nn = int('%s%s'%(num,num))
nnn = int('%s%s%s'%(num,num,num))
print('Result: ', n+nn+nnn)
input()




# num = int(input('Enter an integer: '))
# n = int('%i'%num)
# # print(n, type(n))
# nn = int('%i%i'%(num,num))
# # print(nn, type(nn))
# nnn = int('%i%i%i'%(num,num,num))
# print('Result: ', n+nn+nnn)
# input()
