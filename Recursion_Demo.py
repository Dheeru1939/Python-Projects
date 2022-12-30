print('\nCode being developed by 202204104610033\n')
def binary_search(alist, start, end, key):
    if not start < end:
        return -1
    mid = (start + end)//2
    if alist[mid] < key:
        return binary_search(alist, mid + 1, end, key)
    elif alist[mid] > key:
        return binary_search(alist, start, mid, key)
    else:
        return mid
def user_input():
  alist = input('Enter the numbers in the list seperated by white space: ')
  alist = alist.split()
  print(alist)
  return alist
alist=user_input()
alist = [int(x) for x in alist]
key = int(input('The number to search for: '))

index = binary_search(alist, 0, len(alist), key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index+1))