def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    new_list=sorted(scores,reverse=True)
    top_3=new_list[:3]
    return top_3

