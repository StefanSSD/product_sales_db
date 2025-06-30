INSERT INTO REVENUE (sku_id, date_id, price, sales, revenue)
SELECT p.sku_id,
       s.orderdate_utc AS date_id,
       p.price,
       s.sales,
       p.price * s.sales AS revenue
  FROM product p
  LEFT JOIN sales s 
    ON p.sku_id = s.sku_id;
