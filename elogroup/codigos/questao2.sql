SELECT 
COUNT(*) AS Quantidade_Clientes
FROM DIM_Cliente
WHERE Estado_civil = "Divorciada" AND Sexo = "Feminino";