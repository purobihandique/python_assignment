from catalog import available_movies

rented_movies = {}  # Dictionary to store customer rentals {customer_name: [list of rented movies]}

def rent_movie(customer_name, movie_title):
    """Rent a movie to a customer if available."""
    
    customer_name = customer_name.upper()
    movie_title = movie_title.upper()
    
    for movie in available_movies:
        if movie[0] == movie_title:
            rented_movies.setdefault(customer_name, []).append(movie)
            available_movies.remove(movie)
            print(f"{movie_title} rented to {customer_name}.")
            return
    print(f"{movie_title} is not available.")

def return_movie(customer_name, movie_title):
    """Return a movie from a customer."""
    
    customer_name = customer_name.upper()
    movie_title = movie_title.upper()
    
    if customer_name in rented_movies:
        for movie in rented_movies[customer_name]:
            if movie[0] == movie_title:
                rented_movies[customer_name].remove(movie)
                available_movies.append(movie)
                print(f"{movie_title} returned by {customer_name}.")
                return
        print(f"{customer_name} did not rent {movie_title}.")
    else:
        print(f"{customer_name} has no rentals.")

def display_rented_movies():
    """Display all rented movies."""
    if not rented_movies:
        print("No movies are currently rented.")
    else:
        print("Rented Movies:")
        for customer, movies in rented_movies.items():
            print(f"{customer} has rented:")
            for movie in movies:
                print(f" - {movie[0]} (${movie[2]:.2f})")
