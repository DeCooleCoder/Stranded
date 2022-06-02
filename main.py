#Idea 1: Your stranded from a time machine and are stranded between timelines So there may be dino's or medieval knights or dragons to conquer

#Plugins
import random
import time
import os
import sys
import colorama as cr
cr.init(autoreset=True)

#Alle antwoorden vor Ja en Nee
yes = ('y', 'yes', 'all right', 'alright', 'very well', 'ofc', 'ofcourse',
    'of course', 'sure', 'certainly', 'absolutely','yessir',
    'why not','yee', 'indeed', 'roger', 'aye','aye aye', 'yeah', 'yah', 'yep', 
    'yup', 'yuppers', 'mhm', 'okay', 'ok',
    'righto', 'yea', 'surely', 'ye', 'yuh', 'ya', 'yarr', 'aight')
no = ('n', 'no', 'nah', 'nope', 'naw', 'nay', 'noway', 'no way', 'never',
    'nae', 'not at all', 'not really', 'no thanks', 'of course not',
    'negative', 'nope', 'nuh', 'neh', 'nein', 'hell no', 'nonono',
    'forget that', 'nya','nuuu')

# Welcome System
print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
print(' ')
time.sleep(1)
print(f"{cr.Fore.BLUE}        █▀▀ ▀▀█▀▀ █▀▀▄ ▀▀█▄ ▄▄  █▀▀▄ █▀▀ █▀▀▄")
time.sleep(0.3)
print(f"{cr.Fore.BLUE}        ▀▀█   █   ██▀  ████ █ █ █  █ █▀  █  █")
time.sleep(0.3)
print(f"{cr.Fore.BLUE}        ▀▀▀   ▀   ▀ ▀  ▀ ▀  ▀ ▀ ▀▀▀  ▀▀▀ ▀▀▀")
print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
print(' ')
time.sleep(1.2)
print(' ')
print(f'{cr.Fore.CYAN}{cr.Style.BRIGHT}                       Controls:')
time.sleep(0.3)
print(' ')
print(f'{cr.Fore.CYAN}                    [n]    =  north')
time.sleep(0.1)
print(f'{cr.Fore.CYAN}                    [e]    =  east')
time.sleep(0.1)
print(f'{cr.Fore.CYAN}                    [s]    =  south')
time.sleep(0.1)
print(f'{cr.Fore.CYAN}                    [w]    =  west')
time.sleep(0.1)
print(' ')
print(f'{cr.Fore.CYAN}                    [q]    =  quit')
print(f'{cr.Fore.LIGHTBLACK_EX}_' * 60)
time.sleep(1)
print(' ')
print(f'{cr.Fore.WHITE}                Press [ENTER] to continue')
time.sleep(0.1)
startoroptions = input()
os.system("clear")

#copy paste room
#  "Stay asleep" :  {
#      "title" : "",
#      "description" : "",
#      "extradialogue" : "",
#      "options" : [],
#  }

print("Please enter your name here:")
name = input("- "),

#definition variables
n = 'N'
e = 'E'
s = 'S'
w = 'W'
q = 'Q'

