# list 
names = ['aaa', 'bbb', 'ccc' , 'ddd' , 'eee']
print (names)

numbers = [1,2,3,4,5,6,7,8,9]
max = numbers[0]
for number in numbers :
    if number > max :
        max = number
print (max)

#2d list

matrix = [
    [1,2,3],
    [2,3,4],
    [3,4,5]
]
matrix[0][2]
print(matrix[0][2])
for row in matrix :
    for no in matrix :
        print(no)
        
        
     
numbers = [4,5,6,7,8,9,2,]
numbers.append(20)
numbers.insert(0,3)
numbers.remove(2)
numbers.pop()
numbers.sort()
numbers.reverse()
print(numbers)


numbers = [2,4,5,3,7,8,9,5,3,5,6,7,8,5,4,3,3]
uniques =[]
for  no in numbers:
    if no not in uniques :
        uniques.append(no)
    print(uniques)  
    print(uniques.sort)  
    