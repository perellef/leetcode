-- 175. Combine Two Tables  
-- https://leetcode.com/problems/combine-two-tables/  
-- Write a SQL query to join Person and Address using LEFT JOIN.  

select distinct p.firstName, p.lastName, a.city, a.state
from Person p
    left join Address a on (p.personId = a.personId)