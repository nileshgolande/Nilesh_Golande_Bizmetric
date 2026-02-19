# Write a list comprehension to generate squares of numbers from 1 to 10.

a = [i**2 for i in range(1,11)]
print(a)

# 2. Create a list of even numbers between 1 and 50 using list 
# comprehension.

b= [i for i in range(1,51) if i%2==0]
print(b)

# 3. Convert all strings in a list to uppercase using list comprehension.

a = ["a",'b','c']
b =  [i.upper() for i in a]
print(b)


# 4. Given a list of integers, create a new list that contains only the positive 
# numbers.

a =  [ 1,2,3,4,5,6,-5,-4]
b = [i for i in a if i > 0]
print(b)



# 5. Create a list of tuples (num, num^2) for numbers 1 to 5.

lst = [1,2,3,4]

tup = [(i,i**2) for i in lst]

print(tup)

# 6. Extract all vowels from a given string using list comprehension.

str1 = 'qwertyuiopasdfghjklzxcvbnm'
vow = 'aeiou'

vowels = [ i for i in str1 if i  in vow]
con = [ i for i in str1 if i not in vow]

print(vowels )
print(con)

# 7.Flatten a 2D list using list comprehension.

lst=[[1,2,3,4],[2,3,4,5]]

flt = [item for i in lst for item in i ]
print(flt)

# 8. Replace all negative numbers in a list with 0 using list comprehension.
a =  [ 1,2,3,4,5,6,-5,-4]
rep = [i if i >= 0  else 0 for i in a ]
print(rep)

# 9. Given a list of words, create a list of lengths of each word.

lst = ["abcd",'abcde','asdfg']
lst2  = []
for i in lst:
    lst2.append((i , len(i)))
print(lst2)

# 10. Filter out words that start with the letter 'A' or 'a
lst = ["abcd",'Abcde','bsdfg']
lst2  = []
for i in lst:
    lst2.append((i , len(i)))
print(lst2)


# 11. From a list of numbers, generate a list of “even” or “odd” strings using 
# list comprehension.

a = [i for i in range(10)]
b= ['even' if i%2 == 0 else  'odd' for i in a ]

print(b)

# 12. Create a list of numbers divisible by both 3 and 5 in range 1–100.
l = [i for i in range(1,101) if i%3==0 and i%5==0]
print(l)

# 13. Write a nested list comprehension to generate a multiplication table 
# for 1–5.

a = [[[i*j for i in range(1,11)] for j in range(1,6)]]
print(a)

# 14. Convert a dictionary’s keys into a list using list comprehension.
data = {
    "E001": {"name": "Alice", "salary": 50000, "department": "HR"},
    "E002": {"name": "Bob", "salary": 60000, "department": "IT"},
    "E003": {"name": "Charlie", "salary": 55000, "department": "Finance"},
    "E004": {"name": "David", "salary": 65000, "department": "IT"},
    "E005": {"name": "Eva", "salary": 48000, "department": "HR"},
    "E006": {"name": "Frank", "salary": 70000, "department": "Management"},
    "E007": {"name": "Grace", "salary": 53000, "department": "Finance"},
    "E008": {"name": "Hannah", "salary": 62000, "department": "IT"},
    "E009": {"name": "Ian", "salary": 47000, "department": "HR"},
    "E010": {"name": "Jane", "salary": 58000, "department": "Finance"}
}

a = [i for i in data.keys()]
print(a)

# 15. Extract numeric digits from a string using list comprehension.

a = "gr4323543tew  "
a = [i for i in a if i.isdigit()]
print(a)


# 16. Use list comprehension to remove all spaces from a string.

a = ["gr4323543tew  ","   r"]

a =[i.strip() for i in a]
print(a)

# 17. Create a list of characters that appear more than once in a string.
a = "qwertytre3w2qwertytreee"
b= {}
for i in a:
    i  = str(i)
    if i in b:
        b[i] +=1
    else:
        b[i] = 1
