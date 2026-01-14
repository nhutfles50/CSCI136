"""
        Nathan Hutfles
        CSCI 136 Spring 2026
        Spell Checker Warmup
        January 14th, 2026
"""



#get the user's input word or phrase
def getInput():

    #arbitrary true loop to run until user input is valid
    while True:

        #try to get valid user input
        try:

            #user input
            userMessage = input("Please enter your message, it should be a word or phrase separated with spaces with only alphabetic characters: ")

            #create a list of only the alphabetical words in userMessage
            check = [word for word in userMessage.strip().split() if word.isalpha()]

            #if the length of check is greater than 0 and the same as the length of userMessage as a list
            if len(check) > 0 and len(check) == len(userMessage.split()):

                #return the user's message
                return userMessage.split()

            #otherwise
            else:

                #inform the user
                print("Please ensure input is an entirely alphabetic word or phrase.\n")

        #all other cases
        except:

            #inform the user
            print("Please ensure input is an entirely alphabetic word or phrase.\n")
        #end function



#this function checks the spelling of each word in a list by taking a reference list of
#correctly spelled words and the list of words to check by comparing each word to check
#to the reference list to see if it is in the reference list
def checkSpelling(reference, toCheck):

    #to count how many correct spellings
    count = 0

    #list of misspelled words
    misspelled = []

    #iterate through list to check
    for i in range(len(toCheck)):

        #if the word is in the reference list
        if toCheck[i].upper() in reference:

            #add to correct number of spellings
            count += 1

        #otherwise
        else:

            #add the misspelled word to the list of misspellings
            misspelled.append(toCheck[i])

    #of the number of correct spellings is equal to the number of words in the list
    if count == len(toCheck):

        #tell user the spelling is correct
        print("The spelling is correct!")

    #otherwise
    else:

        #begin the list of misspelled words
        print("Misspelled words: ", end = "")

        #iterate the list of misspelled words
        for i in range(len(misspelled)):

            #if the current word is not the end of the list
            if i != len(misspelled) - 1:

                #print the word
                print(f"{misspelled[i]}", end=", ")

            #if the word is the last word
            else:

                #end the list of misspelled words
                print(f"{misspelled[i]}", end=".\n")
    #end function



#
def main():

    #open the file of correctly spelled words
    f = open("AARHUS.txt", "rt")

    #create a list of correctly spelled words from the file
    words = f.read().split()

    #close the file
    f.close()

    #conditional to continue spell checking or not
    currentChoice = True

    #maybe continuously run program
    while currentChoice:

        #get user message
        message = getInput()

        #check if the spelling is correct
        checkSpelling(reference = words, toCheck = message)

        #try to get user answer to continue
        try:

            #ask user
            userChoice = input("Would you like to spell check more words? (Y/N): ")

            #if user said yes
            if userChoice.upper() == "Y":

                #continue
                currentChoice = True

            #if user said no
            elif userChoice.upper() == "N":

                #do not continue
                currentChoice = False

            #if input was not y or n
            else:

                #inform user
                print("Input was invalid, the program will stop running.")  

                #do not continue
                currentChoice = False

        #all other possible errors  
        except:

            #inform user
                print("Input was invalid, the program will stop running.")  

            #do not continue
               currentChoice = False                     
    #end function
    
#run program if __name__ is equal to __main__
if __name__ == "__main__":
    main()
