import random

min = 1
max = 3
score = 0
user1 = ""
user2 = ""
count = 0
name1 = input("enter your name")
name2 = input("enter your name")
user1 = {'name1': name1, 'score': 0}
user2 = {'name2': name2, 'score': 0}
print(user1)
print(user2)
while True:
    game = ['rock', 'paper', 'scissor']
    roll = input("lets start the game y/n : ")

    if roll == "no" or roll == "n" or roll == "N":
        print("GAME OVER")
        input("......PRESS ENTER TO CONTINUE.....")
        continue

    elif roll == "yes" or roll == "y" or roll == "Y":
        # print("GAME STARTED")
        print(f"TRIES {count}")
        roll1 = random.choice(game)
        roll2 = random.choice(game)

        #print(roll1)
        #print(roll2)

        if roll1 == game[0] and roll2 == game[1]:
            user2['score'] = user2['score'] + 1

            print(user1['name1'],"throws",roll1)
            print(user2['name2'],"throws",roll2)
            print(user2['name2'], "get", user2['score'], "point")
            count = count + 1
            print("------------------------------------------")
        elif roll1 == game[1] and roll2 == game[0]:
            user1['score'] = user1['score'] + 1

            print(user1['name1'],"throws",roll1)
            print(user2['name2'],"throws",roll2)
            print(user1['name1'], "get", user1['score'], "point")

            count = count + 1
            print("------------------------------------------")

        elif roll1 == game[2] and roll2 == game[1]:
            user1['score'] = user1['score'] + 1

            print(user1['name1'],"throws",roll1)
            print(user2['name2'],"throws",roll2)
            print(user1['name1'], "get", user1['score'], "point")
            count = count + 1
            print("------------------------------------------")

        elif roll1 == game[1] and roll2 == game[1]:
            user1['score'] = user1['score'] = 0

            user2['score'] = user2['score'] = 0

            print(user1['name1'],"throws",roll1)
            print(user2['name2'],"throws",roll2)
            print(user1['name1'], "get", user1['score'], "point")
            print(user2['name2'], "get", user2['score'], "point")
            count = count + 1
            print("------------------------------------------")

        elif roll1 == game[2] and roll2 == game[0]:
            user2['score'] = user2['score'] + 1

            print(user1['name1'],"throws",roll1)
            print(user2['name2'],"throws",roll2)
            print(user2['name2'], "get", user2['score'], "point")
            count = count + 1
            print("------------------------------------------")

        elif roll1 == game[0] and roll2 == game[0]:
            user1['score'] = user1['score'] = 0

            user2['score'] = user2['score'] = 0

            print(user1['name1'],"throws",roll1)
            print(user2['name2'],"throws",roll2)
            print(user1['name1'], "get", user1['score'], "point")
            print(user2['name2'], "get", user2['score'], "point")
            count = count + 1
            print("------------------------------------------")

        elif roll1 == game[2] and roll2 == game[2]:
            user1['score'] = user1['score'] = 0

            user2['score'] = user2['score'] = 0

            print(user1['name1'],"throws",roll1)
            print(user2['name2'],"throws",roll2)
            print(user1['name1'], "get", user1['score'], "point")
            print(user2['name2'], "get", user2['score'], "point")
            count = count + 1
            print("------------------------------------------")

        elif roll1 == game[0] and roll2 == game[2]:
            user1['score'] = user1['score'] + 1

            print(user1['name1'],"throws",roll1)
            print(user2['name2'],"throws",roll2)
            print(user1['name1'], "get", user1['score'], "point")
            count = count + 1
            print("------------------------------------------")

        if count == 8:
            print("------------GAME OVER---------")
            print("------------------------------------------")
            print("maximum", count, "tries reached")
            print("sana got", user1['score'], "score")
            print("fahmi got", user2['score'], "score")
            break
