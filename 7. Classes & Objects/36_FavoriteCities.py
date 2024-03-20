class City:
    def __init__(self, name, county, population, landmarks):
        self.name = name
        self.county = county
        self.population = population
        self.landmarks = landmarks


Torroella = City('Torroella de Montgri', 'Girona', 10000, False)

print(vars(Torroella))


Girona = City('Girona', 'Catalunya', 50000, True)

print(vars(Girona))


Madrid = City('Madrid', 'España', 100000, False)

print(vars(Madrid))
