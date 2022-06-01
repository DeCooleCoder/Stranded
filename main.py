#Idea 1: Your stranded from a time machine and are stranded between timelines So there may be dino's or medieval knights or dragons to conquer

#copy paste room
# "The Lab" :  {
#   "title" : "The Lab",
#   "description" : "",
#   "extradialogue" : "",
#   "options" : []
# },

# all the rooms!
rooms = {
  "Home" :  {
    "title" : "Home",
    "description" : "You hear your alarm going off,",
    "extradialogue": "",
    "options": ["Wake up", "Stay asleep"],
  },

  "Wake up" :  {
      "title" : "You wake up in your bedroom and check your agenda. You see you made an appointment with the professors today to test their new invention out.",
      "description" : "You should head out right about now…you wouldn't want to be late at the lab...",
      "extradialogue": "Note: Press S to Stay at Home and Press L to go to the Lab",
      "options": ["S", "L"],
      "S" = "Lab"
      "L" = "Stay to Home"
  },

  "Stay to Home" : 

  "Lab" :  {
    "title" : "The Lab",
    "description" : "You arrive at the Lab and see 2 doors waiting for you. Both have a sign. One saying “THE SMART AND AMAZING PROFESSOR ” and the other “The Man”. Which will you open first?",
    "extradialogue" : "Note: Type N for Open door THE SMART AND AMAZING PROFESSOR and Type M for Open door The Man",
    "options": ["N", "M"]
    ""
  },

 "N" :  {
   "title" : "THE SMART AND AMAZING PROFESSOR's office",
   "description" : "Professor Hunter: Hello and welcome to our lab. I’m professor Hunter and this is where we do all of our very scientific experiments and take our jobs very seriously. We have never made a SINGLE mistake so you don’t have to worry about your safety ;) So… what was your name again?",
    player.name = input("- "),
   "extradialogue" : f"Professor Hunter: Riiight gotcha… so… {player.name} Have you met the other professor yet? Note: Type M to speak to professor Jerkmoose and Press N to continue talking to professor Hunter",
   "options" : ["M", "N"]
 },
    
  "Crater" :  {
    "title" : "Crater",
    "description" : "You start regaining your consciousness. Your blurry vision starts to clear and you observe your surroundings. You are in the middle of a crater filled with junk metal, machine parts and other bits and odds.",
    "extradialogue": "",
    "Options": ["aap", "noot"]
  }
}

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