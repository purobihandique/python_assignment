available_movies = []  # List to store available movies as tuples (title, genre, rental price)

def add_movie(title, genre, price):
    """Add a new movie to the catalog."""
    
    movie = (title.upper(), genre.upper(), price)
    available_movies.append(movie)

def display_available_movies():
    """Display all available movies."""
    
    if not available_movies:
        print("No movies available.")
    else:
        print("Available Movies:")
        for movie in available_movies:
            print(f"Title: {movie[0]}, Genre: {movie[1]}, Price: ${movie[2]:.2f}")
