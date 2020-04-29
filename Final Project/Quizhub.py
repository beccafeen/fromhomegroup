
def movie_quiz():
    play_again = True
    while play_again == True:
        print("Pick between these movies  and will tell you what book you should read next")
        movie = input("What movie do you like the best? choose only one\n a. Blue Valentine\n b.Shutterisland\n c.Deadpool\n d.Big Hero 6\n e.Clueless\n f.The Conjuring\n g.Barbie Princess School\n h.Mean Girls\n i.Babadook\n j.Aquaman\n k.The Hangover\n l.Get out")
        print("You should read")

        if movie == 'a':
            print ("Beautiful Disaster by Jamie McGuire")
        elif movie == 'b':
            print ("The Last Sister by Kendra Elliot")
        elif movie == 'c':
            print ("Darkly Dreaming Dexter by Jeff Lindsay")
        elif movie == 'd':
             print ("A Good Kind of Trouble by Lisa Moore Ramee")
        elif movie == 'e':
             print ("Anna and the French Kiss by Stephanie Perkins")
        elif movie == 'f':
            print("The Hunting Hill House by Shirley Jackson")
        elif movie == 'i':
            print("Beloved by Toni Morrison")
        elif movie == 'k':
            print("Boys Don't Knit by T.J. Jackson")
        elif movie == 'j':
            print("The Other daughter by Shalini Boland")
        elif movie == 'h':
            print("Beauty Queens by Libbie Bray")
        elif movie == 'g':
            print("Amina's Voice by Hera Khan")
        else:
            print("Sorry, better luck next time")

        again = input('Do you want to play again?')
        if again == 'y' or again == 'yes':
            play_again = True
        else:
            play_again = False
            print('Thanks for playing')
            return

def profession_quiz():
    play_again = True
    while play_again == True:
        print("Pick outfit and it will tell you your profession")
        points=0
        shirt = input("What mascara do you use?\n a. graphic T-shirt\n b.plad shirt\n c.Scrubs or sleeved folded button up\n d.Formal shirt or Button down\n ")
        pants = input("What bottoms do you prefer?\n a.underwear only\n b.jeans or long skirt\n c. khaki pants\n d.dress pants or formal dress\n")
        jackets = input("What Jacket would you wear?\n a. hoddie or lounge cardigan\n b.pullover sweater or cardigan\n c.white coat\n d.blazer or suit coat\n")
        shoes = input ("What shoes would you wear?\n a.socks only\n b. converse\n c. loafers/ballerina flats\n d.derby/stilletos\n ")
        accessories = input ("You get one more thing for your outfit, what would you choose?\n a. I just need my controllers.\n b.Dry erase markers\n c.Stethoscope\n d.Just my laptop and phone, both are key.\n")
        if shirt == "d" or shirt == "formal shirt" or shirt == "button-down shirt":
            points += 3
        elif shirt == "c":
            points += 2
        elif shirt == "b":
            points +=1
        elif shirt == "a":
            points += 0

        if pants == "d":
            points += 3
        elif pants == "c":
            points += 2
        elif pants == "b":
            points +=1
        elif pants == "a":
            points += 0

        if jackets == "d":
            points += 3
        elif jackets == "c":
            points += 2
        elif jackets == "b":
            points +=1
        elif jackets == "a":
            points += 0

        if shoes == "d":
            points += 3
        elif shoes == "c":
            points += 2
        elif shoes == "b":
            points +=1
        elif shoes == "a":
            points += 0

        if accessories == "d":
            points += 3
        elif accessories == "c":
            points += 2
        elif accessories == "b":
            points +=1
        elif accessories == "a":
            points += 0


        if points >= 12:
            print ("The Corparate World is for you! Dress to impress. ")
        elif points >= 8:
            print ("Nurse or Doctor, the Medical field is waiting for you! You will be a life saver :D!")
        elif points >= 4:
            print ("Respect to you, you are made for teaching! You will be shaping young minds")
        elif points >= 0:
            print("Either you are a professional gamer or youtuber. Just know that we all are jealous of you!")

        again = input('Do you want to play again?')
        if again == 'y' or again == 'yes':
            play_again = True
        else:
            play_again = False
            print('Thanks for playing')
            return

