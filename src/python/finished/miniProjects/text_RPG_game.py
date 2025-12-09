import re
from random import randint

def get_input():
  # The main part of the say function down below. Say is still there so 
  def sentence():
    # After say, if there are quotes:
    if noun[0] == "\"":
      list = []
      # Iterate through command
      for i in range(1,len(command)):
        # Add substring (word) to list
        list.append(command[i])
        # If the last character of the current substring (word) is a quote, end the loop
        if command[i][len(command[i])-1] == "\"":
          break
      if list[-1][-1] != "\"":
        print("> Your speech must start and end with a double quotation mark: \"")
        return
      # Join the words with spaces to form a sentence
      sentence = " ".join(list)
      # If the command is longer than i + 1, 2, 3
      # If length of command is greater than i from the if statement + 1,2,3
      if len(command) > i+1:
        # If the word after the end quote is 'to'
        # If the word after the end quote is 'to'
        if command[i+1] == "to":
          if len(command) > i+2:
            if command[i+2] == "the":
              if len(command) > i+3:
                # If the word 2 words after the end quote (the noun) is a GameObject
                # If the 3rd word after the end quote (the noun) is a GameObject
                if command[i+3] in GameObjects.objects:
                  say(sentence)
                  pick = []
                  # Iterate through all sprites
                  for sprite in Sprites.sprites:
                    # Pick the ones that match the description
                    if Sprites.sprites[sprite]._class_name == command[i+3]: 
                      pick.append(Sprites.sprites[sprite].ID)
                  # Choose one of them
                  chosen = pick[randint(0,len(pick)-1)]
                  # Respond to the phrase
                  print(Sprites.sprites[chosen].response)
                  return
                else:
                  print("> Unknown recipient \"" + command[i+3] + "\"")
                  return
              else:
                print("> Please specify who/what you are talking to")
                thing = input()
                if thing[0:3] == "the":
                  thing = thing[4:]
                if thing in GameObjects.objects:
                  say(sentence)
                  pick = []
                  # Iterate through all sprites
                  for sprite in Sprites.sprites:
                    # Pick the ones that match the description
                    if Sprites.sprites[sprite]._class_name == thing: 
                      pick.append(Sprites.sprites[sprite].ID)
                  # Choose one of them
                  chosen = pick[randint(0,len(pick)-1)]
                  # Respond to the phrase
                  print(Sprites.sprites[chosen].response)
                  return
                # If a named sprite
                elif thing in Sprites.sprites:
                  say(sentence)
                  # Print its response
                  print(Sprites.sprites[thing].response)
                  return
                else:
                  print("> Unknown recipient \"" + thing + "\"")
                  return
            # If a named sprite
            elif command[i+2] in Sprites.sprites:
              say(sentence)
              # Print its response
              print(Sprites.sprites[command[i+2]].response)
              return
            else:
              print("> Unknown recipient \"" + command[i+2] + "\"")
              return
          else:
            print("> Please specify who/what you are talking to")
            thing = input()
            if thing[0:3] == "the":
              thing = thing[4:]
            if thing in GameObjects.objects:
              say(sentence)
              pick = []
              # Iterate through all sprites
              for sprite in Sprites.sprites:
                # Pick the ones that match the description
                if Sprites.sprites[sprite]._class_name == thing: 
                  pick.append(Sprites.sprites[sprite].ID)
              # Choose one of them
              chosen = pick[randint(0,len(pick)-1)]
              # Respond to the phrase
              print(Sprites.sprites[chosen].response)
              return
            # If a named sprite
            elif thing in Sprites.sprites:
              say(sentence)
              # Print its response
              print(Sprites.sprites[thing].response)
              return
            else:
              print("> Unknown recipient \"" + thing + "\"")
              return
        else:
          say(sentence)
          return
      else:
        say(sentence)
        return
    else:
      print("> Your speech must start and end with a double quotation mark: \"")
      return
      
  inp=input("> What would you like to do?: ") # Get input from user
  command = inp.split() # Split input into words
  verb_word = command[0] # Verb is the first word
  if verb_word in verb_dict: # Checking if we know verb
    verb = verb_dict[verb_word] # If verb_word recognised, set it to verb
  elif verb_word in End: # If player wants to stop
    raise ZeroDivisionError # To break out of while loop
  else: 
    print("> Verb \"{}\" unknown".format(verb_word)) # Unknown verb
    return
  if len(command) >= 2: # More than one word
    if (verb == "attack" or verb == "examine") and command [1] == "the":
      noun = command[2]
    else:
      noun = command[1] # Declaring noun
    if verb == attack and command[1] == "Acorpseinprogress": #easter egg
        print("> You dare try to attack me?")
        test2.health = 0
        raise ZeroDivisionError
    elif verb == say:
      sentence()
      if len(command) == 4:
        if verb == say and command[1] == "\"hi\"" and command[2] == "to" and command[3] == "Acorpseinprogress":
          print("He says hi back ;)")
    else: # Easter eggs out of way, do thing
      print(verb(noun))
  else:
    print("> You can\'t just {0}, you have to {0} something".format(verb_word))

