tpl = input('Enter the comma seperate values for tuple: ')
lst = input('Enter the comma seperate values for list: ')
# print(lst)
# print(type(lst))
lst = lst.split(',')
# print(lst)
# print(type(lst))
lst = [int(x) for x in lst]
print('Tuple:', tuple(lst))
print('List:', lst)
input()
