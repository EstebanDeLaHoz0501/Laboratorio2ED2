class Aereopuerto:
    def __init__(self, code, name, city, country, lat, lon):
        self.code = code
        self.name = name
        self.city = city
        self.country = country
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return f"{self.code} - {self.name} ({self.city}, {self.country}) | Coordenadas: ({self.lat}, {self.lon})"
        