def makeup_quiz():
    play_again = True
    while play_again == True:
        print("Pick this makeup items and will tell you the typed of beauty Guru you are")
        points=0
        mascara = input("What mascara do you use? Too face BTS, Mac, Maybellin, or Thrive? ")
        lipstick = input("What type of lipstick? Matte, Gloss, Cream, or Balm ")
        lipstickcompany = input("Which company would you buy lip products? Mac, Kylie Cosmatics, Glossier, or L'Oreal ")
        eyeshadow = input ("What company would you buy an eyeshadow palette from? Kylie Cosmatics, Urban Decay, Morphe, or Nars ")
        highlight = input ("How much higlight would you wear? Just a tad, average?, To the high heavens, or none")
        if mascara == "Too face BTS" or mascara == "Too face":
            points += 3
        elif mascara == "Mac":
            points += 2
        elif mascara == "Thrive Cosmatics" or mascara == "Thrive" or mascara == "thrive":
            points +=1
        elif mascara == "Maybellin" or mascara == "maybellin":
            points += 0

        if lipstick == "Matte" or lipstick == "matte":
            points += 3
        elif lipstick == "Cream" or lipstick == "cream" :
            points += 2
        elif lipstick == "Gloss" or lipstick == "gloss" or lipstick == "lip gloss":
            points +=1
        elif lipstick == "balm" or lipstick == "lip balm" or lipstick == "Balm":
            points += 0

        if lipstickcompany == "Kylie Cosmatics" or lipstickcompany == "kylie" or lipstickcompany == "kylie cosmatics":
            points += 3
        elif lipstickcompany == "Mac" or lipstickcompany == "mac" :
            points += 2
        elif lipstickcompany == "L'Oreal" or lipstickcompany == "L'oreal;" or lipstickcompany == "loreal" or lipstickcompany == "l'oreal":
            points +=1
        elif lipstickcompany == "Glossier" or lipstickcompany == "glossier":
            points += 0

        if eyeshadow == "Kylie Cosmetics" or eyeshadow == "kylie" or eyeshadow == "kylie cosmatics":
            points += 3
        elif eyeshadow == "Urban Decay" or eyeshadow == "urban decay" or eyeshadow =="naked palettes":
            points += 2
        elif eyeshadow == "Morphe" or eyeshadow == "morphe":
            points +=1
        elif eyeshadow == "Nars" or eyeshadow == "nars":
            points += 0

        if highlight == "to the high heavens" or highlight == "To the high heavens" or highlight == "a lot":
            points += 3
        elif highlight == "average?" or highlight == "average" or highlight =="Average":
            points += 2
        elif highlight == "Just a tad" or highlight == "just a tad":
            points +=1
        elif highlight == "none" or highlight == "None":
            points += 0

        print("You are")

        if points >= 12:
            print ("a Trendy Beauty guru: follows all the new trends. Obsessed with buying the latest and most popular makeup products")
        elif points >= 8:
            print ("a High-end Beauty Guru: Might follow popular trends but tends to focus on high priced makeup brands and all in the name of the love of makeup")
        elif points >= 4:
            print ("a Makeup Lover Beauty Guru: Does not care if it is a high-end product. Only focuses on the performance of the product")
        elif points >= 0:
            print("Not a guru: Just loves skin care not about the caking life!")

        again = input('Do you want to play again?')
        if again == 'y' or again == 'yes':
            play_again = True
        else:
            play_again = False
            print('Thanks for playing')
            return

