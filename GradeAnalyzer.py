import operator
def welcome():
    print()
    print("************************************************************************")
    print("*                                                                      *")
    print("*                         Welcome To The SGAA System                   *")
    print("*                                                                      *")
    print("************************************************************************")
    print()

def readdetails():
    print()
    print("Enter the no of students in class: ")
    noofstudents = int(input())
    details = {}
    for student in range(0, noofstudents):
        print("Enter the name of student: ")
        Name = input()
        print("Enter the marks of student: ")
        Marks = int(input())
        details[Name] = Marks
        print()
    return details

def rank(details):
    try:
        print()
        sorteddetails = sorted(details.items(), key = operator.itemgetter(1), reverse = True)
        print(sorteddetails)
        print("{} has scored first rank with {} marks".format(sorteddetails[0][0], sorteddetails[0][1]))
        print("{} has scored second rank with {} marks".format(sorteddetails[1][0], sorteddetails[1][1]))
        print("{} has scored third rank with {} marks".format(sorteddetails[2][0], sorteddetails[2][1]))
        print()
        return sorteddetails
    except IndexError:
        print("Please! Enter a valid entry of student")
        quit()
        

def awardstudent(sorteddetails, award):
    print()
    print("{} has received reward of ${} for scoring 1st Rank in the class".format(sorteddetails[0][0], award[0]))
    print("{} has received reward of ${} for scoring 2nd Rank in the class".format(sorteddetails[1][0], award[1]))
    print("{} has received reward of ${} for scoring 3rd Rank in the class".format(sorteddetails[2][0], award[2]))
    print()

def appreciation(sorteddetails):
    print()
    for record in sorteddetails:
        if record[1] >= 950:
            print("Congratulation & Greetings on acheiving {} marks, {}".format(record[1], record[0]))
        else:
            break
        print()

def farewell():
    print()
    print("Thanks To All The Students Who Have Been A Part OF This Exam!!!")
    print("Do Well. Best OF Luck For Your Future!!")
    print()

welcome()
details = readdetails()
sorteddetails = rank(details)
award = (500, 300, 100)
awardstudent(sorteddetails, award)
appreciation(sorteddetails)
farewell()
