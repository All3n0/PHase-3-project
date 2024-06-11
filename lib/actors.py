from Database.connection import get_connection

class Actor:
    def __init__(self,id,name):
        self._id=id
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
        if not isinstance(name,str):
            raise TypeError('name must be a string')
        self._name=name
    @property
    def movies(self):
        from lib.movies import Movie
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
            SELECT m.title,m.genre,m.director_id,m.chief_crew_id,m.actors_id
            FROM movies m
            JOIN actors au ON m.actors_id=au.id
            WHERE au.name=?
    ''',(self.id,))
        movies=cursor.fetchall()
        conn.close()
        if movies:
            return [Movie(movie['id'],movie['title'],movie['genre'],movie['director_id'],movie['chief_crew_id'],movie['actors_id']) for movie in movies]
    def  directors(self):
        from lib.directors import Director
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
            SELECT d.id,d.name
            FROM directors d
            JOIN movies m ON d.id=m.director_id
            JOIN actors au ON m.actors_id=au.id
            WHERE au.name=?
    ''')
        directors=cursor.fetchall()
        conn.close()
        if directors:
            return [Director(director['id'],director['name']) for director in directors]
        else:
            return []
    def __str__(self):
        return f'<Actor {self.name}>'