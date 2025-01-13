#Ana Milosevic
#Mad Libs
#12-13-24
#Initalize

#Functions
def Mad_Libs_Game():
    print("Welcome To The Mad Libs Game! Please respond to the following questions.")
    verb = input ("Choose an adjective ending in 'ing'")
    bodypart = input ("Choose a bodypart")
    noun = input ("Choose a noun")
    country = input ("Choose a country")
    color = input ("Choose a color")

    print("Once upon a time, in " + str(country) + ", you were escaping the evil " + str(noun) +
          ". As you were " + str(verb) + ", you fell and broke your " + str(bodypart) +
          ". However, the very " + str(color) + " knight saved you. He took you to his palace and your "
          + str(bodypart) + " was fixed!""")
#Main
Mad_Libs_Game()
