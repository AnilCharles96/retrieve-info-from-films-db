import requests
import json 
import argparse


def get_data_from_page(title):
    """
    Fetches movie data from the API based on the provided title.

    Args:
        title (str): The title of the movie to search for.
    Returns:
        dict: A dictionary containing movie data.
    Raises:
        Exception: If there is an error fetching data from the API.
    Example:
        get_data_from_page("spiderman")

    """
    # Return if title is empty
    if not title:
        print("Title cannot be empty.")
        return

    url = f"https://jsonmock.hackerrank.com/api/movies/search/?Title={title}"
    # Get request to the API
    try:
        response = requests.get(url)
        movie_data = json.loads(response.text)
    except Exception as e:
        print(f"Error fetching data: {e}")
        
    return movie_data

# PEP8 Guidelines suggest function names should be lowercase with words separated by underscores.
# Question asks for getMovieTitles, but I will use get_movie_titles to follow PEP8.
def get_movie_titles(title):
    """
    Fetches unique movie titles from the API based on the provided title.

    Args:
        title (str): The title of the movie to search for.
    Returns:
        list: A list of unique movie titles sorted alphabetically.
    """
    movie_data = get_data_from_page(title)    
    data = movie_data["data"]
    total_pages =  movie_data["total_pages"]
    total = movie_data["total"]

    for page in range(2, total_pages + 1):
        page_data = get_data_from_page(title + f"&page={page}")
        data.extend(page_data["data"])
    
    # Check if data is empty
    if not data:
        print("No movies found.")
        return

    # Extract movie titles from the data
    titles = [movie["Title"] for movie in data]

    # Remove duplicates, Question asks for unique titles
    titles = list(set(titles))

    # Sort the titles alphabetically
    titles.sort()

    return titles
    

def main():
    parser = argparse.ArgumentParser(description="Fetch movie titles from Hackerrank API.")
    parser.add_argument("title", type=str, help="Title of the movie to search for")
    args = parser.parse_args()

    titles = get_movie_titles(args.title)
    if titles:
        print("Movie Titles:")
        for title in titles:
            print(title)
    else:
        print("No titles to display.")

if __name__ == "__main__":
    main()
