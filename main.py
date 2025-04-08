from grading.final_scorer import get_final_score
import argparse

from utils.result_exporter import notify_classroom

parser = argparse.ArgumentParser(description="Process token argument.")
parser.add_argument("--token", type=str, required=True, help="GitHub token")
args = parser.parse_args()

github_token = args.token

result = get_final_score()


notify_classroom(result, github_token)

