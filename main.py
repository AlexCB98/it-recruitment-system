from data import candidates

def format_data(candidat):
    name = candidat['name']
    age = candidat['age']
    experience = candidat['experience_years']
    score = candidat['test_score']

    return f'- Name: {name}\n- Age: {age}\n- Experience: {experience}\n- Score: {score}\n'

def technic_score(score, projects, experience):
    return (score * 0.5) + (projects * 2) + (experience * 5)

def is_affordable(salary):
    if salary <= 6000:
        return True
    else:
        return False

def good_communication(e_level, test_s):
    if e_level >= 7 and test_s >= 80:
        return True
    else:
        return False

def final_decision(score, affordable, communication):

    if score >= 80 and affordable and communication:
        return 'Hire'
    elif score >= 80 and communication:
        return 'Interview'
    else:
        return 'Reject'


for participant in candidates:

    score = technic_score(participant['test_score'],
                          participant['github_projects'],
                          participant['experience_years'])

    affordable = is_affordable(participant['salary_expectation'])

    communication = good_communication(participant['english_level'],
                                       participant['test_score'])

    decision = final_decision(score,affordable, communication)

    print(f'{format_data(participant)}\n --> {decision} \n')