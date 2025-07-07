from sqlalchemy.orm import Session
from app.models.movie_models import Actor, Director, Genre, Movie
from app.database import Base, SessionLocal, engine
import random

def seed_db(db: Session):
    # Avoid re-seeding
    if db.query(Movie).first():
        print("Database already seeded.")
        return

    # Create 100 Genres
    genres_data = [
        "Action", "Drama", "Sci-Fi", "Horror", "Romance", "Comedy", "Thriller", "Fantasy",
        "Adventure", "Mystery", "Crime", "Biography", "History", "War", "Western",
        "Musical", "Animation", "Documentary", "Family", "Sport", "Film-Noir", "Short",
        "News", "Reality-TV", "Talk-Show", "Game-Show", "Adult", "Superhero", "Zombie",
        "Vampire", "Werewolf", "Alien", "Time Travel", "Post-Apocalyptic", "Dystopian",
        "Utopian", "Space Opera", "Cyberpunk", "Steampunk", "Martial Arts", "Heist",
        "Spy", "Gangster", "Prison", "Courtroom", "Medical", "School", "College",
        "Coming-of-Age", "Romantic Comedy", "Dark Comedy", "Slapstick", "Parody",
        "Satire", "Mockumentary", "Found Footage", "Psychological", "Supernatural",
        "Paranormal", "Ghost", "Demon", "Witch", "Magic", "Fairy Tale", "Mythology",
        "Epic", "Historical Fiction", "Period Drama", "Costume Drama", "Buddy",
        "Road Trip", "Survival", "Disaster", "Natural Disaster", "Monster", "Kaiju",
        "Giant Robot", "Mecha", "Anime", "Manga", "Live Action", "Silent Film",
        "Black and White", "Color", "3D", "IMAX", "Virtual Reality", "Augmented Reality",
        "Interactive", "Experimental", "Avant-Garde", "Art House", "Independent",
        "Foreign", "International", "Regional", "Local", "Underground", "Cult",
        "B-Movie", "Exploitation", "Grindhouse", "Slasher", "Giallo"
    ]
    
    genres = []
    for genre_name in genres_data:
        genre = Genre(name=genre_name)
        genres.append(genre)
    
    db.add_all(genres)
    db.commit()

    # Create 100 Directors
    directors_data = [
        "Christopher Nolan", "Steven Spielberg", "Martin Scorsese", "Quentin Tarantino",
        "Alfred Hitchcock", "Stanley Kubrick", "Francis Ford Coppola", "George Lucas",
        "Ridley Scott", "James Cameron", "Tim Burton", "David Lynch", "Woody Allen",
        "Coen Brothers", "Paul Thomas Anderson", "Wes Anderson", "David Fincher",
        "Denis Villeneuve", "Rian Johnson", "Jordan Peele", "Greta Gerwig", "Chloé Zhao",
        "Bong Joon-ho", "Park Chan-wook", "Wong Kar-wai", "Akira Kurosawa", "Hayao Miyazaki",
        "Pedro Almodóvar", "Lars von Trier", "Terrence Malick", "Charlie Kaufman",
        "Spike Jonze", "Michel Gondry", "Darren Aronofsky", "Guillermo del Toro",
        "Alejandro González Iñárritu", "Alfonso Cuarón", "Gaspar Noé", "Nicolas Winding Refn",
        "Yorgos Lanthimos", "Robert Eggers", "Ari Aster", "Robert Zemeckis", "Ron Howard",
        "Clint Eastwood", "Mel Gibson", "Kevin Costner", "Ben Affleck", "George Clooney",
        "Bradley Cooper", "John Krasinski", "Regina King", "Olivia Wilde", "Emerald Fennell",
        "Kathryn Bigelow", "Sofia Coppola", "Patty Jenkins", "Nia DaCosta", "Céline Sciamma",
        "Lulu Wang", "Minari Lee Isaac Chung", "Barry Jenkins", "Ryan Coogler", "Taika Waititi",
        "Peter Jackson", "Zack Snyder", "Joss Whedon", "Kevin Feige", "Russo Brothers",
        "Sam Raimi", "Bryan Singer", "Matthew Vaughn", "Guy Ritchie", "Edgar Wright",
        "Simon Pegg", "Nick Frost", "Seth Rogen", "Judd Apatow", "Adam McKay",
        "Will Ferrell", "Steve Carell", "Tina Fey", "Amy Poehler", "Kristen Wiig",
        "Melissa McCarthy", "Paul Feig", "Jason Reitman", "Ivan Reitman", "Harold Ramis",
        "John Hughes", "John Landis", "David Zucker", "Jerry Zucker", "Jim Abrahams",
        "Mel Brooks", "Rob Reiner", "Christopher Guest", "Eugene Levy", "Catherine O'Hara",
        "Parker Posey", "Jennifer Coolidge", "Jane Lynch", "Maya Rudolph", "Ellie Kemper",
        "Mindy Kaling", "Aziz Ansari", "Donald Glover", "Issa Rae", "Michaela Coel",
        "Phoebe Waller-Bridge", "Lena Dunham", "Shonda Rhimes", "Ryan Murphy", "Brad Falchuk"
    ]
    
    directors = []
    for director_name in directors_data:
        director = Director(name=director_name)
        directors.append(director)
    
    db.add_all(directors)
    db.commit()

    # Create 100 Actors
    actors_data = [
        "Leonardo DiCaprio", "Tom Hanks", "Christian Bale", "Robert De Niro", "Al Pacino",
        "Meryl Streep", "Cate Blanchett", "Tilda Swinton", "Frances McDormand", "Viola Davis",
        "Denzel Washington", "Will Smith", "Brad Pitt", "George Clooney", "Matt Damon",
        "Mark Wahlberg", "Ryan Gosling", "Jake Gyllenhaal", "Oscar Isaac", "Adam Driver",
        "Timothée Chalamet", "Saoirse Ronan", "Margot Robbie", "Emma Stone", "Jennifer Lawrence",
        "Scarlett Johansson", "Natalie Portman", "Amy Adams", "Jessica Chastain", "Lupita Nyong'o",
        "Mahershala Ali", "Sterling K. Brown", "Michael B. Jordan", "Chadwick Boseman",
        "Daniel Kaluuya", "LaKeith Stanfield", "Tessa Thompson", "Anya Taylor-Joy", "Florence Pugh",
        "Zendaya", "Tom Holland", "Robert Downey Jr.", "Chris Evans", "Chris Hemsworth",
        "Chris Pratt", "Mark Ruffalo", "Scarlett Johansson", "Jeremy Renner", "Paul Rudd",
        "Brie Larson", "Benedict Cumberbatch", "Tom Hiddleston", "Anthony Mackie", "Sebastian Stan",
        "Elizabeth Olsen", "Paul Bettany", "Don Cheadle", "Gwyneth Paltrow", "Jon Favreau",
        "Samuel L. Jackson", "Nick Fury", "Clark Gregg", "Cobie Smulders", "Emily VanCamp",
        "Frank Grillo", "Georges St-Pierre", "Hayley Atwell", "Dominic Cooper", "Neal McDonough",
        "Tommy Lee Jones", "Stanley Tucci", "Toby Jones", "Maximiliano Hernández", "Garry Shandling",
        "Robert Redford", "Jenny Agutter", "Alan Dale", "Callan Mulvey", "Frank Grillo",
        "Dolph Lundgren", "Sylvester Stallone", "Arnold Schwarzenegger", "Bruce Willis", "Mel Gibson",
        "Liam Neeson", "Kevin Costner", "Harrison Ford", "Sean Connery", "Pierce Brosnan",
        "Daniel Craig", "Roger Moore", "Timothy Dalton", "George Lazenby", "Sean Bean",
        "Ralph Fiennes", "Judi Dench", "Maggie Smith", "Helen Mirren", "Emma Thompson",
        "Kate Winslet", "Keira Knightley", "Helena Bonham Carter", "Bonnie Wright", "Evanna Lynch",
        "Matthew Lewis", "Tom Felton", "Rupert Grint", "Emma Watson", "Daniel Radcliffe",
        "Alan Rickman", "Robbie Coltrane", "Julie Walters", "Imelda Staunton", "David Thewlis",
        "Gary Oldman", "Timothy Spall", "Warwick Davis", "John Cleese", "Maggie Smith"
    ]
    
    actors = []
    for actor_name in actors_data:
        actor = Actor(name=actor_name)
        actors.append(actor)
    
    db.add_all(actors)
    db.commit()

    # Create 100 Movies with duration (in minutes)
    movies_data = [
        ("Inception", 2010, 4.5, 148), ("The Dark Knight", 2008, 4.6, 152), ("Interstellar", 2014, 4.4, 169),
        ("Dunkirk", 2017, 4.2, 106), ("Tenet", 2020, 4.1, 150), ("The Prestige", 2006, 4.3, 130),
        ("Memento", 2000, 4.4, 113), ("Batman Begins", 2005, 4.2, 140), ("The Dark Knight Rises", 2012, 4.1, 165),
        ("Insomnia", 2002, 3.9, 118), ("Jaws", 1975, 4.5, 124), ("E.T.", 1982, 4.3, 115),
        ("Jurassic Park", 1993, 4.4, 127), ("Schindler's List", 1993, 4.7, 195), ("Saving Private Ryan", 1998, 4.6, 169),
        ("Raiders of the Lost Ark", 1981, 4.5, 115), ("Indiana Jones and the Last Crusade", 1989, 4.3, 127),
        ("Close Encounters", 1977, 4.2, 138), ("Munich", 2005, 4.1, 164), ("Lincoln", 2012, 4.0, 150),
        ("Goodfellas", 1990, 4.6, 146), ("The Godfather", 1972, 4.8, 175), ("Taxi Driver", 1976, 4.5, 114),
        ("The Departed", 2006, 4.4, 151), ("Casino", 1995, 4.3, 178), ("Raging Bull", 1980, 4.4, 129),
        ("Mean Streets", 1973, 4.2, 112), ("The Wolf of Wall Street", 2013, 4.1, 180), ("Shutter Island", 2010, 4.0, 138),
        ("The Irishman", 2019, 4.2, 209), ("Pulp Fiction", 1994, 4.7, 154), ("Kill Bill", 2003, 4.4, 111),
        ("Django Unchained", 2012, 4.3, 165), ("Inglourious Basterds", 2009, 4.2, 153), ("Reservoir Dogs", 1992, 4.3, 99),
        ("Once Upon a Time in Hollywood", 2019, 4.1, 161), ("Jackie Brown", 1997, 4.0, 154), ("Death Proof", 2007, 3.8, 127),
        ("The Hateful Eight", 2015, 3.9, 168), ("From Dusk Till Dawn", 1996, 3.9, 108), ("Psycho", 1960, 4.6, 109),
        ("Vertigo", 1958, 4.5, 128), ("Rear Window", 1954, 4.4, 112), ("North by Northwest", 1959, 4.3, 136),
        ("The Birds", 1963, 4.2, 119), ("Dial M for Murder", 1954, 4.1, 105), ("Strangers on a Train", 1951, 4.0, 101),
        ("Shadow of a Doubt", 1943, 3.9, 108), ("Rebecca", 1940, 4.1, 130), ("Notorious", 1946, 4.2, 102),
        ("2001: A Space Odyssey", 1968, 4.6, 149), ("A Clockwork Orange", 1971, 4.4, 136), ("The Shining", 1980, 4.3, 146),
        ("Full Metal Jacket", 1987, 4.2, 116), ("Dr. Strangelove", 1964, 4.5, 95), ("Barry Lyndon", 1975, 4.1, 185),
        ("Eyes Wide Shut", 1999, 4.0, 159), ("Paths of Glory", 1957, 4.3, 88), ("Spartacus", 1960, 4.2, 197),
        ("Lolita", 1962, 3.9, 153), ("The Godfather Part II", 1974, 4.7, 202), ("Apocalypse Now", 1979, 4.5, 147),
        ("The Conversation", 1974, 4.3, 113), ("Bram Stoker's Dracula", 1992, 4.0, 128), ("The Rainmaker", 1997, 3.9, 135),
        ("The Cotton Club", 1984, 3.8, 127), ("Gardens of Stone", 1987, 3.7, 111), ("Tucker", 1988, 3.8, 110),
        ("Peggy Sue Got Married", 1986, 3.9, 103), ("Jack", 1996, 3.6, 113), ("Star Wars", 1977, 4.6, 121),
        ("The Empire Strikes Back", 1980, 4.7, 124), ("Return of the Jedi", 1983, 4.4, 131), ("American Graffiti", 1973, 4.2, 110),
        ("THX 1138", 1971, 3.9, 86), ("Alien", 1979, 4.5, 117), ("Blade Runner", 1982, 4.4, 117),
        ("Gladiator", 2000, 4.3, 155), ("The Martian", 2015, 4.2, 144), ("Thelma & Louise", 1991, 4.1, 130),
        ("Black Hawk Down", 2001, 4.0, 144), ("Kingdom of Heaven", 2005, 3.9, 144), ("Robin Hood", 2010, 3.8, 140),
        ("Exodus: Gods and Kings", 2014, 3.7, 150), ("All the Money in the World", 2017, 3.8, 132),
        ("Terminator", 1984, 4.4, 107), ("Terminator 2", 1991, 4.6, 137), ("Aliens", 1986, 4.5, 137),
        ("Titanic", 1997, 4.2, 194), ("Avatar", 2009, 4.1, 162), ("The Abyss", 1989, 4.0, 140),
        ("True Lies", 1994, 3.9, 141), ("Piranha II", 1982, 3.5, 94), ("Strange Days", 1995, 3.8, 145),
        ("Point Break", 1991, 3.9, 122), ("Batman", 1989, 4.2, 126), ("Batman Returns", 1992, 4.0, 126),
        ("Edward Scissorhands", 1990, 4.3, 105), ("Big Fish", 2003, 4.1, 125), ("Sweeney Todd", 2007, 4.0, 116),
        ("Alice in Wonderland", 2010, 3.8, 108), ("Charlie and the Chocolate Factory", 2005, 3.9, 115),
        ("Corpse Bride", 2005, 4.0, 77), ("Frankenweenie", 2012, 3.9, 87), ("Dumbo", 2019, 3.7, 112)
    ]
    
    movies = []
    for i, (title, year, rating, duration) in enumerate(movies_data):
        # Assign random director
        director = random.choice(directors)
        
        # Assign random actors (1-5 actors per movie)
        num_actors = random.randint(1, 5)
        movie_actors = random.sample(actors, num_actors)
        
        # Assign random genres (1-3 genres per movie)
        num_genres = random.randint(1, 3)
        movie_genres = random.sample(genres, num_genres)
        
        movie = Movie(
            title=title,
            release_year=year,
            director_id=director.id,
            actors=movie_actors,
            genres=movie_genres,
            rating=rating,
            duration=duration
        )
        movies.append(movie)
    
    db.add_all(movies)
    db.commit()
    
    print(f"Seeding complete:")
    print(f"- {len(genres)} genres created")
    print(f"- {len(directors)} directors created") 
    print(f"- {len(actors)} actors created")
    print(f"- {len(movies)} movies created")

def main():
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Get database session
    db = SessionLocal()
    try:
        # Run the seeder
        seed_db(db)
        print("Database seeded successfully!")
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()