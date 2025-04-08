from grading.grader import grade
from utils.path import Path

def get_final_score():
    path = Path(__file__,'tests')
    base_score = grade(path.getFilePath('test_base.py'),9)
    bonus_score = grade(path.getFilePath('test_bonus.py'),4)
    penalty_score = grade(path.getFilePath('test_penalty.py'),5)
    final_score = (
        ((base_score * 0.8 ))+
        ((bonus_score * 0.2)) -
        ((penalty_score * 0.3)))/100
    return final_score


if __name__ == '__main__':
    print(get_final_score())
