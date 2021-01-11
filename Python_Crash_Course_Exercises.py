#	Python Crash Course Exercises 

#	What is 7 to the power of 4?

output = 7 ** 4


#	Split this string into a list:
# 
#	s = "Hi there Sam!"

s = "Hi there Sam!"

output = s.split()


#	Given the variables:
# 
#	planet = "Earth"
#	diameter = 12742
# 
#	The diameter of Earth is 12742 kilometers.

planet = "Earth"
diameter = 12742

print(f'The diameter of {planet} is {diameter} kilometers.')


#	Given this nested list, use indexing to grab the word "hello".

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]

output = lst[3][1][2][0]


#	Given this nested dictionary grab the word "hello". 

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

output = d['k1'][3]['tricky'][3]['target'][3]


#	What is the main difference between a tuple and a list?

#	Tuple is immutable


#	Create a function that grabs the email website domain from a string in the form:
# 
#	user@domain.com
#     
#	So for example, passing "user@domain.com" would return: domain.com

def domainGet(email):
    return email.split('@')[-1]

output = domainGet('user@domain.com')


#	Create a basic function that returns True if the word 'dog' is contained in
#	the input string. Don't worry about edge cases like a punctuation being attached
#	to the word dog, but do account for capitalization.

def findDog(input_string):
    return 'dog' in input_string.lower().split()

output = findDog('Is there a dog here?')


#	Create a function that counts the number of times the word "dog" occurs in a
#	string. Again ignore edge cases.

def countDog(input_string):
    
    count = 0
    string_list = input_string.lower().split()
    
    for word in string_list:
        if word == 'dog':
            count += 1
    
    return count

output = countDog('This dog runs faster than the other dog dude!')


#	Use lambda expressions and the filter() function to filter out words from a
#	list that don't start with the letter 's'. For example:
# 
#	seq = ['soup','dog','salad','cat','great']
# 
#	should be filtered down to:
# 
#	['soup','salad']

seq = ['soup','dog','salad','cat','great']

output = list(filter(lambda word: (word[0] == 's'), seq))


# 	Final Problem:
#
#	You are driving a little too fast, and a police officer stops you. Write a function
#   to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
#   If your speed is 60 or less, the result is "No Ticket". If speed is between 61 
#   and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is
#	"Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters
#	of the function) -- on your birthday, your speed can be 5 higher in all cases.

def caught_speeding(speed, is_birthday):
    
    if is_birthday:
        speed -= 5
    
    if speed <= 60:
        return 'No Ticket'
    elif 60 < speed <= 80:
        return 'Small Ticket'
    else:
        return 'Big Ticket'

output = caught_speeding(81,True)

output = caught_speeding(81,False)
