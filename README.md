# 1. Problema de Negócio

Você acaba de ser contratado como Cientista de Dados da empresa Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer utilizando dados.

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.

O CEO também foi recém contratado e precisa entender melhor o negócio para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da empresa e que sejam gerados dashboards, a partir dessas análises, para responder às seguintes perguntas:

## Geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?

## País
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?

## Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?

## Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?

## Tipos de Culinária
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?


O CEO também pediu que fosse gerado um dashboard que permitisse que ele visualizasse as principais informações das perguntas que ele fez. O CEO precisa dessas informações o mais rápido possível, uma vez que ele também é novo na empresa e irá utilizá-las para entender melhor a empresa Fome Zero para conseguir tomar decisões mais assertivas.

Seu trabalho é utilizar os dados que a empresa Fome Zero possui e responder as perguntas feitas do CEO e criar o dashboard solicitado.


# 2. Premissas assumidas para a análise
1. Os dados não possuem datas de registro, por isso não serão feitas análises temporais em primeiro momento.
2. Marketplace foi o modelo de negócio assumido.
3. As 4 principais visões do negócio foram: Visão restaurantes, visão países, visão cidades e visão tipos de culinárias.


# 3. Estratégia da solução
O painel estratégico foi desenvolvido utilizando as métricas que refletem as 3 principais visões do modelo de negócio da empresa:
1. Visão dos restaurantes
2. Visão dos países
3. Visão das cidades
4. Visão dos tipos de culinárias

## 1. Visão dos restaurantes:
1. Total de Restaurantes Cadastrados
2. Total de Países Cadastrados
3. Total de Cidades Cadastradas
4. Total de Avaliações Feitas na Plataforma
5. Total de Tipos de Culinárias oferecidas
6. Localização dos restaurantes no mapa, agrupados por proximidade

## 2. Visão dos países:
1. Quantidade de Restaurantes Registados por país
2. Quantidade de Cidades Registradas por país
3. Médias da quantidade de avaliações feitas por países
4. Média de preço de um prato para Duas pessoas por País  

## 3. Visão das cidades:
1. Top Cidades com mais restaurantes na base de dados
2. Top Cidades com média de avaliação acima de 4
3. Top Cidades com média de avaliação acima de 2.5
4. Cidades com mais restaurantes com tipos de culinárias distintos

## 4. Visão dos tipos de culinária:
1. Melhores Restaurantes dos principais tipos de Culinárias: Italiana, Americana, Árabe, Japonesa e Brasileira
2. Top Restaurantes melhores avaliados
3. Melhores tipos de culinárias
4. Piores tipos de culinária


# 4. Top 3 Insights de dados
1. Índia e Estados Unidos possuem a maioria dos restaurantes
2. Nenhuma cidade possui mais que 80 restaurantes cadastrados
3. Os restaurantes localizados no Brasil possuem poucas avaliações comparados com os demais países.


# 5. O produto final do projeto
Painel online, hospedado em um Cloud e disponível para acesso em qualquer dispositivo conectado à internet.
O painel pode ser acessado através desse link: https://gabs-fomezero.streamlit.app/


# 6. Conclusão
O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas que exibam essas métricas da melhor forma possível para o CEO.

Com as visões implementadas no Dashboard, podemos concluir que Índia e Estados Unidos possuem a maioria dos restaurantes, que nenhuma cidade possui mais de 80 restaurantes, e que os clientes não estão avaliando os restaurantes dentro do Brasil.


# 7. Próximos Passos:
1. Melhorar a performance de carregamentos dos gráficos e mapas quando muitos países são selecionados ao mesmo tempo.
2. Exibir métricas relacionadas ao quanto influência as avaliações caso o restaurante faça reservas e entregas.
3. Fazer a conversão do valor das moedas de cada país para uma moeda única, com objetivo de fazer comparações mais robustas entre os valores dos pratos de cada país.




