from data import candidates

def format_data(candidat, tech_score):
    name = candidat['name']
    age = candidat['age']
    experience = candidat['experience_years']
    score = candidat['test_score']
    salary = candidat['salary_expectation']

    return f'- Name: {name}\n- Age: {age}\n- Experience: {experience}\n- Test Score: {score}\n- Technical Score: {tech_score:.1f}\n- Salary: {salary}€'

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


hire_count = 0
interview_count = 0
reject_count = 0

for participant in candidates:

    score = technic_score(participant['test_score'],
                          participant['github_projects'],
                          participant['experience_years'])

    affordable = is_affordable(participant['salary_expectation'])

    communication = good_communication(participant['english_level'],
                                       participant['test_score'])

    decision = final_decision(score, affordable, communication)

    if decision == 'Hire':
        hire_count += 1
    elif decision == 'Interview':
        interview_count += 1
    else:
        reject_count += 1

    print(f'{format_data(participant, score)}\n --> Decision: {decision}')
    print('-' * 40)

print('=' * 40)
print(f'SUMMARY')
print('=' * 40)
print(f'Hire:      {hire_count}')
print(f'Interview: {interview_count}')
print(f'Reject:    {reject_count}')
print('=' * 40)