# second questions

## Test Variables
cv_list_of_dicts_sample_for_testing: list = [
    {'user': 'name1', 'jobs': ['job1', 'job2', 'job3']},
    {'user': 'name2', 'jobs': ['job1', 'job2', 'job4']},
    {'user': 'name3', 'jobs': ['job1', 'job5', 'job6']}
]

desired_output_q4: list = [
    {'job1': ['name1', 'name2', 'name3']}, # only list portion is expected in output, i.e. ['name1', 'name2', 'name3']
    {'job2': ['name1', 'name2']}, # job 2
    {'job3': ['name1']}, # job 3
    {'job4': ['name2']}, # job 4
    {'job5': ['name3']}, # job 5
    {'job6': ['name3']} # job 6
] 

desired_output_q5: dict = {
    'job1': 3,
    'job2': 2,
    'job3': 1,
    'job4': 1,
    'job5': 1,
    'job6': 1,
}


## 4
def has_experience_as(cv_list: list[dict], job_title: str):
    usernames_who_worked_job = []
    for person in cv_list:
        if 'jobs' in person and job_title in person['jobs']:
            usernames_who_worked_job.append(person['user'])
    return usernames_who_worked_job

result_q4: list = has_experience_as(cv_list_of_dicts_sample_for_testing, 'job1')
print(result_q4)

# 5
def job_counts(cv_list: list[dict]):
    count_of_jobs_per_job_title: dict = {}
    for person in cv_list:
        for job in person['jobs']:
            if job in count_of_jobs_per_job_title:
                count_of_jobs_per_job_title[job] = count_of_jobs_per_job_title[job] + 1
            else: count_of_jobs_per_job_title[job] = 1
    return count_of_jobs_per_job_title

result_q5: dict = job_counts(cv_list_of_dicts_sample_for_testing)
print(result_q5)

## 6
def most_popular_job(cv_list: list[dict]):
    job_counts_result: dict = job_counts(cv_list)
    top_job_with_count: tuple = ()
    max_count = 0
    for job, count in job_counts_result.items():
        if count >= max_count:
            max_count: int = count
            top_job_with_count: tuple = (job, count)
    return top_job_with_count
            
result_q6: tuple = most_popular_job(cv_list_of_dicts_sample_for_testing)
print(result_q6)