from rentals import rented_movies

def calculate_earnings():
    """Calculate total rental earnings."""
    total = sum(movie[2] for movies in rented_movies.values() for movie in movies)
    print(f"Total Earnings: ${total:.2f}")
    return total
