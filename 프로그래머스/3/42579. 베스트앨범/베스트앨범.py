# def solution(genres, plays): 
#     # 장르별 재생 횟수
#     music = {}
#     for g, p in zip(genres, plays):
#         music[g] = music.get(g, 0) + p  # 장르g의 현재 합계를 가져와서 p를 더해주기
    
#     sorted_music = dict(sorted(music.items(), key=lambda item: item[1], reverse=True))
    
#     # 장르별 곡 목록
#     music_genre = {}
#     for i in range(len(genres)):
#         g = genres[i]
#         p = plays[i]
#         if g not in music_genre:      # 처음 보는 장르면
#             music_genre[g] = []       # 빈 리스트 만들기
#         music_genre[g].append((p, i)) # (재생수, 번호) 넣기
    
#     answer = []
#     for s in sorted_music:
#         songs = sorted(music_genre[s], key=lambda x: (-x[0], x[1]))
#         for p, i in songs[:2]:
#             answer.append(i)
                
#     return answer


# ----------------------------------------------

def solution(genres, plays): 
    # 장르별 재생 횟수
    music = {}
    for g, p in zip(genres, plays):
        music[g] = music.get(g, 0) + p
    # 가장 많이 들은 장르 순으로 정렬
    sorted_music = dict(sorted(music.items(), key = lambda x: x[1], reverse=True))
    
    # 장르별 곡 목록
    music_genre = {}
    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]
        if g not in music_genre:
            music_genre[g] = []
        music_genre[g].append((p, i))
        
    answer = []
    for s in sorted_music:
        songs = sorted(music_genre[s], key = lambda x: (-x[0], x[1]))
        for p, i in songs[:2]:
            answer.append(i)
    return answer