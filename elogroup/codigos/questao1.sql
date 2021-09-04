SELECT 
SUM(Qtde_vendida) AS Quantidade_Vendida
FROM FT_Vendas
INNER JOIN DIM_Tempo
    ON DIM_Tempo.ID_tempo = FT_Vendas.ID_tempo
        WHERE Dia = 1 AND Mes = 4 AND (Ano = 2020 OR Ano = 2021);