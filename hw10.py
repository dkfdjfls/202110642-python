
import pickle
import os

filepath = 'score.bin'

def save_data(scores):
    with open(filepath, 'wb') as file:
        pickle.dump(scores, file)

def load_data():
    with open(filepath, 'rb') as file:
        scores = pickle.load(file)
    return scores


if os.path.exists(filepath):
    print('[파일 읽기]')
    scores = load_data()
    
else:
    print('[점수 입력]')

    scores = []
    while True:
        score = int(input(f"#{len(scores) + 1}? "))
        if score == -1:
            break
        scores.append(score)
    save_data(scores)

    print('\n[점수 출력]')


