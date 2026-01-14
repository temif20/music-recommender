
def similarity(song1,song2):
    score = 0
    if song1["artist"] == song2["artist"]:
        score += 5

    if song1["genre"] == song2["genre"]:
        score += 3
    
    if song1["mood"] == song2["mood"]:
        score += 2

    tempo_diff = abs(song1["bpm"] - song2["bpm"])
    if tempo_diff < 10:
        score += 4
    
    return score

def recommended(user_likes, all_songs, top_n=3):
    recommendations = {}
    for song in all_songs:

        total_score = 0
        for liked_song in all_songs:
            total_score += similarity(liked_song, song)
        recommendations[song["title"]] = total_score

    recommendations = sorted(recommendations.items(), key=lambda x: x[1], reverse=True)
    return [song for song, score in recommendations[:top_n]]