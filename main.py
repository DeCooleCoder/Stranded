#Idea 1: Your stranded from a time machine and are stranded between timelines So there may be dino's or medieval knights or dragons to conquer

# all the rooms!
rooms = {
  "Home" :  {
    "title" : "Home",
    "description" : "You hear your alarm going off,",
    "options": ["Wake up", "Stay asleep"],
  },

  "Wake up" :  {
      "title" : "You wake up in your bedroom and check your agenda. You see you made an appointment with the professors today to test their new invention out.",
      "description" : "You should head out right about now… Though the Market has just opened. Maybe they have some good deals? But you wouldn't want to be late ate the lab...",
      "options": ["Market", "Lab"]
  },

  "Market" :  {
    "title" : "Market",
    "description" : "",
    "options": ["a", "b"]
  },

  "The Lab" :  {
    "title" : "The Lab",
    "description" : ""
  },
    
  "Crater" :  {
    "title" : "Crater",
    "description" : "You start regaining your consciousness. Your blurry vision starts to clear and you observe your surroundings. You are in the middle of a crater filled with junk metal, machine parts and other bits and odds.",
     "Options": ["aap", "noot"]
  }
}

#the game "engine"
def game(room):
  currentRoom = rooms[room]

  # get this room's title and description
  title = currentRoom["title"]
  description = currentRoom["description"]  
  options = currentRoom["options"]

  # show to user
  print(f"{title}")
  print()
  print(description)
  print("What will you do...?")  
  print()
  print("Options: " + ", ".join(options))
  nextRoom = input()

  #TODO: check and sanitize input
  
  # go to next room
  game(nextRoom)

#start the game from the Origin room
game("Home")