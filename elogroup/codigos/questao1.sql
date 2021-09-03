SELECT 
Dia,
Mes,
Ano,
SUM(Qtde_vendida)
FROM FT_Vendas
INNER JOIN DIM_Tempo
    ON DIM_Tempo.ID_tempo = FT_Vendas.vendas_tempo
        WHERE Dia = 1 AND Mes = 4 AND (Ano = 2020 OR Ano = 2021);