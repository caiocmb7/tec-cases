import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""Leitura do csv"""

df_iris = pd.read_csv("/content/iris.csv", sep = ",")

df_iris

"""Encontrar a média do petal_length de cada espécie
presente no dataset
"""

calc_media = df_iris.groupby(df_iris["species"])["petal_length"].mean()
calc_media

"""Para ser mais detalhado nas contas, iremos fazer uma soma e depois dividir => mesma ideia de usar apenas o .mean()"""

calc_soma = df_iris.groupby(df_iris["species"])["petal_length"].sum()
calc_soma

df_iris.species.value_counts() #função para analisar quantos casos existem de cada uma das espécies

"""Logo, existem 50 casos para cada espécie: ["setosa", "versicolor", "virginica"]"""

calc_media2 = calc_soma / 50
calc_media2

"""**Percebe-se, então, que os valores estão corretos!**

# **Visualização dos Dados - Extra!**

Irei separar os dataframes para analisar melhor cada espécie.
"""

df_iris.species.unique() #analisar os nomes que contém na coluna "species"

filtro_Setosa = df_iris.species == "setosa"
df_setosa = df_iris.loc[filtro_Setosa, ["petal_length", "species"]]
df_setosa.head(4) #analisando alguns dados

filtro_Versicolor = df_iris.species == "versicolor"
df_versicolor = df_iris.loc[filtro_Versicolor, ["petal_length", "species"]]
df_versicolor.sample(4) #analisando alguns dados

filtro_Virginica = df_iris.species == "virginica"
df_virginica = df_iris.loc[filtro_Virginica, ["petal_length", "species"]]
df_virginica.tail(4) #analisando alguns dados

"""**Gráficos!**

*Definição do estilo do gráfico*
"""

plt.style.use('ggplot')

df_iris.groupby(df_iris["species"])["petal_length"].mean().plot()
plt.title("Gráfico da média petal_length versus species")
plt.xlabel("species")
plt.ylabel("petal_length")

df_iris.groupby(df_iris["species"])["petal_length"].mean().plot.bar(color = "purple")
plt.title("Gráfico da média petal_length versus species")
plt.xlabel("species")
plt.ylabel("petal_length")

sns.countplot(x = df_iris["species"]) #quantidade de cada espécie

df_setosa.groupby(df_setosa["species"])["petal_length"].value_counts() #analisar quais valores de petal_length existem na espécie == "setosa" e quantas vezes aparecem

df_setosa.groupby(df_setosa["species"])["petal_length"].plot(marker = "x")
plt.title("Gráfico da petal_length versus espécie setosa")
plt.xlabel("species")
plt.ylabel("petal_length")
plt.legend()
#plt.savefig("setosa.png") para salvar o gráfico

df_versicolor.groupby(df_versicolor["species"])["petal_length"].value_counts() #analisar quais valores de petal_length existem na espécie == "versicolor" e quantas vezes aparecem

df_versicolor.groupby(df_versicolor["species"])["petal_length"].plot(color = "green", marker = "o")
plt.title("Gráfico da petal_length versus espécie versicolor")
plt.xlabel("species")
plt.ylabel("petal_length")
plt.legend()
#plt.savefig("versicolor.png") para salvar o gráfico

df_virginica.groupby(df_virginica["species"])["petal_length"].value_counts() #analisar quais valores de petal_length existem na espécie == "virginica" e quantas vezes aparecem

df_virginica.groupby(df_virginica["species"])["petal_length"].plot(color = "black", marker = "v")
plt.title("Gráfico da petal_length versus espécie virginica")
plt.xlabel("species")
plt.ylabel("petal_length")
plt.legend()
#plt.savefig("virginica.png") para salvar o gráfico

"""**Fazendo a junção dos 3 gráficos acima:**"""

df_setosa.groupby(df_setosa["species"])["petal_length"].plot()
df_versicolor.groupby(df_versicolor["species"])["petal_length"].plot(color = "green")
df_virginica.groupby(df_virginica["species"])["petal_length"].plot(color = "black")
plt.title("Gráfico da petal_length versus species")
plt.xlabel("species")
plt.ylabel("petal_length")
plt.legend()
#plt.savefig("todas_especies.png")

"""**Salvando os dataframes construídos, caso queira:**"""

df_setosa.to_csv("setosa.csv")
df_versicolor.to_csv("versicolor.csv")
df_virginica.to_csv("virginica.csv")

"""**Salvando os gráficos construídos, caso queira, basta colocar em cada plot**"""

#plt.savefig("imagem.png")