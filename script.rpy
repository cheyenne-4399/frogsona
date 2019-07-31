#CHARACTERS DEFINED HERE

define m = Character("Marvin")
define k = Character("King Samson II")
define e = Character("xX_DarkRaven496283_Xx")
define p = Character("You")
define u = Character("Unknown Person(?)")
define c = Character("Cult Member One")
define b = Character("Studded Belt Company")
define s = Character("Store Manager")
define x = Character("Policeman One")
define l = Character("Little Suzie")
define h = Character("Demmy's Worker")
define q = Character("Helen")

#NEEDED IMAGES:
#School
#Dorm Building
#Wallblues1 = inside store
#Wallblues 2 = outside store
#Boiled Topic
#Hum Depot1 = inside store
#Hum Deport2 = outside store

label start:

    # bg change = “scene ____”
    #sprite show = “show ___”

    # BG = school
    "You are a new student at XYZ University."
    p "Wow I am so excited! I hope I will get a boyfriend this year..."

    menu:
        "backdoor":
            jump endOfMandDates

    "It's time to look at your new dorm!"
    #BG = dorm building
    "You make your way into your dorm room's building."
    show marvin

    m "Hey neighbour! Are you new here?"
    menu:
         "Yeah… u-uwu… Wanna show me around?":
            jump showmearound
         "Yes. What is it to you?":
            jump ignore
    label showmearound:
         #show marvinBashful
         m "Ok cutie. I have Zoology 101 next, do you? Not that I looked up your student records or anything…"
         p "Yes, I have that class as well."
         #BG = transition
         "You and Marvin walk to class together."
         #BG = classroom
         m "HIIIISSSSSS"
         p "{i} What the heck?? {/i}"
         m "Sit next to me."
         jump kingintro
    label ignore:
         #show marvinFlustered
         m "Hmph. *muttering* Just like my ex-wife…"
         #BG = transition
         "Marvin walks away and makes his way to his class…"
         #BG = classroom
         "Marvin is in the same class as you! There seems to be a limited amount of seats. You reluctantly make your way to the seat next to Marvin"


         jump kingintro

    label kingintro:
        u "hEy ! How dare you reside in my space?"
        p "{i} Get a load of this guy...who does he think he is?{/i}"
        #show kingSamson
        #show marvin but like on the other side of the screen
        m "King Samson II! I didn’t know you had Zoology 101 as well!"
        "King Samson II pushes past you..."
        k "Step aside, peasants!"
        "...and takes the empty seat next to Marvin."
        "You look around the rest of the class for any seats to take."
        "...!"
        "There’s one seat left in the back. You walk over and see a hooded figure lurking in the corner."
        p "You good?"
        u "r-rawr…. >.< ….oh..sorry...didn’t see you there ...hehe"
        "He coughs up a hairball…"
        #show Xx_darkraven496283_xX
        p "hey…"
        "You awkwardly take a seat"
        u "h-hey… >///< you’re kinda cute...what is your handle? I go by Xx_darkraven496283_xX"
        "He waves to you, flexing his fingerless skeleton themed gloves."
        menu:
            "Those are some pretty swaggy swagalicious swags!":
                jump swag
            "Fingerless gloves? What is this, 2005?":
                jump emoInsult
        label swag:
            e "xX haha...thanks i guess… *nuzzles* :3"
            "He seems to have taken a liking for you…"
            "This promises to be an interesting first day."
            jump d2
        label emoInsult:
            e "STOP FLAMING MY PAGE!!! You don't understand...no one does..."
            "He starts to cry into the desk…"
            #Show EmoCry
            "This promises to be an interesting first day."
            jump d2
        label d2:
            "The next day"
            jump wallblues


                        #PUT RANDOM INTERACTIONS HERE

                        #mandatory hangouts
                        #whatever day

        label wallblues:
            "After class…"
            m "Hey you ;) I need to get some laxatives...wanna come with me to Wallblues?"
            menu:
                "Laxatives??? That’s gross why would you tell me that…":
                    jump laxativesWeird
                "Yeah sure...I need some too…":
                    jump laxativesToo

        label laxativesWeird:
            m "Don’t judge me like that sweetie. You look like you might need some too after today’s breakfast. If you know what I mean ;) "
            p "{i}what a rude bastard…{/i}"
            "You follow Marvin to Wallblues"
            jump CVS

        label laxativesToo:
            m "Ew that’s so gross. Why would you tell me that? Did your mother never teach you? A young lady never gives away her laxative status…kids these days"
            "You follow a disgusted Marvin to Wallblues."
            jump CVS

        label CVS:
        #BG = stock photo of CVS
        m "Want to go inside?"
        menu:
            "Yeah! Let’s go.":
                jump inside
            "No thanks, let’s wait here for a bit.":
                jump outside

        label inside:
            "You go inside the store with Marvin and walk towards the gift card aisle."
            m "I was kidding. I don’t actually need laxatives, it was a test of your loyalty to me."
            m "I was actually wondering if you wanted to browse the candy aisle with me."
            menu:
                "Yeah I love candy!":
                    jump yesCandy
                "I’d rather browse the medications":
                    jump noCandy


        label yesCandy:
            m "Thanks bby. My ex-wife Helen never let me eat candy. Something about type 2 diabetes?"
            "You go to the candy aisle."
            m "Back in my day, the kids ate Skittles and M&M’s. As the datee, you get to choose which candy we eat. My treat!"
            menu:
                "Skittles!":
                    jump Skittles
                "M&M’s!":
                    jump MandM

        label Skittles:
            m " Hiss Hiss! A gourmet choice!"
            m "What color do you choose? This is a vital question, so make sure you think before answering."
            menu:
                "Red":
                    jump red
                "Blue":
                    jump blue

        label red:
            "Ahhh red skittles, just like the strawberry scent my ex-wife Helen used to spray."
            "You get sick of Marvin babbling about his ex-wife Helen’s perfume and leave."
            jump endMarvinDateOne

        label blue:
            "Ahhh blue skittles, just like the blueberry scent my ex-wife Helen sprayed on the day of our divorce…"
            "You get sick of Marvin babbling about his ex-wife Helen’s perfume and leave."
            jump endMarvinDateOne

        label MandM:
            m "A splendid choice! I promise I won’t eat more than half of the bag"
            "Marvin ends up eating the entire party-sized bag of M&M’s. You are hungry and annoyed, so you leave."
            jump endMarvinDateOne

        label noCandy:
            m "Okay."
            "You stare at different colored pills for 2 hours. You end up buying Behnardrill, and head outside."
            jump endMarvinDateOne



        label outside:
            "You stand outside the store for twenty minutes."
            "In an attempt to break the awkward silence, you engage Marvin in a conversation about lemons."
            p "Do you like lemons?"
            m "I don’t, but my ex-wife Helen loves them."
            menu:
                "Your ex-wife? You were married!?":
                    jump exwife
                "That’s so interesting. Do you have any kids?":
                    jump kids

        label exwife:
            m "Yeah. You?"
            p "No!"
            p "You leave Marvin outside Wallblues, shocked and disgusted."
            jump endMarvinDateOne

        label kids:
            m "I have four. How many do you have?"
            p "None!"
            p "You leave Marvin outside Wallblues, shocked and disgusted. You loathe children."
            jump endMarvinDateOne


        label endMarvinDateOne:
            "Marvin follows you back to your dorm after your outing at Wallblues."
            m "Thanks for coming with me. I had a really nice time with you…"
            "He struggles to keep up with you."
            menu:
                "Thanks. I had a nice time too.":
                    jump niceTime
                "Can you stop following me please?":
                    jump stopStalker

        label niceTime:
            m "I knew you would like WallBlues! I used to bring my ex-wife there all the time!"
            jump flyScene

        label stopStalker:
            p "{i} Why is he still here? I don’t want to have to call the security…{/i}"
            m "But bhabie...I thought you would like WallBlues…"
            "It seems as if he has started crying…"
            jump flyScene

        label flyScene:
        #show marvinSurprised
        m "WOWZERS !"
        "...!!!"
        "Woah there momma goose ! Is he...Kissing your feet???"
        "Marvin smacks his frog lips."
        #Show MarvinBashful
        m "Sorry....Hiss hisss...there was a fly by your feet. I couldn’t help myself...Anyways, have a good night :) See you tomorrow momma goose."
        "Marvin walks away and you turn into your dorm for the night."

        jump mandDateD2
        label mandDateD2:
            "After class…"
            #show emo
            e "hey… you busy by any chance… o-owo"
            menu:
                "Actually I was planning on studying...wanna come with?":
                    jump studyFreak
                "No. Do you need something?":
                    jump noPlans
            label studyFreak:
                e "aww don't be such a prep...come shopping with me at boiled topic!"
                "xX_DarkRaven49623_Xx drags you to the mall."
                jump boiledTopic
            label noPlans:
                e "that's kinda funky of you my fellow follower of darkness. wanna go to the boiled topic with me? you are qq but your style is off..."
                p "{i} I am holding back from kicking him in the shin...{/i}"
                jump boiledTopic
        label boiledTopic:
            "At Boiled Topic..."
            "Outside the store, a member of a local cult asks if you want to join their cult, XYZ."
            menu:
                "Sure! I'll join.":
                    jump joinCult
                "No thanks.":
                    jump noCult
            label noCult:
                e "i'm glad you didn't leave me :)"
                e "..."
                e "...everyone else does..."
                "You go inside the store. Inside, an employee mutters a greeting and continues to write his will on Google Docs."
                e "i have a few clothes that i want to try, but i'm afraid that i won't buy any of them due to my constant self-deprecation and low self esteem lol XD. that's why i brought u."
                e "i'll go change into my first fit."
                "xX_DarkRaven496283_Xx comes out of the dressing room in a studded belt, fake tattoo sleeves, super-duper
                schmooper black skinny jeans, and Doctor Martins."
                e "he rawred. well..what do u think? "
                menu:
                    "Wow whatta hottie.":
                        jump hotEmo
                    "Laaaaame.":
                        jump lameEmo
                label lameEmo:
                    e " *sad uwu* that's what they all say ..."
                    e "i really thought you'd be different. you know what they say..."
                    e "love can sometimes be magic...but magic..."
                    e "is just an illusion"
                    menu:
                        "I'm sorry, I didn't mean it! Please let me make it up to you...":
                            jump makeUp
                        "Stop being dramatic...geez.":
                            jump dramatic
                    label makeUp:
                        "o-owo? a-are you sure?"
                        menu:
                            "Yes":
                                jump yesMakeUp
                            "...no":
                                jump dramatic
                        label yesMakeUp:
                            e "but are you sure-sure?"
                            menu:
                                "YES.":
                                    jump yesyesMakeUp
                                "...no?":
                                    jump dramatic
                            label yesyesMakeUp:
                                e "...but how sure exactly are you?"
                                menu:
                                    "Absolutely 100 Percent Sure.":
                                        jump yesyesyesSure
                                    "Well now I am 0 Percent sure you ungrateful twat.":
                                        jump dramatic
                                label yesyesyesSure:
                                    e "oh em gee... ^_^ no one's ever been so faithful 2 me. i thought i would perish forever alone..."
                                    "xX_DarkRaven496283_Xx seems to have started to tear up??"
                                    "he runs out of the store crying."
                                    jump endEmoDate1
                    label dramatic:
                        e "the fleeting feeling of love lasts only for a moment...but the pain of love lasts a lifetime..."
                        "it seems xX_DarkRaven496283_Xx has started to tear up."
                        "He runs out of the store crying."
                        jump endEmoDate1
                label hotEmo:
                    e "owo w-weally? no one's ever said that bee four..."
                    e "i'll go wear the second outfit. brb haha XD"
                    "xX_DarkRaven496283_Xx comes out wearing an oversized Evanescence shirt."
                    e "um do i look fat in dis shirt? not that i don't any other time... >w<"
                    menu:
                        "Yuhhh":
                            jump yesFat
                        "Of course knot !":
                            jump noFat
                    label yesFat:
                        e "i knew it... i'll just...not get it i guess..."
                        "xX_DarkRaven496283_Xx starts to tear up. He runs out of the store crying."
                        jump endEmoDateOne
                    label noFat:
                        e "you're too cute :3 let's go buy deez"
                        "You go with xX_DarkRaven496283_Xx to the cash register."
                        "The employee stops writing his will and says that the total is $87.32"
                        e " WHAT XD?! i thought i had a discount from being a five year member of this store..."
                        e "i spent all of my money on guy-liner refills already..."
                        "xX_DarkRaven496283_Xx smile shakily."
                        e "you know what they say... no smile is more beautiful than the one that struggles through the tears...."
                        "xX_DarkRaven496283_Xx runs out of the store crying."
                        jump endEmoDate1


            label joinCult:
                c "Wow, really? You're the first person to ever say 'yes.' "
                c "To join our cult, you must go through an initiation ceremony. Stop by my church for a couple hours to get started."
                p "I can't wait !"
                c "Hey, may I go shopping with you?"
                menu:
                    "Of course! Anything for a fellow worshipper.":
                        jump shop
                    "I don't think that is a good idea.":
                        jump noCult
                label shop:
                    "You go inside the store with Cult Member One and xX_DarkRaven496283_Xx."
                    "You browse the store, and xX_DarkRaven496283_Xx instantly finds the studded belt. He goes to the fitting room to try it on."
                    c "I don't see any cult-related items in this store. I think I'll go check out some other stores. Good day to you fellow worshipper."
                    p "Farewell, enlightened one!"
                    "xX_DarkRaven496283_Xx exits the fitting room wearing the studded belt."
                    e "so...how do i look?"
                    menu:
                        "Awful. Just awful.":
                            jump awful
                        "You look fine, but I wish the belt was in a different colour.":
                            jump diffcolour
                    label awful:
                        e "...r-really?"
                        menu:
                            "No, I was just joking. But I do wish the belt was in an another colour.":
                                jump diffcolour
                            "Yes! You look like someone ran you over with a cement mixer.":
                                jump insultEmoAgain
                    label insultEmoAgain:
                        "xX_DarkRaven496283_Xx sobs his guts out."
                        e "...i won't buy the belt i guess... *sniffles*"
                        p "Wise decision."
                        "xX_DarkRaven496283_Xx runs out of the store, crying for the second time."
                        jump endEmoDate1
                    label diffcolour:
                        e "b-but i like the colour black..."
                        "xX_DarkRaven496283_Xx seems to have started crying..."
                        "You scramble to fix the situation."
                        p "Don't be ridiculous! Let's go see if the store sells a different colour belt."
                        "You ask the employees, but they say that black is the only colour belt they have."
                        "You're about to give up hope, but you notice a customer service number written on the belt's tag. It says to call if you have any questions."
                        "You call the number."
                        b "Hello. This is Crystal from the Studded Belts COmpany. How may I help you?"
                        p "Yes, hi. I was wondering if you sell your oversized studded belt in a colour that isn't black?"
                        b "Yes! We sell this belt in a variety of colours. Which colour would you like?"
                        menu:
                            "Green":
                                jump beltColour
                            "Red":
                                jump beltColour
                            "Blue":
                                jump beltColour
                        label beltColour:
                            b "Alright, just tell me your home address, name, credit card number, social security number, and I will ship the belt over to your house."
                            "You force xX_DarkRaven496283_Xx to give up his private information."
                            b "Excellent. Would you like to pay extra for one day shipping?"
                            e "...no"
                            b "Thank you for calling. Have a nice day. "
                            e "...but i wanted a black belt..."
                            p "Stop complaining!"
                            "xX_DarkRaven496283_Xx starts sobbing and runs out of the mall."
                            jump endEmoDate1
        label endEmoDate1:
            "Today was an eventful day...You were unable to buy anything, but you feel as if you understand xX_DarkRaven496283_Xx more now."
            jump mandDateD3Setup
    label mandDateD3Setup:
        "The Next Day..."
        "Yesterday's date with xX_DarkRaven496283_Xx was certainly...something."
        "You should head to class."
        jump D3Class
    label D3Class:
        "During class..."
        "King Samson II passes you a note."
        k "My fairest lady. My apologies. I should not have taken your seat on the first day. I am sorry...I was having cramps that day. Mayhaps accompany me to a date after class? (check yes or no)"
        menu:
            "Check Yes.":
                jump yesNote
            "Check No.":
                jump noNote
            "Check No and write a snarky response.":
                jump youAreMean
        label yesNote:
            "You check yes and pass the note back over to King Samson II."
            "He gives you slimy smile."
            #Show silmySamson
            jump mandDateD3
        label noNote:
            "You check no and pass the note back over to King Samson II."
            "He feigns a hurt expression at you...?"
            "It appears he has started to cry."
            "You feel guilty...maybe you should go on that date with him."
            jump  mandDateD3
        label youAreMean:
            "You check no and write a little note on the side."
            p "Really? Asking me out by passing a note? Are we in middle school??"
            "You pass the note back to King Samson II. He reads it and starts to cry..."
            "...You feel guilty...maybe you should go on that date with him."
            jump mandDateD3
    label mandDateD3:
        "After class you meet up with King Samson II."
        k "I know you have wanted to date me for a long time now...Be glad you have this opportunity."
        p "{i} I'm one step away from kicking him in the shin...{/i}"
        menu:
            "I'm one step away from kicking you in the shin.":
                jump shinKick
            "Haha yeah...":
                jump hahaYeah
        label shinKick:
            "King Samson II gives you a hearty chuckle."
            k "Don't be like that sweetie!"
            "He drags you outside."
            jump homeDepot
        label hahaYeah:
            k "Are you nervous? Don't be..."
            "He drags you outside."
            jump homeDepot
    label homeDepot:
        "After an awkward walk with King Samson II you arrive in front of...the local hardware store."
        k "Hum DëpÔté! My personal favourite place to loiter at."
        menu:
            "Go inside Hum DëpÔté":
                jump insideHum
            "Stay outside Hum DëpÔté":
                jump outsideHum
        label outsideHum:
            "You stay outside Hum DëpÔté"
            k "By the gods! Observe this complex contraption before us!"
            p "It's a...shopping cart??"
            k "We must treasure such a tool! Quick, before anyone looks!"
            menu:
                "Steal the shopping cart.":
                    jump stealCart
                "Leave the shopping cart where it is":
                    jump leaveCart
            label stealCart:
                "You help King Samson II shoplift the shopping cart."
                p "We can get in big trouble for this..."
                k "Nonsense! Anyone who challenges me to a duel shall feast their eyes upon my fists!"
                " WEE WOO WEE WOO (police siren noises sorry we don't know how to spell out how it sounds)"
                "A wild police officer appears!"
                k "I CHALLENGE YOU TO A DUEL, GOOD SIR."
                menu:
                    "Let King Samson II duel against the police officer. He is a grown frog and can do what he wants.":
                        jump yesDuel
                    "Don't let King Samson II duel against the police officer. He is a man child and does not know what he is doing.":
                        jump noDuel
                label noDuel:
                    p "You don't have to do this! Let's just take the ticket and leave."
                    k "But...my honor!"
                    "You drag King Samson II away from the scene."
                    k "468 dollars? I lack the wealth to accomplish such a feat..."
                    p "{i} ...isn't he a king? {/i}"
                    " It appears King Samson II has started to faint from shock."
                    k "Please...leave me here to die. Go before they catch you as well!"
                    p "Oh...okay then."
                    "You leave...you guess."
                    "As you leave you notice Samson get up and follow you."
                    jump endKingDate1
                label yesDuel:
                    k "PREPARE TO FIGHT! I WILL VOMIT ON YOUR POSSESSIONS, YOU INSOLENT MUSHROOM!"
                    x "Uh sure..."
                    "Both of the contestants pull out nerf guns."
                    "The police officer and King Samson II take 10 steps out. When it's time to turn and shoot, the police officer fires his nerf gun before Samson."
                    "King collapses."
                    k "But alas! Your young and mighty king has failed. This is the start to the downfall of our kingdom..."
                    k "Please, leave me here to die. Go before he catches you as well."
                    p "Uh...aight then lmao bruhhh x"
                    "You leave...you guess."
                    "As you leave you notice Samson get up and follow you."
                    jump endKingDate1
            label leaveCart:
                k "Ah. I admire your refrainment (is that a word lol) from pursuing this holy cart. It brings out your kind and gentle character."
                k "However, I plan to take you somewhere that requires using transportation, and I lack an automobile."
                menu:
                    "Drive shopping cart onto the freeway.":
                        jump driveCart
                    "Take the bus like a normal person.":
                        jump driveBus
                label driveCart:
                    "You somehow drive the shopping cart onto the freeway??"
                    "However, a police officer stops you, as you were driving way under the speed limit."
                    x "I'm sorry, it's rush hour."
                    "You and King Samson II reluctantly push the shopping cart back to where they came from."
                    jump endKingDate1
                label driveBus:
                    "You and King Samson II wait for a public bus."
                    "Instead, a white van with tinted windows stops in front of you."
                    "The sign 'Public Bus' is written in sharpie on a piece of college ruled binder paper and taped to the van."
                    menu:
                        "Get in the suspicious van.":
                            jump insideVan
                        "Do not get in the suspicious van.":
                            jump outsideVan
                    label insideVan:
                        "You both get into the van like idiots, unaware of what's to come."
                        k "To the Shakesperean Museum we go!"
                        x "Not so fast!"
                        x "I saw you eyeing that shopping cart. You're under arrest for suspicioius activiy and hypothetical vandalism."
                        "You and King Samson II reluctantly go to jail."
                        jump altEndKingDate1
                    label outsideVan:
                        "CONGRATS FELLOW PLAYER!! you've encountered a top secret."
                        "https://www.igourmet.com/ST/encyclopedia.asp"
                        "okay continue playing"
                        "You decide to be a prep and stay outside the van."
                        "You both decide to call it a day."
                        jump endKingDate1
        label insideHum:
            "You go inside Hum DëpÔté."
            k "Feast your eyes on the best construction products in the world."
            p "Wow. This is wicked awesome-sauce. I can't wait to shop here."
            "You look around the store."
            "What would you like to buy?"
            menu:
                "Paint.":
                    jump paint
                "Sinks.":
                    jump sinks
            label paint:
                "You walk over to the paint aisle."
                "You see hundreds of cans of paints, arranged by colour."
                "What colour paint do you want to look at?"
                menu:
                    "Purple":
                        jump purple
                    "Orange":
                        jump orange
                    "Yelow":
                        jump yellow
                label yellow:
                    p "Let's go look at the yellow paint."
                    k "Rally? Yellow paint? I prefer purple."
                    p "How come?"
                    k "Purple paint tastes better..."
                    p " You {i} eat {/i} paint???"
                    k " Don't be daft! I drink it!"
                    "You are not in the mood to see that today."
                    p "....Okay.... Let's go look at the sinks instead."
                    jump sink
                label orange:
                    p "Let's go look at the orange paint."
                    k "Really? Orange paint? What obtuse taste...I prefer the purple."
                    p "How come?"
                    k "The purple paint here tastes better."
                    p "You {i} eat {/i} paint???"
                    "He starts to chuckle nervously."
                    #show samsonBashful
                    k "NO!!!!! That would be weird..."
                    p "Okaaaaaaay....Let's go look at the sinks."
                    jump sink
                label purple:
                    p "Let's go look at the purple paint."
                    k "Excellent! I love paint."
                    "You hear a popping sound."
                    "You turn around, and see King Samson II has opened a can of purple paint and..."
                    "..!"
                    "He is furiously shoving handfuls of paint into his mouth."
                    p "Are you {i} eating {/i} paint???"
                    k "Yes. Paint has fiber, and everyone knows fiber is filled with nutrients."
                    menu:
                        "Can I try some?":
                            jump goToSink
                        "Ew. Weirdo.":
                            jump goToSink2
                    label goToSink:
                        k "Sure!"
                        "You try some purple paint."
                        p "Not bad."
                        k "Let's go look at the sinks!"
                        p "Okay!"
                        jump sink
                    label goToSink2:
                        k "wELL exCuUUuUuUuUUUse me if my tastebuds are more refined."
                        p "Whatever. Let's go look at sinks."
                        jump sink
            label sink:
                "You walk over to a row of sinks."
                "After several minutes, you find a sink that you like."
                p "This sink is the bees knees! I hope it works."
                "You ask the store manager to learn more about this fabulous product."
                m "Well, t his sink is the finest on the market. It's stainless steel and has a pull down faucet."
                k "Stainless steel? How horrendous! In my kingdom, all my sinks are made of titanium. Stainless steel is for peasants."
                m "I assure you, this sink is very practical for both peasants and kings. It costs seven hundred dollars."
                p "{i} Seven hundred dollars?/ {/i}"
                menu:
                    "That's too expensive.":
                        jump cheapAss
                    "I'll take it!":
                        jump buySink
                label cheapAss:
                    p "I'm sorry..I don't think I have enough money to buy it! Unless..."
                    "You turn to King Samson."
                    p "...you buy it for me!"
                    k "Oh. *nervous laughter* That is so comical. I must have left my wallet at home."
                    "The manager leaves."
                    "Suddenly, you get a brilliant idea...to steal the sink."
                    k "What are you doing?"
                    p "I am stealing the sink."
                    "You grab the sink and rip it off the counter."
                    "Alams start ringing. Beep Beep Beep..."
                    k "Crap on a cracker! Let's run!!!"
                    p "Aight bruh."
                    "King Samson II starts leaping towards the exit. You trail behind him, dragging the sink."
                    "BeEp! BeeEEP! beePP! Beep!"
                    "In your struggle to steal the sink, you trip and fall."
                    p "Oh no!"
                    "The cops arrive on scene and surround both you and King Samson."
                    x "Is there a problem here?"
                    k "Yes! This person here is stealing the sink!!!"
                    p "Hey!"
                    k "Yup! I was a witness to this horrific crime. I saw them run away with this sink."
                    "King Samson turns to you."
                    k "Shame on you! Some people..."
                    #show KingShakeHead
                    k "This would never happen in my kingdom."
                    x "Alright. We have all the evidence we need. Let's go."
                    p "{i} I knew I should've memorized my rights in government class..."
                    "Policeman One takes you to jail."
                    jump altEndKingDate1
                label buySink:
                    m "Wonderful! Head over the cashier and we'll help you from there."
                    p "Great!"
                    "You pick up the sink with one arm and put it into a shopping cart. You make your way towards the cashier."
                    k "Humph...I disapprove of your purchase. I bet this sink won't last a day. It probably leaks..."
                    p "Don't be ridiculous. Why would anyone sell a leaking sink."
                    "Miraculously, you notice that the sink has started leaking!"
                    k "I told you so."
                    # show KingSigh
                    "King Samson II sighs wistfully."
                    k "It's so hard being right all the time."
                    menu:
                        "You still want to buy the sink.":
                            jump stillBuy
                        "Froget this! You don't want to buy broken kitchenware!":
                            jump forget
                    label stillBuy:
                        p "I don't care! I'm buying this sink whether you like it or not!"
                        "You pay for the sink, and leave the store with it."
                        "While walkin ghome, a rabit skunk bites you in the shin. You drop the sink and it breaks. You've had enough for the day and leave it be."
                        jump endKingDate1
                    label forget:
                        p "This is nutters! Why is this sink leaking?"
                        p "I refuse to buy this!"
                        "You leave the store, sinkless."
                        jump endKingDate1
    label endKingDate1:
        "King Samson II walks you back to your dorm."
        k "Good night my fare carbon based life form."
        " He pats your shoulder and kisses your foot."
        "You're a little weirded out, but you're too tired to care. You turn into your dorm for the night."
        jump endOfMandDates
    label altEndKingDate1:
        "You spend one night in jail."
        x "Alright. Today's your lucky day. You're being released on account of good behaviour."
        "You run out of your cell, and hurry back to your dorm room."
        jump endOfMandDates

    #all approaches for date 1
    # listOfApproaches = ["emoApproach", "marvinApproach", "kingApproach"]
    label endOfMandDates:
        "A week passes..."
        "One day during lunch..."
        "You see the three frogs in line near each other at the cafeteria."
        "Which one do you wave to?"
        menu:
            "xX_DarkRaven496283_Xx":
                jump emoApproach
            "Marvin":
                jump marvinApproach
            "King Samson II":
                jump kingApproach
        label emoApproach:
            e "r-rawr... hey cutie >///> i-if you're not doing anything later...m-ayBee u would wanna hang out with me today? XD"
            "xX_DarkRaven496283_Xx leaps away, hiding his frog face with his fringe along the way."
            "Maybe you should meet up with him after class..."
            jump emoDate2
            #jump nextApproach
        label marvinApproach:
            m "Hey there you little pumpkin. I have a special date planned for us today. Do you wanna go or not? You don't have to...unless...Hiss HIss"
            "Marvin leaps away leaving you wondering about the date."
            "Maybe you should meet up with him after class..."
            jump marvinDate2
        label kingApproach:
            k "GOOD AFTERNOON MY HIGHNESS TO BE. ARE YOU BUSY TODAY? IF NOT PLEASE MEET WITH ME WHEN YOU ARE FREE."
            "King Samson II leaps away, pushing people aside in the process."
            "Maybe you should meet with him later..."
            jump kingDate2
        # jump emoApproach
        # "Someone else seems to be approaching you..."
        # jump marvinApproach
        # "Who do you want to meet up with later?"
        # menu:
        #     "xX_DarkRaven496283_Xx":
        #         jump emoDate2
        #     "Marvin":
        #         jump marvinDate2
    label emoDate2:
        "You meet up with xX_DarkRaven496283_Xx later."
        e " w-wow you actually said yeah 0///0 y-you're the only one that ever cares..."
        "xX_DarkRaven496283_Xx hides his blush behind his fringe."
        e "a-anyways lets get going... u-uwu... i bought us ticket$ 2 da MBR concert..."
        e "do you like them? "
        menu:
            "YES omg i LOVE MBR.":
                jump noYouDont
            "No sorry... who are they?":
                jump noMBR
        label noYouDont:
            "xX_DarkRaven496283_Xx seems unimpressed."
            e " -__- they're pwetty indie so i didn't think u would kno them...are u sure ur not lying 2 me? lol...no need 2 try and impres me..."
            "..."
            jump startEmoDate2
        label noMBR:
            "xX_DarkRaven496283_Xx seems offended."
            e "omgzzz you dun kno who they arrrr??? youre out of the looop ... they r the hottest rawk band out their write nao... XD"
            "..."
            jump startEmoDate2
    label startEmoDate2:
        "You and xX_DarkRaven496283_Xx arrive at the My Biological Romance concert together."
        e "rrrrrrrrrraaaaaaaawwwwwwwwrrrrr XD where heer."
        menu:
            "Go closer to the stage.":
                jump moshPit
            "Stay near the balcony.":
                jump balcony
        label moshPit:
            p "Hey let's go to the mosh pit! It seems like everyone is having fun down there."
            e " w-weally? owo we are really meant 4 each other uwu"
            "You and xX_DarkRaven496283_Xx go to the mosh pit, unaware of what is to come."
            "Y'all start dancing and singing to House of Frogs."
            "You want to show that you are a hardcore concert goer (though you've never been and include yourself in one of the many moshpit stunts."
            menu:
                "Crowd-surf":
                    jump crowdSurf
                "Mosh":
                    jump mosh
            label crowdSurf:
                "Two randos throw you into the crowd and you start to crowd surf."
                "Someone boops your nose and you feel extremely violated."
                menu:
                    "Sneeze on the finger.":
                        jump sneeze
                    "Bite the finger":
                        jump bite
                label sneeze:
                    "You sneeze on the finger like a madlad."
                    "...Turns out it's your own finger. You couldn't keep track due to all the hands around you."
                    "You get back down on your feet and rub the residue on someone's shirt."
                    "..."
                    "They seem weirdly grateful..."
                    "You realize that you can't find xX_DarkRaven496283_Xx so you start to look for him."
                    "Someone's back is turned to you. He is wearing an MBR shirt and a familiar studded belt from Boiling Topic. It looks like xX_DarkRaven496283_Xx but you're not sure."
                    menu:
                        "Say Heyyyy xX_DarkRaven496283_Xx.":
                            jump heyDude
                        "Politely ask if they've seen xX_DarkRaven496283_Xx.":
                            jump askDude
                    label heyDude:
                        "The person turns around. Turns out it's not xX_DarkRaven496283_Xx."
                        "Turns out in his native language, the word 'xX_DarkRaven496283_Xx' is an insult. He looks pissed and storms towards you with his hands clenched."
                        "You run away and he starts to chase you. You coincidently run into xX_DarkRaven496283_Xx."
                        e "o-owo? what is wrong baybee??"
                        e "{i} * sees the dude storming towards you * {/i}"
                        e "O.O how daer u run after my senpai? she is MINE XD"
                        e " 私の靴の臭いを止めることができますか？私は先日水たまりに足を踏み入れた"
                        "Unfortunately, you had no idea that xX_DarkRaven496283_Xx  spoke Japanese, let alone understand what it meant."
                        "Fortunately for you, it seems to intimidate the dude, who nervously slinks away."
                        e "*nuzzles* i wil alwayz protecc u."
                        e "i'll be there for you, even when no one will be there for me ^^."
                        "You and xX_DarkRaven496283_Xx  safely leave the MBR concert. You're kind of weirded out, but also strangely happy..."
                        jump endEmoDate2
                    label askDude:
                        "You ask the dude if he has seen someone dressed like xX_DarkRaven496283_Xx."
                        "The dude instead winks at you and asks for your phone number."
                        menu:
                            "Give him the number 718-899-6161":
                                jump astrology
                            "Give him the number 604-594-9190.":
                                jump astrology
                        label astrology:
                            "You give him the number. Turns out that specific set of numbers is an insult in his culture. He looks pissed and storms towards you with his hands clenched."
                            "He doesn't really intimidate you though..."
                            "You punch him and he falls down."
                            "xX_DarkRaven496283_Xx  comes leaping towards you."
                            "m-my senpai! that was so cool... :3"
                            "You and xX_DarkRaven496283_Xx  safely leave the MBR concert You're kinda weirded out, but strangely happy..."
                            jump endEmoDate2
        label mosh:
            "You have no idea what to do, but you see everyone slamming into each other."
            menu:
                "Jump up.":
                    jump up
                "Duck down.":
                    jump down
            label up:
                "you jump up."
                "Once you're back on your feet, someone slinks towards you and tells you to choose a drug."
            #WHERE JEEVIKA LEFT OFF

    label marvinDate2:
        "You agree to Marvin's date."
        "He tells you to meet at his house..."
        "..."
        "After school you go to Marvin's house for your date."
        "You ring the doorbell."
        "Marvin opens the door...He looks upset."
        m "Hey there momma goose... Come on in."
        m "I am so sorry! I had a very romantic evening planned at the train station, but one of my tadpoles got sick. I have to tadpole-sit because Helen can't make it."
        m "Would you like to join me?"
        "You feel kind of bad..."
        p "Yes, of course I will."
        "You make your way into Marvin's living room. A sickly looking tadpole is lying on the couch."
        m "This is Little Suzie."
        l "HIIIISSSSS."
        p "{i}She takes after her father...{/i}"
        m "I think to cheer Little Suz up, we should play a board game."
        m "What board game should we play?"
        menu:
            "Scrabble":
                jump scrabble
            "The Game of Life":
                jump gameOfLife
            "Monopoly":
                jump monopoly
        label scrabble:
            l "HISSSSS That one is my favourite!"
            "You play a couple rounds of scrabble. After about an hour, Little SUzie is looking considerably happier."
            jump continue
        label gameOfLife:
            l "HISSSS That one is my favourite!"
            "You play a couple rounds of Monopoly. After about an hour, Little Suzie is looking considerably happier."
            jump continue
        label monopoly:
            l "HISSSSS That one is my favourite!"
            "You play a couple rounds of Monopoly. After about an hour, Little Suzie is looking considerably happier."
            jump continue
    label continue:
        l "I am feeling so much better! hiss hiss can I go outside and play?"
        m "Sure, kiddo."
        "Little Suzie crawls out of the house."
        m "Alright, now thajt Suzie is gone, what would you like to do?"
        m "..."
        m "actually..."
        m "You can help me clean the house. Helen always gets so annoyed when it is dirty."
        menu:
            "Yeah! I'd love to help you clean.":
                jump clean
            "No thanks...let's do something else.":
                jump noClean
        label clean: 
            m "Woohoo! Thank God you said yes. This house is a complete dump."

    label kingDate2:
        "jaja"

    #problem with it reading going through all next labels??

    # firstFirstDates = ["marvinDate1", "emoDate1", "kingDate1"]
    # label endOfMandDates:
    #     #example of a choice in dating
    #     "The next day during lunch..."
    #     "Both uhhh marvin and uhhh emo ask u on date who do u choose"
    #     menu:
    #         "marvins p cute":
    #             jump marvinDate1
    #         "emo is p nice ig":
    #             jump emoDate1
    #     if marvinDate1:
    #         "upir ficomg ,p,,a"
    #     else:
    #         "uour mmma"
    #     return
