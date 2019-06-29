# Mad libs where libs get Mad
#  Start Below:


print ('Mad libs where libs get Mad')
print (' Start Below:')
number = int(input("time: "))
Noun = input("Noun(plural): ")
first_name = input(" First Name: ")
first_name = first_name.capitalize()
last_name = input(" Last Name: ")
last_name = last_name.capitalize()
sentence = input("Any sentence: ")
sentence = sentence.upper()
Verb = input("Verb: ")

print ("  It was %d  o'clock when I hears a knock at the door. \n  I opened the door and there was a box full of %s with a note saying  \n  \"From Mr. %s %s\".\n  Just as I closed the door I heard a scream \" %s .\".\n  I froze in place and all I could do was %s." % (number,Noun,first_name,last_name,sentence, Verb))