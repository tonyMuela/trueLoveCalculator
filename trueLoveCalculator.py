number1 = 0
name1 = input("What's your first and last name?\n")
name2 = input("What's your crush's name? \n")
def calculate_love_score(name1, name2):
    combinedName = name1 + name2

    totalOne = 0
    totalTwo = 0

    wordOne = "TRUE"
    wordTwo = "LOVE"

    for letter in combinedName.upper():
        if letter in wordOne:
            totalOne += 1
    for letter in combinedName.upper():
        if letter in wordTwo:
            totalTwo += 1
    print(f"Your true love score is {totalOne}{totalTwo} out of 100")


calculate_love_score(name1,name2)