def personality_quiz():
    play_again = True
    while play_again == True:
        print("Welcome to the personality quiz. This quiz will tell you what kind of weather you like. Please enter your answers using capital letters")
        q1 = input("which shade of blue do you like best?\nA. royal blue\nB. light blue\nC. navy blue\n")
        count_a = 0
        count_b = 0
        count_c = 0
        if (q1=="A" or 'a'):
            count_a += 1
        elif (q1=="B" or 'b'):
            count_b += 1
        elif (q1=="C" or 'c'):
            count_c +=1
        else:
            print("that is not an option")

        q2 = input('which shade of red do you like best?\nA. crimson\nB. pink\nC. maroon\n')
        if (q2=="A" or 'a'):
            count_a += 1
        elif (q2=="B" or 'b'):
            count_b += 1
        elif (q2=="C" or 'c'):
            count_c +=1
        else:
            print("that is not an option")

        q3 = input('which shade of green do you like best?\nA. emerald\nB. sage\nC. forest green\n')
        if (q3=="A" or 'a'):
            count_a += 1
        elif (q3=="B" or 'b'):
            count_b += 1
        elif (q3=="C" or 'c'):
            count_c +=1
        else:
            print("that is not an option")

        q4 = input('which shade of purple do you like best?\nA. violet\nB. lilac\nC. plum\n')
        if (q4=="A" or 'a'):
            count_a += 1
        elif (q4=="B" or 'b'):
            count_b += 1
        elif (q4=="C" or 'c'):
            count_c +=1
        else:
            print("that is not an option")

        q5 = input('which shade of yellow do you like best?\nA. sunshine yellow\nB. blonde\nC. marigold\n')
        if (q5=="A" or 'a'):
            count_a += 1
        elif (q5=="B" or 'b'):
            count_b += 1
        elif (q5=="C" or 'c'):
            count_c +=1
        else:
            print("that is not an option")

        if count_a>=3:
            print("You like the sun.")
        elif count_b>=3:
            print("You like clouds.")
        elif count_c>=3:
            print("You like the rain.")
        elif count_a<3 or count_b<3 or count_c<3:
            print("You like all kinds of weather!")
        else:
            print("wow lame")
        print()
        again = input('Do you want to play again?')
        if again == 'y' or again == 'yes':
            play_again = True
        else:
            play_again = False
            print('Thanks for playing')
            return


def age_quiz():
    points = 0
    play_again = True
    while play_again == True:
        print("This test will reveal your age based on your favorite foods.")
        print("Pick your favorites!")

        while play_again == True:
            print("When you're feeling down, what is your go-to comfort food?")
        #15-25 = 1
        #26-40 = 2
        #40+ = 3
            print("a. Mac and Cheese")
            print("b. Anything with chocolate")
            print("c. Mashed Potatoes")
            response = str(input("Answer:"))
            if response == "a" or response =="A":
                points += 1
                break
            elif response == "b" or response == "B":
                points += 2
                break
            elif response == "c" or response == "C":
                points += 3
                break
            else:
                print("Please enter a valid letter")
                continue



        while play_again == True:
            print("If your date asks where you want to go for dinner, what kind of restaurant would you choose?")
            print("a. Asian")
            print("b. Latin")
            print("c. American")
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 1
                break
            elif response == "b" or response == "B":
                points += 2
                break
            elif response == "c" or response == "C":
                points += 3
                break
            else:
                print("Please enter a valid letter")
                continue

        while play_again == True:
            print("What do you get when you go to the movie theater?")
            print("a. I bring some chips with me; the food there is so overpriced.")
            print("b. A soda and some popcorn.")
            print("c. Junior mints are the way to go.")
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 1
                break
            elif response == "b" or response == "B":
                points += 3
                break
            elif response == "c" or response == "C":
                points += 2
                break
            else:
                print("Please enter a valid letter")
                continue


        while play_again == True:
            print("What is your favorite drunk snack?")
            print("a. Fries")
            print("b. Pizza")
            print("c. Crackers and cheese")
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 2
                break
            elif response == "b" or response == "B":
                points += 1
                break
            elif response == "c" or response == "C":
                points += 3
                break
            else:
                print("Please enter a valid letter")
                continue

        while play_again == True:
            print("What is your favorite ice cream?")
            print("a. Rum Raisin")
            print("b. Cookies & Cream")
            print("c. Chunky Monkey")
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 3
                break
            elif response == "b" or response == "B":
                points += 1
                break
            elif response == "c" or response == "C":
                points += 2
                break
            else:
                print("Please enter a valid letter")
                continue

        if points >= 10 and points<=15:
            print("You are over 40 years old.")

        if points >= 5 and points<=10:
            print("You are between 26 and 40 years old")

        if points >= 1 and points<=5:
            print("You are between 15 and 26 years old")

        again = input('Do you want to play again?')
        if again == 'y' or again == 'yes':
            play_again = True
        else:
            play_again = False
            print('Thanks for playing')
            return

