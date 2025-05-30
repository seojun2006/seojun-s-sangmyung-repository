import os
import pickle

FILENAME = 'score.bin'

def input_scores():
    scores = []
    print('[점수 입력]')
    while True:
        n = int(input(f'#{len(scores) + 1}? '))
        if n < 0:
            break
        scores.append(n)
    return scores

def get_average(scores):
    return sum(scores) / len(scores)

def show_scores(scores):
    print('\n[점수 출력]')
    print('개인 점수:', ' '.join(str(score) for score in scores))
    avg = get_average(scores)
    print(f'평균 {avg:.1f}')

def save_scores(scores):
    with open(FILENAME, 'wb') as f:
        pickle.dump(scores, f)

def load_scores():
    with open(FILENAME, 'rb') as f:
        return pickle.load(f)

if os.path.exists(FILENAME):
    scores = load_scores()
    show_scores(scores)
else:
    scores = input_scores()
    save_scores(scores)
    show_scores(scores)
