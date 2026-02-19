# Write a list comprehension to generate squares of numbers from 1 to 10.

a = [i**2 for i in range(1,11)]
print(a)

# 2. Create a list of even numbers between 1 and 50 using list 
# comprehension.

b= [i for i in range(1,51) if i%2==0]
print(b)

# 3. Convert all strings in a list to uppercase using list comprehension.

a = ["a",'b','c']
b=  [i.upper() for i in a]
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