def disney_princess_quiz():
    points = 0
    play_again = True



    while play_again == True:
        print("What Disney princess are you?")
        while play_again == True:

            print("If you could choose, what superpower would you have?")
        #15-25 = 1
        #26-40 = 2
        #40+ = 3
            print("a. The ability to fly")
            print("b. Invisibility")
            print("c. Shapeshiftting")
            print('d. Controlling nature')
            response = str(input("Answer:"))
            if response == "a" or response =="A":
                points += 1
                break
            elif response == "b" or response == "B":
                points += 2
                break
            elif response == "c" or response == "C":
                points += 3
                break
            elif response == "d" or response == "D":
                points += 4
                break
            else:
                print("Please enter a valid letter")
                continue



        while play_again == True:
            print("How long would you date someone before you would consider marrying them?")
            print("a. One day to a week")
            print("b. One month to a year")
            print("c. One year or more")
            print('d. I never want to get married')
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 1
                break
            elif response == "b" or response == "B":
                points += 2
                break
            elif response == "c" or response == "C":
                points += 3
                break
            elif response == "d" or response == "D":
                points += 4
                break
            else:
                print("Please enter a valid letter")
                continue

        while play_again == True:
            print("What is your favorite way to spend your free time?")
            print("a. In a library, reading.")
            print("b. Bingeing TV or movies on my couch.")
            print("c. Sports or exercising of any kind.")
            print('d. Being creative--crafts, drawing, writing.')
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 1
                break
            elif response == "b" or response == "B":
                points += 3
                break
            elif response == "c" or response == "C":
                points += 2
                break
            elif response == "d" or response == "D":
                points += 4
                break
            else:
                print("Please enter a valid letter")
                continue


        while play_again == True:
            print("What kind of friends are you drawn to?")
            print("a. Anyone who can make me laugh.")
            print("b. People who will take me on crazy adventures!")
            print("c. Someone who will listen to my problems and make me feel better.")
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 2
                break
            elif response == "b" or response == "B":
                points += 1
                break
            elif response == "c" or response == "C":
                points += 3
                break
            else:
                print("Please enter a valid letter")
                continue

        while play_again == True:
            print("What is your favorite kind of animal?")
            print("a. Reptiles")
            print("b. Dogs, all the way")
            print("c. Birds are cool")
            print('d. Cats')
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 3
                break
            elif response == "b" or response == "B":
                points += 1
                break
            elif response == "c" or response == "C":
                points += 2
                break
            elif response == "d" or response == "D":
                points += 4
                break
            else:
                print("Please enter a valid letter")
                continue


        if points >= 18 and points<=19:
            print("You are Tiana from The Princess and the Frog.\n You are incredibly talented and independent in every corner of your life. No matter what comes at you, you can take it and make it better for the people around you.")

        if points >= 15 and points<=17:
            print("You are Cinderella.\n You are in tune with the world around you and you prefer animals and nature to people. You would do anything to leave your hometown. I mean anything. You've been through a lot of tough times and could do with some therapy to help you recover, but some sympathetic friends could also improve your life.")

        if points >= 12 and points<=14:
            print("You are Rapunzel from Tangled.\n You love to be artistic and yearn to be free any time you're locked inside, but you also know how to entertain yourself if you have to. You like to have fun and be spontaneous but you also think things through if they are important (most of the time). The reptile is your best friend because, like you, they crave warmth but are comfortable being alone.")

        if points >= 9 and points<=11:
            print('You are Mulan.\n You are independent, free-willed, athletic, and you love fiercely. Once someone wins your loyalty they will never lose it. Family is the most important thing for you, but you also need your time alone, which you usually spend with your dog.')

        if points >= 5 and points<=8:
            print("You are Anna from Frozen.\n You don't really think much before you act and value fun more than safety sometimes. You are not the best judge of people and that can get you in trouble, but when you love someone you devote everything to them, and the right people will appreciate that and reciprocate.")

        again = input('Do you want to play again?')
        if again == 'y' or again == 'yes':
            play_again = True
        else:
            play_again = False
            print('Thanks for playing')
            return

