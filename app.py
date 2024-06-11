from Database.connection import get_connection
from Database.setup import create_tables
from lib.movies import Movie
from lib.actors import Actor
from lib.crew import ChiefCrew
from lib.directors import Director

def main():
    create_tables()
    movie_name=input("Enter Movie's name: ")
    movie_genre=input("Enter Movie's genre: ")
    movie_director=input("Enter Movie's director: ")
    movie_chief_crew=input(" Movie's chief crew member: ")
    movie_chief_crew_category=input(" chief crew member's category: ")
    movie_actors=input("Enter Movie's main actor: ")
   
    conn=get_connection()
    cursor=conn.cursor()
    #######################################
    cursor.execute('SELECT id FROM actors WHERE name=?',(movie_actors,))
    actor_info=cursor.fetchone()
    if actor_info:
        actor_id=actor_info[0]
    else:
        cursor.execute('INSERT INTO actors(name) VALUES(?)',(movie_actors,))
        actor_id=cursor.lastrowid
    cursor.execute('SELECT id FROM directors WHERE name=?',(movie_director,))
    director_info=cursor.fetchone()
    if director_info:
        director_id=director_info[0]
    else:
        cursor.execute('INSERT INTO directors(name) VALUES(?)',(movie_director,))
        director_id=cursor.lastrowid
    cursor.execute('SELECT id FROM chief_crew WHERE name=? AND category=?',(movie_chief_crew,movie_chief_crew_category))
    chief_crew_info=cursor.fetchone()
    if chief_crew_info:
        chief_crew_id=chief_crew_info[0]
    else:
        cursor.execute('INSERT INTO chief_crew(name,category) VALUES(?,?)',(movie_chief_crew,movie_chief_crew_category))
        chief_crew_id=cursor.lastrowid  
    cursor.execute('INSERT INTO movies(title,genre,director_id,chief_crew_id,actors_id) VALUES(?,?,?,?,?)',(movie_name,movie_genre,director_id,chief_crew_id,actor_id))
    #################################
    conn.commit()
    conn.close()
    movie=Movie(None,movie_name,movie_genre,movie_director,movie_chief_crew,movie_actors)
    display_all()
def display_all():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM movies')
    movies=cursor.fetchall()
    cursor.execute('SELECT * FROM actors')
    actors=cursor.fetchall()
    cursor.execute('SELECT * FROM directors')
    directors=cursor.fetchall()
    cursor.execute('SELECT * FROM chief_crew')
    chief_crew=cursor.fetchall()
    conn.close()
    print("\nMovies:")
    for  movie in movies:
        print(Movie (movie["id"],movie["title"],movie["genre"],movie["director_id"],movie["chief_crew_id"],movie["actors_id"]))
    print("\nActors:")
    for actor in actors:
        print(Actor(actor["id"],actor["name"]))
    print("\nDirectors:")
    for director in directors:
        print(Director(director["id"],director["name"]))
    for chief in chief_crew:
        print(ChiefCrew(chief["id"],chief["name"],chief["category"]))
if __name__=="__main__":
    main()