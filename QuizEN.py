q1chk = 0 #q1chk is 0 for now
q2chk = 0 #q2chk is 0 for now
q3chk = 0 #q3chk is 0 for now
q4chk = 0 #q4chk is 0 for now
q5chk = 0 #q5chk is 0 for now
q6chk = 0 #q6chk is 0 for now
q7chk = 0 #q7chk is 0 for now
q8chk = 0 #q8chk is 0 for now
q9chk = 0 #q9chk is 0 for now
q101chk = 0 #q10chk is 0 for now

q1 = ("what's 9 + 10") # define question1
q2 = ("what is the meaning of life the universe and everything") # define question2
q3 = ("""if jon is moving at 1 km/hour and his home is 1 km away.
what's the square root of pi?""")# define question3
q4 = ("who is best superhero dceu")# define question4
q5 = ("are you going to give Eric N 10$")# define question5
q6 = ("what is the best search engine")# define question6
q7 = ("what is the distamce from earth to the sun")# define question7
q8 = ("what is the shape of the earth")# define question8
q9 = ("what point on earth has the least distance from space")# define question9
q10 = ("""if a triangle has 3 angles tri = 3 and angle = angle
why is a square not called a quad angle quad = 4 and angle = angle""")# define question10
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
        elif 4 >= a1 > 1:
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
        if a1 == 3:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q2chk = 1#escape condish
        elif 4 >= a1 > 1:
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
        if a1 == 4:# if answer 1 equal 1
            print ("Ok I got it")#tell user ok answer
            grade += 1#change grade by one
            q3chk = 1#escape condish
        elif 4 >= a1 > 1:
            print("Ok I got it")#tell user ok answer
            q3chk = -1 #escape condish
        elif a1 > 4: #if answer more then 4
            print ("no answers more then 4 duh") # tell user no answer more then 4
        else:
            print ("no answers less then 1 duh") #tell user no answer less then 1
    except ValueError: #if ValueError
        print("answer must be a integer 1,2,3 or 4")   #tell user it must be int
print("your grade is",grade,"/ 10") #print the grade
