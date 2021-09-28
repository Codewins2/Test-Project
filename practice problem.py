"""
# first problem solution 

def age():
    try:
            
        user = int(input("Enter your age "))
        print(f"The user is currently {user} years old")

        if user == 100:
            print("Congrats, you turned into 100 years old")

        elif user > 100:
            print("You seemed to be pretty old.")

        elif user < 100:
            print(f"You will turn 100 after {100-user} years")
            birth_year = 2021- user
            hundred = 100 - user
            this_year = 2021
            print("\n")
            print(f"He was born in {birth_year}")
            print("\n")
            print(f"He will turn 100 in {this_year+hundred-1}")



        else:
            print("Python greets you with an wonderful error message")
    except:
        print("You might have entered some wrong input")


def year():
    try:


        user = int(input("Enter the year you were born"))

        if user > 2021 or user < 0:
            print("You are not yet born")

        elif user < 1930:
            print("You seem to be the oldest person I have ever seen")


        else:
            print(f"The user's birth year is {user}")
            current_year = 2021 - user
            if current_year == 100:
                print("Congo, you turned into 100")


            elif current_year > 100:
                print("You seem to be pretty old.")


            elif current_year < 100:
                print("\n")
                print(f"He will turn 100 after {100 - current_year} years")
                another = 2021 - user
                another = 100 - another
                this_year = 2021
                print("\n")
                print(f"He will turn 100 into {this_year+another}")


            else:
                print("You might have entered some wrong input")
    except:
        print("You might have entered some wrong input")

print("Enter 1 for age \nor Enter 2 for birth year")


user_choice = int(input(""))

if user_choice == 1:
    age()


elif user_choice == 2:
    year()

else:
    print("Something is wrong")


# practice problem 2



try:
        
    apple_input = int(input("Enter the ammount of apples harry has got"))
    student_number = int(input("Enter how many students are there"))
    divisor  = int(input("Enter the divisor"))




    if student_number == divisor:
        print("This is not a range")
        for x in range(divisor,student_number+1):
            print(x,f"is the divisor of {apple_input}")


    else:
            
        if student_number > divisor or student_number<divisor:


            for x in range(divisor,student_number+1):
                if apple_input % x == 0:
                    print(x,f"is the divisor of {apple_input} and every kid will get {apple_input / x} apples") 
                    


except:
    print("You might have entered some wrong input")



# practice problem 3 - solution

user = []

size = int(input("Enter length of the list or the total element number -> "))

i = 0

for x in range(size):
    i += 1
    user.append(int(input(f"The {i} element is ")))




# first reverse 
print("The orignal list is ",user)

# making a copy of the input list. Otherwise the reverse will overwrite it
first = user[:]
first.reverse()
print("The first reverse is ",first)



fourth = user[:]
second = fourth[::-1]
print("The second reverse is ",second)


fourth = user[:]
third = [x for x in reversed(fourth)]
print("The third reverse is ",third)


fourth = user[:]
# fourth = []

for x in range(len(fourth)//2):
    fourth[x],fourth[len(fourth)-x-1] = fourth[len(fourth)-x-1], fourth[x]

print("The fourth reverse is ",fourth)

if first == second == third == fourth:
    print("Four of them have the same reverse value")


else:
    print("No. The values are not matching")






# practice problem - 4 - solution
# Author - Ismail Hossain
# purpose - Finding the next palindrome 




def palindrome(number):
    for x in range(1, number):
        number += 1
        var = str(number)
        new = var[::-1]
        if var == new:
            return number

        else:
            continue


lst = []

user = int(input("Enter how many number you wanna check\n"))

for b in range(1,user+1):
    lst.append(int(input(f"Enter {b} element\n")))


for v in lst:
    print(f"The next palindrome for {v} is ", palindrome(v))




# practice problem 5 - solution
# Author - Ismail Hossain
# purpose - if list element is greater than 10 return its the next palindrome else return that number


def palindrome(number):
    for x in range(1, number):
        number += 1
        var = str(number)
        rev = var[::-1]
        if var == rev:
            return number

        else:
            continue


lst = []

size = int(input("Enter how many elements you wanna add to the list"))


for x in range(1, size+1):
    lst.append(int(input(f"Enter {x} element ->")))

print("The orignal list",lst)

var = [palindrome(c) if c > 10 else c for c in lst]
print("Palindrofied list ", var)


"""