v = [i for i,j in b.items() if j>1 ]
print(v)


# 18. From a list of sentences, generate a list of all words (split using list 
# comprehension).

a =[ "my name is nilesh" ,"i am mcaa Student"]
for i in a:
    for j in i:
        if j != " ":
            print(j)



# 19. Create a list of unique elements from a list using list comprehension + 
# condition.


# 20. Generate all pairs (x, y) where x is from list A and y is from list B 
# (cartesian product).

a= [1,2,3,4,5,6]
b= [1,2,3,4,5,6]
a = list(zip(a,b))
print(a)



#lambda
# 1. Write a lambda to add two numbers.

a = lambda x,y:x+y


# 2. Create a lambda to check if a number is even.
b = lambda i : i%2 == 0 


#3. Write a lambda to get the last character of a string.

c = lambda str1 : str1[-1]
print(c("asdf"))

# 4. Use lambda with map() to square every number in a list.

square = map(lambda x : x**2,[1,2,3,4,5])
print(list(square))


# 5. Use lambda with filter() to get only odd numbers from a list.

odd = filter(lambda x : x%2==1,[1,2,3,4,5,6,7])
print(list(odd))


#6. Use sorted() + lambda to sort a list of tuples by second value.
a = [(1,2),(3,4),(1,1),(1,9)]
s = sorted(a , key=lambda x:x[1])
print(s)

# 7. Create a lambda to check if a string is a palindrome.

a = "nitin"
b = 'raju'
pal = lambda x : x == x[::-1]
print(pal(a))
print(pal(b))

# 8. Use lambda to find maximum of three numbers.
a = [1,2,3,4,5,2,3,3,2,]
c = lambda x : sorted (x , reverse=True)[:3]
print(c(a))

# 9. Write a lambda to reverse a string.
a = "abcd"
b= lambda x : x[::-1]
print(b(a))


# 10. Use lambda with map() to convert a list of strings to integers.

d =['1','2','4','5']

# a = lambda x : [int(i) for i in x]
# print(a(d))
b = map(lambda x: int(x) , d)
print(list(b))


# 11. Use lambda with filter() to remove empty strings from a list.
x = ['q','e','t',"",'']
b= filter(lambda x : x!=''  , x)
print(list(b))

# 12. Use lambda to compute factorial using reduce() (yeah, that one-liner 
# madness).

from functools import reduce
fact = reduce(lambda a,b:a*b , [i for i in range(1,5)])
print(fact)

# 13. Write a lambda that returns the larger of two numbers.

x = lambda x,y: x if x>y else y
print(x(20,10))

#14. Use lambda to check if number is divisible by 5.

x = lambda x : True if x%5 == 0 else False
print(x(5))

# 15. Use lambda + map() to add 10 to each element of a list.

a = [1,2,3,4,5,6]
b= map(lambda x : x+10 , a)
print(list(b))


# 16. Use lambda to sort a list of dictionaries by a key (like "age").

d = {'b': 2, 'a': 5, 'c': 1}

l = lambda x : sorted(x.items())

print(dict(l(d)))

# 17. Write a lambda that returns True if a character is a vowel.

l = lambda x : x in "AEIOUaeiou"
print("vowel =" ,l("a"))

#18. Use lambda + filter to extract words of length > 5 from a list.

a = ['qwerrrrrrrty', 'qweregsdc','qwer','a']
l = list(filter(lambda x : len(x) > 5  , a))
print(l)

# 19. Use lambda to calculate the area of a circle (πr²).

area  = lambda r : 3.14*r*r
print(area(3))

#20. Write a lambda to remove duplicates from a list using filter + set
b = ['a','a','b','b','c','c']
a  = list(filter(lambda x : x , set(b)))
print(a)


# 21. Use lambda with reduce() to find the product of all numbers in a list.

fact = reduce(lambda a,b:a*b , [i for i in range(1,5)])
print(fact)

# 22. Write a lambda that returns absolute value of a number.