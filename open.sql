USE University

SELECT 
ProductName + ' ('+ Manufacturer +')'AS Model,
Price,
ProductCount AS Lefted,
Price * ProductCount AS TotalSum
FROM Phones

SELECT
ProductName + ' ('+ Manufacturer +')'AS Model,
Price*ProductCount AS TotalSum,
ProductCount
FROM Phones
ORDER BY TotalSum
