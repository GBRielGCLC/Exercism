"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    for index, score in enumerate(student_scores):
        student_scores[index] = round(score)

    return student_scores

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    negative_scores = 0
    for score in student_scores:
        if score <= 40:
            negative_scores += 1

    return negative_scores

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    above_threshold_list = []

    for score in student_scores:
        if score >= threshold:
            above_threshold_list.append(score)

    return above_threshold_list

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
    """
    # Determine the interval size
    interval = (highest - 40) // 4

    return [41 + interval * i for i in range(4)]

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    rank = []
    for index, score in enumerate(student_scores):
        rank.append(f'{index + 1}. {student_names[index]}: {score}')

    rank = sorted(rank)
    return rank

print (student_ranking([90, 75, 60, 95], ["Alice", "Bob", "Charlie", "Dave"]))

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    perfect_scores = []
    for info in student_info:
        if info[1] == 100:
            perfect_scores = info
            break

    return perfect_scores