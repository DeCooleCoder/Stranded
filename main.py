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
      "options" : [],
  },

  "Wake up" :  {
      "title" : "You wake up in your bedroom and check your agenda. You see you made an appointment with the professors today to test their new invention out.",
      "description" : "You should head out right about now…you wouldn't want to be late at the lab...",
      "extradialogue": "Note: Press S to Stay at Home and Press N to go to the Lab",
      "options": ["Lab / Stay at Home"],
  },

  "Stay at Home" : {
      "title" : ""
  },

  "Lab" :  {
    "title" : "The Lab",
    "description" : "You arrive at the Lab and see 2 doors waiting for you. Both have a sign. One saying “THE SMART AND AMAZING PROFESSOR ” and the other “The Man”. Which will you open first?",
    "extradialogue" : "Note: Type N for Open door THE SMART AND AMAZING PROFESSOR and Type S for Open door The Man",
    "options": ["THE SMART AND AMAZING PROFESSOR's office", "The Man's office"],
  },

"The Man's office" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],    
},

 "THE SMART AND AMAZING PROFESSOR's office" :  {
   "title" : "THE SMART AND AMAZING PROFESSOR's office",
   "description" : "Professor Hunter: Hello and welcome to our lab. I’m professor Hunter and this is where we do all of our very scientific experiments and take our jobs very seriously. We have never made a SINGLE mistake so you don’t have to worry about your safety ;) So… what was your name again?",
   "extradialogue" : f"Professor Hunter: ...Riiight gotcha… so… {name} Have you met the other professor yet? Note: Type M to speak to professor Jerkmoose and Press N to continue talking to professor Hunter",
   "options" : ["M", "N"]
 },
    
  "Crater" :  {
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

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },

  "" : {
      "title" : "",
      "description" : "",
      "extradialogue" : "",
      "options" : [],      
  },
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

def game_loop():
 #controls
 wdywd = input('> ')
 if wdywd.lower() == 'n':
   if wdywd.capitalize() not in locations[player.location][exits]:
     delay_print("You cannot go that way!")
     etc()
   else:
    move_action = locations[player.location][N]
    move_player(move_action)
 elif wdywd.lower() == 'e':
   if wdywd.capitalize() not in locations[player.location][exits]:
    delay_print("You cannot go that way!")
    etc()
   else:
    move_action = locations[player.location][E]
    move_player(move_action)
 elif wdywd.lower() == 's':
    if wdywd.capitalize() not in locations[player.location][exits]:
        delay_print("You cannot go that way!")
        etc()
    else:
     move_action = locations[player.location][S]
     move_player(move_action)
 elif wdywd.lower() == 'w':
    if wdywd.capitalize() not in locations[player.location][exits]:
        delay_print("You cannot go that way!")
        etc()
    else:
        move_action = locations[player.location][W]
        move_player(move_action)
 elif wdywd.lower() == 'g':
        get()
 elif wdywd.lower() == 'd':
        drop()
 elif wdywd.lower() == 'i':
        show_inventory()
 elif wdywd.lower() == 'q':
            quit()
 else:
   delay_print('You can\'t do that! Try something else...')
   etc()

def quit():
    global isGameRunning
    os.system('clear')