def randomLine(p1, p2, p3, p4):
  num = randint(1, 4)
  if num == 1:
    return p1
  if num == 2:
    return p2
  if num == 3:
    return p3
  if num == 4:
    return p4

def say(noun):  # Defining say command
  nothing = ""
  if noun != nothing:
    print("You said " + noun)
  else:
    print("You said nothing")
  
def attack(noun): # Defining the attack command
  # Check if noun is player, etc  
  if noun in GameObjects.objects:
      pick = []
      # Iterate through all sprites
      for sprite in Sprites.sprites:
        # Pick the ones that match the description
        if Sprites.sprites[sprite]._class_name == noun: 
          pick.append(Sprites.sprites[sprite].ID)
      # Choose one of them
      chosen = pick[randint(0,len(pick)-1)]
      # Death
      # Take 1 away from health
      if Sprites.sprites[chosen].health > 0:
        Sprites.sprites[chosen].health -= 1
        line1 = "You strike true"
        line2 = "You graze its skin"
        line3 = "The " + chosen + " fails to dodge"
        line4 = "You hit"
        if Sprites.sprites[chosen].health == 0:
          line01 = "It collapses"
          line02 = "You watch the life leave its eyes"
          line03 = "The " + chosen + " collapse"
          line04 = "IDK filler line bro this ain\'t permanent anyway"
          return randomLine(line1, line2, line3, line4) + "\n" + randomLine(line01, line02, line03, line04)
        return randomLine(line1, line2, line3, line4)
      else:
        line1 = "It makes a squelching sound"
        line2 = "Do you feel good about attacking a dead body?"
        line3 = "You attack the dead body"
        line4 = "It still lies there"
        return randomLine(line1, line2, line3, line4)
    # If a named sprite
  elif noun in Sprites.sprites:
    # Take 1 away from health
    if Sprites.sprites[noun].health > 0:
      Sprites.sprites[noun].health -= 1
      line1 = "You strike true"
      line2 = "You graze its skin"
      line3 = "The " + noun + " fails to dodge"
      line4 = "You hit"
      if Sprites.sprites[noun].health == 0:
        line01 = "It collapses"
        line02 = "You watch the life leave its eyes"
        line03 = "The " + noun + " collapses"
        line04 = "With that strike, you foe is defeated"
        return randomLine(line1, line2, line3, line4) + "\n" + randomLine(line01, line02, line03, line04)
      return randomLine(line1, line2, line3, line4)

    else:
      line1 = "It makes a squelching sound"
      line2 = "Do you feel good about attacking a dead body?"
      line3 = "You attack the dead body"
      line4 = "It still lies there"
      return randomLine(line1, line2, line3, line4)
      
def examine(noun):
  if noun in GameObjects.objects:
    pick = []
    # Iterate through all sprites
    for sprite in Sprites.sprites:
      # Pick the ones that match the description
      if Sprites.sprites[sprite]._class_name == noun: 
        pick.append(Sprites.sprites[sprite].ID)
    # Choose one of them
    chosen = pick[randint(0,len(pick)-1)]
    return Sprites.sprites[chosen].desc
  elif noun in Sprites.sprites:
    return Sprites.sprites[noun].desc
  else:
    return "Unknown noun \"" + noun + "\""
    
