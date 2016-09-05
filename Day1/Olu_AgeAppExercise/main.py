#create an application that ask the user for his or her name, age, and gender
#if user's age is less than 18, you should display "Hello [title] [name], you are not allowed into this arena"
#if user's age is between 18 and 50,
    #if user is male, application should ask user to pay
    #if user is female, application should ask user not to pay
    #if payment is successful, application should display "Hello [title] [name], you are allowed into this arena"
    #if payment is not made, application should display "Thank you [title] [name], bye!!!"
#if user is above 50, application should display "Hello [title] [name], you are allowed into this arena"


#In above,
#[title] is
    # Master for male below 18 and Mr for all males
    #Miss for female below 18 and Ms for all females

#[name] is the user's name

#please use modules







































import arenaLogic as al

def startApp():

    #ask user for his or her name
    name = input("What is your name?")

    #ask user for his or her age
    age = input("What is your age? (Type only numbers)")

    #ask user for his or her gender
    gender = input("What is your gender? (Type M or F)")

    #display result
    try:

        al.getResult(name, age, gender)

    except TypeError:
        print("only numbers allowed for age")

    except:
        print("Something bad happened, pls contact IT support")



    print()

    #repeat
    startApp()


#################start###############
startApp()