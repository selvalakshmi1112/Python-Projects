loop = 1
while (loop < 10):

    # All the questions that the program asks the user
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose a noun: ")
    place = input("Name a place: ")
    adjective = input("Choose an adjective (Describing word): ")
    noun3 = input("Choose a noun: ")

    # Displays the story based on the users input
    print ("------------------------------------------")
    print ("Be happy with your",noun,"and", p_noun)
    print ("This may be an interesting", noun2,",")
    print ("Be safe and stay home",p_noun,"in",place)
    print ("Where the virus is spreading",adjective,".")
    print ()
    print ("You may think that this is the",noun3,",")
    print ("Hope this will change soon.")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1

