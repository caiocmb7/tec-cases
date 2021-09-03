SELECT 
ID_produto,
Cod_produto,
Receita_venda
FROM FT_Vendas
INNER JOIN DIM_Produto
    ON DIM_Produto.ID_produto = FT_Vendas.vendas_produto
        WHERE (DIM_Produto.Cod_produto = 55 OR DIM_Produto.Cod_produto = 120 OR DIM_Produto.Cod_produto = 142) AND Receita_venda > 120;