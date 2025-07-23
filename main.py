from recommender.music_recommender import MusicRecommender


def main():
    recommender = MusicRecommender("data/music_data.csv")
    print("Recommendations for genre='Pop', mood='Energetic':")
    print(recommender.recommend(genre='Pop', mood='Energetic'))


if __name__ == "__main__":
    main()
