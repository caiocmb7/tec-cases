## Autor: Caio Martim Barros
## Título: Case Técnico Entrevista para Estágio em Engenharia de Dados.

___________________________________________________

### Informações

Olá!!

As três perguntas (duas + questão extra) foram resolvidas em Python, como pedido. Utilizei o Google Colab (Jupyter Notebook) para fazer a implementação dos códigos, então
nesse repositório contém arquivos .py e .pynb para caso deseja analisar as respostas pelo próprio notebook ou por uma IDE.

Como utilizei o Colab, as minhas respostas ficaram com bastante comentários. Porém, como pedido, irei ressaltar e/ou repetir alguns passos comentados no notebook.

Aconselho visualizar as respostas pelo próprio repositório aqui do github, com o .pynb, pois ele retorna a compilação produzida por mim anteriormente. Mas caso seja necessário rodar em sua máquina, recomendo que utilize o notebook ou uma IDE utilizando o .py

Nesse repositório contém 2 arquivos principais, com 2 formatos cada. Uma para solução da 1 questão e a outra para (questão 2 + questão extra).

___________________________________________________

### Questão 1 

"1 - Desenvolva um script em python para retornar o primeiro valor não repetido de uma string.
Exemplo:
input -> 'teste'
output -> 's'
input -> 'engenharia de dados'
output -> 'g'"

R: 

Foi-se pensado na criação de duas novas listas, uma para transformar a string em lista e uma outra para adicionar as letras (valores) que só aparecem uma vez na lista criada. 

Dessa forma, poderemos usar as propriedades das listas e tornar a questão mais fácil de ser resolvida.

No código, portanto, tem uma interação para o usuário digitar uma certa frase e, após isso, irá retornar o primeiro valor(ou letra) não repetido.

Depois, deixei mais 2 linhas de código para retornar uma lista com todos os valores que só aparecem UMA vez (logo não se repetem) na frase e 
também será mostrado, na próxima linha, o primeiro valor não repetido para deixar mais elaborado o entedimento. [pois eu usei no script e quis deixar um print
pra mostrar os valores]


___________________________________________________

### Questão 2 + Questão Extra

"Pergunta da Questão 2:

"2 - O conjunto de dados flor Íris ou conjunto de dados Íris de Fisher é um conjunto de dados
multivariados introduzido pelo estatístico e biólogo britânico Ronald Fisher em seu artigo de
1936.
Desenvolva um script em python para encontrar a média do petal_length de cada espécie
presente no dataset.
Utilize a função pd.read_csv() para baixar o conteúdo disponível na url:"
https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

Pergunta da Questão Extra: 

"Na segunda questão, é um diferencial plotar gráficos para visualização dos resultados"

R:

Então, pela pergunta, temos um foco em agrupar 2 colunas, species e petal_length. Para isso, precisamos utilizar a função .groupby para 
conseguir juntar essas duas colunas e poder fazer a análise conjunta, já adicionando também o método .mean(), que assim já garante nossa resposta.

Para certificar que está correto, fiz uma outra solução que basicamente é muito parecido, porém utilizando mais dois artíficios, que seria o .sum(), 
para somar todos os valores de cada espécie definida, e o value_counts() para contarmos quantos casos existem em cada espécie, que no caso são 50 para cada uma delas.

Então, fazendo a compilação somente dessa parte, iremos descobrir a resposta para a Questão 2.

Para a Questão Extra, recomendo, se possível, analisar no notebook mesmo (Usando o Google Colab ou Jupyter Notebook) 
Realizei alguns gráficos para ressaltar a resposta acima e adicionei mais algumas análises, como a construção de 3 novos dataframes a partir
do mesmo df. Nesse contexto, fiz uma análise para o comportamento desses valores de cada espécie e plotei mais alguns gráficos e por fim, caso necessário,
deixei códigos para salvar essas respostas dos gráficos (que no caso deixei como comentário) e do dataframes em .csv.

Para conseguir rodar o código construído, precisa-se baixar o .csv e colocar o caminho correto na parte do pd.read_csv. De resto, basta executar que dará certo =)
