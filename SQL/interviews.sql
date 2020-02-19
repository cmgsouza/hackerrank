# Interviews

with sum_ss as 
(
select challenge_id, 
sum(total_submissions) as sum_total_submissions, 
sum(total_accepted_submissions) as sum_total_accepted_submissions
from Submission_Stats
group by challenge_id
), 

sum_vs as 
(
select challenge_id, 
sum(total_views) as sum_total_views, 
sum(total_unique_views) as sum_total_unique_views
from View_Stats
group by challenge_id
)

select Contests.contest_id, 
	   Contests.hacker_id, 
	   Contests.name, 
	   sum(sum_ss.sum_total_submissions), 
	   sum(sum_ss.sum_total_accepted_submissions), 
	   sum(sum_vs.sum_total_views), 
	   sum(sum_vs.sum_total_unique_views)
from Contests
inner join Colleges on Contests.contest_id = Colleges.contest_id 
inner join Challenges on Challenges.college_id = Colleges.college_id
left join sum_ss on sum_ss.challenge_id = Challenges.challenge_id
left join sum_vs on sum_vs.challenge_id = Challenges.challenge_id
group by Contests.contest_id, Contests.hacker_id, Contests.name
order by Contests.contest_id