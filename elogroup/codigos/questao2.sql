SELECT 
COUNT(*) AS quantidade_clientes
FROM DIM_Cliente
WHERE Estado_civil = "Divorciada" AND Sexo = "Feminino";