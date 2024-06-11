# training-day-2
#Description of the day-2 training session

#data types in python:
#.Numeric type(int ,float, complex)
#2.Sequence type(str,list tuple)
#3.Mapping type (dict)
#4.Boolean types

#Example code
a,b,c=1,2,3
print(type(a))    #print the type of the variable

fruits=['apple','mango','grapes']
a,b,c= fruits
print(a)

a=1j
print(type(a))

#operators in python
#1.Arithmetic operators(addition, subtraction, multiplication, division, modulus, floor division)
#2.Assignment operators(=, +=, -=, *=, /=, %=, //=, **=)
#3.comparison operators(==, !=, >, <, >=, <=)
#4.Logical operators(and,or,not)
#5.Identity operators(is , is not)
#6.Membership operators(in, not in)
#7.Bitwise operators(&, |, ~,^,<<,>>)

#example for if else and comparison operator
a=10 #if string value is used it always gives you true as an answer
b=20
if b>a:
    print("b is greater than a")
else:
    print("a is greater than b")

#upper and lower case examples
num="sannidhi"
print(num.upper())
nam="SANN"
print(nam.lower())

#list Examples#
fruits=['apple','mango','orange'] #duplicATE IS ALLOWED 
veg=['onion','bell pepper'] 
print(len(fruits))
print(type(fruits))
print(fruits[2]) #negative indexing starts from -1
print(fruits[0:2]) #slice
fruits[1]="berry" #replace
print(fruits)

fruits.insert(1,"watermelon") #insert
print(fruits)

fruits.append("cherry") #append
print(fruits)

fruits.remove("apple") #remove
veg.pop(1)
print(veg)
print(fruits)

(veg.extend(fruits))
print(veg) #join 

fruits.sort(reverse=True) # reverse sort
print(fruits)

b=fruits.copy()
print(b)

#sorting
name="sannidhi"
c=sorted(name)
print(c)

#length of the 
name="sannidhi"
for i in name:
    print(i)
print(len(name))

#concat examples
a="susha, L,jain ok ,hedge"
print(a.split(","))
l1="susha"
l2="L"
print(concat(l1,l2))
