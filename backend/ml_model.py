import numpy as np
from sklearn.preprocessing import MultiLabelBinarizer, StandardScaler
from sklearn.cluster import KMeans

def extract_features(artists):
    # Extract all genres from top artists
    genres = [artist["genres"] for artist in artists]
    popularities = [artist["popularity"] for artist in artists]

    # Convert genres to numerical features using one-hot encoding
    mlb = MultiLabelBinarizer()
    genre_matrix = mlb.fit_transform(genres)

    # Add popularity as a feature
    popularity_array = np.array(popularities).reshape(-1, 1)

    # Combine genre and popularity features
    if genre_matrix.shape[1] > 0:
        features = np.hstack([genre_matrix, popularity_array])
    else:
        features = popularity_array

    return features, mlb.classes_

def get_personality_cluster(artists):
    if not artists:
        return None, None, []

    features, genre_labels = extract_features(artists)

    # Scale features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Cluster into personality types
    n_clusters = min(4, len(artists))
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(scaled_features)

    # Get the user's dominant cluster
    user_cluster = int(kmeans.labels_[0])

    # Get top genres from the user's artists
    all_genres = []
    for artist in artists:
        all_genres.extend(artist["genres"])

    # Count genre frequency
    genre_counts = {}
    for genre in all_genres:
        genre_counts[genre] = genre_counts.get(genre, 0) + 1

    top_genres = sorted(genre_counts, key=genre_counts.get, reverse=True)[:5]

    return user_cluster, n_clusters, top_genres