import pickle
import gzip
import numpy as np
import pandas as pd
import os

def generate_mock_data():
    print("Generating mock data...")

    # 1. movie_dict.pkl
    # Should be a dictionary that can be converted to DataFrame with 'title' and 'overview' columns.
    movies = [
        {"title": "The Matrix", "overview": "A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers."},
        {"title": "Inception", "overview": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O."},
        {"title": "Interstellar", "overview": "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival."},
        {"title": "The Dark Knight", "overview": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice."},
        {"title": "Pulp Fiction", "overview": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption."},
        {"title": "Fight Club", "overview": "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into something much, much more."},
        {"title": "Forrest Gump", "overview": "The presidencies of Kennedy and Johnson, the events of Vietnam, Watergate and other historical events unfold from the perspective of an Alabama man with an IQ of 75, whose only desire is to be reunited with his childhood sweetheart."},
        {"title": "The Shawshank Redemption", "overview": "Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency."},
        {"title": "The Godfather", "overview": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son."},
        {"title": "Titanic", "overview": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic."}
    ]

    # Create the dictionary structure expected: {'title': [...], 'overview': [...]}
    movie_dict = {
        "title": [m["title"] for m in movies],
        "overview": [m["overview"] for m in movies]
    }

    with open('movie_dict.pkl', 'wb') as f:
        pickle.dump(movie_dict, f)
    print("Created movie_dict.pkl")

    # 2. collab_titles.pkl
    # Just a list of titles for collaborative filtering
    collab_titles = [m["title"] for m in movies]
    with open('collab_titles.pkl', 'wb') as f:
        pickle.dump(collab_titles, f)
    print("Created collab_titles.pkl")

    # 3. similarity.pkl.gz (Content-Based)
    # A similarity matrix (N x N). Using random values for demo purposes, but diagonal should be 1.
    n_movies = len(movies)
    # Create a random similarity matrix
    content_sim = np.random.rand(n_movies, n_movies)
    # Make it symmetric and diagonal 1
    content_sim = (content_sim + content_sim.T) / 2
    np.fill_diagonal(content_sim, 1.0)

    with gzip.open('similarity.pkl.gz', 'wb') as f:
        pickle.dump(content_sim, f)
    print("Created similarity.pkl.gz")

    # 4. collab_similarity.pkl.gz (Collaborative Filtering)
    # Similar structure
    collab_sim = np.random.rand(n_movies, n_movies)
    collab_sim = (collab_sim + collab_sim.T) / 2
    np.fill_diagonal(collab_sim, 1.0)

    with gzip.open('collab_similarity.pkl.gz', 'wb') as f:
        pickle.dump(collab_sim, f)
    print("Created collab_similarity.pkl.gz")

if __name__ == "__main__":
    generate_mock_data()
