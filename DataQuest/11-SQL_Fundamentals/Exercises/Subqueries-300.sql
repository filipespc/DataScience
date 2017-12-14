## 2. Subqueries ##

SELECT Major,Unemployment_rate 
FROM recent_grads 
WHERE Unemployment_rate < (
    SELECT AVG(Unemployment_rate)
    FROM recent_grads)
ORDER BY Unemployment_rate ASC
    

## 3. Subquery In SELECT ##

SELECT CAST(COUNT (*) AS Float) / (SELECT COUNT (*) FROM recent_grads) as proportion_abv_avg
FROM recent_grads
WHERE ShareWomen > (SELECT AVG(ShareWomen) FROM recent_grads)

## 4. Returning Multiple Results In Subqueries ##

SELECT Major,Major_category FROM recent_grads
WHERE Major_category IN (
    SELECT Major_category FROM recent_grads
    GROUP BY Major_category
    ORDER BY SUM(Total) DESC 
    LIMIT 5)

## 5. Building Complex Subqueries ##

SELECT AVG(CAST(Sample_size as Float) / CAST(Total as Float)) avg_ratio FROM recent_grads

## 6. Practice Integrating A Subquery With The Outer Query ##

select Major, Major_category, (cast(Sample_size as Float) / cast(Total as float)) as ratio from recent_grads
where ratio > 
    (select avg(cast(Sample_size as Float) / cast(Total as Float)) from recent_grads)