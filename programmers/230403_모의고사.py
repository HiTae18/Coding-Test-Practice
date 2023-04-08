def solution(answers):
    answer = []
    
    one = [1,2,3,4,5] 
    two = [2,1,2,3,2,4,2,5] 
    thr = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    
    for idx, ans in enumerate(answers):
        score[0] += 1 if one[idx%len(one)] == ans else 0
        score[1] += 1 if two[idx%len(two)] == ans else 0
        score[2] += 1 if thr[idx%len(thr)] == ans else 0
    
    max_score = max(score)
    
    for s_index, s_score in enumerate(score):
        answer.append(s_index+1) if s_score == max_score else None
        
    return answer