class GameObjects(): # Class for all game objects
  _class_name="" # Instantising these now for later subclasses
  desc=""
  objects={}
  def __init__(self, name): # Instantiating objects
    self.name = name # Creating the name method
    GameObjects.objects[self._class_name]=self # Adding class_name to the dictionary obejcts assigning it to the instance
  def get_desc(self):
    return(self._class_name+"\n"+self.desc) # Defining the get desc function

class Sprites(GameObjects):
  sprites={}
  def __init__(self, name, ID, health, ac, atkbonus):
    super().__init__(name)
    self.health = health
    self.ac = ac
    self.atkbonus = atkbonus
    self.ID = ID
    Sprites.sprites[self.ID] = self

class Goblin(Sprites):
  def __init__(self, name, ID, health, ac, atkbonus):
    self._class_name="goblin" # Class name
    self._desc = "A foul creature" # Class description
    super().__init__(name, ID, health, ac, atkbonus) # Instantising the object as an object of GameObjects as well as giving it the name method

  @property # Allows calling as method, and not func
  def desc(self): # Defining the desc func
    if self.health >= 3: # Full health
      return self._desc
    elif self.health == 2:
      health_line = "It has a cut on its knee"
    elif self.health == 1:
      health_line = "Its arm has been cut off"
    elif self.health == 0:
      health_line = "It\'s dead... You know it had a family right? You Monster."
    return self._desc+"\n"+health_line

  @property # Allows calling as method, and not func
  def response(self): # Defining the desc func
    if self.health >= 3: # Full health
      line1 = "The goblin grunts back"
      line2 = "It looks in your direction, confused"
      line3 = "It picks its nose"
      line4 = "It spits on the ground"
      return randomLine(line1, line2, line3, line4)
    elif self.health == 2:
      line1 = "The goblin whimpers and spits at you"
      line2 = "The goblin growls back"
      line3 = "It tries to keep you at a distance"
      line4 = "It looks angry"
      return randomLine(line1, line2, line3, line4)
    elif self.health == 1:
      line1 = "The goblin grunts and snarls at you, with crazed eyes"
      line2 = "The goblin stares you down"
      line3 = "It looks scared"
      line4 = "It looks at you with murderous intent"
      return randomLine(line1, line2, line3, line4)
    elif self.health == 0:
      line1 = "It\'s dead, so you get no response"
      line2 = "Did you expect it to speak? It's dead"
      line3 = "Silence"
      line4 = "The goblin lays still"
      return randomLine(line1, line2, line3, line4)

class Player(Sprites):
  def __init__(self, name, ID, health, ac, atkbonus):
    self._class_name = "player"
    self._desc = "It\'s only you C="
    super().__init__(name, ID, health, ac, atkbonus)

  @property
  def desc(self):
    if self.health >= 3:
      return self._desc
    elif self.health == 2:
      health_line = "You\'ve got a couple bruises and cuts"
    elif self.health == 1:
      health_line = "You\'re just barely alive"
    elif self.health == 0:
      health_line = "... You died. How are you examining yourself?"
    return self._desc+"\n"+health_line

  @property
  def response(self): # Defining the desc func
    if self.health > 0:
      line1 = "Talking to yourself is a sign of intelligence... Not in your case"
      line2 = "Why are you speaking to yourself?"
      line3 = "You could have just thought that"
      line4 = "You look like a crazy person"
      return randomLine(line1, line2, line3, line4)
  
test = Goblin("Testgob", "goblin1", 3, 11, 0)
test3 = Goblin("Testgob2", "goblin2", 3, 11, 0)
test2 = Player("You", "player", 3, 16, 1)
print(GameObjects.objects)
print(Sprites.sprites)
print("======================================================")


End = ("End", "end", "Stop", "stop", "Finish", "finish")
verb_dict={"say":say, "Say":say, "attack": attack, "Attack": attack, "examine":examine, "Examine":examine}

while True:
  try:
    get_input()
  #except IndexError:
   # continue
  except ZeroDivisionError:
    break