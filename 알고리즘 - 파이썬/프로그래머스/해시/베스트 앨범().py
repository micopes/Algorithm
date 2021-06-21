def solution(genres, plays):
    answer = []
    
    genres_play = dict()
    genres_songs = dict()
    
    i = 0
    for g, p in zip(genres, plays):
        try:
            genres_play[g] += p
            genres_songs[g].append((p, i))
        except:
            genres_play[g] = 0
            genres_play[g] += p
            genres_songs[g] = []
            genres_songs[g].append((p, i))
        i += 1
            
    sorted_genres = sorted(genres_play.items(), key = lambda x : x[1], reverse = True)
    
    for g in sorted_genres: 
        sorted_ans = sorted(genres_songs[g[0]], key = lambda x : x[0], reverse = True) # x[0] : 재생 횟수, x[1] : 고유번호
        answer.append(sorted_ans[0][1])
        if len(sorted_ans) > 1:
            answer.append(sorted_ans[1][1])
        
    return answer