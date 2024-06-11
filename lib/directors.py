class Director:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        if not isinstance(id,int):
            raise TypeError('id must be an integer')
        self._id=id
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if len(name)<2:
            raise ValueError('name must be at least 2 characters')
        self._name=name
    def movies(self):
        pass
    def __str__(self):
        return f'<Director {self.name}>'