select  customer_id as 'Customer ID', id as 'Receipt ID', total, created_at as 'Receipt Initialization' from receipts
where customer_id in (4162,39285,57200,12842)
order by total;


