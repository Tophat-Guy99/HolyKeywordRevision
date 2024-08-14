import random

keywordfile = open("keywords.txt", "r")
keywordanddefinitionslist = keywordfile.readlines()
keywordfile.close()
keywordlist = [[],[],[],[],[],[],[],[],[],[],[],[]]
definitionlist = [[],[],[],[],[],[],[],[],[],[],[],[]]

chapterreferencelist = [
    "Computer Architecture",
    "Algorithms",
    "Designing Algorithms",
    "Programming",
    "Program Development",
    "Program Testing",
    "Ethics",
    "Number Systems & Applications",
    "Logic Gates",
    "Excel Theory",
    "Excel Functions",
    "Computer Networks",
]
chapterkeywordcount = [
    36,
    10,
    18,
    56,
    11,
    17,
    49,
    10,
    7,
    32,
    33,
    33
]

locationindex = 0
for i in range(len(keywordanddefinitionslist)):
    keywordanddefinitionslist[i] = (keywordanddefinitionslist[i])[:-1]
    if keywordanddefinitionslist[i] != "":
        keywordlist[locationindex].append((keywordanddefinitionslist[i].split("; "))[0])
        definitionlist[locationindex].append((keywordanddefinitionslist[i].split("; "))[1])
    else:
        locationindex += 1

def CheckEmpty(Dictionary):
    keys = list(Dictionary.keys())
    for i in range(len(Dictionary)):
        if len(Dictionary[keys[i]]) != 0:
            return False
    return True

def PickAndRemoveQuestionIndex(Dictionary):
    ChapterIndex = random.choice(list(Dictionary.keys()))
    while len(Dictionary[ChapterIndex]) == 0:
        ChapterIndex = random.choice(list(Dictionary.keys()))
    QuestionIndex = Dictionary[ChapterIndex][0]
    (Dictionary[ChapterIndex]).pop(0)
    return int(ChapterIndex), QuestionIndex

def RawAlphaNumeric(String):
    New = ""
    for i in range(len(String)):
        if String[i].isalnum() or String[i].isspace():
            New += String[i]
        else:
            New += " "
    return New

def Startup():
    print("What chapters would you like to revise? Input a corresponding number to select.")
    print("""
    1: Computer Architecture\n
    2: Algorithms\n
    3: Designing Algorithms\n
    4: Programming\n
    5: Program Development\n
    6:Program Testing\n
    7: Ethics\n
    8: Number Systems & Applications"\n
    9: Logic Gates\n
    10: Excel Theory\n
    11: Excel Functions\n
    12: Computer Networks\n
""")
    ChapterIndexes = []
    while True:
        try:
            while True:
                Chapter = int(input())
                if Chapter-1 not in list(range(0, 12)):
                    raise ValueError("just to force an except code")
                elif Chapter-1 not in ChapterIndexes:
                    ChapterIndexes.append(Chapter-1)
                    break
        except:
            print("I said 'input a corresponding number' to the chapters provided, idiot.")
        PickAnother = input("Input 'Y' to add another chapter. Input anything else to begin revision.")
        if PickAnother.upper() != "Y":
            break
    return ChapterIndexes

print("HOLY COMPUTING KEYWORD REVISION")
print("Credits: Michael de Beyer\n")
ShuffledPool = {}

while True:
    ChapterIndexes = Startup()

    for i in range(len(ChapterIndexes)):
        RandomisedOrder = list(range(chapterkeywordcount[ChapterIndexes[i]]))
        random.shuffle(RandomisedOrder)
        ShuffledPool[str(ChapterIndexes[i])] = RandomisedOrder

    KeywordTemp = []
    DefinitionTemp = []
    QuestionCounter = 0
    CorrectAnswers = 0
    if len(ChapterIndexes) != 0:
        print("\nTYPE THE KEYWORD THAT FITS THE DEFINITION: \n")
    while CheckEmpty(ShuffledPool) == False:
        QuestionCounter += 1
        Index, QuestionIndex = PickAndRemoveQuestionIndex(ShuffledPool)
        print("\nQuestion " + str(QuestionCounter) + ": " + definitionlist[Index][QuestionIndex])
        KeywordTemp.append(keywordlist[Index][QuestionIndex]+"\n")
        DefinitionTemp.append(definitionlist[Index][QuestionIndex])
        FirstTry = True
        while True:
            Answer = input("Answer: ")
            if RawAlphaNumeric(Answer).lower() == RawAlphaNumeric(keywordlist[Index][QuestionIndex]).lower():
                print("Answer is correct!")
                if FirstTry == True:
                    CorrectAnswers += 1
                break
            else:
                Retry = input("Answer is incorrect. Press 'R' to retry, anything else to reveal answer: ")

                if Retry.upper() != "R":
                    print("Answer: " + keywordlist[Index][QuestionIndex])
                    break
                else:
                    FirstTry = False

    try:
        print("Score: " + str(CorrectAnswers) + "/" + str(QuestionCounter), "({}%)".format(str(round(CorrectAnswers/QuestionCounter, 3)*100)))
        print("Answers inputted correctly after a wrong answer are not counted towards the final score. \n")
        print("\n")
        print("\n")
        print("Now here are all the keywords. Attempt to input the definition of the keywords, and compare with the answers provided. No marking is conducted.")
        for i in range(len(KeywordTemp)):
            print(KeywordTemp[i])
            Definition = input("Definition: ")
            print("Answer: " + DefinitionTemp[i] + "\n")
        print("\n You have reached the end of the keyword revision session.")
    except:
        print("You didn't even pick any chapter tf are you here for")
    Continue = input("Would you like to conduct another session? 'Y' to proceed: \n")
    if Continue.upper() == "Y":
        continue
    else:
        break
