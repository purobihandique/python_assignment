# main.py

import catalog
import rentals
import earnings

def main():
    while True:
        print("\nMovie Rental System")
        print("1. Add New Movie")
        print("2. Display Available Movies")
        print("3. Rent a Movie")
        print("4. Return a Movie")
        print("5. Display Rented Movies")
        print("6. Calculate Earnings")
        print("7. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            title = input("Enter movie title: ")
            genre = input("Enter movie genre: ")
            price = float(input("Enter rental price: "))
            catalog.add_movie(title, genre, price)
        
        elif choice == "2":
            catalog.display_available_movies()
        
        elif choice == "3":
            customer_name = input("Enter customer name: ")
            movie_title = input("Enter movie title: ")
            rentals.rent_movie(customer_name, movie_title)
        
        elif choice == "4":
            customer_name = input("Enter customer name: ")
            movie_title = input("Enter movie title to return: ")
            rentals.return_movie(customer_name, movie_title)
        
        elif choice == "5":
            rentals.display_rented_movies()
        
        elif choice == "6":
            earnings.calculate_earnings()
        
        elif choice == "7":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
