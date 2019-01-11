q1chk = 0 #q1chk is 0 for now
q2chk = 0 #q2chk is 0 for now
q3chk = 0 #q3chk is 0 for now
q4chk = 0 #q4chk is 0 for now
q5chk = 0 #q5chk is 0 for now
q6chk = 0 #q6chk is 0 for now
q7chk = 0 #q7chk is 0 for now
q8chk = 0 #q8chk is 0 for now
q9chk = 0 #q9chk is 0 for now
q10chk = 0 #q10chk is 0 for now

q1 = ("what's 9 + 10?") # define question1
q2 = ("what is the meaning of life the universe and everything?") # define question2
q3 = ("""if jon is moving at 1 km/hour and his home is 1 km away.
what's the square root of pi?""")# define question3
q4 = ("can a match box?")# define question4
q5 = ("are you going to give Eric N 10$?")# define question5
q6 = ("rewsna siht noitseuq sdrawkcab?")# define question6
q7 = ("""if 2+2 is 4 and trains in new york are always late
what is the distamce from earth to the sun?""")# define question7
q8 = ("what is the shape of the earth?")# define question8
q9 = ("what point on earth has the least distance from space?")# define question9
q10 = ("what is the best icecream flaver?")# define question10
grade = 0 # grade is 0

print(q1)
print(" ")
print("""1. 19 
2. 21 
3. an old meme that was never funny 
4. 69420 """) #print question1

while q1chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 1:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q1chk = 1#escape condish
        elif 4 >= a1 >= 1:
            print("Ok I got it")#tell user ok answer
            q1chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int


a1 = 0
print(q2)
print("""
1. to live, love and be happy for as long as you can
2. to spread the human race to as far as we can and keep it alive
3. there is no meaning :(
4. 42""")

while q2chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 4:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q2chk = 1#escape condish
        elif 4 >= a1 >= 1:
            print("Ok I got it")#tell user ok answer
            q2chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int


print(q3)
print("""
1. 1 hour
2. I am bad at math
3. 1.77245385091
4. 2""")
a1 = 0

while q3chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 3:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q3chk = 1#escape condish
        elif 4 >= a1 >= 1:
            print("Ok I got it")#tell user ok answer
            q3chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int


print(q4)
print("""
1. I dunno
2. no but a tin can
3. yes light them up
4. there is no smoking in the ring""")
a1 = 0

while q4chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 2:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q4chk = 1#escape condish
        elif 4 >= a1 >= 1:
            print("Ok I got it")#tell user ok answer
            q4chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int


print(q5)
print("""
1. yes, I will right now or I suck.
2. no, I will give 20$ or I suck.
3. no, I will give 50$ or I suck.
4. no, I will give 100$ right now or I suck.""")
a1 = 0

while q5chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 4:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q5chk = 1#escape condish
        elif 4 >= a1 >= 1:
            print("Ok I got it")#tell user ok answer
            q5chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int


print(q6)
print("""
1. wwhhhhhaaaaaaaaaaaaaatttttttttt
2. the program is broken
3. ko 
4. sure""")
a1 = 0

while q6chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 3:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q6chk = 1#escape condish
        elif 4 >= a1 >= 1:
            print("Ok I got it")#tell user ok answer
            q6chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int

print(q7)
print("""
1. 92.96 million mi
2. 92.97 million mi
3. 92.98 million km 
4. I give up""")
a1 = 0

while q7chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 1:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q7chk = 1#escape condish
        elif 4 >= a1 >= 1:
            print("Ok I got it")#tell user ok answer
            q7chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int

print(q8)
print("""
1. flat pancake
2. a donut
3. a sphere 
4. a geoid""")
a1 = 0

while q8chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 4:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q8chk = 1#escape condish
        elif 4 >= a1 >= 1:
            print("Ok I got it")#tell user ok answer
            q8chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int

print(q9)
print("""
1. mount everest
2. mount k2
3. the sky
4. mount chimborazo""")
a1 = 0

while q9chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 4:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q9chk = 1#escape condish
        elif 4 >= a1 >= 1:
            print("Ok I got it")#tell user ok answer
            q9chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int

        
print(q10)
print("""
1. chocolate
2. vanilla
3. mint choclate chip
4. pineapple""")
a1 = 0

while q10chk == 0: #while test is false run loop
    try:
        a1 = int(input(" "))#answer one equal an integer input
        if a1 == 1:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q10chk = 1#escape condish
        elif 4 >= a1 >= 1:
            print("Ok I got it")#tell user ok answer
            q10chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int
  

print("your grade is",grade,"/ 10") #print the grade
if grade == 10:
    print ("you did it perfect")
elif grade == 9:
    print ("almost perfect oof 9/10")
elif grade == 8:
    print ("ok 8/10 very normal")
elif 7 >= grade >= 6:
    print ("ok, ok try a little harder")
elif  5 >= grade >= 1:
    print ("what a fail go try again")
elif grade == 0:
    print ("FFS try guessing next time you will get a better score")

