create database churn
use churn
select * from clean
--------------------------------------------------------------
-- 1️ Find the overall churn rate (%) from the customer dataset.

with churn_rates as (
select customer_id,round(sum(churn) * 100/count(*),2) as percentage
from clean
group by customer_id
)
select * from churn_rates

-- Identify the top 5 cities with the highest number of churned customers.
select city,count(churn)
from clean
where churn = 1
group by city
order by count(churn) desc
limit 5

-- Calculate average total revenue for churned vs non-churned customers.

select customer_id,sum(total_revenue) as total_amount
from clean
group by customer_id

-- List the top 10 high-value customers based on total revenue.

select customer_id,sum(total_revenue) as high_value
from clean
group by customer_id
order by high_value desc
limit 10

-- Find customers who are inactive for more than 90 days and classify them as high-risk.

select customer_id,days_since_last_order,
  case 
	when days_since_last_order > 90 then 'high risk'
	else 'low risk'
  end as 'rist customers'
from clean;

--  Determine whether customers with fewer orders have a higher churn rate.

select
	case
		when total_orders <= 3 then 'low oredrs'
		when total_orders <= 6 then 'median orders'
		else 'high orders'
	end as 'orders',
	count(total_orders) as total_orders,
    sum(total_revenue) as total_amount,
    round(sum(total_revenue)*count(total_orders),2) as churn_rate
from clean
group by orders 

-- 7️⃣ Rank customers within each city based on total revenue using window functions.

select customer_id,city,sum(total_revenue) as total_amount,
dense_rank() over(partition by city order by sum(total_revenue) desc) as ranks
from clean
group by customer_id,city

-- 8️⃣ Create a customer risk category (Low, Medium, High) based on days_since_last_order using CASE statements.

select customer_id,days_since_last_order,
	case
		when days_since_last_order <= 90 then 'low'
        when days_since_last_order <= 200 then 'median'
        else 'high'
	end as 'customer_last_order_date'
from clean

-- 9️⃣ Find the percentage of churned customers in each city.

select round(sum(churn) * 100.0 / count(*),2) as percentage,city
from clean
group by city

-- 🔟 Prepare a SQL query that returns an ML-ready dataset by selecting only relevant features and filtering invalid records.

select customer_id,age,gender,city,total_orders,total_revenue,days_since_last_order,churn
from clean
where age is not null and city is not null
and total_orders is not null and total_revenue is not null and days_since_last_order is not null

