def optimalFreelancing(jobs):
    jobs.sort(key=lambda job: job["payment"], reverse=True)
    sum = 0
    WEEK_LENGTH = 7
    finalJobs = [0]*WEEK_LENGTH
    for job in jobs:
        deadline = job["deadline"] - 1
        if deadline >= WEEK_LENGTH:
            deadline = WEEK_LENGTH-1
        payment = job["payment"]
        for i in range(deadline, -1, -1):
            if payment > finalJobs[i]:
                finalJobs[i] = payment
                break
    for job in finalJobs:
        sum+= job
    return sum
# O(nlogn) time, O(1) space