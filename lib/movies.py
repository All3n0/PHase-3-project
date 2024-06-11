class Movie:
    def __init__(self,id,title,genre,director,chief_crew,actors):
        self.id=id
        self.title=title
        self.genre=genre
        self.director=director
        self.chief_crew=chief_crew
        self.actors=actors
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        if not isinstance(id,int):
            raise TypeError('id must be an integer')
        self._id=id
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        if len(title)<2:
            raise ValueError('title must be at least 2 characters')
        self._title=title
    @property
    def genre(self):
        pass
    @property
    def director(self):
        pass
    def __repr__(self):
        return f'<Movie {self.title}>'  