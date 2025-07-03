#string applications
College='''"Zeal college of engineering"
 Nahre road , zeal point , Pune -41
'''
print(College)
string=('abcdefghijklmnopqrstuvwxyz')
print(string[-10])
print(string[12])
print(string[10:22])
print(string[:10])
print(string[3:-10])
print(string[-10:])
#to  copy whole string 
print(string[:])

#formatted string
f_name='yash'
l_name='patil'
message=f_name + ''+ l_name +' is a coder '
print(message)
msg=f'{f_name} {l_name} is a coder'
print(msg)


#string methods 
#len function 
course='python progam for beginners '
print(len(course)) 
print(course.upper())
print(course.find('f'))
print(course.replace('progam','program'))
print('for' in course)