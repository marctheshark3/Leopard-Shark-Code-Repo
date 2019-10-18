select TOP 100 
customer_id, count(1) as num_of_occurences, sum(total) as total
from receipts group by customer_id
having count(1)> 10;