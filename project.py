def play():
    import random

    class test:

        
        def player_match(self):
            print("Your player is batting right now.")
            player_point = 0
            player = ""
            options = ["One","Two","Three","Four","Five","Six"]
            while True:
                print("Enter 1 for One")
                print("Enter 2 for Two")
                print("Enter 3 for Three")
                print("Enter 4 for Four")
                print("Enter 5 for Five")
                print("Enter 6 for Six")

                player_choice = int(input("Enter your choice"))
                try:
                    if player_choice == 1:
                        player = "One"
                        print("Player chooosed One")

                    elif player_choice == 2:
                        player = "Two"
                        print("Player chooosed Two")
                    

                    elif player_choice == 3:
                        player = "Three"
                        print("Player choosed Three")


                    elif player_choice == 4:
                        player = "Four"
                        print("Player choosed Four")


                    elif player_choice == 5:
                        player = "Five"
                        print("Player choosed Five")

                    elif player_choice == 6:
                        player = "Six"
                        print("Player choosed Six")



                    else:
                        print("You might have entered some invalid input")

                except Exception as e:
                    print("You might have entered some wrong input")

                
                computer_choice = random.choice(options)
                print("The computer chooses ",computer_choice)


                if player == computer_choice:
                    print("You are out. ")
                    print("You scored ",player_point,"runs","\n")
                    print(f"The computer need to score {player_point + 1}")
                    print("Now, it's computer's turn to bat. Ball well!!! ")
                    return player_point
                    exit()

                elif player == "One":
                    print("You scored one run")
                    player_point += 1


                elif player == "Two":
                    print("You scored Two runs")
                    player_point += 2



                elif player == "Three":
                    print("You scored Three runs")
                    player_point += 3


                elif player == "Four":
                    print("You scored Four runs")
                    player_point += 4


                elif player == "Five":
                    print("You scored Five runs")
                    player_point += 5


                elif player == "Six":
                    print("You scored Six runs")
                    player_point += 6
                


        def computer_match(self):
            computer_point = 0
            player = ""
            options = ["One","Two","Three","Four","Five","Six"]
            while True:
                print("Enter 1 for One")
                print("Enter 2 for Two")
                print("Enter 3 for Three")
                print("Enter 4 for Four")
                print("Enter 5 for Five")
                print("Enter 6 for Six")

                player_choice = int(input("Enter your choice"))
                try:
                    if player_choice == 1:
                        player = "One"
                        print("Player chooosed One")

                    elif player_choice == 2:
                        player = "Two"
                        print("Player chooosed Two")
                    

                    elif player_choice == 3:
                        player = "Three"
                        print("Player choosed Three")


                    elif player_choice == 4:
                        player = "Four"
                        print("Player choosed Four")


                    elif player_choice == 5:
                        player = "Five"
                        print("Player choosed Five")

                    elif player_choice == 6:
                        player = "Six"
                        print("Player choosed Six")



                    else:
                        print("You might have entered some invalid input")

                except:
                    print("You might have entered some wrong input")
                    
                
                new = player_score
                computer_choice = random.choice(options)
                print("The computer chooses ",computer_choice)


                if player == computer_choice:
                    print("computer is out. ")
                    
                    print("The computer scored",computer_point)
                    return computer_point
                    exit()

                elif computer_point > new:
                    
                    print(f"Game over! The player scored {new} and the computer score {computer_point} ")
                    print("The computer won this match")
                    break



                elif computer_choice == "One":
                    print("computer scored one run")
                    computer_point += 1


                elif computer_choice == "Two":
                    print("Computer scored Two runs")
                    computer_point += 2



                elif computer_choice == "Three":
                    print("computer scored Three runs")
                    computer_point += 3


                elif computer_choice == "Four":
                    print("computer scored Four runs")
                    computer_point += 4


                elif computer_choice == "Five":
                    print("computer scored Five runs")
                    computer_point += 5


                elif computer_choice == "Six":
                    print("computer scored Six runs")
                    computer_point += 6


    var = test()
    player_score = var.player_match()
    computer_score = var.computer_match()
    try:
        if player_score == computer_score:
            print(f"The match drawn. The player scored {player_score} and the computer scored {computer_score}")
            
        elif player_score > computer_score:
            print(f"The player's score is {player_score} and computer's score is {computer_score}")
            print("The player has won the match")


        elif computer_score > player_score:
            print(f"The player's score is {player_score} and computer's score is {computer_score}")
            print("The computer has won the match")


        else:
            print("Python greets you with an wonderful error message")


    except Exception as e:
        print("")

