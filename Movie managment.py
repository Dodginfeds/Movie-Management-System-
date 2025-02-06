# ---------------------------------------------
# Movie Management System
# ---------------------------------------------
# This program allows users to:
# 1. Add new movies to the database.
# 2. Retrieve and view a movie's details.
# 3. Remove a movie from the database.
# 4. Search for a movie by title.
# 5. Exit the program.
# ---------------------------------------------
# Movies are stored in a dictionary where:
# - Key: Movie Name
# - Value: Dictionary with {Genre, Year}
# ---------------------------------------------

movies = {}

# ---------------------------------------------
# Function to Add Movies
# ---------------------------------------------

def add_movie():
    """
    Allows the user to add one or multiple movies to the system.
    Each movie entry includes a title, genre, and release year.
    """
    try:
        count = int(input("How many movies would you like to add?: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    for _ in range(count):
        movie_name = input("\nEnter the movie title: ").strip()
        movie_genre = input("Enter the genre: ").strip()
        movie_year = input("Enter the release year: ").strip()

        if movie_name in movies:
            print(f"{movie_name} is already in your list.")
        else:
            movies[movie_name] = {"Genre": movie_genre, "Year": movie_year}
            print(f"Movie '{movie_name}' has been added!")

# ---------------------------------------------
# Function to Retrieve a Movie
# ---------------------------------------------

def retrieve_movie():
    """
    Retrieves and displays details of a specific movie by title.
    """
    name = input("Enter the movie title to retrieve: ").strip()

    if name in movies:
        movie_detail = movies[name]
        print("\n------------------------------------")
        print(f"Movie Name: {name}")
        print(f"Genre: {movie_detail['Genre']}")
        print(f"Release Year: {movie_detail['Year']}")
        print("------------------------------------")
    else:
        print(f"Movie '{name}' is not in your list.")

# ---------------------------------------------
# Function to Remove a Movie
# ---------------------------------------------

def remove_movie():
    """
    Removes a movie from the system by title.
    """
    name = input("Enter the movie title to remove: ").strip()

    if name in movies:
        movies.pop(name)
        print(f"Movie '{name}' has been removed!")
    else:
        print(f"Movie '{name}' is not in your list.")

# ---------------------------------------------
# Function to Search for a Movie
# ---------------------------------------------

def search_movie():
    """
    Checks if a movie exists in the system by title.
    """
    name = input("Enter the movie title to search for: ").strip()

    if name in movies:
        print(f"Movie '{name}' is in your list!")
    else:
        print(f"Movie '{name}' is not in your list.")

# ---------------------------------------------
# Function to Handle User Menu Choices
# ---------------------------------------------

def movie_management():
    """
    Provides an interactive menu for managing movies.
    """
    while True:
        print("\n--- Movie Management System ---")
        print("1. Add a Movie")
        print("2. Retrieve Movie Details")
        print("3. Remove a Movie")
        print("4. Search for a Movie")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            add_movie()
        elif choice == 2:
            retrieve_movie()
        elif choice == 3:
            remove_movie()
        elif choice == 4:
            search_movie()
        elif choice == 5:
            print("\nThank you for using the Movie Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option (1-5).")

# ---------------------------------------------
# Program Entry Point
# ---------------------------------------------

if __name__ == "__main__":
    movie_management()
