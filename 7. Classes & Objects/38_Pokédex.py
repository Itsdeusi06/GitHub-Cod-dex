class Pokemon:
    def __init__(self, entry, name, types, description, is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    def speak(self):
        print(self.entry,self.name,self.types,self.description,self.is_caught, 'this is what',self.name,'says alsways',self.name, self.name)
        return print

Picka = Pokemon(25, 'Pikachu', 'Electric', 'cute and main pokemon', True)
Picka.speak()