select retailer_id, count(distinct product_number) as Unique_products_sold , count(distinct(customer_id)) as Number_of_Customers from receipts
left join Receipt_Items on receipts.id = receipt_items.receipt_id
where created_at >= DATEADD(WEEK, -4, GETDATE())
group by retailer_id;
