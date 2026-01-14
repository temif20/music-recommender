from songs import songs 
from recommender import recommended

user_likes = ["Billie Jean", "Love Me", "No Role Modelz"]

recommendations = recommended(user_likes, songs)

print("Based on your likes, we recommend:")
for song in recommendations:
    print("- " + song)