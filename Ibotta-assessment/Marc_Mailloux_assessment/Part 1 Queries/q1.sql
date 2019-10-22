SELECT r.id as Receipt_ID, r.customer_id as Customer_ID, count(*) as Num_items_on_receipt 
FROM receipts as r left JOIN receipt_items as ri ON r.id=ri.receipt_id
group by r.id, r.customer_id
order by r.customer_id;