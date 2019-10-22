SELECT r1.customer_id, r1.total, r1.created_at
FROM receipts as r1
inner join (
    select customer_id, max(created_At) as recent
    from receipts group by customer_id
) as r2
on r1.customer_id = r2.customer_id AND r1.created_At = r2.recent
order by r1.customer_id; 

