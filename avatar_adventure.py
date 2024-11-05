#debugging lab
#  import pdb
#creating characters and elemts
class Character: 
    def __init__(self, name, house,):
        self.name = name
        self.house = house

    def introduce(self):
        return f"my name is {self.name}, and I am a {self.house} ."

#character objects
Harry = Character("Harry", "Gryffindor")
Cho = Character("Cho", "Ravenclaw")
Cedric = Character("Cedric", "Hufflepuff")

def journey_to_house(character):
    if character.house == "Gryffindor":
        return "Harry flies with Buckbeak"
    elif character.house == "Ravenclaw":
        return "Cho creates a patronous"
    elif character.house == "Hufflepuff":
        return "Cedric helps Harry during Tri-wizard cup."
    
# pdb.set_trace()

#simulate journey
print(Harry.introduce())
print(journey_to_house(Harry))
print(Cho.introduce())
print(journey_to_house(Cho))
print(Cedric.introduce())
print(journey_to_house(Cedric))