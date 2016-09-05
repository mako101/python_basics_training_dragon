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

def getResult(name, age, gender):

    #convert gender to upper
    gender = str(gender).upper()

    #convert age
    age = int(age)

    ###################Hiding function start#######################
    #function encapsulation
    def getTitle(age, gender):

        if gender == "M" and age < 18:
            return "Master"

        elif gender == "M" and age > 18:
            return "Mr"

        elif gender == "F" and age < 18:
            return "Miss"

        elif gender == "F" and age > 18:
            return "Ms"

    ###################Hiding function end#######################

    #get the title
    title = getTitle(age, gender)

    #logic
    if age < 18:
        #print not allowed
        print("Hello", title, name, "you are not allowed into this arena")

    elif age >=18 and age <= 50:

        if (gender == "M"):
            #male pays

            #ask for payment
            pay = str(input("Do you wish to pay? (Type Y for Yes and N for No)")).upper()

            if pay == "Y":

                #print allowed
                print("Hello", title, name, "you are allowed into this arena")

            else:

                #print bye
                print("Thank you", title, name, ", bye!!!")

        else:
            #female don't pay
            print("Hello", title, name, "you are allowed into this arena")

    elif age > 50:

        #print allowed
        print("Hello", title, name, "you are allowed into this arena")
