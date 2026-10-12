SELECT name AS Customers FROM customers c
WHERE id NOT IN (Select customerId from Orders)