def quarantine_quiz():
    points = 0
    play_again = True

    while play_again == True:
        print("What kind of person are you in quarantine?")
        while play_again == True:
            print("What is your relationship like with the people you're locked down with?")

            print("a. They're driving me up the wall!")
            print("b. I'm driving them up the wall!")
            print("c. We're getting along pretty well, I think.")
            print("d. I'm alone, but I think I'm getting along pretty well with my dog.")
            response = str(input("Answer:"))
            if response == "a" or response =="A":
                points += 3
                break
            elif response == "b" or response == "B":
                points += 4
                break
            elif response == "c" or response == "C":
                points += 2
                break
            elif response == "d" or response == "D":
                points += 1
                break
            else:
                print("Please enter a valid letter")
                continue



        while play_again == True:
            print("With whom are you quarantined?")
            print("a. My parents. I know.")
            print("b. Significant other")
            print("c. Roommates")
            print("d. I'm alone.")
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 1
                break
            elif response == "b" or response == "B":
                points += 3
                break
            elif response == "c" or response == "C":
                points += 2
                break
            elif response == "d" or response == "D":
                points += 4
                break
            else:
                print("Please enter a valid letter")
                continue

        while play_again == True:
            print("What activity have you picked up to pass the time?")
            print("a. I'm making my own clothes. This is partly because my washing machine broke and no one is available to fix it. I've learned how to sew underwear.")
            print("b. Mind puzzles like crosswords, jigsaws, and word jumbles.")
            print("c. Sports or exercising either outside, in my living room, or home gym.")
            print("d. Cooking and baking. My fridge and pantry are full and there's a pie in the oven.")
            print("e. Activity? I'm taking advantage of the time to Do. Absolutely. Nothing.")
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 4
                break
            elif response == "b" or response == "B":
                points += 3
                break
            elif response == "c" or response == "C":
                points += 2
                break
            elif response == "d" or response == "D":
                points += 1
                break
            elif response == "e" or response == "E":
                points += 5
                break
            else:
                print("Please enter a valid letter")
                continue


        while play_again == True:
            print("How have you and your quarantine buddies managed being cooped up together?")
            print("a. We have mandatory alone time during business hours. Sometimes I wish it lasted longer.")
            print("b. I want to be with them all the time anyway, we spend every moment together!")
            print("c. We try to spend quality time together, use the quarantine to get closer, but we also know when to leave each other alone.")
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 2
                break
            elif response == "b" or response == "B":
                points += 1
                break
            elif response == "c" or response == "C":
                points += 3
                break
            else:
                print("Please enter a valid letter")
                continue

        while play_again == True:
            print("What pet do you have in your house with you? If you do not have a pet, what kind would you like most?")
            print("a. A reptile")
            print("b. A dog...or two...or three.")
            print("c. Many, many cats. I am very aware of the litterbox.")
            print("d. Pet? Singular? Take your pick, I've got one of each.")
            print("e. Small pet--guinea pig, rabbit, etc.")
            response = str(input("Answer:"))
            if response == "a" or response == "A":
                points += 3
                break
            elif response == "b" or response == "B":
                points += 1
                break
            elif response == "c" or response == "C":
                points += 2
                break
            elif response == "d" or response == "D":
                points += 4
                break
            elif response == "e" or response == "E":
                points += 5
                break
            else:
                print("Please enter a valid letter")
                continue


        if points >= 17 and points<=18:
            print("The going insane quarantiner.\n You chose to go on lockdown on your own because you know that if you shacked up with your family or friends they wouldn't be either by the time you both got out. You are enjoying your isolation and the relaxation that comes with it, but you're starting to feel a bit like Tom Hanks--at least your Wilson is a pet instead of a volleyball.")
        if points >= 15 and points<=16:
            print("The trying your best quarantiner.\n You are an ambivert, you enjoy being around people but you also value spending time alone. You're constantly working, trying to get done anything you can. You haven't been driving anyone crazy yet, but you might if you don't put your laptop down and enjoy the free time.")

        if points >= 12 and points<=14:
            print("The active quarantiner.\n You are an extrovert. You crave spending time with people. The quarantine is hard since you can't go out, so you take out your need for human contact by making everyone in your house spend as much time with you as possible. You keep busy, as a restless and always moving person even before lockdown, you spend a lot of time outside walking or running.")

        if points >= 9 and points<=11:
            print("The 'I just want to be alone' quarantiner.\n You don't like the fact that your house is always full these days, and you spend most of yor time locked up in your room to avoid that fact. You are trying to take this time to learn, about yourself, about the world, about annything, because you're worried that you're losing time while you're locked up.If you have a pet, they're usually locked in your room with you.")

        if points >= 5 and points<=8:
            print("The caretaker quarantiner.\n You're the parent of every friend group. You're dealing with the quarantine by taking care of other people, even if you're living in the same house as your own parents. Just make sure to let other people take care of you as well.")

        again = input('Do you want to play again?')
        if again == 'y' or again == 'yes':
            play_again = True
        else:
            play_again = False
            print('Thanks for playing')
            return
