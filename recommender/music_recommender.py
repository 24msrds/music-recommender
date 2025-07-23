import pandas as pd


class MusicRecommender:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)

    def recommend(self, genre=None, mood=None, artist=None):
        result = self.data
        if genre:
            result = result[result['genre'].str.lower() == genre.lower()]
        if mood:
            result = result[result['mood'].str.lower() == mood.lower()]
        if artist:
            result = result[result['artist'].str.lower() == artist.lower()]
        return result['track'].tolist()
