CREATE VIEW vw_revenue AS
		  select pr.sku_id,        
			       sl.orderdate_utc,
			       pr.price,
			       sl.sales,
			       pr.price*sl.sales as revenue
			  from product pr
			  left join sales sl
			    on pr.sku_id = sl.sku_id
			 where 1 = 1
			   and sl.orderdate_utc between '2025-01-01' and '2025-01-31';
