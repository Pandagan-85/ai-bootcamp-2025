class Country:
    def __init__(self, name, regions = None):
        self.name = name
        self.regions = [ ]
    def add(self, region):
        return self.regions.append(region)

    @property
    def pop(self):
        """The total population of this country"""
        return sum(region.pop for region in self.regions if region.pop is not None)

    @property
    def most_populuous_city(self):
        most_populus_city = None
        max_population = 0
        for region in self.regions:
            for city in region.cities:
                if city.pop > max_population:
                    most_populus_city = city
                    max_population = city.pop
        return most_populus_city

class Region:
    def __init__(self, name, cities = None, pop = 0):
        self.name = name
        self.cities = []

    def add(self, city):
        return self.cities.append(city)

    @property
    def pop(self):
        """Calcola la popolazione totale della regione"""
        return sum(city.pop for city in self.cities if city.pop is not None)


class City:
    """A city"""
    def __init__(self, name, pop=None):
        self.name = name
        self.pop = pop


### Test verifiche - da eliminare prima del push!
italy = Country("Italy")
# print(italy.name)
sicily = Region("Sicily")
# print(sicily.name)

italy.add(sicily)

print(f"le regioni in Italia: {[region.name for region in italy.regions]}")
sicily.add(City("Catania", pop=300_000))
sicily.add(City("Palermo", pop=600_000))


print(f"le città in Sicilia sono: {[(city.name, city.pop) for city in sicily.cities]}")

print(f"la popolazione totale delle città in sicilia è: {sicily.pop}") # dpvrebbe essre 900_000

calabria = Region("Calabria")
calabria.add(City("Reggio Calabria", pop=170_000))
# Aggiungo la nuova regione all'Italia
italy.add(calabria)

print(f"le regioni in Italia {[region.name for region in italy.regions]}")

print(f"la popolazione totale delle Regioni in Italia è: {italy.pop}")


print(f"la città con la popolazione più alta in Italia è: {italy.most_populuous_city.name}")