#all the rooms!
rooms = {
  "Home" :  {
    "title" : "Home",
    "description" : "You hear your alarm going off,",
    "extradialogue": "Note: Type N to wake up and type S to stay asleep",
    "options": ["Wake up / Stay asleep"],
  },

  "Stay asleep" :  {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : []
  },

  "Wake up" :  {
      "title" : "You wake up in your bedroom and check your agenda. You see you made an appointment with the professors today to test their new invention out.",
      "description" : "You should head out right about now…you wouldn't want to be late at the lab...",
      "extradialogue": "",
      "options": ["Lab"],
  },

  "Stay at Home" : {
      "title" : "",
      "description" : "",
      "extradialogue" : ""
  },

  "Lab" :  {
    "title" : "The Lab",
    "description" : "You arrive at the Lab and see 2 doors waiting for you. Both have a sign. One saying “THE SMART AND AMAZING PROFESSOR ” and the other “The Man”. Which will you open first?",
    "extradialogue" : "Note: Type N for Open door THE SMART AND AMAZING PROFESSOR and Type S for Open door The Man",
    "options": ["THE SMART AND AMAZING PROFESSOR's office", "The Man's office"],
  },

"The Man's office" or "Talk to professor JerkMoose" : {
      "title" : "",
      "description" : "Professor JerkMoose: Hello my padawan, have you come to bargain?\n\nProfessor JerkMoose: Aaaaaah, it is you.....The experiment that's stupid enough to come and try our machine...\n\nProfessor JerkMoose: Anyways, again welcome to our lab! This is where we do all of our very safe and totally not illegal experiments and take our jobs very seriously (not). We have never made a SINGLE mistake so you don’t have to worry about your safety at all. Maybe one or two mistakes….a few more then two…. OK, a lot of mistakes, BUT this experiment is safer than anything you’ve ever done before this AND we have insurance that covers everything you need, except maybe being stranded throughout time, but that would never happen right?!?!\n\nProfessor JerkMoose: Now please….GET THE F OUT OF HERE B*TCH, AND SPEAK TO THE OTHER DUMBASS HERE!",
      "extradialogue" : ".\n.\n.\n.\n.\n(A friendly reminder of Prof. Hunter; If you haven’t spoken to the other professor yet, please do, if only for your mental health (and mine).)",
      "options" : ["Speak to professor Hunter", "Die"],    
},

    "Die" : {
        "title" : "",
        "description" : "You die...What did you expect? Some hidden achievement or some sh*t?",
        "extradialogue" : ""
    },

 "THE SMART AND AMAZING PROFESSOR's office" or "Speak to professor Hunter" :  {
   "title" : "THE SMART AND AMAZING PROFESSOR's office",
   "description" : "Professor Hunter: Hello and welcome to our lab. I’m professor Hunter and this is where we do all of our very scientific experiments and take our jobs very seriously. We have never made a SINGLE mistake so you don’t have to worry about your safety ;) So… what was your name again?",
   "extradialogue" : f"Professor Hunter: ...Riiight gotcha… so… {name} Have you met the other professor yet?",
   "options" : ["Talk to professor JerkMoose", "Continue talking to professor Hunter"]
 },

  "Continue talking to professor Hunter" : {
      "title" : "",
      "description" : "Professor Hunter: Alright than you may come right this way to THE EXPERIMENT *curtains slowly reveal a HUUUUUGE dong*\n\nProfessor Hunter: oops that's a project professor JerkMoose is working on moving on…\nWelcome to our biggest project yet THE TIME MACHINE!!!\nYou may enter the machine but be cautious of the wires!!\n\nProfessor JerkMoose:, because if one gets killed, you die as well…MWAHAHAHAHAHAHA!!!!\n\n(Friendly reminder from prof. Hunter: Please ignore him, he’s here for personal reasons….please don’t ask)\n\nWe're going to send you to the past and zap you back in exactly 24 hours so come back to the exact spot within that time or else you’ll be left Stranded o-o. (Here have this watch to check the time when you’ve made the jump) You received an old ragged looking watch, it’s 09:38:42am in the morning and counting.",
      "extradialogue" : "Professor Hunter: Here, have this just in case…\n\nYou received the Manual!!\n\nI’m not sure what Professor JerkMoose has done with the machine but it can’t be anything good so I'll just give you this in case anything bad happens…You’ll probably be fine anyways but just in case you never know… ¯\_(ツ)_/¯",
      "options" : ["Enter the Machine (AND DIE, MWAHAHAHA)", "Do a 180 and go through the exit (Footnote; ignore the AND DIE)"]
  },

  "Do a 180 and go through the exit (Footnote; ignore the AND DIE)" : {
      "title" : "You start moving towards the exit",
      "description" : "Professor JerkMouse: HEEEEYYYY, YAAA**EHOOO LEE, GET THE F BACK AERE, GET YAERE SH*TE AND STEP INTO THE F***IN’ MACHINE, AND BE GLAD A WON’T KICK YAERE A**E FROM ‘ERE TA M*****F***IN’ AFRIKA, B*TCH!!!!!! AN’ DONTAY DEERE TRYNA STEALIN'' OUR HIGHLY, HIGHLY SOPHISTICATED WATCH, YA B*STERD!!!",
      "extradialogue" : "You get into the machine against your own will (and partly due to the crazy professor) and get ready for the worst",
      "options" : ["Enter the Machine (AND DIE, MWAHAHAHA)"]
  },

  "Enter the Machine (AND DIE, MWAHAHAHA)" : {
      "title" : "",
      "description" : "You enter the suspiciously wobbly, high-tech, sophisticated  machine and get ready for the testing trip (P.S. I got no f-ing clue what this is -prof JerkMoose.)",
      "extradialogue" : "You've entered the time machine\n\nYou hear a switch being flipped and see a bunch of lights flashing before you and suddenly feel weightless and slowly lose consciousness…",
      "options" : ["Continue the story"]
  },
    
  "Continue the story" :  {
    "title" : "Crater",
    "description" : "Some time has passed and you start regaining your consciousness. Your blurry vision starts to clear and you observe your surroundings. You are in the middle of a crater filled with junk metal, machine parts and other bits and odds. you look at your watch and read 12:05:23pm you’ve been unconscious for 3 HOURS!!!",
    "extradialogue": "You decided to look around and see if you could find anything useful. You found the manual prof. Hunter gave you! There is a sticky note on it saying “Because this is our HIGHLY, SOPHISTICATED and BEAUTIFUL time traveling machine, this magnificent piece of art would never EVER go kaputt. So if you pick up this manual and need to repair MY BEAUTIFUL and AMAZING machine, then you are a dumb*ss who can’t even ride a F-ING bike…You’re welcome for the compliment-prof. JerkMoose” To repair the time machine you need these three items in case of a crash which is highly unlikely of course, because this machine was made by the two most renowned geniuses of the world, but just in case which is again HIGHLY unlikely to happen.",
    "Options": ["Get out of the Crater", ""]
  },

  "Craters edge" : {
      "title" : "",
      "description" : "You got out of the crater and spotted a path through the woods towards a beach",
      "extradialogue" : "",
      "options" : ["Go back into Crater", "Go to Beach", "Go to the Woods"],      
  },

  "Beach" : {
      "title" : "",
      "description" : "You go towards the beach and see a pirate camp to your right which seems to be empty.. To your left you spot a HUUUUUGE pirate ship almost seemingly as big as Noah’s Ark. On the side it says “THE BLACK PEARL”.",
      "extradialogue" : "",
      "options" : ["Go towards THE BLACK PEARL", "Go towards Pirate’s campsite", "Go back to the Woods"],    
  },

  "THE BLACK PEARL" : {
      "title" : "",
      "description" : "You went to THE BLACK PEARL and spotted absolutely nothing and saw the ship’s door closed and you are wasting your time…",
      "extradialogue" : "",
      "options" : ["Stay", "Go to pirate campsite", "Go back to the Beach"],      
  },

  "Pirate campsite" : {
      "title" : "",
      "description" : "You head towards the Pirate  Campsite and hear strange noises coming from a big looking tent. You also spot some movement behind some trees which will you investigate first?",
      "extradialogue" : "",
      "options" : ["Tent", "Go towards the woods", "Go towards THE BLACK PEARL", "Go back to the Beach"],      
  },

  "Tent" : {
      "title" : "",
      "description" : "You hear some mumbling noises in the tent and see a parrot on top of a stool squawking nonsense. You go investigate where the mumbling is coming from and hear someone behind you say: “peekaboo”.",
      "extradialogue" : f"You look around and see nothing except the parrot you look around to make sure and hear: “Whatcha doin hear {name}?” You look towards the parrot and it appears to be sentient. {name}: how’d you know my name? Parrot: I know and see everything {name}: you also know how to get me back? The parrot seems startled by your question and quickly flies away never to be seen again or heard of. (Though you seem to recognise it from somewhere…but where?). You don't find anything in the Tent and you go back outside.",
      "options" : ["Tent", "Go towards the woods", "Go towards THE BLACK PEARL", "Go back to the Beach"],      
  },

  "Woods" : {
      "title" : "",
      "description" : "Whilst heading towards the woods you spot a small knife and a cute lil pirate bunny plushie behind a rock.",
      "extradialogue" : "",
      "pickup" : ["Plushie", "Knife"],
      "options" : ["Continue"],      
  },

  "Continue" : {
      "title" : "",
      "description" : "You go and investigate the movements and spot a group of sheep.You go ahead and investigate the flock. You suddenly feel a thud on the back of your head. you’ve blacked out… (oh dear)",
      "extradialogue" : "Later…..\nYou start to regain consciousness…You seem to be in one of the pirate tents in the camp. You are tied to a pole in the middle of the tent. You seem to be alone in the tent.",
      "options" : ["Try to escape", "Stay tied up and find out what happened"],      
  },

  "Try to escape" : {
      "title" : "",
      "description" : "You try to escape. You failed to escape…",
      "extradialogue" : "You tried using the small knife but it failed and fell on the ground/\nYou tried using the plushie and… nothing happened… I mean what did you expect honestly?",
      "options" : ["Stay tied up and find out what happened"],      
  },

  "Stay tied up and find out what happened" : {
      "title" : "",
      "description" : "You stay still and wait to see if someone might come to you. You hear footsteps outside of the tent. A person walks in…he looks like a pirate with the eyepatch and hook. Not to mention his cool hat and sword. He looks at you.\nPirate: Aaaahhh…Yar finally awake! Now ah’m gonna ask ya some questions and yar gonna answer them, if not, weeellll ah do need to practice ma swordsmanship again…ya would be nice target practice. So yar gonna tell meh what ah want, capiche?",
      "extradialogue" : "",
      "options" : ["Say capiche", "Say not capiche"],   
  },

  "Say capiche" : {
      "title" : "",
      "description" : "Pirate: Excellent! Now, what's your name and what are you doing here?",
      "extradialogue" : "",
      "options" : ["Lie", "Tell the truth"],      
  },

  "Say not capiche" : {
      "title" : "",
      "description" : "Pirate: Don’t know what not means but you do you. So, what's your name and what are you doing here?",
      "extradialogue" : "",
      "options" : ["Say capiche"],      
  },

  "Lie" : {
      "title" : "",
      "description" : "Pirate: so… your tellin’ me ya just happened to stumble across our camp and just so happened to wander right into mah trap. Riiiiight…\nThe pirate Slowly approaches the player whilst sharpening his sword.\nYa know what i hate more than anythin’’ else?...LIARS!! Those who lie go to h*ll so imma ask you one more time what is yar business here?",
      "extradialogue" : "",
      "options" : ["Tell the truth"],      
  },

  "Tell the truth" : {
      "title" : "",
      "description" : f"Pirate: Soooo… {name} Yar tellin’ meh ya time traveled?",
      "extradialogue" : " Well, ah’ve seen weirder things than that, so ah guess ah believe ya. Now ya have trouble going back since yar machine is kaputt…well ah guess ah can help ya. But for a fee of course.",
      "options" : ["Accept the help", "Be egotistical and deny"],      
  },

  "Be egotistical and deny" : {
      "title" : "",
      "description" : "Pirate: Alrighty then ah got no use for ye *kills player",
  },

  "Accept the help" : {
      "title" : "",
      "description" : "Pirate: Alrighty! Let’s go and find those pieces yar missin’, kay? What? Ah never introduced maself?!?!?!?! Ah completely forgot! Ma name’s Edward ‘Moose’ Teach, also known as the biggest, baddest and overall most amazing pirate sailin’ over the seven seas', BLACKBEARD! I might have an idea of where the first part of your machine is so LETS-SA-GO, TO THA BLACK PEARL!!! (Don’t question how he know he just does).",
      "extradialogue" : "you head towards the ship and hop aboard going across the wide open sea’s. The captain shows you around and introduces you to the crew while the captain orders the crew to head east. After what felt like an eternity you check your watch just to make sure to see how much time you’ve got left and DAMN you see you’ve spent only 15 minutes aboard.\nYou hear the captain say: “LAND AHOY!!!” you look over the railing of the ship and see some weird Jungle like landscape ahead of you. The captain tells you to look ahead for the parts while he organizes stuff at the ship. You go ahead  and jump right into the jungle and get to an open area… you spot two different pathways which way will you go?",
      "options" : ["Go North", "Go East", "Go back to the island"],      
  },

  "Go North" : {
      "title" : "",
      "description" : "You head North and spot a HUUUUGE boulder blocking your way",
      "extradialogue" : "",
      "options" : ["Attack boulder with Dagger", "Go back to Beach 2"],      
  },

  "Go back to Beach 2" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : ["Go North", "Go East", "Go back to the island"],      
  },

  "Attack boulder with Dagger" : {
      "title" : "",
      "description" : "You tried attacking the boulder… But nothing happened… Dumbass…",
      "extradialogue" : "",
      "options" : ["Go back Beach 2"],      
  },

  "Go east" : {
      "title" : "",
      "description" : "You Headed East and spotted a :3 on the floor it seems as if it’s hinting towards placing something there…",
      "extradialogue" : "",
      "options" : ["Place Plushie", "Place Dagger", "Go back Beach 2"],      
  },

  "Place Dagger" : {
      "title" : "",
      "description" : "You place the dagger… Nothing happened…",
      "extradialogue" : "",
      "options" : [],      
  },

  "Place Plushie" : {
      "title" : "",
      "description" : "You place the plushie and hear a sudden rumbling. You step back and spot movements from afar… what will you do next?",
      "extradialogue" : "",
      "options" : ["Hide behind a Tree", "Hide behind a pebble", "Confront the upcoming threat"],      
  },

  "Confront the upcoming threat" : {
      "title" : "",
      "description" : "You run towards the speeding object. The bushes in front of you suddenly part and out comes a pachycephalosaurus running full speed straight at you. It rams it’s head straight into your face, killing you instantly.",
      "extradialogue" : "",
  },

  "Hide behind a Tree" : {
      "title" : "",
      "description" : "You hid behind a tree. Suddenly, you get struck in the back. You look behind you and see a pachycephalosaurus. What will you do next?",
      "extradialogue" : "",
      "options" : ["Attack (Ief ya haz za dager)", "Run towards Dwayne the rock"],      
  },

  "Hide behind a pebble" : {
      "title" : "",
      "description" : "You hid behind a pebble…are you stupid? Suddenly, you get struck in the back. You look behind you and see a pachycephalosaurus. What will you do next?",
      "extradialogue" : "",
      "options" : ["Attack (Ief ya haz za dager)", "Run towards Dwayne the rock"],            
  },

  "Attack (Ief ya haz za dager)" : {
      "title" : "",
      "description" : "You try to attack the dino and miss… damn you're really bad with the dagger huh? What will you do now? (tip: you’re absolute trash at almost everything you do except running so think carefully of what you're about to do.)",
      "extradialogue" : "",
      "options" : ["Attack AGAIN", "Run away"],      
  },

  "Attack AGAIN" : {
      "title" : "",
      "description" : "You tried to attack the dino again and… IT HITS! but what’s this??? The dino seems to have pulled an uno reverse card. You get rekt and get your skull crushed…",
      "extradialogue" : "",
  },

  "Run away" : {
      "title" : "",
      "description" : "You try to run away…but the dino is too fast for you. You get trampled underfoot.",
      "extradialogue" : "",
  },

  "Run towards Dwayne the rock" : {
      "title" : "",
      "description" : "You run towards Dwayne the rock. You get trapped between the rock and the dino…You didn’t really think this through, did you?",
      "extradialogue" : "",
      "options" : ["Stay in place (and die)", "Jump out of the way"],      
  },

  "Stay in place (and die)" : {
      "title" : "",
      "description" : "You stay in your place and die…Seriously, what did you expect? Some secret ending our something?",
      "extradialogue" : "",
  },

  "Jump out of the way" : {
      "title" : "",
      "description" : "You run towards Dwayne the rock and quickly hop aside for it to break the rock with its vulnerable skull… you monster… The dino which was chasing now laid dead right in front of you as you stare at it’s cold dead body… well… At least the paths opened up. Where will you go next?",
      "extradialogue" : "",
      "options" : ["Go Further North", "Go back South"],      
  },

  "Go Further North" : {
      "title" : "",
      "description" : "You head further up north and spot a nice small pond with steam coming from it. You spot something shiny in the pond. It seems like a part of the time machine! O-o",
      "extradialogue" : "You go into the pond and grab the piece and think to yourself: I should probably head back to the captain now and report back to him… What will you do?",
      "options" : ["Chill for a bit in the pond", "Go back to the Captain"],      
  },

  "Chill for a bit in the pond" : {
      "title" : "",
      "description" : "You chill in the pond (and heal up completely(if you fought the dino)). You check your watch and see that you're running out of time. You should hurry back now…",
      "extradialogue" : "",
      "options" : ["Chill longer in the pond", "Go back to the captain"],      
  },

  "" : {
      "title" : "",
      "description" : " You chill for even longer and start losing track of time. You are really cutting it close now if you don’t leave now you might not be able to make it back in time!!!",
      "extradialogue" : "",
      "options" : ["Chill EVEN longer in the pond", "Go back to the captain"],      
  },

  "" : {
      "title" : "",
      "description" : "You completely lose track of time and chill there for eternity. You've become the chill master and decide to live a nice peaceful life in the pod… after a couple of years you start devolving into a human fish and start to peacefully sink into the water whereby it suddenly starts raining… The rain drags you into the ocean where you see the captain still waiting for his boy to one day return… you swim past the ship explore a whole new world before you and live peacefully among the fish (You’ve unlocked the secret Chill ending)",
      "extradialogue" : "",
  },

  "Go back to the captain" or "Go back to ship and set sail": {
      "title" : "",
      "description" : "You go back to the Black Pearl and spot the captain waiting for you patiently. The captain tells you his crew found another clue regarding the next piece which is towards the south.",
      "extradialogue" : "Your at open sea and decide to go to the following area:",
      "options" : ["Go East(Back to Crater)", "Go West (Dino Jungle Island)", "Go South"],      
  },

  "Go south" : {
      "title" : "",
      "description" : "You told the captain to set sail towards the south and spot an island with weird looking buildings. You think to yourself that there might be some sort of civilization going on here and head to land. The captain tells you to go ahead and says he’ll stay behind to search for more clues",
      "extradialogue" : "",
      "options" : ["Go back to ship and set sail", "Go into the woods"],      
  },

  "Go into the woods" : {
      "title" : "",
      "description" : "(If you don’t have a dagger in inventory) To go further into the woods it seems like you may need something sharp to be able to continue… (Maybe a dagger of some sorts that was left behind at the pirate camp).",
      "extradialogue" : f"(If you do have a dagger in your inventory)You go into the woods and suddenly feel dizzy and faint…OOF (Damn ur really weak).\nYou wake up after a while and feel your hands and feet tied tightly. You wake up in a cell and see weird dudes in old loki looking gear and speak in a language you can’t seem to understand.. after a while they leave you alone since you don’t seem to understand a thing. You look around the dark, dim and grimy cell. You see nothing but dirt, moss and sh*t.\nWhat now? Are you gonna die!? Are you gonna starve to death!?!? Are you gonna be sacrificed to some f*cked up GOD!?!?!??!??! BUT WAIT, calm down {name}…No need for a panic attack…The guards haven’t seemed to search your pockets and it appears you may have something up your sleeve…quite literally…it’s ya dagger…What will you do?",
      "options" : ["Use your dagger"],      
  },

  "Use your dagger" : {
      "title" : "",
      "description" : "You use the dagger which suddenly appears to have a switch it turns out it was never turned on to begin with… You turn the dagger on and use it to cut loose. Your FREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE.\n.\n.\n.\n.\n.",
      "extradialogue" : " well… kind off… you still have to get out of the cell somehow…\nyou see a guard next to the cell sleeping with his boxers down…how- why- wha-...ignoring that, he seems to have keys in his hand…what will you do?",
      "options" : ["KILL HIM!", "Try to pry the keys out of his hands"],      
  },

  "KILL HIM!" : {
      "title" : "",
      "description" : "You kill the guard…but he managed to screech tao alort thu other guardas and onw you hev ta fihgt thom oar dies trying…you die trying… (it seems as if the person who wrote this had a stroke… just ignore it please…you’ll just hurt yourselves and your last two brain cells will fade to dust by reading this leaving you with one functional brain cell #mathematics #QuickMaths…ROASTED!!!!!)",
      "extradialogue" : "",
  },

  "Try to pry the keys out of his hands" : {
      "title" : "",
      "description" : "You pry the keys out of his hands without waking the guard up and open up the locked cell door…what the h*ll are you gonna do now that you are once again a free human!?",
      "extradialogue" : "(well first try to get past the guards except if you wanna die)",
      "options" : ["Make a run for it", "Slowly AND quietly pass the guards"],      
  },

  "Make a run for it" : {
      "title" : "",
      "description" : "You run away as fast as you can…you get intercepted by the guards…they call the army and generals…let’s just say they weren’t nice to you, m’kay? (please for your sanity and ours, don’t question it) you start running in any direction you can and see a building in the distance in which you can take shelter. you B-Line straight to the building and seem to be able to shake those guards of your tail.",
      "extradialogue" : "You arrive at the building and spot lots and lots of people who seem to be dressed in long robes and are reading books?? You appear to have arrived at a sort of library? There’s someone who looks like Einstein and another guy who’s painting in a corner which seems to be Leonardo Da Vinci and see someone else who seems like Will Smith??? What’s he doing here? What will you do?",
      "options" : ["Talk to Einstein", "Talk to Da Vinci", "Talk to WILL FREAKING SMITH NOW!!!"],      
  },

  "Slowly AND quietly pass the guards" : {
      "title" : "",
      "description" : "You walk veeeeeeeeeeeeeery slooooooooooooooowly and barely manage to sneak past the guards and head to what seems to be an exit. you reached the exit but suddenly hear an alarm going off o-o (THEY HAVE ALARM SYSTEMS???) you start running in any direction you can and see a building in the distance in which you can take shelter. you B-Line straight to the building and seem to be able to shake those guards of your tail.",
      "extradialogue" : "You arrive at the building and spot lots and lots of people who seem to be dressed in long robes and are reading books?? You appear to have arrived at a sort of library? There’s someone who looks like Einstein and another guy who’s painting in a corner which seems to be Leonardo Da Vinci and see someone else who seems like Will Smith??? What’s he doing here? What will you do?",
      "options" :["Talk to Einstein", "Talk to Da Vinci", "Talk to WILL FREAKING SMITH NOW!!!"],     
  },

  "Talk to Einstein" : {
      "title" : "",
      "description" : "You head towards Einstein who seems to be working on a formula which doesn’t seem to be complete yet. Einstein sees you and greets you:",
      "extradialogue" : f"Einstein: Well and who might you be? Ah welcome to the school of Athens {name} All of us who gather here love to study and discuss lots of science together or we get together for a nice chat once in a while… Anyway, enough about this place. To what do I owe the pleasure of your visit here?",
      "options" : ["(Truth) I’ve come to seek shelter from guards", "(Lie) I’ve come to seek knowledge"],      
  },

  "Talk to Da Vinci" : {
      "title" : "",
      "description" : "You head towards Da Vinci who seems to be working on a painting which doesn't seem to be finished yet. Da Vinci sees you and greets you:",
      "extradialogue" : f"Da Vinci: Well and who might you be? Ah welcome to the school of Athens {name} All of us who gather here love to study and discuss lots of science together or we get together for a nice chat once in a while… Anyway, enough about this place. To what do I owe the pleasure of your visit here?",      "options" : ["(Truth) I’ve come to seek shelter from guards", "(Lie) I’ve come to seek knowledge"],      
  },

  "Talk to WILL FREAKING SMITH NOW!!!" : {
      "title" : "",
      "description" : "You head towards Will Smith who seems to be doing Will Smith things. Will Smith sees you and greets you:",
      "extradialogue" : f"Will Smith: Well and who might you be? Ah welcome to the school of Athens {name} All of us who gather here love to study and discuss lots of science together or we get together for a nice chat once in a while… Anyway, enough about this place. To what do I owe the pleasure of your visit here?",
      "options" : ["(Truth) I’ve come to seek shelter from guards", "(Lie) I’ve come to meet you"],      
  },

  "Truth:" : {
      "title" : "",
      "description" : "Well that’s a pretty shocking announcement isn’t it… I could turn you in and get a handsome reward so… I’ll give you a chance to prove yourself by doing a QUIZ!!! if you fail I'll tell you but if you succeed you are welcome to stay here and be a part of the school of Athens. so… shall we begin?",
      "extradialogue" : "Question 1:\nWhat is missing from Einstein’s Formula? (E=2)\na)Minecraft\nb)Mc\nc)EEEEEEEeeeee\nd)=\n\nQuestion 2:\nWhat is Will Smith’s last name?\na)Bald\nb)SmIth\nc)Smith\nd)One Punch Man\n\nQuestion 3:\nWaar is Leonardo Da Vinci Bekend voor?: (Editors note: ze zijn allemaal correct)\na)Zijn Anatomische Kennis\nb)Als Uitvinder\nc)Als Architect\nd)Als Natuurkundige",
      "options" : ["bcb, dab, cad, dca, dbc"],      
  },

  "Lie" : {
      "title" : "",
      "description" : "Einstein/Da Vinci/Will Smith: Now don't lie to me. Tell me, why are you here",
      "extradialogue" : "",
      "options" : ["Tell the truth"],      
  },

  "dab" or "cad" or "dca" or "dbc" : {
      "title" : "",
      "description" : "Well… I think you could do better so how about we try again? I know you know it so let’s just get it right this time shall we?",
      "extradialogue" : "",
      "options" : ["Truth"],      
  },

  "bcb" : {
      "title" : "",
      "description" : "Einstein/Da Vinci: Wow I guess you’re smarter than you seem! You seem to even know the answer to my/Einstein's Formula u really smart! it’s almost as if you’re from the future or something and are able to search up the answers to the questions. We can’t let you go empty handed ofcourse so here take this!\n\n*You received the second Part of the machine!*\n\nWe found it lying around in the bushes and thought it’s part of an elaborate machine. Well we hope to see you again you are on your way now!",
      "extradialogue" : "Will Smith: Nice you smart. you are very smart… So uhhh… I found this shiny thing and since you completed the quiz i thought i should give it to you as a reward here ya go! You received the 2nd Piece of the Machine! aight well i’ll see ya around!\n\nYou stand there in the school and head out to go back to the ship. Once you arrive at the ship the captain tells you he got some good news for ye. You go aboard and check it out Captain  Edward ‘Moose’ Teach found the third piece of the machine while you were out and about!!! WHAT?!! you’ve got all the parts now and are ready to head back to the crater. You start sailing back to the ocean whilst the captain asks for your direction which way will you go?",
      "options" : ["South(School of Athens)", "West (Crater and Pirate camp)", "East (Dino Island)"],      
  },

  "West (Crater and Pirate camp)" : {
      "title" : "",
      "description" : "You head West and arrive back at the beach where will you go next?",
      "extradialogue" : "",
      "options" : ["Pirate Camp", "Back to the Time Machine"],      
  },

  "Back to the Time Machine" : {
      "title" : "",
      "description" : "You head to the crater and check the manual. You realize that it seems like a huge project and can’t seem to do it on your own in the amount of time that’s left. You check your watch and it says you only have 8 hours left to figure this out… If only there were smart people who would be able to help you with rebuilding the machine…",
      "extradialogue" : "",
      "options" : ["Go back to South(School of Athens)"],      
  },

  "Go back to South(School of Athens)" : {
      "title" : "",
      "description" : "You head back to Athens and arrived there safe and sound. While going to the school of Athens you think of your experience so far and what you think of it and look back at the friends you’ve made along the way. You finally Arrive at the School of Athens and ask the scholars for help with rebuilding the time machine. They agree because you’ve completed the uncompletable quiz and would gladly help a genius such as yourself. You head back and board the ship and go back all the way to the crater… you think to yourself whilst on the boat what a wild adventure you’ve been on and start to question your life… have I really just wasted some of my time i’ll never get back again? yes… yes I have… Was it worth it? Probably not, but in the end did I have fun? That's only a question YOU dear player can answer… ",
      "extradialogue" : "You arrive at the crater where the Scholars try to encrypt the language and fix up the time machine. you have 1 Hour left, how will you spend it? Will you say goodbye and greet everyone for one last time or just ditch them?",
      "options" : ["Ditch them", "Say your goodbye’s"],      
  },

  "Ditch them" : {
      "title" : "",
      "description" : "You try to ditch them but the 4th wall has been broken and you get stopped by the creators of the game. you are not able to ditch them please greet them…",
      "extradialogue" : "",
      "options" : ["Say your goodbye’s"],      
  },

  "Say your goodbye’s" : {
      "title" : "",
      "description" : "you say your goodbye to everyone and thank the captain for his immense help on this trip. The captain says: No worries Laddy. I'm glad I'm able to help if it ain’t on the name of the Moose I’ll always be with ye… I'll miss ya kiddo. You say your goodbyes to the crew who helped you reach your destination and eventually say your goodbyes to the scholars who helped you fix the machine. You set your last step into the machine and as you do you wave to all the people who’ve gathered around you you step into the machine and start pulling the levers and pressing the buttons as it says in the manual that was written by professor Hunter. There’s a white flash before you and you slowly open your eyes… you smell a big stinky odor coming from outside and see the professors standing right before you YOU'VE MADE IT BACK!!! You’re finally back home… ",
      "extradialogue" : "Professor Hunter: Welcome back! How was the trip? Did my manual help at all? I’m glad you’ve made it safely back. It’s good to see you again. you can go through the left door exit to try and avoid Prof JerkMoose so you can end this nice and quietly! we’ll ask you back for a later date to answer some of our questions. you must be exhausted you may go now!",
      "options" : ["Leave Quietly", "Go by Professor JerkMoose"],      
  },

  "Leave Quietly" : {
      "title" : "",
      "description" : "Professor JerkMoose: Now hold up my Padawan where do you think you’re going?",
      "extradialogue" : f"you spot a parrot in a cage next to him it seems very familiar...IT’S THE PARROT FROM THE TENT!!\n\n {name}: HEY! THAT'S THE PARROT THAT RAN AWAY FROM ME IN THE WEIRD TIME ZONE YOU SENT ME TO!!!\n Professor JerkMoose: Ooooh! That parrot was from my great great great something grandfather! Edward ‘Moose’ Teach, otherwise known as BLACKBEARD! Most feared pirate in the seven seas! Captain of the BLACK PEARL! He is my HERO! And I learned my cussing from his journal! He was cursing a lot about some idiot that got stranded and needed some weird*ss machine fixed but I don’t get that part…Anyways, it’s good that you're back! Go home, my Padawan, tomorrow's a new day, and of course, A BRAND NEW ADVENTURE!!!\n\n",
      "options" : ["Go Home"],      
  },

  "Go by Professor JerkMoose" : {
      "title" : "",
      "description" : f"Professor JerkMoose: Why hello, my young Padawan.\nWhile walking to Professor JerkMoose, you spot a parrot in a cage next to him that seems very familiar...IT’S THE PARROT FROM THE TENT!!\n\n {name}: HEY! THAT'S THE PARROT THAT RAN AWAY FROM ME IN THE WEIRD TIME ZONE YOU SENT ME TO!!!\n Professor JerkMoose: Ooooh! That parrot was from my great great great something grandfather! Edward ‘Moose’ Teach, otherwise known as BLACKBEARD! Most feared pirate in the seven seas! Captain of the BLACK PEARL! He is my HERO! And I learned my cussing from his journal! He was cursing a lot about some idiot that got stranded and needed some weird*ss machine fixed but I don’t get that part…Anyways, it’s good that you're back! Go home, my Padawan, tomorrow's a new day, and of course, A BRAND NEW ADVENTURE!!!\n\n",
      "extradialogue" : "",
      "options" : ["Go Home"],      
  },

  "Go Home" : {
      "title" : "",
      "description" : "You head out onto the streets heading back home. Once home you stretch out and lay in bed… you think to yourself… man… that felt like a fantasy dream… and fell asleep!\n\n\n",
      "extradialogue" : "We hope you enjoyed our Text Adventure game\n\n\bJoshua L. & Bo H. 4H3 2021-2022 :)",
  }
}

def etc():
    print(f'\n{cr.Fore.WHITE}Press [ENTER] to continue')
    input()

#definition player movement
def move_player(move_action):
    player.location = move_action
 
#the game "engine"
def game(room):
  currentRoom = rooms[room]

  # get this room's title and description
  title = currentRoom["title"]
  description = currentRoom["description"]  
  extradialogue = currentRoom["extradialogue"]
  options = currentRoom["options"] 

  # show to user
  print(f"{title}")
  print()
  print(description)
  print("What will you do...?")  
  print(extradialogue)
  print()
  print("Options: " + ", ".join(options))
  nextRoom = input()

  #TODO: check and sanitize input
  
  # go to next room
  game(nextRoom)

#start the game from the Origin room
game("Home")