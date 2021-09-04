SELECT 
SUM(Receita_venda) AS Receita_total
FROM FT_Vendas
INNER JOIN DIM_Loja
    ON DIM_Loja.ID_loja = FT_Vendas.ID_loja
        WHERE DIM_Loja.Cod_loja = 32 AND Dia >= 1 AND Mes >= 4 AND Ano >= 2021
GROUP BY DIM_Loja.Cod_loja;