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
define n = Character("Some Obscure Skunk")
define d = Character("Local Doctor One")
define a = Character("Rando One")
define f = Character("Crazy Fangirl One")
define w = Character("La Bouteille D'eau Waiter One")
define t = Character("King Samson II's Servant")

#DEFINING IMAGES: BACKGROUNDS
image alleyway = "alleyway.jpg"
image apartmentInside = "apartmentInside.jpg"
image apartmentOutside = "apartmentOutside.jpg"
image bathAndBody = "bathAndBooty.jpg"
image blackTransition = "blackTransition.png"
image boiledTopic = "boiledTopic.jpg"
image boiledTopicInside = "boiledTopicInside.jpg"
image busStop = "busStop.jpg"
image cafeteria = "cafeteria.jpg"
image cemetery = "cemetery.jpg"
image classroom = "classroom.jpg"
image concert = "concert.jpg"
image concertCrowd = "concertCrowd.jpg"
image concertOutside = "concertOutside.jpg"
image corporate = "corporate.jpg"
image crowdSurf = "crowdSurf.jpg"
image dinerInside = "dinerInside.jpg"
image dinerOutside = "dinerOutside.jpg"
image door = "door.jpg"
image fancyRestaurant = "fancyRestaurant.jpg"
image fitnessCenter = "fitnessCenter.jpg"
image forest = "forest.jpg"
image forestClearing = "forestClearing.jpg"
image homeDepot = "homeDepot.jpg"
image homeDepotOut = "homeDepotOut.png"
image jailHouse = "jailHouse.jpg"
image kingdom = "kingdom.jpg"
image kitchen = "kitchen.jpg"
image livingRoom = "livingRoom.jpg"
image london = "london.jpg"
image paintAisle = "paintAisle.jpg"
image sinkAisle = "sinkAisle.jpg"
image trainStation = "trainStation.jpg"
image uniCampus = "uniCampus.jpg"
image wallbluesInterior = "wallbluesInterior.jpg"
image wallbluesOutside = "wallbluesOutside.jpg"

#DEFINING IMAGES: SPRITES
image emoAngry = "emoAngry.png"
image emoBlush = "emoBlush.png"
image emoCry = "emoCry.png"
image emoDefault = "emoDefault.png"
image emoSad = "emoSad.png"
image emoShadow = "emoShadow.png"
image helen = "helen.png"
image kingAngry = "kingAngry.png"
image kingBelch = "kingBelch.png"
image kingBlush = "kingBlush.png"
image kingChuckle = "kingChuckle.png"
image kingCry = "kingCry.png"
image kingDefault = "kingDefault.png"
image kingProc = "kingProc.png"
image kingShocked = "kingShocked.png"
image kingSlimy = "kingSlimy.png"
image kingShadow = "kingShadow.png"
image mbrGuy = "mbrGuy.png"
image mCry = "marvinCry.png"
image mBlush = "marvinBlush.png"
image mDefault = "marvinDefault.png"
image mGross = "marvinGrossedOut.png"
image mHiss = "marvinHiss.png"
image mMOF = "marvinMOF.png"
image mSad = "marvinSad.png"
image mWink = "marvinWink.png"
image mWow = "marvinWowzers.png"
image suzieDefault = "suzieDefault.png"
image suzieHiss = "suzieHiss.png"


