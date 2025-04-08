from grading.grader import get_test_results,get_score
from utils.path import Path
from utils.report_generator import generate_md
def get_final_score():
    path = Path(__file__,'tests')
    base_score = get_test_results(path.getFilePath('test_base.py'))
    bonus_score = get_test_results(path.getFilePath('test_bonus.py'))
    penalty_score = get_test_results(path.getFilePath('test_penalty.py'))

    final_score = (
        ((get_score(base_score[0],9) * 0.8 ))+
        ((get_score(bonus_score[0],4) * 0.2)) -
        ((get_score(penalty_score[0],5) * 0.3)))
    generate_md({"passed":base_score[0],"failed":base_score[1]},
                {"passed":bonus_score[0],"failed":bonus_score[1]},
                {"passed":penalty_score[0],"failed":penalty_score[1]},
                final_score)
    return final_score


if __name__ == '__main__':
    print(get_final_score())
