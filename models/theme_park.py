class Theme_park:

    def __init__(self, name, recommended_attraction, country, visited = False, id = None):
        self.name = name
        self.recommended_attraction = recommended_attraction
        self.country = country
        self.visited = visited
        self.id = id