label start:

    #show cheesy hearts pic

    "Welcome to F Cubed."
    "DEVELIP ERS NOTE: WE ARE AWARE OF TYPOS. PRETEND THEY ARE THERE ON PURPOSE."

    # bg change = "scene ____"
    #sprite show = "show ___"

    scene uniCampus

    "You are a new student at XYZ University."
    p "Wow I am so excited! I hope I will get a boyfriend this year..."
    scene blackTransition
    "And so your Flirtatious Froggy Fantasy begins..."

    "It's time to look at your new dorm!"
    scene hallway
    "You make your way into your dorm room's building."
    show mDefault

    m "Hey neighbour! Are you new here?"
    menu:
         "Yeah… u-uwu… Wanna show me around?":
            jump showmearound
         "Yes. What is it to you?":
            jump ignore
    label showmearound:
         show mBlush
         m "Ok cutie. I have Zoology 101 next, do you? Not that I looked up your student records or anything…"
         p "Yes, I have that class as well."
         hide mBlush
         scene blackTransition
         "You and Marvin walk to class together."
         scene classroom
         show mHiss
         m "HIIIISSSSSS"
         p "{i} What the heck?? {/i}"
         hide mHiss
         show mDefault
         m "Sit next to me."
         hide mDefault
         jump kingintro
    label ignore:
         show mSad
         m "Hmph. *muttering* Just like my ex-wife…"
         scene blackTransition
         hide mSad
         "Marvin walks away and makes his way to his class…"
         scene classroom
         "Marvin is in the same class as you! There seems to be a limited amount of seats. You reluctantly make your way to the seat next to Marvin."
         jump kingintro
    label kingintro:
        show kingShadow
        u "hEy ! How dare you reside in my space?"
        hide kingShadow
        p "{i} Get a load of this guy...who does he think he is?{/i}"
        show mDefault
        m "King Samson II! I didn’t know you had Zoology 101 as well!"
        hide mDefault
        "King Samson II pushes past you..."
        show kingShocked
        k "Step aside, peasants!"
        "...and takes the empty seat next to Marvin."
        hide kingShocked
        "You look around the rest of the class for any seats to take."
        "...!"
        "There’s one seat left in the back. You walk over and see a hooded figure lurking in the corner."
        show emoShadow
        p "You good?"
        u "r-rawr…. >.< ….oh..sorry...didn’t see you there ...hehe"
        hide emoShadow
        "He coughs up a hairball…"
        show emoDefault
        p "hey…"
        "You awkwardly take a seat"
        u "h-hey… >///< you’re kinda cute...what is your handle? I go by Xx_darkraven496283_xX"
        "He waves to you, flexing his fingerless skeleton themed gloves."
        hide emoDefault
        menu:
            "Those are some pretty swaggy swagalicious swags!":
                jump swag
            "Fingerless gloves? What is this, 2005?":
                jump emoInsult
        label swag:
            show emoBlush
            e "xX haha...thanks i guess… *nuzzles* :3"
            hide emoBlush
            "He seems to have taken a liking for you…"
            "This promises to be an interesting first day."
            scene blackTransition
            jump d2
        label emoInsult:
            show emoAngry
            e "STOP FLAMING MY PAGE!!! You don't understand...no one does..."
            hide emoAngry
            show emoCry
            "He starts to cry into the desk…"
            hide emoCry
            "This promises to be an interesting first day."
            scene blackTransition
            jump d2
        label d2:
            "The next day"
            jump wallblues
        label wallblues:
            scene classroom
            "After class…"
            show mDefault
            m "Hey you ;) I need to get some laxatives...wanna come with me to Wallblues?"
            hide mDefault
            menu:
                "Laxatives??? That’s gross why would you tell me that…":
                    jump laxativesWeird
                "Yeah sure...I need some too…":
                    jump laxativesToo
        label laxativesWeird:
            show mWink
            m "Don’t judge me like that sweetie. You look like you might need some too after today’s breakfast. If you know what I mean ;) "
            p "{i}what a rude bastard…{/i}"
            hide mWink
            scene blackTransition
            "You follow Marvin to Wallblues"
            jump CVS
        label laxativesToo:
            show mGross
            m "Ew that’s so gross. Why would you tell me that? Did your mother never teach you? A young lady never gives away her laxative status…kids these days"
            "You follow a disgusted Marvin to Wallblues."
            hide mGross
            scene blackTransition
            jump CVS
        label CVS:
        scene wallbluesOutside
        show mDefault
        m "Want to go inside?"
        hide mDefault
        menu:
            "Yeah! Let’s go.":
                jump inside
            "No thanks, let’s wait here for a bit.":
                jump outside
        label inside:
            scene wallbluesInterior
            "You go inside the store with Marvin and walk towards the gift card aisle."
            show mWink
            m "I was kidding. I don’t actually need laxatives, it was a test of your loyalty to me."
            hide mWink
            show mDefault
            m "I was actually wondering if you wanted to browse the candy aisle with me."
            hide mDefault
            menu:
                "Yeah I love candy!":
                    jump yesCandy
                "I’d rather browse the medications":
                    jump noCandy
            label yesCandy:
                show mDefault
                m "Thanks bby. My ex-wife Helen never let me eat candy. Something about type 2 diabetes?"
                hide mDefault
                "You go to the candy aisle."
                show mMOF
                m "Back in my day, the kids ate Skittles and M&M’s. As the datee, you get to choose which candy we eat. My treat!"
                hide mMOF
                menu:
                    "Skittles!":
                        jump Skittles
                    "M&M’s!":
                        jump MandM
                label Skittles:
                    show mHiss
                    m " Hiss Hiss! A gourmet choice!"
                    hide mHiss
                    show mDefault
                    m "What color do you choose? This is a vital question, so make sure you think before answering."
                    hide mDefault
                    menu:
                        "Red":
                            jump red
                        "Blue":
                            jump blue
                    label red:
                        show mMOF
                        "Ahhh red skittles, just like the strawberry scent my ex-wife Helen used to spray."
                        hide mMOF
                        "You get sick of Marvin babbling about his ex-wife Helen’s perfume and leave."
                        jump endMarvinDateOne
                    label blue:
                        show mMOF
                        "Ahhh blue skittles, just like the blueberry scent my ex-wife Helen sprayed on the day of our divorce…"
                        hide mMOF
                        "You get sick of Marvin babbling about his ex-wife Helen’s perfume and leave."
                        jump endMarvinDateOne
                label MandM:
                    show mDefault
                    m "A splendid choice! I promise I won’t eat more than half of the bag"
                    hide mDefault
                    "..."
                    "Marvin ends up eating the entire party-sized bag of M&M’s. You are hungry and annoyed, so you leave."
                    jump endMarvinDateOne
            label noCandy:
                show mDefault
                m "Okay."
                hide mDefault
                "You stare at different colored pills for 2 hours. You end up buying Behnardrill, and head outside."
                jump endMarvinDateOne
        label outside:
            scene wallbluesOutside
            "You stand outside the store for twenty minutes."
            "In an attempt to break the awkward silence, you engage Marvin in a conversation about lemons."
            p "Do you like lemons?"
            show mMOF
            m "I don’t, but my ex-wife Helen loves them."
            hide mMOF
            menu:
                "Your ex-wife? You were married!?":
                    jump exwife
                "That’s so interesting. Do you have any kids?":
                    jump kids
            label exwife:
                show mDefault
                m "Yeah. You?"
                hide mDefault
                p "No!"
                scene blackTransition
                p "You leave Marvin outside Wallblues, shocked and disgusted."
                jump endMarvinDateOne
            label kids:
                show mMOF
                m "I have four. How many do you have?"
                hide mMOF
                p "None!"
                p "You leave Marvin outside Wallblues, shocked and disgusted. You loathe children."
                scene blackTransition
                jump endMarvinDateOne
    label endMarvinDateOne:
        scene hallway
        "Marvin follows you back to your dorm after your outing at Wallblues."
        show mBlush
        m "Thanks for coming with me. I had a really nice time with you…"
        hide mBlush
        "He struggles to keep up with you."
        menu:
            "Thanks. I had a nice time too.":
                jump niceTime
            "Can you stop following me please?":
                jump stopStalker
        label niceTime:
            show mMOF
            m "I knew you would like WallBlues! I used to bring my ex-wife there all the time!"
            hide mMOF
            jump flyScene
        label stopStalker:
            p "{i} Why is he still here? I don’t want to have to call the security…{/i}"
            show mSad
            m "But bhabie...I thought you would like WallBlues…"
            hide mSad
            show mCry
            "It seems as if he has started crying…"
            hide mCry
            jump flyScene
    label flyScene:
        show mWow
        m "WOWZERS !"
        "...!!!"
        "Woah there momma goose ! Is he...Kissing your feet???"
        hide mWow
        show mHiss
        "Marvin smacks his frog lips."
        hide mHiss
        show mBlush
        m "Sorry....Hiss hisss...there was a fly by your feet. I couldn’t help myself...Anyways, have a good night :) See you tomorrow momma goose."
        hide mBlush
        scene blackTransition
        "Marvin walks away and you turn into your dorm for the night."
        jump mandDateD2
        label mandDateD2:
            scene classroom
            "After class…"
            show emoBlush
            e "hey… you busy by any chance… o-owo"
            hide emoBlush
            menu:
                "Actually I was planning on studying...wanna come with?":
                    jump studyFreak
                "No. Do you need something?":
                    jump noPlans
            label studyFreak:
                show emoDefault
                e "aww don't be such a prep...come shopping with me at boiled topic!"
                hide emoDefault
                "xX_DarkRaven49623_Xx drags you to the mall."
                jump boiledTopic
            label noPlans:
                show emoBlush
                e "that's kinda funky of you my fellow follower of darkness. wanna go to the boiled topic with me? you are qq but your style is off..."
                hide emoBlush
                p "{i} I am holding back from kicking him in the shin...{/i}"
                jump boiledTopic
        label boiledTopic:
            scene boiledTopic
            "At Boiled Topic..."
            #cult member default
            "Outside the store, a member of a local cult asks if you want to join their cult, ZYX."
            menu:
                "Sure! I'll join.":
                    jump joinCult
                "No thanks.":
                    jump noCult
            label noCult:
                show emoBlush
                e "i'm glad you didn't leave me :)"
                hide emoBlush
                show emoSad
                e "..."
                e "...everyone else does..."
                hide emoSad
                scene boiledTopicInside
                "You go inside the store. Inside, an employee mutters a greeting and continues to write his will on Google Docs."
                show emoDefault
                e "i have a few clothes that i want to try, but i'm afraid that i won't buy any of them due to my constant self-deprecation and low self esteem lol XD. that's why i brought u."
                e "i'll go change into my first fit."
                hide emoDefault
                "xX_DarkRaven496283_Xx comes out of the dressing room in a studded belt, fake tattoo sleeves, super-duper
                schmooper black skinny jeans, and Doctor Martins."
                e "rawr XD well..what do u think? "
                menu:
                    "Wow whatta hottie.":
                        jump hotEmo
                    "Laaaaame.":
                        jump lameEmo
                label lameEmo:
                    show emoSad
                    e " *sad uwu* that's what they all say ..."
                    e "i really thought you'd be different. you know what they say..."
                    hide emoSad
                    show emoCry
                    e "love can sometimes be magic...but magic..."
                    e "is just an illusion"
                    hide emoCry
                    menu:
                        "I'm sorry, I didn't mean it! Please let me make it up to you...":
                            jump makeUp
                        "Stop being dramatic...geez.":
                            jump dramatic
                    label makeUp:
                        show emoBlush
                        e "o-owo? a-are you sure?"
                        hide emoBlush
                        menu:
                            "Yes":
                                jump yesMakeUp
                            "...no":
                                jump dramatic
                        label yesMakeUp:
                            show emoBlush
                            e "but are you sure-sure?"
                            hide emoBlush
                            menu:
                                "YES.":
                                    jump yesyesMakeUp
                                "...no?":
                                    jump dramatic
                            label yesyesMakeUp:
                                show emoSad
                                e "...but how sure exactly are you?"
                                hide emoSad
                                menu:
                                    "Absolutely 100 Percent Sure.":
                                        jump yesyesyesSure
                                    "Well now I am 0 Percent sure you ungrateful twat.":
                                        jump dramatic
                                label yesyesyesSure:
                                    show emoBlush
                                    e "oh em gee... ^_^ no one's ever been so faithful 2 me. i thought i would perish forever alone..."
                                    hide emoBlush
                                    "xX_DarkRaven496283_Xx seems to have started to tear up??"
                                    show emoCry
                                    "he runs out of the store crying."
                                    hide emoCry
                                    jump endEmoDate1
                    label dramatic:
                        show emoSad
                        e "the fleeting feeling of love lasts only for a moment...but the pain of love lasts a lifetime..."
                        hide emoSad
                        show emoCry
                        "it seems xX_DarkRaven496283_Xx has started to tear up."
                        hide emoCry
                        scene blackTransition
                        "He runs out of the store crying."
                        jump endEmoDate1
                label hotEmo:
                    show emoBlush
                    e "owo w-weally? no one's ever said that bee four..."
                    hide emoBlush
                    show emoDefault
                    e "i'll go wear the second outfit. brb haha XD"
                    hide emoDefault
                    "xX_DarkRaven496283_Xx comes out wearing an oversized Evanescence shirt."
                    show emoBlush
                    e "um do i look fat in dis shirt? not that i don't any other time... >w<"
                    hide emoBlush
                    menu:
                        "Yuhhh":
                            jump yesFat
                        "Of course knot !":
                            jump noFat
                    label yesFat:
                        show emoSad
                        e "i knew it... i'll just...not get it i guess..."
                        hide emoSad
                        scene blackTransition
                        show emoCry
                        "xX_DarkRaven496283_Xx starts to tear up. He runs out of the store crying."
                        hide emoCry
                        jump endEmoDate1
                    label noFat:
                        show emoBlush
                        e "you're too cute :3 let's go buy deez"
                        hide emoBlush
                        "You go with xX_DarkRaven496283_Xx to the cash register."
                        "The employee stops writing his will and says that the total is $87.32"
                        show emoDefault
                        e " WHAT XD?! i thought i had a discount from being a five year member of this store..."
                        hide emoDefault
                        show emoSad
                        e "i spent all of my money on guy-liner refills already..."
                        "xX_DarkRaven496283_Xx smile shakily."
                        hide emoSad
                        show emoCry
                        e "you know what they say... no smile is more beautiful than the one that struggles through the tears...."
                        hide emoCry
                        scene blackTransition
                        "xX_DarkRaven496283_Xx runs out of the store crying."
                        jump endEmoDate1
            label joinCult:
                #cult member shocked
                c "Wow, really? You're the first person to ever say 'yes.' "
                #cult member default
                c "To join our cult, you must go through an initiation ceremony. Stop by my church for a couple hours to get started."
                p "I can't wait !"
                c "Hey, may I go shopping with you?"
                menu:
                    "Of course! Anything for a fellow worshipper.":
                        jump shop
                    "I don't think that is a good idea.":
                        jump noCult
                label shop:
                    scene boiledTopicInside
                    "You go inside the store with Cult Member One and xX_DarkRaven496283_Xx."
                    "You browse the store, and xX_DarkRaven496283_Xx instantly finds the studded belt. He goes to the fitting room to try it on."
                    #cult member default
                    c "I don't see any cult-related items in this store. I think I'll go check out some other stores. Good day to you fellow worshipper."
                    p "Farewell, enlightened one!"
                    "xX_DarkRaven496283_Xx exits the fitting room wearing the studded belt."
                    show emoDefault
                    e "so...how do i look?"
                    hide emoDefault
                    menu:
                        "Awful. Just awful.":
                            jump awful
                        "You look fine, but I wish the belt was in a different colour.":
                            jump diffcolour
                    label awful:
                        show emoSad
                        e "...r-really?"
                        hide emoSad
                        menu:
                            "No, I was just joking. But I do wish the belt was in an another colour.":
                                jump diffcolour
                            "Yes! You look like someone ran you over with a cement mixer.":
                                jump insultEmoAgain
                    label insultEmoAgain:
                        show emoCry
                        "xX_DarkRaven496283_Xx sobs his guts out."
                        e "...i won't buy the belt i guess... *sniffles*"
                        hide emoCry
                        p "Wise decision."
                        scene blackTransition
                        "xX_DarkRaven496283_Xx runs out of the store, crying for the second time."
                        jump endEmoDate1
                    label diffcolour:
                        show emoSad
                        e "b-but i like the colour black..."
                        hide emoSad
                        show emoCry
                        "xX_DarkRaven496283_Xx seems to have started crying..."
                        "You scramble to fix the situation."
                        p "Don't be ridiculous! Let's go see if the store sells a different colour belt."
                        hide emoCry
                        "You ask the employees, but they say that black is the only colour belt they have."
                        "You're about to give up hope, but you notice a customer service number written on the belt's tag. It says to call if you have any questions."
                        "You call the number."
                        #studded belt company default
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
                            show emoDefault
                            e "...no"
                            hide emoDefault
                            b "Thank you for calling. Have a nice day. "
                            show emoSad
                            e "...but i wanted a black belt..."
                            hide emoSad
                            p "Stop complaining!"
                            scene blackTransition
                            "xX_DarkRaven496283_Xx starts sobbing and runs out of the mall."
                            jump endEmoDate1
    label endEmoDate1:
        scene blackTransition
        "Today was an eventful day...You were unable to buy anything, but you feel as if you understand xX_DarkRaven496283_Xx more now."
        jump mandDateD3Setup
    label mandDateD3Setup:
        scene blackTransition
        "The Next Day..."
        "Yesterday's date with xX_DarkRaven496283_Xx was certainly...something."
        "You should head to class."
        jump D3Class
    label D3Class:
        scene classroom
        "During class..."
        "King Samson II passes you a note."
        show kingDefault
        k "My fairest lady. My apologies. I should not have taken your seat on the first day. I am sorry...I was having cramps that day. Mayhaps accompany me to a date after class? (check yes or no)"
        hide kingDefault
        menu:
            "Check Yes.":
                jump yesNote
            "Check No.":
                jump noNote
            "Check No and write a snarky response.":
                jump youAreMean
        label yesNote:
            "You check yes and pass the note back over to King Samson II."
            show kingSlimy
            "He gives you slimy smile."
            hide kingSlimy
            jump mandDateD3
        label noNote:
            "You check no and pass the note back over to King Samson II."
            show kingShocked
            "He feigns a hurt expression at you...?"
            hide kingShocked
            show kingCry
            "It appears he has started to cry."
            "You feel guilty...maybe you should go on that date with him."
            hide kingCry
            jump  mandDateD3
        label youAreMean:
            "You check no and write a little note on the side."
            p "Really? Asking me out by passing a note? Are we in middle school??"
            show kingCry
            "You pass the note back to King Samson II. He reads it and starts to cry..."
            "...You feel guilty...maybe you should go on that date with him."
            hide kingCry
            jump mandDateD3
    label mandDateD3:
        "After class you meet up with King Samson II."
        show kingDefault
        k "I know you have wanted to date me for a long time now...Be glad you have this opportunity."
        hide kingDefault
        p "{i} I'm one step away from kicking him in the shin...{/i}"
        menu:
            "I'm one step away from kicking you in the shin.":
                jump shinKick
            "Haha yeah...":
                jump hahaYeah
        label shinKick:
            show kingChuckle
            "King Samson II gives you a hearty chuckle."
            k "Don't be like that sweetie!"
            hide kingChuckle
            "He drags you outside."
            jump homeDepot
        label hahaYeah:
            show kingBlush
            k "Are you nervous? Don't be..."
            hide kingBlush
            "He drags you outside."
            jump homeDepot
    label homeDepot:
        scene homeDepotOut
        "After an awkward walk with King Samson II you arrive in front of...the local hardware store."
        show kingDefault
        k "Hum DëpÔté! My personal favourite place to loiter at."
        hide kingDefault
        menu:
            "Go inside Hum DëpÔté":
                jump insideHum
            "Stay outside Hum DëpÔté":
                jump outsideHum
        label outsideHum:
            scene homeDepotOut
            "You stay outside Hum DëpÔté"
            show kingProc
            k "By the gods! Observe this complex contraption before us!"
            #shopping cart
            p "It's a...shopping cart??"
            k "We must treasure such a tool! Quick, before anyone looks!"
            hide kingProc
            menu:
                "Steal the shopping cart.":
                    jump stealCart
                "Leave the shopping cart where it is":
                    jump leaveCart
            label stealCart:
                "You help King Samson II shoplift the shopping cart."
                p "We can get in big trouble for this..."
                show kingProc
                k "Nonsense! Anyone who challenges me to a duel shall feast their eyes upon my fists!"
                hide kingProc
                " WEE WOO WEE WOO (police siren noises sorry we don't know how to spell out how it sounds)"
                #police officer
                "A wild police officer appears!"
                show kingProc
                k "I CHALLENGE YOU TO A DUEL, GOOD SIR."
                hide kingProc
                menu:
                    "Let King Samson II duel against the police officer. He is a grown frog and can do what he wants.":
                        jump yesDuel
                    "Don't let King Samson II duel against the police officer. He is a man child and does not know what he is doing.":
                        jump noDuel
                label noDuel:
                    p "You don't have to do this! Let's just take the ticket and leave."
                    show kingProc
                    k "But...my honor!"
                    hide kingProc
                    "You drag King Samson II away from the scene."
                    "He takes a look at the ticket given to him."
                    show kingShocked
                    k "468 dollars? I lack the wealth to accomplish such a feat..."
                    hide kingShocked
                    p "{i} ...isn't he a king? {/i}"
                    "..."
                    " It appears King Samson II has started to faint from shock."
                    show kingDefault
                    k "Please...leave me here to die. Go before they catch you as well!"
                    hide kingDefault
                    p "Oh...okay then."
                    "You leave...you guess."
                    "As you leave you notice Samson get up and follow you."
                    jump endKingDate1
                label yesDuel:
                    show kingProc
                    k "PREPARE TO FIGHT! I WILL VOMIT ON YOUR POSSESSIONS, YOU INSOLENT MUSHROOM!"
                    hide kingProc
                    x "Uh sure..."
                    "Both of the contestants pull out nerf guns."
                    "The police officer and King Samson II take 10 steps out. When it's time to turn and shoot, the police officer fires his nerf gun before Samson."
                    "King collapses."
                    show kingDefault
                    k "But alas! Your young and mighty king has failed. This is the start to the downfall of our kingdom..."
                    k "Please, leave me here to die. Go before he catches you as well."
                    hide kingDefault
                    p "Uh...aight then lmao bruhhh x"
                    "You leave...you guess."
                    "As you leave you notice Samson get up and follow you."
                    jump endKingDate1
            label leaveCart:
                show kingProc
                k "Ah. I admire your refrainment (is that a word lol) from pursuing this holy cart. It brings out your kind and gentle character."
                k "However, I plan to take you somewhere that requires using transportation, and I lack an automobile."
                hide kingProc
                menu:
                    "Drive shopping cart onto the freeway.":
                        jump driveCart
                    "Take the bus like a normal person.":
                        jump driveBus
                label driveCart:
                    "You somehow drive the shopping cart onto the freeway??"
                    #police default
                    "However, a police officer stops you, as you were driving way under the speed limit."
                    x "I'm sorry, it's rush hour."
                    "You and King Samson II reluctantly push the shopping cart back to where they came from."
                    jump endKingDate1
                label driveBus:
                    scene busStop
                    "You and King Samson II wait for a public bus."
                    #white van sprite
                    "Instead, a white van with tinted windows stops in front of you."
                    "The sign 'Public Bus' is written in sharpie on a piece of college ruled binder paper and taped to the van."
                    menu:
                        "Get in the suspicious van.":
                            jump insideVan
                        "Do not get in the suspicious van.":
                            jump outsideVan
                    label insideVan:
                        "You both get into the van like idiots, unaware of what's to come."
                        show kingProc
                        k "To the Shakesperean Museum we go!"
                        hide kingProc
                        #police officer default
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
            scene homeDepot
            "You go inside Hum DëpÔté."
            show kingDefault
            k "Feast your eyes on the best construction products in the world."
            hide kingDefault
            p "Wow. This is wicked awesome-sauce. I can't wait to shop here."
            "You look around the store."
            "What would you like to buy?"
            menu:
                "Paint.":
                    jump paint
                "Sinks.":
                    jump sinks
            label paint:
                scene paintAisle
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
                    show kingDefault
                    k "Rally? Yellow paint? I prefer purple."
                    p "How come?"
                    k "Purple paint tastes better..."
                    hide kingDefault
                    p " You {i} eat {/i} paint???"
                    show kingShocked
                    k " Don't be daft! I drink it!"
                    hide kingShocked
                    "You are not in the mood to see that today."
                    p "....Okay.... Let's go look at the sinks instead."
                    jump sink
                label orange:
                    p "Let's go look at the orange paint."
                    show kingShocked
                    k "Really? Orange paint? What obtuse taste...I prefer the purple."
                    hide kingShocked
                    p "How come?"
                    show kingDefault
                    k "The purple paint here tastes better."
                    hide kingDefault
                    p "You {i} eat {/i} paint???"
                    show kingBlush
                    "He starts to chuckle nervously."
                    k "NO!!!!! That would be weird..."
                    hide kingBlush
                    p "Okaaaaaaay....Let's go look at the sinks."
                    jump sink
                label purple:
                    p "Let's go look at the purple paint."
                    show kingChuckle
                    k "Excellent! I love paint."
                    hide kingChuckle
                    "You hear a popping sound."
                    "You turn around, and see King Samson II has opened a can of purple paint and..."
                    "..!"
                    "He is furiously shoving handfuls of paint into his mouth."
                    p "Are you {i} eating {/i} paint???"
                    show kingProc
                    k "Yes. Paint has fiber, and everyone knows fiber is filled with nutrients."
                    hide kingProc
                    menu:
                        "Can I try some?":
                            jump goToSink
                        "Ew. Weirdo.":
                            jump goToSink2
                    label goToSink:
                        show kingSlimy
                        k "Sure!"
                        hide kingSlimy
                        "You try some purple paint."
                        p "Not bad."
                        show kingProc
                        k "Let's go look at the sinks!"
                        hide kingProc
                        p "Okay!"
                        jump sinks
                    label goToSink2:
                        show kingAngry
                        k "wELL exCuUUuUuUuUUUse me if my tastebuds are more refined."
                        hide kingAngry
                        p "Whatever. Let's go look at sinks."
                        jump sinks
            label sinks:
                scene sinkAisle
                "You walk over to a row of sinks."
                "After several minutes, you find a sink that you like."
                p "This sink is the bees knees! I hope it works."
                "You ask the store manager to learn more about this fabulous product."
                s "Well, this sink is the finest on the market. It's stainless steel and has a pull down faucet."
                show kingShocked
                k "Stainless steel? How horrendous! In my kingdom, all my sinks are made of titanium. Stainless steel is for peasants."
                hide kingShocked
                s "I assure you, this sink is very practical for both peasants and kings. It costs seven hundred dollars."
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
                    show kingDefault
                    k "Oh. *nervous laughter* That is so comical. I must have left my wallet at home."
                    hide kingDefault
                    "The manager leaves."
                    "Suddenly, you get a brilliant idea...to steal the sink."
                    show kingDefault
                    k "What are you doing?"
                    p "I am stealing the sink."
                    hide kingDefault
                    "You grab the sink and rip it off the counter."
                    "Alams start ringing. Beep Beep Beep..."
                    show kingShocked
                    k "Crap on a cracker! Let's run!!!"
                    hide kingShocked
                    p "Aight bruh."
                    "King Samson II starts leaping towards the exit. You trail behind him, dragging the sink."
                    "BeEp! BeeEEP! beePP! Beep!"
                    "In your struggle to steal the sink, you trip and fall."
                    p "Oh no!"
                    "The cops arrive on scene and surround both you and King Samson."
                    x "Is there a problem here?"
                    show kingProc
                    k "Yes! This person here is stealing the sink!!!"
                    p "Hey!"
                    k "Yup! I was a witness to this horrific crime. I saw them run away with this sink."
                    "King Samson turns to you."
                    k "Shame on you! Some people..."
                    hide kingProc
                    show kingSlimy
                    k "This would never happen in my kingdom."
                    hide kingSlimy
                    x "Alright. We have all the evidence we need. Let's go."
                    p "{i} I knew I should've memorized my rights in government class..."
                    "Policeman One takes you to jail."
                    jump altEndKingDate1
                label buySink:
                    s "Wonderful! Head over to the cashier and we'll help you from there."
                    p "Great!"
                    "You pick up the sink with one arm and put it into a shopping cart. You make your way towards the cashier."
                    show kingDefault
                    k "Humph...I disapprove of your purchase. I bet this sink won't last a day. It probably leaks..."
                    hide kingDefault
                    p "Don't be ridiculous. Why would anyone sell a leaking sink."
                    "Miraculously, you notice that the sink has started leaking!"
                    k "I told you so."
                    show kingDefault
                    "King Samson II sighs wistfully."
                    hide kingDefault
                    k "It's so hard being right all the time."
                    menu:
                        "You still want to buy the sink.":
                            jump stillBuy
                        "Froget this! You don't want to buy broken kitchenware!":
                            jump forget
                    label stillBuy:
                        p "I don't care! I'm buying this sink whether you like it or not!"
                        "You pay for the sink, and leave the store with it."
                        scene blackTransition
                        "While walking hhome, a rabid skunk bites you in the shin. You drop the sink and it breaks. You've had enough for the day and leave it be."
                        jump endKingDate1
                    label forget:
                        p "This is nutters! Why is this sink leaking?"
                        p "I refuse to buy this!"
                        scene blackTransition
                        "You leave the store, sinkless."
                        jump endKingDate1
    label endKingDate1:
        scene hallway
        "King Samson II walks you back to your dorm."
        show kingBlush
        k "Good night my fare carbon based life form."
        " He pats your shoulder and kisses your foot."
        hide kingBlush
        scene blackTransition
        "You're a little weirded out, but you're too tired to care. You turn into your dorm for the night."
        jump endOfMandDates
    label altEndKingDate1:
        scene jailHouse
        "You spend one night in jail."
        #police officer default
        x "Alright. Today's your lucky day. You're being released on account of good behaviour."
        "You run out of your cell, and hurry back to your dorm room."
        scene blackTransition
        jump endOfMandDates
    label endOfMandDates:
        scene blackTransition
        "A week passes..."
        "One day during lunch..."
        scene cafeteria
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
            show emoDefault
            e "r-rawr... hey cutie >///> i-if you're not doing anything later...m-ayBee u would wanna hang out with me today? XD"
            hide emoDefault
            "xX_DarkRaven496283_Xx leaps away, hiding his frog face with his fringe along the way."
            "Maybe you should meet up with him after class..."
            scene blackTransition
            jump emoDate2
        label marvinApproach:
            show mDefault
            m "Hey there you little pumpkin. I have a special date planned for us today. Do you wanna go or not? You don't have to...unless...Hiss HIss"
            hide mDefault
            "Marvin leaps away leaving you wondering about the date."
            "Maybe you should meet up with him after class..."
            scene blackTransition
            jump marvinDate2
        label kingApproach:
            show kingDefault
            k "GOOD AFTERNOON MY HIGHNESS TO BE. ARE YOU BUSY TODAY? IF NOT PLEASE MEET WITH ME WHEN YOU ARE FREE."
            hide kingDefault
            "King Samson II leaps away, pushing people aside in the process."
            "Maybe you should meet with him later..."
            scene blackTransition
            jump kingDate2
    label kingDate2:
        "You agree to meet up with King Samson II."
        "Instead of seeing him after class though, you receive a text message."
        show kingDefault
        k "Greetings Big Momma 47. I have arranged for a date for the two of us today. Your carriage is waiting near the school entrance to escort you."
        hide kingDefault
        menu:
            "Big Momma 47???":
                jump bigMomma
            "How did you get this number???":
                jump stalkerPhone
        label bigMomma:
            show kingChuckle
            k "Oh I apologize my beautiful toad princess. Would you like me to refer to you as something else?"
            hide kingChuckle
            p "{i} I just don't want him to refer to me at all at this point...{/i}"
            show kingDefault
            k "My beautiful toad royalty! I regret to interrupt your internal monologue but the chauffeur is waiting for you!"
            hide kingDefault
            p "{i}....??{/i}"
            "You should get ready for your date..."
            scene blackTransition
            jump startKingDate2
        label stalkerPhone:
            show kingChuckle
            k "Don't be silly honey. You gave it to me! Well kind of. Private investigators can do quite a bit if you pay them enough."
            hide kingChuckle
            "It seems King Samson II has done some research on you..."
            scene blackTransition
            "Anyhow, you need to get ready for your date."
            jump startKingDate2
    label startKingDate2:
        scene blackTransition
        "You get ready for your date with King Samson II in the bathroom and make your way outside to your supposed chauffeur."
        scene uniCampus
        "...It seems he is taking you out in a stolen shopping cart."
        p "{i} Why does this feel stangely familiar...{/i}"
        "King Samson II perks up when he sees you."
        show kingSlimy
        "He slicks back his frog head with his own frog saliva."
        k "Good day to you...Have you eaten yet?"
        hide kingSlimy
        "How do you respond?"
        menu:
            "Say 'No I haven't.'":
                jump noEat
            "Say 'No I haven't' but with an unecessary snarky comment.":
                jump youreAnAsshole
        label noEat:
            p "No I have not."
            show kingBlush
            k "Good, you have conserved your appetite in anticipation of our date. How considerate of you...I may consider you for a marriage candidate."
            hide kingBlush
            p "{i}....{/i}"
            jump startStartKingDate2
        label youreAnAsshole:
            p "...I haven't but after seeing you slick back your own head with saliva I have no appetite."
            show kingChuckle
            "King Samson II feigns hurt before chuckling heartily."
            k " *chuckles heartily* "
            hide kingChuckle
            show kingBlush
            k "You're kind of cute when you're trying to act insulting. *chuckles heartily some more, throwing some snorts in here and there."
            hide kingBlush
            p "{i} I am holding back from kicking him in the shin {/i}"
            scene blackTransition
            jump startStartKingDate2
    label startStartKingDate2:
        "And so your date with King Samson II begins..."
        show kingDefault
        k "I have reservations for us at the classiest dining restaurant in town."
        hide kingDefault
        "King Samson II makes you push him int he shopping cart, giving you directions along the way..."
        scene dinerOutside
        "You arrive in front of your destination: Demmy's Diner."
        menu:
            "You call THIS fine dining??? Demmy's Diner?":
                jump pickyFineDining
            "I'm so excited! I've always wanted to eat at Demmy's Diner!":
                jump loveDemmys
        label pickyFineDining:
            "You complain about King Samson II's restaurant choice."
            show kingShocked
            k "You have a broken palette. Demmy's Diner has the finest chimichangas in the world. It is very disappointing that you are so ungrateful."
            hide kingShocked
            "King Samson II's face has started to turn red. He begins to resemble an angry toad. Just the slightest big."
            show kingAngry
            k " You know, I feel like you are not putting enough effort into this relationship...It feels quite one sided, don't you think?"
            "He seems really angry with you..."
            hide kingAngry
            "You ignore him."
            #hostess default
            h "Table for two, first name King...last name Samson?"
            "King Samson's mood instantly changes."
            "..."
            "You suspect he has some issues."
            show kingSlimy
            k "That's us! This way honey."
            hide kingSlimy
            scene blackTransition
            "King Samson II holds the door open for you like the gentlfrog he is, and he leads the way."
            jump demmysStart
        label loveDemmys:
            "You express your lifelong dream of dining at Demmy's diner to King Samson II."
            show kingDefault
            k "Wow, you really are a piece of work, huh? You've never eaten here before???"
            hide kingDefault
            p "{i} Wow, what a jerk... {/i}"
            "King Samson II takes no notice of your insulted feelings, and starts blabbering about chimichangas."
            show kingProc
            k "Their chimichangas are the best!"
            hide kingProc
            #hostess default
            h "Table for two, first name King...last name Samson?"
            jump demmysStart
    label demmysStart:
        scene dinerInside
        "you are led to a table in the back of the diner."
        "King Samson II immediately starts pasting napkins onto his slimy skin (since he can't tuck a napkin into his shirt like a regular person...cause he's a frog)"
        show kingProc
        k "WAITER! BRING ME TWO GLASSES OF YOUR FINEST WINE."
        hide kingProc
        #hostess default, other side
        h "Sir, I am so sorry, but we do not serve wine here. We are a family friendly resturant. Can I interest you in some orange juice?"
        show kingDefault
        k "...fine."
        hide kingDefault
        show kingProc
        k "BUT GIVE ME TWO PLATES OF YOUR FINEST CHIMICHANGAS ALONG WITH IT."
        hide kingProc
        #hostess default
        h "Sir w don't serve chimichangas here. We are a classic American diner...can I interest you in some pancakes?"
        "King Samson II starts to throw a fit."
        show kingAngry
        k "but I WANTED chimichangas..."
        k "I CAME HERE JUST FOR THE DARN CHIMICHANGAS!!!"
        hide kingAngry
        #hostess default
        h "Sir I'm not sure what to tell you...the cooks most likely don't even know what those are."
        "The situation seems to be heating up. Do you want to defuse the situation???"
        menu:
            "interject":
                jump interject
            "Watch the situation unfold":
                jump dontInterject
        label interject:
            "You decide to interject before Samson decides to do anything too rash."
            p "Hey King Samson II...It's fine... we can eat something else right??"
            "The worker looks at you graciously..."
            "King Samson II does some breathing excercises to calm down, giving the hostess one last dirty look."
            show kingProc
            k "You're lucky my beautiful partner is here to hold me back. Or else you would have been sorry!"
            hide kingProc
            jump endKingDate2
        label dontInterject:
            "King Samson II continues to yell at the hostess."
            show kingAngry
            k "GIVE ME SOME DAM CHIMICHANGAS WRITE NOW!!! (btw i put write instead of right for comedic purposes please do not complain about it not being the 'right right' )"
            hide kingAngry
            "The hostess has no choice but to order the cooks to make some chimichangas."
            "..."
            #hostess default
            h "Here are your chimichangas...."
            "The hostess walks away, muttering to herself."
            #hostess default
            h "*muttering* I knew I should've taken the later shift."
            show kingAngry
            k "Ah, yes. Finally some good darn food."
            "..."
            "He starts to chow down all the chimichangas, including your portion."
            hide kingAngry
            show kingBelch
            k "*belches loudly*"
            hide kingBelch
            show kingDefault
            k "That was really good, wouldn't you say so?"
            hide kingDefault
            menu:
                "bruh moment.":
                    jump postChimi
                "Yeah. of course.":
                    jump postChimi
            label postChimi:
                show kingDefault
                k "I'm glad you think so too, honey."
                k "...."
                hide kingDefault
                show kingBlush
                k "Oh dear..."
                hide kingBlush
                "King Samson II suddenly gets up and rushes to the bathroom."
                show kingProc
                k "Leave without me! I have some complications I must address."
                hide kingProc
                jump endKingDate2
    label endKingDate2:
        scene blackTransition
        "You end up walking back to your dorm by yourself."
        p "{i} I hope he's okay...{/i}"
        jump postAllSecondDates
    label emoDate2:
        scene blackTransition
        "You meet up with xX_DarkRaven496283_Xx later."
        show emoBlush
        e " w-wow you actually said yeah 0///0 y-you're the only one that ever cares..."
        hide emoBlush
        "xX_DarkRaven496283_Xx hides his blush behind his fringe."
        show emoDefault
        e "a-anyways lets get going... u-uwu... i bought us ticket$ 2 da MBR concert..."
        e "do you like them? "
        hide emoDefault
        menu:
            "YES omg i LOVE MBR.":
                jump noYouDont
            "No sorry... who are they?":
                jump noMBR
        label noYouDont:
            show emoDefault
            "xX_DarkRaven496283_Xx seems unimpressed."
            e " -__- they're pwetty indie so i didn't think u would kno them...are u sure ur not lying 2 me? lol...no need 2 try and impres me..."
            hide emoDefault
            "..."
            jump startEmoDate2
        label noMBR:
            show emoAngry
            "xX_DarkRaven496283_Xx seems offended."
            e "omgzzz you dun kno who they arrrr??? youre out of the looop ... they r the hottest rawk band out their write nao... XD"
            hide emoAngry
            "..."
            jump startEmoDate2
    label startEmoDate2:
        scene blackTransition
        "You and xX_DarkRaven496283_Xx arrive at the My Biological Romance concert together."
        scene concert
        e "rrrrrrrrrraaaaaaaawwwwwwwwrrrrr XD where heer."
        menu:
            "Go closer to the stage.":
                jump moshPit
            "Stay near the balcony.":
                jump balcony
        label balcony:
            "You and xX_DarkRaven496283_Xx walk towards the balcony."
            "My Biological Romance walks onto the stage."
            scene concertCrowd
            "The crowd goes wild. The people around you start to scream. People are clapping, and you see seme fans pull their hair out from excitement."
            "You feel this is all getting a little two hectic."
            p "I want to go outside and get some fresh air."
            show emoDefault
            e "...wha? but the concert just started..."
            hide emoDefault
            "You ignore xX_DarkRaven496283_Xx and start heading outside. On your way own from the balcony, xX_DarkRaven496283_Xx trips!"
            "When you turn around, Froggy Frogerson over here is in tears. Again!"
            p "{i} This guy is such a wimp. but not because he is a guy and crying, because the developers do not condone toxic masculinity and traditional gender roles. it is because he has cried in every interaction with you.{/i}"
            show emoCry
            e "...me thinks i broke me wrist..."
            hide emoCry
            scene concertOutside
            "You drag xX_DarkRaven496283_Xx outside, by the wrist, because you're kind of an Basshole."
            p "Much better. It's so much quieter out here."
            "You turn around and see xX_DarkRaven496283_Xx holding his limp wrist. It doesn't even look like he hurt it. Actually you're not even sure that he tripped..."
            show emoCry
            e "i think i need to go to the hospital."
            hide emoCry
            menu:
                "No, you're fine.":
                    jump noHospital
                "Yeah, you're right.":
                    jump hospital
            label noHospital:
                show emoSad
                e "you s-sure?...it weally hurts..."
                hide emoSad
                p "Yeahhhh you're fine..."
                "You give xX_DarkRaven496283_Xx's wrist a poke. It falls off. Yeah you read that right. Like as in his entire wrist just falls off."
                "A rabid skunk crawls over, grabs the wrist, and then sprints away."
                "At this point, xX_DarkRaven496283_Xx starts sobbing like there is no tomorrow."
                show emoCry
                e "my wrist...gone....we have to go after it."
                hide emoCry
                p "No. Heck no. I am NOT about to go chasing after your stupid wrist in the middle of the night."
                show emoCry
                e "...pls?"
                hide emoCry
                menu:
                    "Fine. Let's go.":
                        jump chaseSkunk
                    "No.":
                        jump noChase
                label chaseSkunk:
                    scene forest
                    "You begin your manhunt for the skunk."
                    "You check the ground first. You have excellent vision, and notice a trail of wrist pus leading off into the darkness."
                    p "I've found a trail. Let's  follow it."
                    "You follow the trail of wrist pus. It takes you through a forest, and then another forest, and then a third forest. When you leave the woods, you realize you have been walking for three weeks."
                    "Then, suddenly you see the skunk!"
                    p "Over there!"
                    scene forestClearing
                    "You and xX_DarkRaven496283_Xx run over to the skunk."
                    show emoDefault
                    e "..give my wrist back :(((((("
                    hide emoDefault
                    n "*skunk noises*"
                    "developers note: we made an entire new character just for this skunk to say skunk noises. isn't that something?"
                    e "...plz give me my wrist *starts sobbing*"
                    "The skunk cannot understand him. It is a skunk. Instead, it turns around and runs away."
                    p "Whelp, sucks to suck. I guess we better get you to a hospital."
                    scene forest
                    "You go back through the three forests, and go inside your local hospital."
                    #doctor default
                    d "Well well well. You're very lucky to be alive right now."
                    show emoDefault
                    e "....i am?"
                    d "Bruh yes. Your wrist fell off. Another minute and you would have died. Now let's see if we can reattach that wrist."
                    d "...Where is the wrist?"
                    p "We lost it."
                    d "You LOST it? How did - you know what? I don't even want to know."
                    d "In this unique situation, I will install a wooden wrist instead."
                    scene blackTransition
                    "A couple hours later, xX_DarkRaven496283_Xx  has a new, not-shiny furnished wooden wrist."
                    jump endEmoDate2
        label moshPit:
            p "Hey let's go to the mosh pit! It seems like everyone is having fun down there."
            show emoDefault
            e " w-weally? owo we are really meant 4 each other uwu"
            hide emoDefault
            scene concertCrowd
            "You and xX_DarkRaven496283_Xx go to the mosh pit, unaware of what is to come."
            "Y'all start dancing and singing to House of Frogs."
            "You want to show that you are a hardcore concert goer (though you've never been and include yourself in one of the many moshpit stunts."
            menu:
                "Crowd-surf":
                    jump crowdSurf
                "Mosh":
                    jump mosh
            label crowdSurf:
                scene crowdSurf
                "Two randos throw you into the crowd and you start to crowd surf."
                "Someone boops your nose and you feel extremely violated."
                menu:
                    "Sneeze on the finger.":
                        jump sneeze
                    "Bite the finger":
                        jump bite
                label bite:
                    "You bite on the finger."
                    "Turns out, it's your own finger. You couldn't keep track due to all the hands around you."
                    "You get back down on your feet and rub the saliva on someone's shirt."
                    "They seem weirdly grateful..."
                    scene concert
                    "You look for xX_DarkRaven496283_Xx and find him having an epic dance battle with a rando."
                    p "{i}I can't believe what I'm seeing...{/i}"
                    "After xX_DarkRaven496283_Xx finishes breakdancing, you both start dancing."
                    "You lose xX_DarkRaven496283_Xx and start looking for him."
                    #mbr shadow
                    "Someone's back is turned to you. He’s wearing an MBR shirt and a familiar studded belt from Boiling Topic. It looks like xX_DarkRaven496283_Xx but you’re not quite sure."
                    menu:
                        "Say ‘Heyyy xX_DarkRaven496283_Xx.'":
                            jump heyDude
                        "Politely ask if they have seen xX_DarkRaven496283_Xx.":
                            jump askDude
                label sneeze:
                    "You sneeze on the finger like a madlad."
                    "...Turns out it's your own finger. You couldn't keep track due to all the hands around you."
                    "You get back down on your feet and rub the residue on someone's shirt."
                    "..."
                    "They seem weirdly grateful..."
                    scene concert
                    "You realize that you can't find xX_DarkRaven496283_Xx so you start to look for him."
                    #mbr shadow
                    "Someone's back is turned to you. He is wearing an MBR shirt and a familiar studded belt from Boiling Topic. It looks like xX_DarkRaven496283_Xx but you're not sure."
                    menu:
                        "Say Heyyyy xX_DarkRaven496283_Xx.":
                            jump heyDude
                        "Politely ask if they've seen xX_DarkRaven496283_Xx.":
                            jump askDude
                    label heyDude:
                        show mbrGuy
                        "The person turns around. Turns out it's not xX_DarkRaven496283_Xx."
                        "Turns out in his native language, the word 'xX_DarkRaven496283_Xx' is an insult. He looks pissed and storms towards you with his hands clenched."
                        scene concertCrowd
                        "You run away and he starts to chase you. You coincidently run into xX_DarkRaven496283_Xx."
                        hide mbrGuy
                        show emoDefault
                        e "o-owo? what is wrong baybee??"
                        e "{i} * sees the dude storming towards you * {/i}"
                        hide emoDefault
                        show emoAngry
                        e "O.O how daer u run after my senpai? she is MINE XD"
                        e " Watashi no kutsu no nioi o tomeru koto ga dekimasu ka? Watashi wa senjitsu mizutamari ni ashi o fumiireta"
                        hide emoAngry
                        "Unfortunately, you had no idea that xX_DarkRaven496283_Xx  was a weeaboo, let alone understand what it meant."
                        "Fortunately for you, it seems to intimidate the dude, who nervously slinks away."
                        show emoBlush
                        e "*nuzzles* i wil alwayz protecc u."
                        e "i'll be there for you, even when no one will be there for me ^^."
                        hide emoBlush
                        scene blackTransition
                        "You and xX_DarkRaven496283_Xx  safely leave the MBR concert. You're kind of weirded out, but also strangely happy..."
                        jump endEmoDate2
                    label askDude:
                        show mbrGuy
                        "You ask the dude if he has seen someone dressed like xX_DarkRaven496283_Xx."
                        "The dude instead winks at you and asks for your phone number."
                        hide mbrGuy
                        menu:
                            "Give him the number 718-899-6161":
                                jump astrology
                            "Give him the number 604-594-9190.":
                                jump astrology
                        label astrology:
                            show mbrGuy
                            "You give him the number. Turns out that specific set of numbers is an insult in his culture. He looks pissed and storms towards you with his hands clenched."
                            "He doesn't really intimidate you though..."
                            "You punch him and he falls down."
                            hide mbrGuy
                            "xX_DarkRaven496283_Xx  comes leaping towards you."
                            show emoBlush
                            e "m-my pwincess of darkness! that was so cool... :3"
                            hide emoBlush
                            "You and xX_DarkRaven496283_Xx  safely leave the MBR concert You're kinda weirded out, but strangely happy..."
                            scene blackTransition
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
            menu:
                "Take a dose of shrooms.":
                    jump shroom
                "Inhale whatever's inside a suspicious bottle.":
                    jump perfume
            label shroom:
                "You decide to be hardcore and take a dose of shrooms."
                "Turns out they're just crushed Port Ah Bell Ah mushrooms."
                "..."
                "You're a bit disappointed..."
                "You then remember that you are playing a game rated E for everyone, you think..."
                "You realize that you're breaking the fourth wall and promptly forget what you previously thought."
                "You don't really know what to do with the 'shrooms' because you don't like port ah bell ah mushrooms. You like shit-Ah Kay mushrooms."
                menu:
                    "Ditch xX_DarkRaven496283_Xx and become a contestant on Chopped.":
                        jump chopped
                    "Throw the 'shrooms' to the north-east.":
                        jump throwShrooms
                label chopped:
                    scene corporate
                    "You go to the Food Network official building and request permission to become a contestant on Season 15 Episode 4 of Chopped."
                    "Unfortunately, the offical Food Network people declined. You dejectedly walk back the MBR concert."
                    scene concert
                    show emoDefault
                    "You find xX_DarkRaven496283_Xx  in the corner humming to 'The apparition of You' and snapping his disgusting webbed fingers."
                    "You are compelled to join."
                    hide emoDefault
                    scene blackTransition
                    "An hour later, you and xX_DarkRaven496283_Xx  safely leave the MBR concert. You're kind of weirded out, but also strangely happy..."
                    jump endEmoDate2
                label throwShrooms:
                    "You throw the disgusting Port Ah Bell Ah mushrooms to the north-east."
                    show emoDefault
                    "That's where xX_DarkRaven496283_Xx  is standing, who is now humming to 'The Apparition of You' and snapping those webbed fingers, covered in mushrooms."
                    "You're compelled to join."
                    hide emoDefault
                    scene blackTransition
                    "An hour later, you and xX_DarkRaven496283_Xx safely leave the MBR concert. You're kind of weirded out, but also strangely happy..."
                    jump endEmoDate2
            label perfume:
                "You decide to be hardcore and take a huge whiff of the bottle's contents."
                "Turns out it's just a Balsam and Cedar scented perfume. It actually smells really nice and not at all eggy fart."
                "You take another whiff...and start to feel a bit woozy..."
                p "I think this perfume is spiked...where's xX_DarkRaven496283_Xx when you need him???"
                show emoDefault
                e "u-um im rite here :3 i cant help u senpie cuz im allergic to balsam and cedar ... >.<"
                hide emoDefault
                show emoSad
                e "....as well as genuine hap-pee-ness and self-confidence and rainbows and self-appreciation etc."
                hide emoSad
                menu:
                    "Go to the nearest Bath and Booty Works and sample another perfume to get rid of the balsam and cedar scent emitting from your clothes.":
                        jump bathAndBody
                    "Leave.":
                        jump leaveConcert
                label bathAndBody:
                    scene bathAndBooty
                    "You go to the nearest Bath and Booty Works with xX_DarkRaven496283_Xx."
                    p "Which scent do you want me to wear?"
                    show emoBlush
                    e "hmmm >.< me thinks u would smeel good in Onyx Blade Pitch-Black Metallic Dark Luster."
                    hide emoBlush
                    "Unfortunately the store is out of stock in that scent. You spray a simple Cherry Blossom instead."
                    show emoBlush
                    e "o-owo? what is dis feeling im feeling? O.O"
                    e "it seems 2 bee....luv..."
                    hide emoBlush
                    scene concert
                    "You and the edgelord go back to the My Biological Romance concert."
                    "..."
                    scene blackTransition
                    "An hour later you and xX_DarkRaven496283_Xx  safely leave the MBR Concert."
                    "You're kind of weirded out, but also strangely happy..."
                    jump endEmoDate2
                label leaveConcert:
                    scene concertOutside
                    "You step out of the concert area to get rid of the scent."
                    show kingShadow
                    "While outside, you see King Samson II checking out pumpkins in front of K-Fart."
                    "You go over to say hi."
                    hide kingShadow
                    show kingDefault
                    k "My my what a pleasant surprise! I did not plan on encountering you on this fine night!"
                    k "And is that Balsam and Cedar?"
                    hide kingDefault
                    k " *shivers* "
                    show kingBlush
                    k "It's as if we were meant to be!"
                    hide kingBlush
                    "Unfortunately xX_DarkRaven496283_Xx  arrives just then."
                    show emoDefault
                    e "O.O how dare you run after my sen pie!!! she is MINE XD"
                    hide emoDefault
                    show emoAngry
                    e "Watashi no kutsu no nioi o tomeru koto ga dekimasu ka? Watashi wa senjitsu mizutamari ni ashi o fumiireta"
                    hide emoAngry
                    "Unfortunately, you had no idea that xX_DarkRaven496283_Xx was a weeaboo, let alone undersood what that meant."
                    "Fortunately it seems to intimidate King Samson II, who nervously hops away."
                    show emoBlush
                    e " *nuzzles* i will always protecc you"
                    e "i will be there 4 u ... even when no one will be there for me ... ^_^"
                    hide emoBlush
                    "..."
                    scene blackTransition
                    "You and xX_DarkRaven496283_Xx safely leave the MBR concert. You're kind of weirded out, but also strangely happy...."
                    jump endEmoDate2
        label down:
            "You duck."
            "When you stand back up, you see a stranger at the bar twitching his finger awkwardly."
            "..."
            "It seems he is beckoning you to join him."
            "You're compelled, so you go towards him."
            show mbrGuy
            a "Hey bby. Can I get you a drink?"
            menu:
                "Heckity heck yeah, free drinks!":
                    jump alcohol
                "Uhhhhh no thanks.":
                    jump zodiac
            label alcohol:
                show mbrGuy
                a " oh bar ten der! Can we get two alcohol pwetty pwease?"
                hide mbrGuy
                "The bartender comes back with mineral water on the rocks."
                a "So what's a doll like you doin here all alone?"
                p "Uh actually I’m on a date with xX_DarkRaven496283_Xx."
                show mbrGuy
                a "Sounds fake."
                hide mbrGuy
                show emoDefault
                e " LOL XD are you saying i'm non-existent?"
                hide emoDefault
                show emoSad
                e "becuz i wish u were right..."
                hide emoSad
                show mbrGuy
                a "Wow, I didn't know you were actually on a date with someone. Thanks for leading me on."
                hide mbrGuy
                "The rando leaves haughtily with mineral water."
                show emoDefault
                e "i-im sowwy for ruining ur convo. i always ruin everything..."
                hide emoDefault
                p "bruh you good?"
                "..."
                scene blackTransition
                "You and xX_DarkRaven496283_Xx  start dancing."
                "An hour later, you and xX_DarkRaven496283_Xx  safely leave the MBR concert. You are kind of weirded out, but also strangely happy..."
                jump endEmoDate2
            label zodiac:
                show mbrGuy
                a "Alright baby dog, Can I at least know your star sign? BBY?"
                hide mbrGuy
                menu:
                    "Scorpio":
                        jump scorpio
                    "Sagittarius.":
                        jump sagittarius
                label scorpio:
                    show mbrGuy
                    a "OOOoOOo a fiesty scorpion. Me likely!"
                    hide mbrGuy
                    show emoAngry
                    e " *storms over* "
                    hide emoAngry
                    show emoDefault
                    e "I ponder of something great My lungs will fill and then deflate They fill with fire, exhale desire I know it's dire my time today I have these thoughts, so often I ought To replace that slot with what I once bought 'Cause somebody stole my car radio And now I just sit in silence"
                    "Developers note: Just a disclaimer, do not sue us. more importantly, I am not a 21p fan. i am not in 8th grade anymore."
                    e "- Twenty One Pilots"
                    hide emoDefault
                    "The rando seems intimidated by these wise words, and scrambles away."
                    show emoSad
                    e "i-im sowwy for ruining your convo...i always ruin everything..."
                    hide emoSad
                    p "Bruh you good??"
                    "..."
                    scene blackTransition
                    "You and  xX_DarkRaven496283_Xx  start dancing."
                    "An hour later you and  xX_DarkRaven496283_Xx  safely leave the MBR concert. You're kinda weirded out, but also strangely happy..."
                    jump endEmoDate2
                label sagittarius:
                    show mbrGuy
                    a "Gosh darn I would love to hang out with a hot centaur such as yourself, but unfortunately we aren't compatible. I'm sorry darlin. "
                    hide mbrGuy
                    " xX_DarkRaven496283_Xx storms over."
                    show emoAngry
                    e "h-ow dare you mr rando :("
                    hide emoAngry
                    "The rando just grumbles in disgust and leaves."
                    show emoDefault
                    e "i-im sowwy for ruining your convo...i always ruin everything..."
                    hide emoDefault
                    p "Bruh you good??"
                    "..."
                    scene blackTransition
                    "You and  xX_DarkRaven496283_Xx  start dancing."
                    "An hour later you and  xX_DarkRaven496283_Xx  safely leave the MBR concert. You're kinda weirded out, but also strangely happy..."
                    jump endEmoDate2
    label endEmoDate2:
        "You go back to your dorm after your date."
        jump postAllSecondDates
    label marvinDate2:
        "You agree to Marvin's date."
        "He tells you to meet at his house..."
        scene blackTransition
        "..."
        scene door
        "After school you go to Marvin's house for your date."
        "You ring the doorbell."
        "Marvin opens the door...He looks upset."
        show mSad
        m "Hey there momma goose... Come on in."
        m "I am so sorry! I had a very romantic evening planned at the train station, but one of my tadpoles got sick. I have to tadpole-sit because Helen can't make it."
        hide mSad
        show mDefault
        m "Would you like to join me?"
        "You feel kind of bad..."
        hide mDefault
        p "Yes, of course I will."
        scene livingRoom
        "You make your way into Marvin's living room. A sickly looking tadpole is lying on the couch."
        show mDefault
        m "This is Little Suzie."
        hide mDefault
        show suzieDefault
        l "..."
        hide suzieDefault
        show suzieHiss
        l "HIIIISSSSS."
        hide suzieHiss
        p "{i}She takes after her father...{/i}"
        show mDefault
        m "I think to cheer Little Suz up, we should play a board game."
        m "What board game should we play?"
        hide mDefault
        menu:
            "Scrabble":
                jump scrabble
            "The Game of Life":
                jump gameOfLife
            "Monopoly":
                jump monopoly
        label scrabble:
            show suzieHiss
            l "HISSSSS That one is my favourite!"
            hide suzieHiss
            scene blackTransition
            "You play a couple rounds of Scrabble. After about an hour, Little SUzie is looking considerably happier."
            jump continue
        label gameOfLife:
            show suzieHiss
            l "HISSSS That one is my favourite!"
            hide suzieHiss
            scene blackTransition
            "You play a couple rounds of Game of Life. After about an hour, Little Suzie is looking considerably happier."
            jump continue
        label monopoly:
            show suzieHiss
            l "HISSSSS That one is my favourite!"
            hide suzieHiss
            scene blackTransition
            "You play a couple rounds of Monopoly. After about an hour, Little Suzie is looking considerably happier."
            jump continue
    label continue:
        show suzieDefault
        l "I am feeling so much better! hiss hiss can I go outside and play?"
        hide suzieDefault
        show mDefault
        m "Sure, kiddo."
        hide mDefault
        "Little Suzie crawls out of the house."
        show mDefault
        m "Alright, now that Suzie is gone, what would you like to do?"
        m "..."
        m "actually..."
        hide mDefault
        show mWink
        m "You can help me clean the house. Helen always gets so annoyed when it is dirty."
        hide mWink
        menu:
            "Yeah! I'd love to help you clean.":
                jump clean
            "No thanks...let's do something else.":
                jump noClean
        label clean:
            show mDefault
            m "Woohoo! Thank God you said yes. This house is a complete dump."
            hide mDefault
            "What do you want to do first?"
            menu:
                "Clean the shelves.":
                    jump shelves
                "Dust.":
                    jump dust
            label shelves:
                scene kitchen
                "You go to the kitchen and open the first shelf."
                "Inside, there is a half eaten sandwich, an old sock, and a bag of cheerios. What a mess!"
                p "This is gonna take some time."
                scene blackTransition
                "Three hours later and you've finished cleaing the shelves. They are organized by product, alphabetically."
                "You are pretty proud of yourself, but you want to do even more to help Marvin..for some reason."
                "When you look around Marvin's house, you notice every visible surface is covered in a thick layer of dust."
                "You grab a fluffy pink duster, and get to work."
                "An hour later, Marvin's house is dust-free, but you want to do some more housework."
                jump vacuum
            label dust:
                scene livingRoom
                "You look around Marvin's house. You notice every visible surface is covered in a thick layer of dust."
                "You grab a fluffy, pink duster and get to work."
                "An hour later, Marvin's house is dust-free, but you want to do some more housework."
                "You go to the kitchen and open the first shelf."
                "Inside, there is a half eaten sandwich, an old sock, and a bag of cheerios. What a mess!"
                p "This is gonna take some time."
                scene blackTransition
                "Three hours later, and you've finished cleaning the shelves. They are organized by product, alphabetically."
                "You are pretty proud of yourself, but you want to do even more to help Marvin."
                jump vacuum
        label noClean:
            show mDefault
            m "Okay. How about we have dinner?"
            hide mDefault
            p "That would be great."
            show mHiss
            m "Okay! Here, let me call Helen and she whip something up real quick."
            hide mHiss
            "Marvin has Helen on speed dial. He calls her. Five minutes later, she comees to Marvin house."
            show helen
            q "Greetings, Marvin."
            "..."
            "Helen turns to you."
            q "And you are...his date?"
            p "Yeah."
            q "Excellent. Now, I'll just mosey down to the kitchen and make some dinner."
            hide helen
            scene blackTransition
            "..."
            "Half an hour later, Helen brings out two steaming plates of lemons. Not like sliced or anything. Just legit like whole lemons, steaming from their lemon pores."
            menu:
                "This looks appetizing!":
                    jump yum
                "Lemon? Are you kidding me?!":
                    jump ick
            label yum:
                show helen
                q "Many thanks!"
                hide helen
                p "This tastes amazing! I can't thank you enough."
                show mGross
                "Marvin looks like he wants to throw up."
                m "Yeah... *muttering* I hate lemon..."
                hide mGross
                "Helen leaves the room and you finish eating the tasty lemon."
                "Marvin goes into the kitchen to get something else to eat because apparently steaming lemon is not deserving of three Michelle Lin stars."
                "He comes out holding an onion and blue paint."
                show mWink
                m "mMMmMmMmmm This is amaze-balls."
                "you watch Marvin bite into the onion and drink some paint."
                p "Is that healthy?"
                m "*chewing noisily* Beats me. Probably not."
                hide mWink
                p "okaay. This has been...fun... but I think I'm going to go now. Tell the tadpoles I said hello."
                scene blackTransition
                "You leave Marvin's house."
                jump endMarvinDateTwo
            label ick:
                p "I hate sour food."
                show mDefault
                m "Yeah! Let's get something else to eat."
                hide mDefault
                "Helen storms out of the house."
                "You take the lemons and throw the in the trash. When you turn around, Marvin hands you a raw onion and a can of blue paint."
                p "What is this??"
                show mBlush
                m "Your dinner!"
                hide mBlush
                menu:
                    "Gross! I am not eating this.":
                        jump ickAgain
                    "Neat. Yummy.":
                        jump yummy
                label ickAgain:
                    show mHiss
                    m "Fine!"
                    hide mHiss
                    "Marvin pours paint onto the onion and starts to furiously chow it down."
                    "..."
                    scene blackTransition
                    "You stand there awkwardly for five minutes before leaving his house."
                    jump endMarvinDateTwo
                label yummy:
                    "You eat the onion and the paint. It tastes funky... don't know why though."
                    p "Thanks."
                    "You turn around, and discover that Marvin has fallen asleep {i} again {/i} at the kitchen table."
                    scene blackTransition
                    "You stand there awkwardly for five minutes, and then leave Marvin's house."
                    jump endMarvinDateTwo
    label vacuum:
        "You pick up Marvin's vacuum, the Oreck XL2100RHS 12 Lightweight Upright Bagged Vacuum Cleaner."
        "You start to vacuum. It makes a loud choking noise, but starts working."
        "..."
        "You continue to vacuum, while Marvin settles back on the couch with {i} The Old York Times {/i}"
        "Three hours later, the floor is shining and spotless. Marvin has fallen asleep on the couch."
        p "{i} What kind of date is this?? He fell asleep!{/i}"
        p "{i} I kind of feel like kicking him in the shin...or maybe yelling at his face to wake him up...{/i}"
        menu:
            "Kick Marvin really hard in the shin to wake him up.":
                jump marvinWakes
            "Yell in Marvin's face to wake him up.":
                jump marvinWakes
        label marvinWakes:
            "Marvin wakes up!"
            show mHiss
            m "HISSSSSSS!??? What happened??"
            hide mHiss
            p "You fell asleep! While I was cleaning too...!"
            show mDefault
            m "Did I? Darn Double D's! Here, I'll make it up to you! We can have a nice outing with Helen and the kids. Tonight. What do you say?"
            hide mDefault
            p "I don't want to have dinner with your ex-wife! I'm out of here. I'm bouncing."
            scene blackTransition
            "You bounce out of Marvin's house."
            jump endMarvinDateTwo
    label endMarvinDateTwo:
        scene hallway
        "You end up at your dorm. You turn in for the night."
        jump postAllSecondDates
    label postAllSecondDates:
        scene blackTransition
        "A few weeks pass..."
        "It is Februrary now..."
        "Valentine's day is coming up."
        "..."
        "You need to head to class."
        "..."
        scene classroom
        "In zoology class."
        "You take your usual seat next to xX_DarkRaven496283_Xx."
        "He turns to you"
        show emoDefault
        e "u-uwu...hey"
        hide emoDefault
        menu:
            "Hey xX_DarkRaven496283_Xx.":
                jump heyDarkRaven
            "What is it this time.":
                jump rudeBinch
        label rudeBinch:
            show emoSad
            e "w-why are u so mean 2 me :("
            hide emoSad
            p " {i} Is he going to start crying again...Here we go again..."
            "You scramble to make xX_DarkRaven496283_Xx feel better, but he cuts you off."
            show emoDefault
            e "haha XD i kno u dun weally mean it bee cuz u luv me <3 ^_^."
            hide emoDefault
            p " {i} ...{/i} "
            "You hold back from kicking him in the shin."
            jump continueDarkRavenV
        label heyDarkRaven:
            show emoDefault
            e "w-what a bland answer... >:("
            hide emoDefault
            "You hold back from kicking him in the shin."
            jump continueDarkRavenV
    label continueDarkRavenV:
        show emoDefault
        e "a-anyways...uwu...uh..."
        hide emoDefault
        show emoBlush
        e " uh... >///<"
        hide emoBlush
        menu:
            "Hurry it up bucko.":
                jump hurryBucko
            "...yes?":
                jump dotDotYes
        label hurryBucko:
            show emoSad
            e "w-why are you so rood :((((("
            hide emoSad
            "xX_DarkRaven496283_Xx looks flustered."
            "You feel like a jerk."
            jump continueContinueDarkRavenV
        label dotDotYes:
            show emoBlush
            e "u-uh >///< "
            hide emoBlush
            "You seem to have made him even more nervous."
            jump continueContinueDarkRavenV
    label continueContinueDarkRavenV:
        show emoBlush
        e "u-uh..."
        e "u-uwu"
        e " >///< wait don't look @ meee"
        " You turn away from xX_DarkRaven496283_Xx at his request."
        e "a-are yew doo-ing anyting o-on valentines day? O////O"
        hide emoBlush
        "It seems that xX_DarkRaven496283_Xx wants to spend Valentine's Day with you."
        "Maybe you should spend the holiday with him..."
        show emoDefault
        e "a-anyways.... it's thiz coming fry day so i'll wait 4 u after class u-uwu..."
        hide emoDefault
        "xX_DarkRaven496283_Xx runs away."
        "..."
        "Class didn't even properly start yet..."
        jump kingAsks
    label kingAsks:
        "During the lecture..."
        "..."
        " {i} ping! {/i}"
        "It seems you have recieved a text message."
        "..."
        "It's from King Samson the II."
        show kingProc
        k " {i} GREETINGS MY LOVELY PETUNIA. I WOULD LIKE  YOU TO ACCOMPANY ME ON A DATE FOR VALENTINE'S DAY. IF THAT IS OK WITH YOU...."
        hide kingProc
        "You look over at him across the room. King Samson II is pretending he does not see you."
        "What do you text back to him with?"
        menu:
            "Sure! :) ":
                jump sureKing
            " I actually have a date already..":
                jump alreadyDate
        label sureKing:
            " {i} ping! {/i} "
            "King Samson II replies quickly with his speedy frog phalanges."
            show kingDefault
            k "ALRIGHT. I LOOK FORWARD TO IT. NOT THAT I DOUBTED YOU WOULD SAY YES OR ANYTHING. -KING SAMSON II, PHD"
            hide kingDefault
            "It seems you've got yourself a date with King Samson II."
            "..."
            "You focus your attention back on the lecture."
            jump marvinAsks
        label alreadyDate:
            "You look over at him and see that he looks offended."
            "He starts to furiously type."
            " {i} ping! {/i}"
            show kingProc
            k "NONSENSE. I'LL MAKE SURE YOU'RE FREE IF SOMEONE ELSE IS BOTHERING YOU ABOUT A DATE. I LOOK FORWARD TO IT, MY LOVELY LOAF OF WHOLE WHEAT BREAD."
            hide kingProc
            "..."
            "It seems he thinks you two are going on a date no matter what."
            "You focus your attention back on the lecture."
            jump marvinAsks
    label marvinAsks:
        "After your class, you start to walk home."
        "You hear Marvin's disgusting frog feet hopping over to you."
        show mDefault
        m "hEY tHErE Momma Goose!"
        hide mDefault
        "You walk faster to avoid him."
        "Marvin starts hopping towards you faster."
        show mDefault
        m "So... *pants* I was wondering *pants* if  you would *pants* want to *pants* go on a dATE * pants* with me on Valentine's day..."
        hide mDefault
        "Wow the third offer today...aren't you a special little player."
        menu:
            "Walk even faster.":
                jump walkFaster
            "Accept his offer.":
                jump acceptOffer
        label walkFaster:
            "You speed walk away and do your best to ignore Marvin like the jerk that you are."
            "Marvin calls after you in the distance..."
            show mBlush
            m "I assume that's a yes then!"
            hide mBlush
            "..."
            scene blackTransition
            "You head home for the day."
        label acceptOffer:
            "There are other frogs that wanted to spend Valentine's day with you already though..."
            "You actually realize that you don't care, because you're horrible like that."
            p "I'll go with you Marvin! :)"
            "You speed walk away after your quick acceptance."
            "You hear Marvin celebrating in the background."
            jump endVDayOffers
    label endVDayOffers:
        scene blackTransition
        "A few days pass by..."
        "Today is Valentine's day, AKA July 4th."
        "You recall the offers from the three frogs for Valentine's day dates..."
        "Today promises to be an interesting day, almost as if the end of this game is approaching soon."
        jump startVDayMess
    label startVDayMess:
        scene classroom
        "During Zoology classs...which seems like the only class you take..."
        "The three frogs seem to be extremely jittery, but they refuse to talk to you."
        "..."
        "It seems they are all nervous about their dates.."
        "But who will you choose?"
        "..."
        "You start to get a little nervous yourself..."
        jump startStartVDayMess
    label startStartVDayMess:
        "Class ends and you make your way out of the classroom."
        "..."
        scene uniCampus
        p "{i} uh-oh... {/i}"
        "All three frogs are waiting for you by the door."
        show kingProc
        k "AHA THERE IS MY BEAUTIFUL EGGPLANT RESIDUE! ARE YOU READY FOR OUR ROMANTIC EVENING OUT THIS VALENTINE'S DAY? "
        hide kingProc
        show mDefault
        m "..."
        hide mDefault
        show mGross
        m "...You have another date planned? What the damn hell?!"
        hide mGross
        show emoDefault
        e "...w-what is the m-meaning of this :("
        hide emoDefault
        "xX_DarkRaven496283_Xx starts to cry..."
        show kingShocked
        k "Wait...I wasn't the only one...?"
        hide kingShocked
        "All eyes are turned to you right now..."
        show mGross
        m "Have you been seeing other frogs the entire time we've been dating..?"
        hide mGross
        menu:
            "Hanging out a couple of times does not mean dating.":
                jump notDating
            "It's not what it looks like!!!":
                jump cheatingBastard
        label notDating:
            "..."
            show kingDefault
            k "Yeah, what my lovely royalty-to-be said. It is ME who is obviously in the relationship with them!"
            hide kingDefault
            show mGross
            m "What do you MEAN?! *mutters* Just like Helen...Always like Helen..."
            hide mGross
            show emoCry
            e "i-i i thought we had some ding special :((((("
            hide emoCry
            "xX_DarkRaven496283_Xx is crying furiously>.."
            "..."
            jump vDayChoice
        label cheatingBastard:
            "..."
            show mSad
            m "I thought you were something special...I even took you to WallBlues..."
            hide mSad
            show emoCry
            e " *sniff* >:( y-you can't just go on dates with us and t-then go with another f-frog..."
            hide emoCry
            show kingAngry
            "King Samson II remains silent for the first time in his life. He appears to be really angry..."
            hide kingAngry
            "..."
            jump vDayChoice
    label vDayChoice:
        "You're in big trouble now..."
        show mDefault
        m "So which one of us do you REALLY love..."
        hide mDefault
        show emoDefault
        e " :( y-yeah which one do u achilly like..."
        hide emoDefault
        show kingDefault
        k "BE TRUTHFUL THIS TIME."
        hide kingDefault
        "..."
        "You have to choose one of them"
        menu:
            "I love King Samson II.":
                jump loveKing
            "I love xX_DarkRaven496283_Xx.":
                jump loveEmo
            "I love Marvin.":
                jump loveMarvin
        label loveKing:
            show kingSlimy
            k "AHA! I KNEW YOU WOULD CHOOSE ME! *CHUCKLES HEARTILY* "
            hide kingSlimy
            show emoSad
            e "i...i guess i just never meant any ding 2 u.... </3"
            hide emoSad
            show mSad
            m "theyre all the same i guess...."
            hide mSad
            "..."
            "You choose King Samson II over everyone else."
            "..."
            scene blackTransition
            "It's time for your date with him."
            "It is Valentine's day after all..."
            jump startKingVDate
        label loveMarvin:
            show mHiss
            m "Thank the lord you picked me! Helen will be so pleased you are now part of the family..."
            hide mHiss
            show emoSad
            e "i...i guess i wasnt gud e-nuff... </3"
            hide emoSad
            show kingCry
            k "I Was going to make you royalty...."
            hide kingCry
            "..."
            scene blackTransition
            "You choose Marvin over everyone else."
            "..."
            "It's time for your date with him."
            "It's Valentine's day after all..."
            jump startMarvinVDate
        label loveEmo:
            show emoBlush
            e "y-yay *nuzzles* :3 i new u love me ... you r my every ding... <3"
            hide emoBlush
            show kingAngry
            k "Wow...you really are shallow...they always take advantage of the rich royalty..."
            hide kingAngry
            show mSad
            m "the tadpoles will be so disappointed...."
            hide mSad
            "..."
            scene blackTransition
            "You choose xX_DarkRaven496283_Xx over everyone else."
            "..."
            "It's time for your date with him..."
            "It's Valentine's day after all..."
            jump startEmoVDate
    label startKingVDate:
        "King Samson II shows up at your dorm room later..."
        show kingProc
        k "MY BLOSSOMING PETUNIA! I HAVE A SURPRISE FOR YOU."
        hide kingProc
        p "{i}This better be good...{/i}"
        "You open the door and he is standing outside. He pushes you into a stolen shopping cart."
        show kingDefault
        k "Since you have chosen be to be your beautiful frog husband, I will take you to my kingdom."
        hide kingDefault
        p "A kingdom?"
        "..."
        scene blackTransition
        "After about two hours of riding around in a shopping cart, you arrive at King Samson II's kingdom."
        "You go inside a sketchy looking building, and walk up five flights of stairs. King Samson II opens the door to his... kingdom?"
        "When you go peer inside, you realize his kingdom is actually just a regular apartment."
        menu:
            "Go inside King Samson II's fake kingdom.":
                jump fakeKing
            "Stand outside in the hallway to yell at him.":
                jump yell
        label fakeKing:
            p "{i}I'm kind of curious now... {/i}"
            jump bite2Eat
        label yell:
            "You catfished me! This isn't a castle, it's an unfurnished apartment!"
            show kingAngry
            k "HOW DARE YOU. I spent hours yelling at my servants to get my kingdom ready."
            hide kingAngry
            "You refuse to go inside the musty apartment."
            "King Samson II looks really hurt."
            "You almost start to feel bad...almost."
            show kingDefault
            k "Where else would you want to go if not my beautiful kingdom???"
            hide kingDefault
            "You glance at the time..."
            "It's already the evening...You spent so much time traveling to King Samson II's 'kingdom' in a shopping cart that the time flew by."
            menu:
                "I'm tired, I'm hungry, and I need to poop. I'm just gonna go home.":
                    jump tiredHungryPoop
                "I'm tired, I'm hungry, and I need to poop. Wanna grab a bite to eat and call it a day?":
                    jump bite2Eat
            label bite2Eat:
                "King Samson II belches really loudly."
                show kingBelch
                k "Yeah I'm kind of hungry..."
                hide kingBelch
                show kingProc
                k "Actually! MY SERVENTS HAVE PREPARED A NICE MEAL FOR YOU IN PREPERATION."
                hide kingProc
                "He gestures you inside the apartment."
                p "{i} Ah what the hell... {/i}"
                "You go inside his apartment."
                scene apartmentInside
                "He leads you past about 6 rows of different sinks."
                "It looks extremely run down and musty."
                show kingDefault
                k "Through this way, m'lady."
                hide kingDefault
                "He holds a door open for you."
                scene transitionBlack
                "You hesitantly go through; you think he's about to murder you."
                "..."
                "...!"
                "He has an actual damn kingdom!"
                scene kingdom
                "Inside his run down walk in closet looking door seems to be a whole other world...?"
                "There are buildings made of gold, people roaming around and participting in their every day lives..."
                "...??? There are rows of titanium sinks."
                show kingSlimy
                k "HERE M'LADY."
                hide kingSlimy
                "He leads you into a palace, where you are greeted by various frog servants."
                "It feels like a dream..."
                "You could imagine a future here, especially if you're going to be royalty..."
                "Bring up becoming royalty?"
                menu:
                    "Yes":
                        jump goldDigger
                    "No.":
                        jump nahGoldDigger
                label nahGoldDigger:
                    "You realize that you haven't exactly been the nicest to King Samson II."
                    p " {i}It would be wrong to be nice to him just for his wealth...I'm a jerk but not THAT much of a jerk... {/i}"
                    "You choose to follow your moral compass and just enjoy your date with King Samson II as it is."
                    "..."
                    scene blackTransition
                    "You enjoy like a pretty nice meal that the developer is not about to write out."
                    "After your date you are escorted back to your dorm by one of King Samson II's servants."
                    #servant default
                    t "Boss seems to have taken a liking for you..."
                    p "Yeah ..."
                    "You can't believe he's an actual KING..."
                    "School promises to be interesting tomorrow..."
                    "THE END."
                    return
                label goldDigger:
                    p "So King Samson II...I've been thinking about...our future together a lot..."
                    show kingShocked
                    "King Samson II seems really surprised. But like happy surprised not like omg wtf surprised."
                    hide kingShocked
                    "Suddenly a servant comes up to him out of nowhere."
                    #servant default on other side
                    t "SIR! AN URGENT MESSAGE!!!"
                    k "What is it, King Samson II's Servant???"
                    t "A warning about this person over here..."
                    k "? WHAT ABOUT MY LOVELY BEAUTIFUL BUTTERNUT SQUASH?"
                    t "This intruder over here is a level 5 threat. Security calls it a...Gold Digger."
                    "King Samson II looks at you, horrified."
                    show kingShocked
                    k "T-THEYRE NOT RIGHT, ARE THEY HONEY??"
                    k "I THOUGHT YOU REALLY LOVED ME..."
                    hide kingShocked
                    show kingAngry
                    k "BUT NOW THAT I THINK ABOUT IT...YOU'VE BEEN QUITE RUDE UP UNTIL NOW, HAVEN'T YOU?"
                    hide kingAngry
                    "..."
                    "It seems that you are in trouble with King Samson II's kingdom."
                    "..."
                    scene blackTransition
                    "You're kicked out and banned from his kingdom..."
                    "You're forced to walk home..."
                    "This Valentine's Day was a disaster."
                    "You start to feel a little guilty."
                    "..."
                    "School's gonna be awkward from now on..."
                    "THE END."
                    return
            label tiredHungryPoop:
                show kingDefault
                k "PLEASE DO NOT TELL ME ABOUT YOUR BOWEL MOVEMENTS. IT IS VERY UNLADY LIKE AND QUITE HONESTLY JUST DISGUSTING AND UNFITTING FOR ROYALTY."
                hide kingDefault
                "...King Samson II says, while picking his nose."
                k "Anyways...  you want to go home I guess you can. I can't force you to stay if you don't want to, that would be disrespectful to you, and I respect you."
                p "{i} What is he being so nice for?? {/i}"
                show kingProc
                k "I'LL TAKE YOU BACK IN MY CARRIAGE."
                hide kingProc
                "...he goes back to yelling."
                menu:
                    "Take up his offer to go home in his 'carriage'.":
                        jump goInCarriage
                    "You're not about to go in that crusty shopping cart again. Take a LyfBer (joint company made by the taxi services Lift and OohBer.)":
                        jump takeUber
                label goInCarriage:
                    scene blackTransition
                    "You agree to King Samson II to at least taking you home."
                    "You get in the shopping cart and he starts pushing you."
                    show kingProc
                    k "EVEN THOUGH YOU INSULTED BY HARD WORK I WANTED YOU TO KNOW..."
                    k "..."
                    hide kingProc
                    show kingBlush
                    "King Samson II looks flustered for the first time in his life."
                    k "UH..."
                    hide kingBlush
                    show kingBelch
                    "He belches loudly."
                    hide kingBelch
                    show kingBlush
                    k "I AM GLAD THAT I COULD SPEND THIS EVENING WITH YOU, EVEN IF ALL I AM DOING IS PUSHING YOU IN A SHOPPING CART."
                    hide kingBlush
                    p "{i} is he being...romantic? {/i}"
                    menu:
                        "Tell him that you're glad you're with him too.":
                            jump gladToo
                        "Thank him still but with a snarky comment about his kingdom because you're rude.":
                            jump gladToo
                    label gladToo:
                        "..."
                        "Before you could even actually say anything, King Samson II belches loudly."
                        show kingBelch
                        k "EXCUSE ME MY WONDERFUL BEAUTIFUL LOVELY ADORABLE ROYALTY...CAN YOU GET OFF? I'M GETTING KIND OF TIRED."
                        k "YOU KNOW THE WAY HOME FROM HERE RIGHT?"
                        hide kingBelch
                        "..."
                        scene blackTransition
                        "King Samson II makes you get off from the shopping cart and walk the rest of the way home by yourself."
                        "..."
                        "You start on a long trek back to your dorm."
                        "The date with King Samson II was...kind of underwhelming. Almost like the developer has burnt out by the time she started to write the ending to some of the dates."
                        "Not like that's the case or anything though..."
                        "THE END."
                        return
                label takeUber:
                    p "Actually I think I'm good with taking a LyBer home."
                    show kingShocked
                    k "A LYFBER??? YOU KNOW THOSE THINGS CAN BE PRETTY DANGEROUS. I HEARD THE OTHER DAY FROM ONE OF MY SERVANTS THAT THEIR DRIVER TURNED OUT TO BE SUPER TALKATIVE!!! IMAGINE BEING STUCK WITH SUCH AN ANNOYINGLY TALKATIVE PERSON FOR THAT LONG?? HEY BY THE WAY DID YOU SEE THE NEWS THE OTHER DAY?"
                    hide kingShocked
                    "..."
                    "It continues this way for a while..."
                    "..."
                    scene blackTransition
                    "While King Samson II is talking you secretly call a LyfBer and leave."
                    "He doesn't even notice."
                    "In your shared LyfBer you see another passenger."
                    "..!"
                    "It's the cult member from outside Boiled Topic that like you know that one time you went to Boiled Topic!"
                    #cult member default
                    c "Oh hey! It's you again."
                    p "Hello..."
                    "You strike up a conversation with the cult member..."
                    "You two turn out to really hit it off!"
                    "..."
                    "He asks you out on a date."
                    menu:
                        "Agree":
                            jump cultEnding
                        "Say no, you can't do that to King Samson!":
                            jump noCultEnding
                    label cultEnding:
                        "You agree to a date with the cult member some time next weekend."
                        "It seems as if your Valentine's Day has turned out to be quite eventful."
                        "..."
                        "Kinda weird that you chose to date a cult member instead of a frog though...but whatever."
                        "THE END."
                        return
                    label noCultEnding:
                        #cult member default
                        c "Ah, I understand."
                        "The lyfBer arrives in front of a sketchy building...almost like a cult headquarters."
                        c "Well have a good day, tortured soul."
                        "You wave goodbye to the cult member."
                        "The LyfBer makes its way to your dorm."
                        "..."
                        "School's gonna be weird tomorrow."
                        "THE END."
                        return
    label startEmoVDate:
        "..."
        scene alleyway
        "You meet xX_DarkRaven496283_Xx in front of a dark suspicious alleyway."
        p "...So where are we going?"
        show emoDefault
        e "h-huh? oh...we're already here ^_^"
        hide emoDefault
        p "Our date is in an alleyway??"
        p " {i} Is he going to kill me... {/i}"
        menu:
            "Enter the alleyway.":
                jump enterAlley
            "Do not, by any means, enter the alleyway.":
                jump noAlley
        label enterAlley:
            "You hesitantly enter the alleyway with  xX_DarkRaven496283_Xx ."
            show emoBlush
            e "prepare to bee amazed >.< "
            hide emoBlush
            menu:
                "Take a right.":
                    jump alleyRight
                "Take a left.":
                    jump alleyLeft
            label alleyRight:
                "You and  xX_DarkRaven496283_Xx  take a right..."
                "And keep taking a right..."
                p "{i} Why is this path taking so long? {/i}"
                scene london
                "You and  xX_DarkRaven496283_Xx somehow end up in London..?"
                p "Woah...I've never been to London! Let's go to the London Bridge!"
                show emoSad
                e "the sky is dark and grey... just the way i like it.... "
                hide emoSad
                "You and  xX_DarkRaven496283_Xx go sightseeing, starting with the London Bridge."
                show emoDefault
                e "we have one more place to visit... you'll love it u-uwu;"
                hide emoDefault
                scene blackTransition
                "..."
                "You arrive at your final destination."
                scene cemetery
                "...the cemetery."
                p "{i} Of course...{/i}"
                " xX_DarkRaven496283_Xx leads you to a gravestone in the corner, far away from the others."
                " xX_DarkRaven496283_Xx  replaces the flowers in front of the gravestone with a fresh bouquet of chrysanthemums."
                p "If I may ask...who is this grave dedicated to?"
                show emoSad
                e "..."
                e "my serotonine and dopamine levels..."
                hide emoSad
                p "Are you being forreal??"
                show emoSad
                e " *hic* ya...sad uwu"
                hide emoSad
                menu:
                    "Did you take biology? That's not how it works.":
                        jump biology
                    "Rest in peace??":
                        jump rip
                label biology:
                    show emoAngry
                    e " *sniffle* YOU DON'T UNDERSTAND DX"
                    e "THE BIOLOGISTS ARE CONSPIRACY"
                    hide emoAngry
                    "You are taken aback."
                    "...He rarely ever speaks in capslock."
                    show emoDefault
                    e "when i leave this realm i hope to be buried next to my happiness..."
                    hide emoDefault
                    p "...alright that's enough sad boi hours for now."
                    scene blackTransition
                    "You wait for  xX_DarkRaven496283_Xx to finish and drag him out of the graveyard."
                    scene alleyway
                    "You find your way back to the alleyway and go back to where you came from. It's somehow still the middle of the night..."
                    jump almostEnd
                label rip:
                    p "Well wherever your serotonin and dopamine is gone, I'm sure they're having a nice time..."
                    " xX_DarkRaven496283_Xx  continues to cry."
                    show emoCry
                    e "thx dat meanz a lotta :,("
                    hide emoCry
                    scene blackTransition
                    "..."
                    "You wait for  xX_DarkRaven496283_Xx  to finish and drag him out of the graveyard."
                    "You stop by London's WallBlues to grab some tissues for him before heading back out the alleyway."
                    "It's still somehow the middle of the night when you arrive back..."
                    jump almostEnd
            label alleyLeft:
                "You decide to take a left."
                scene fitnessCenter
                "You end up in front of a dark building. Others walk in with work-out clothes from Boiled Topic..."
                p "Is this...a fitness center for emos?"
                show emoDefault
                e "i thought it would be nice to work out away from our sadness and pain..."
                hide emoDefault
                "You both enter the building and open the fifth door on your right."
                "It's a zumba class!"
                "Which unfitting new wave emo song will you work out to?"
                menu:
                    "I Write Sins not Tragedies by Panic! at the Disco.":
                        jump zumba
                    "Stressed out by Twenty One Pilots.":
                        jump zumba
                label zumba:
                    "You dance to teenage emo music."
                    "You're having a lot more fun than you thought. You're dancing but sweating super hard at the same time !"
                    "Suddenly the audio plays a random G note at max volume. The whole class goes silent."
                    p "...what's happening??"
                    "The entire class, including  xX_DarkRaven496283_Xx  starts to tear up."
                    show emoSad
                    e "w-why? i skipped yezterdays zumba class specifically to avoid this note..."
                    hide emoSad
                    show emoCry
                    e "W-WHEN I WAS...A YOUNG BOY...M-MY FATHER....TOOK ME INTO THE CITY..."
                    hide emoCry
                    "The entire class except for you joins in, crying and singing along..."
                    "It seems this is some sort of overused emo anthem..."
                    scene blackTransition
                    "You're extremely weirded out, so you drag  xX_DarkRaven496283_Xx  out of the building and head back out the alleyway."
                    jump almostEnd
        label noAlley:
            p "I don't really feel comfortable walking inside a pitch black alleyway...Can we just grab a bite at La Fermue du Roi?"
            show emoDefault
            e "...you want to go to a 5 star french restaurant?? on valentines day?? w-what a weirdo omg... >.< XD"
            e "...sure why not."
            hide emoDefault
            scene fancyRestaurant
            "You and  xX_DarkRaven496283_Xx travel to La Fermue du Roi. There's no seating available so you go to La Bouteille D'eau instead. It also has 5 Michelle Lin stars."
            "You get seated. Your server is kind of confused that there's a frog with a fringe sitting across from you  (in case you forgot you're literally dating frogs)."
            #food workerd default
            w "Erm madame, is this your pet?"
            show emoDefault
            e " we are all pets of the universe....trapped and forgotten once we perish..."
            hide emoDefault
            w "..."
            w "Anyways *clears throat* what would you like to order?"
            menu:
                "Pasta.":
                    jump pasta
                "A burger.":
                    jump burger
            label pasta:
                w "Excellent choice!"
                show emoSad
                e "i cant eat pasta...its lent month."
                hide emoSad
                #food worker default
                w "Benisse les dieux...YOU ARE A FROG! FROGS CANNOT PARTICIPATE IN LENT."
                "You're kind of offended that your waiter is speaking so rudely to your frog companion."
                menu:
                    "Say 'La Bouteille D'eau? More like la BOOTY.'":
                        jump offensive
                    "Throw your 303.15 degrees Kelvin water at the poopy waiter.":
                        jump offensive
                label offensive:
                    #food worker mad
                    w "How dare you??"
                    scene blackTransition
                    "You grab  xX_DarkRaven496283_Xx and run out of the restaurant before the waiter whistles for his dogs to chase you."
                    jump almostEnd
            label burger:
                #food worker default
                w "I'm sorry madame, we do not serve burgers. This is French cuisine *kisses fingers and makes a MUAH sound.*"
                w "In fact...we're out of steamed frogs, and the local frog market is closed..."
                w "Say...you wouldn't happen to be terribly sad if I borrowed your pet frog for...purposes, would you?"
                show emoDefault
                e " *sigh* it's about time i left this world."
                hide emoDefault
                " xX_DarkRaven496283_Xx sadly leaps to you."
                show emoBlush
                e "you've stirred up an emotion in my chest. some call this emotion love. i wanted to thank you for sticking by my side when no one else."
                hide emoBlush
                "You're shocked that  xX_DarkRaven496283_Xx  would give his life to a French restaurant, only to have people eat his steamed remains."
                "You suddenly get a flashback to middle school, when your teacher told your class to confront the bully, rather than be a bystander."
                menu:
                    "Say ' La Bouteille D'eau? More like La BOOTY.'":
                        jump offensive
                    "Throw your 303.15 degrees Kelvin water at the poopy waiter.":
                        jump offensive
    label almostEnd:
        scene alleyway
        "You and xX_DarkRaven496283_Xx stumble back to the alley."
        " xX_DarkRaven496283_Xx looks a bit down...but when does he not?"
        p "Look...you shouldn't care about what others think. Like what the heck, I'm attracted to frogs?"
        p "As Teenager Post #10216 says: 'Whenever you feel sad just remember that there are billions of cells in your body and all there care about is you..'"
        show emoDefault
        e "..."
        e "n-no offwense...but ur kinda cringey >.< XD"
        e "...anyways..."
        e "i...i guess..."
        hide emoDefault
        show emoBlush
        e "thanks for bweing mai princess of darkness ^_^"
        e "uwu owo ewe awa iwi XD XD :D :'D"
        hide emoBlush
        jump endEmoVDate
    label endEmoVDate:
        "..."
        scene blackTransition
        " xX_DarkRaven496283_Xx kind of drops you off at your dorm afterwards..."
        "He started to get tired after about 10 minutes of walking while nuzzling your shoulder, so you said it was fine to walk yourself home."
        "Your date with  xX_DarkRaven496283_Xx seems to have been... a sucess???"
        "School promises to be interesting tomorrow..."
        "THE END."
        return
    label startMarvinVDate:
        "..."
        scene door
        "You leave with Marvin and go to his house."
        "Marvin opens the door."
        m "*opens door*"
        show mHiss
        m "HIIIISSSSS! Hello momma goose! Are you ready for a romantic evening at..."
        hide mHiss
        "Marvin pauses for dramatic effect. You hold your breath in anticipation."
        show mWow
        m "...the train station!"
        hide mWow
        menu:
            "What the heck???":
                jump loser
            "Sounds great!":
                jump trainLover
        label loser:
            p "That sounds dreadful! Why would anyone want to go to the train station for a Valentine's day date??"
            "Marvin seems offended."
            show mSad
            m "Well {i} I {/i} think it is a good idea. You have to come! It'll be great."
            hide mSad
            scene blackTransition
            "Marvin grows really upset, and you feel pretty guilty. You agree to go to the train station with Marvin."
            jump trainsGalore
        label trainLover:
            show mDefault
            m "Really?"
            hide mDefault
            p "Yeah! Train stations are my jam."
            scene blackTransition
            "You walk towards the train station with Marvin."
    label trainsGalore:
        scene trainStation
        "You arrive at the train station."
        show mDefault
        m "Let's sit down."
        hide mDefault
        p "Okay."
        "You sit down on a metal bench."
        "Twenty minutes pass. You are growing pretty bored sitting here silently. You try to start a conversation about oranges."
        p "Do you like oranges?"
        show mMOF
        m "I hate them, but my ex-wife Helen loves them."
        hide mMOF
        p "{i} This feels familiar...{/i}"
        p "...Cool."
        "You sit in awkward silence."
        "Suddenly, a train arrives at the station. The doors open."
        "What do you want to do?"
        menu:
            "Stay with Marvin at the train station.":
                jump stayWithMarvin
            "Hop on the train without Marvin.":
                jump leaveMarvin
        label leaveMarvin:
            "Are you sure?"
            menu:
                "Yes":
                    jump leaveMarvin2
                "No, I'll stay with Marvin":
                    jump stayWithMarvin
        label stayWithMarvin:
            "The train leaves the station."
            show mMOF
            m "Whew! For a second there I thought you were gonna leave me. Oh look, a quarter! Marvin hops over and picks the quarter off the floor."
            hide mMOF
            "You begin to regret your decision."
            "..."
            "Marvin is still staring at the quarter."
            show mMOF
            m "Helen never lets me have money. *chuckles* That's why I always collect coins off the street."
            hide mMOF
            show mWink
            m "Hey! That's an idea. Let's find loose change on the street!"
            hide mWink
            "Without waiting for a response, Marvin jumps off the bench, and starts crawling on the ground looking for coins."
            p "{i} Great. {/i}"
            "You reluctantly join Marvin. On the ground, there's dust and hair and gum and trash (no commas were found on the ground)."
            show mWow
            m "Hey look! Another quarter!"
            hide mWow
            "Turns out it's not a quarter, ut a chewed up piece of gum. Marvin looks at the gum for a bit and smacks his frog lips. He puts it in his mouth."
            "You watch, horrified."
            show mDefault
            m "Oh, how rude of me."
            "Marvin spits out the gum."
            m "Want some?"
            p "No thanks..."
            m "*shrugs* Suit yourself."
            hide mDefault
            "He puts the gum back in his mouth."
            "You continue looking for coins with Marvin. After an hour, you have a total of of two dollars and seventeen cents."
            show mWow
            m "What a find! I can buy some more gum with this!"
            hide mWow
            "He pockets the change and you sit back down on the bench."
            "When you turn around, Marvin is gone. He comes back five minutes later carrying a big cardboard box."
            show mMOF
            m "Look at what I just found!"
            hide mMOF
            "He dumps the cardboard box onto the bench. Out falls a bunch of dirty newspapers, some old socks, more gum, PVC pipe, and a tube of used chapstick."
            "Marvin picks up the chapstick, and waves it in your face."
            show mDefault
            m "Isn't this great?"
            hide mDefault
            "He seems overly excited. It's a free tube of chapstick, after all."
            "Marvin stares at the chapstick for a minute, mesmerized."
            show mDefault
            m "Should I eat this? I want to eat it."
            hide mDefault
            menu:
                "Yeah go for it dude.":
                    jump eat
                "Are you crazy??? NO!":
                    jump noEat2
                "Do whatever you want. You're an adult frog.":
                    jump eat
            label eat:
                show mWink
                m "Okay!"
                "Marvin shoves the entire tube of chapstick in his mouth and swallows it whole."
                hide mWink
                p "Uhhh..."
                "One minute passes, and then Marvin falls to the ground, choking and hacking. You think about giving him the heimlick maneuver, but you decide against it after you realize you'd crush his small insignificant frog body."
                "Marvin finishes his choke-fest, and stands up. His left eye is twitching."
                p "You good?"
                show mDefault
                m "Yup.  That tasted just like paint! Who knew?"
                hide mDefault
                "You sit down on the bench next to Marvin."
                "..."
                "An awkward silence fills the air."
                "In an attempt to fill the silence, Marvin forces out a loud belch."
                show mBlush
                m " *BELCH*"
                hide mBlush
                "..."
                "..."
                "You're not quite sure out to respond to that."
                show mBlush
                m " So..."
                m "Uh..."
                m "How's your toe infection?"
                hide mBlush
                menu:
                    "It's doing better.":
                        jump toeBetter
                    "What toe infection??":
                        jump whatToe
                label toeBetter:
                    show mWink
                    m "That's good that's good..."
                    hide mWink
                    "..."
                    "This is getting kinda dry..."
                    jump endMarvinVDay
                label whatToe:
                    show mWink
                    m "Oh you know the one you told me about the other day?"
                    m "The one that's making your toe all green??"
                    hide mWink
                    p "..."
                    show mDefault
                    m "..."
                    hide mDefault
                    show mSad
                    m "...I think I'm thinking about Helen."
                    hide mSad
                    p "Haha."
                    "..."
                    "This is getting kinda dry.."
                    jump endMarvinVDay
            label noEat2:
                "Marvin ignores you and starts to eat the chapstick. You have to intervene somehow, so you grab the chapstick from him and throw it at an unsuspecting passenger."
                p "You can't eat someone else's used chapstick! You could die."
                show mSad
                m "Humph. *muttering* Just like my ex-wife..."
                hide mSad
                "It seems like you're expecting deja vu. You sit down on the bench next Marvin."
                "Another train comes. When it leaves, Marvin has started blabbering about the many different types of citrus that he hates."
                show mDefault
                m "...and I also hate grapefruit, and limes, and..."
                hide mDefault
                "You feel your IQ drop a hundred points. You need to change the conversation topic, and fast."
                "What do you want to talk about first?"
                menu:
                    "Marvin's tadpoles":
                        jump tadpoles
                    "His addiction to paint.":
                        jump druggy
                    "Zoology 101":
                        jump whoNeedsEducationAnyways
                label tadpoles:
                    p "So, Marvin, how's the Missus? And your tadpoles?"
                    "Marvin perks up."
                    show mMOF
                    m "Oh, just great! Little Suzie is felling all better, and Rebecca is just starting retirement."
                    "Marvin smiles fondly."
                    m "She was an architect."
                    m "Claude is biting everything in sight...I really gotta talk to him about that..."
                    m "And Maximus Detrimus just won a hissing competition. He's the smart one in the family."
                    hide mMOF
                    p "...Yeah. That's good. And Helen?"
                    show mDefault
                    m "Oh? Helen? She's still kicking."
                    hide mDefault
                    p "Oh..."
                    "..."
                    p "Eat any paint lately?"
                    show mMOF
                    m "Actually, I've only had two cans today! I'm trying to cut back. You know how it is."
                    p "Not really..."
                    "Marvin continues as if you hadn't spoken."
                    m "Yeah I ate a blue can and a purple can in one sitting."
                    "Marvin sighs happily."
                    m "Good times."
                    hide mMOF
                    p "Ah...."
                    p "So how's Zoology 101 going?"
                    show mGross
                    "Marvin almost chokes on his saliva."
                    hide mGross
                    m "Zoology? School? I don't think I've been to XYZ University in weeks. I've failed all my classes by now."
                    "Marvin makes a noise that is half-laughing and half-weeping. He cries/laughs his guts out while you sit there awkwardly."
                    p " {i} This is feeling like an interview. {/i}"
                    jump endMarvinVDay
                label druggy:
                    p "So Marvin, eat any paint lately?"
                    show mMOF
                    m "Actually, I've only had two cans today! I'm trying to cut back. You know how it is."
                    p "Not really..."
                    "Marvin continues as if you hadn't spoken."
                    m "Yeah I ate a blue can and a purple can in one sitting."
                    "Marvin sighs happily."
                    m "Good times."
                    hide mMOF
                    p "Ah...."
                    p "Right. How are your tadpoles doing?"
                    "Marvin perks up."
                    show mDefault
                    m "Oh, just great! Little Suzie is felling all better, and Rebecca is just starting retirement."
                    "Marvin smiles fondly."
                    m "She was an architect."
                    m "Claude is biting everything in sight...I really gotta talk to him about that..."
                    m "And Maximus Detrimus just won a hissing competition. He's the smart one in the family."
                    p "...Yeah. That's good. And Helen?"
                    m "Oh? Helen? She's still kicking."
                    hide mDefault
                    p "Oh..."
                    p "So how's Zoology 101 going?"
                    show mGross
                    "Marvin almost chokes on his saliva."
                    m "Zoology? School? I don't think I've been to XYZ University in weeks. I've failed all my classes by now."
                    "Marvin makes a noise that is half-laughing and half-weepin. He cries/laughs his guts out while you sit there awkwardly."
                    hide mGross
                    p " {i} This is feeling like an interview. {/i}"
                    jump endMarvinVDay
                label whoNeedsEducationAnyway:
                    p "So how's Zoology 101 going?"
                    show mGross
                    "Marvin almost chokes on his saliva."
                    m "Zoology? School? I don't think I've been to XYZ University in weeks. I've failed all my classes by now."
                    "Marvin makes a noise that is half-laughing and half-weepin. He cries/laughs his guts out while you sit there awkwardly."
                    hide mGross
                    "You think you should restart the conversation."
                    p "How are your tadpoles doing?"
                    show mDefault
                    "Marvin perks up."
                    hide mDefault
                    show mMOF
                    m "Oh, just great! Little Suzie is felling all better, and Rebecca is just starting retirement."
                    "Marvin smiles fondly."
                    m "She was an architect."
                    m "Claude is biting everything in sight...I really gotta talk to him about that..."
                    m "And Maximus Detrimus just won a hissing competition. He's the smart one in the family."
                    p "...Yeah. That's good. And Helen?"
                    m "Oh? Helen? She's still kicking."
                    p "Oh..."
                    p "Eat any paint lately?"
                    m "Actually, I've only had two cans today! I'm trying to cut back. You know how it is."
                    p "Not really..."
                    "Marvin continues as if you hadn't spoken."
                    m "Yeah I ate a blue can and a purple can in one sitting."
                    "Marvin sighs happily."
                    hide mMOF
                    show mDefault
                    m "Good times."
                    hide mDefault
                    p "Ah...."
                    p " {i} This is feeling like an interview. {/i}"
                    jump endMarvinVDay
    label leaveMarvin2:
        "But are you sure?"
        menu:
            "Yes, definitely.":
                jump leaveMarvin3
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin3:
        "But are you really sure?"
        menu:
            "Yes!":
                jump leaveMarvin4
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin4:
        "Are you one hundred percent positive?"
        menu:
            "Yup":
                jump leaveMarvin5
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin5:
        "Are you sure you want to leave Marvin?"
        menu:
            "Yeah.":
                jump leaveMarvin6
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin6:
        "Are you sure?"
        menu:
            "As sure as mud.":
                jump leaveMarvin7
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin7:
        "Are you totally sure?"
        menu:
            "As sure as gold.":
                jump leaveMarvin8
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin8:
        "But like do you really want to ditch him?"
        menu:
            "Yes, I really do.":
                jump leaveMarvin9
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin9:
        "Yeah but are you super positive???"
        menu:
            "bruh yes...":
                jump leaveMarvin10
            "No I'll stay with Mr. Marvin":
                jump stayWithMarvin
    label leaveMarvin10:
        "Are you really really sure?"
        menu:
            "Yeah!":
                jump leaveMarvin11
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin11:
        "C’mon, think about this. Do you actually want to leave Marvin?"
        menu:
            "Yes, I really do.":
                jump leaveMarvin12
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin12:
        "Are you sure?"
        menu:
            "Yes.":
                jump leaveMarvin13
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin13:
        "Are you two hundred percent positive?"
        menu:
            "Heck yeah I am.":
                jump leaveMarvin14
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin14:
        "Are you three hundred percent positive?"
        menu:
            "Yes!":
                jump leaveMarvin15
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin15:
        "But like are you SURE sure?"
        menu:
            "Mhhhmmmmm":
                jump leaveMarvin16
            "No, I’ll stay with Marvin.":
                jump stayWithMarvin
    label leaveMarvin16:
        scene blackTransition
        "Congratulations Asshole."
        "You hop on the train, and it takes off."
        "You leave a dejected Marvin at the station."
        jump endMarvinVDayTrain
    label endMarvinVDayTrain:
        "..."
        "You're on the train to god knows where after leaving Marvin."
        "Hey what is wrong with you?"
        "Marvin may have a few strange quirks but just leaving him out of nowhere is kinda mean."
        "Like he may be a frog or whatever but...Marvin was there for you when no one else was."
        "You are beginning to regret your decision."
        "It's gonna be awkward at school tomorrow..."
        "THE END."
        return
    label endMarvinVDay:
        "..."
        "An awkward conversation with Marvin goes on for a few hours."
        "You didn't want to be rude and leave him so you put up with it."
        "..."
        "It's getting late."
        p "Hey Marvin don't you think it's getting kinda late?"
        show mHiss
        m "A little bit?! I mean... Are you not having the time of your life though?"
        hide mHiss
        "You're starting to regret your decision..."
        show mDefault
        m "..."
        m "I'm gonna go now actually... Helen's probably waiting for me."
        hide mDefault
        "...??"
        "Marvin hops onto a train and leaves you alone at the station."
        "..."
        p "{i} What a jerk. {/i}"
        "You get the feeling that Marvin's a little too hung up on Helen."
        scene blackTransition
        "...The day's almost over. You head back to your dorm alone."
        "It's gonna be awkward at school tomorrow..."
        "THE END."
        return
