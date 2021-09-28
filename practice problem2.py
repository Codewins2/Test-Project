"""
# Guess the number
# this game can be played between two friends
# Author - Ismail Hossain


try:

    import random
    print("Welcome to the guessing game/n ")
    player1 = int(input("Enter your number > "))
    other_player1 = int(input("Enter your friends number > "))

    def player():
        secret_number = random.randint(player1, other_player1)
        print("First it's your turn to guess the number\n")
        attempt = 0

        while True:
            print(secret_number)
            print(f"Guess the number between {player1} and {other_player1}")
            guess = int(input("Enter your guess number > "))

            if guess == secret_number:
                print("Congratulations, you guessed the right number\n")
                attempt += 1
                print(f"And you have taken {attempt} attempts\n")
                break

            elif guess > secret_number:
                attempt += 1
                print(
                    "Wrong guess! You guessed number is lower than the secret number!\n")

            elif guess < secret_number:
                attempt += 1
                print(
                    "Wrong guess! Your guessed number is higher than the secret number!\n")
            else:
                print("You might have entered some wrong input")

        return attempt

    player_attempt = player()

    def another_player():
        secret_number2 = random.randint(player1, other_player1)
        print("Now, it's your friends turn to guess the secret_number")

        attempt = 0
        count = 0

        while count <= player_attempt:
            print(
                f"Please guess the number between {player1} and {other_player1} numbers ")
            print(secret_number2)
            guess = int(input("Enter your guess number > "))

            count += 1
            # if attempt > player_attempt:
            #     print("Your friends has lost the game.")
            #     print(f"He has already taken {attempt} attempts")
            #     break

            if guess == secret_number2:
                print("Congratulations, you guessed the right number\n")
                attempt += 1
                print(f"And you have taken {attempt} attempts")
                break

            elif guess > secret_number2:
                attempt += 1
                print(
                    "Wrong guess! Your guessed number is lower than the secret number!\n")

            elif guess < secret_number2:
                attempt += 1
                print(
                    "Wrong guess! Your guessed number is higher than the secret number!\n")

            else:
                print("You might have entered some wrong input")

        return attempt

    other_attempt = another_player()

    if player_attempt == other_attempt:
        print("You both have taken the same amount of attempts\n")
        print("The match tied")

    elif player_attempt < other_attempt:
        print("You're friend has lost the game\n")
        print("Congratulations, you have won the guess game")

    elif other_attempt > player_attempt:
        print("You're friend has won the the game")


except:
    print("Please enter the right input")




# author - Ismail Hossain
# purpose - searchbar - finds matches according to a query string



def matches(sentence0,sentence1):
    first = sentence0.strip().split(" ")
    second = sentence1.strip().split(" ")
    score = 0
    for x in first:
        for y in second:
            if x in y:
                score += 1
                

    return score


if __name__ == '__main__':

    sentence0 = "What is your name buddy"
    sentence1 = "My name is Ismail"

    # print(matches(sentence0,sentence1))

    sentences = ["What is your name","What are you gonna do with that",
    "I just wanted to know","Everything has a price"]


    query = input("Enter a query string\n").lower()

    scores = [matches(query,sentence) for sentence in sentences]
    
    
    sortsentscore = [x for x in sorted(zip(scores,sentences))[::-1] if x[0] != 0]
    # print(sortsentscore)

    print(f"{len(sortsentscore)} results found")

    for score,item in sortsentscore:
        print(f"\"{item}\" with a score of {score}")

"""

# author - Ismail
# purpose - finding the false number in the mulitplication table


def iscorrect(number):
    var = [number*x for x in range(1,10+1)]
    return var


def wrongmulti(number1):
    var1 = [number1*x for x in range(1, 10+1)]

    user = int(input("""Enter 1 if you want to return the correct mulitplication table/n
    #   Or, enter 2 If you want to return a wrong multiplication table\n"""))
    if user == 1:
        return var1

    elif user == 2:
        var1[int(input("Enter you want to change"))] = int(input("Enter the wrong number"))
        return var1




if __name__ == '__main__':
    result = iscorrect(int(input("Enter which number's multiplication you want")))
    wrong = wrongmulti(int(input("Enter the fraud's mulit table")))

    # trans = set(result)
    # trans1 = set(wrong)

    if result == wrong:
        print("He has given the right multiplication table",result)
        print("He has become honest now")

    else:
        def compare(x, y):
            # converting the list to set. So that we could get the non matching number
            return set(x) - set(y)

        unmatching_number = compare(wrong, result)
        first = list(unmatching_number)
        second = first[0]
        print("He has given a wrong multiplication table","\n",wrong)
        print("His given wrong number is ", second, "\n")
        final = wrong.index(second)
        print("Rohan's mulitplication table has wrong output at ", final, "index\n")
        print("Rohan is a fraud")



 

