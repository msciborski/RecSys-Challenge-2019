from score_submission import score_subm as ss
from verify_submission import verify_subm as vs
from baseline_algorithm import rec_popular as rp

submission_file = 'data/submission_popular.csv'
ground_truth_file = 'data/groundTruth.csv'
test_file = 'data/test.csv'
data_path = 'data/'


def baseline():
    rp.main(data_path)


def verify():
    vs.main(submission_file, test_file)


def score():
    ss.main(ground_truth_file, submission_file)


def main():
    baseline()
    verify()
    score()


if __name__ == '__main__':
    main()
