# Economarket
Economarket é um projeto desenvolvido para o trabalho final da disciplina de Algoritmos em Grafos do curso de Ciência da Computação da Universidade Federal de Lavras. A disciplina é ministrada pelo Prof. Dr. Mayron César de Oliveira Moreira. Os autores do projeto são os alunos Igor Antônio dos Santos Alves Mendes, Isaías Gonçalves Ribeiro e Pedro Antônio de Souza.

## Motivação
A crise de saúde que vivemos atualmente, em meio à pandemia mundial do novo coronavírus, têm forçado mudanças de hábitos na vida de toda população. Não é mais adequado que os cidadãos passem grandes períodos de tempo em locais públicos e com aglomeração. Além disso, muitas pessoas tiveram sua renda diminuída, ou até mesmo totalmente perdida, seja por reajuste salarial, demissão ou, no caso de empreendedores, decréscimo no movimento de estabelecimentos.

Nesse cenário, manter a demanda doméstica de suprimentos básicos de alimentação tornou-se um desafio duplo para as pessoas: além de os supermercados serem ambientes altamente propícios para o contágio do covid-19, por ser um ambiente fechado em que há aglomeração de clientes frequentemente, há também a crise financeira enfrentada pela população.

Pensando nisso, foi proposto um sistema capaz de gerar listas de compras partir de produtos selecionados pelo usuário buscando o máximo de economia, i. e., são geradas listas priorizando a ocorrência mais barata dos produtos dentre as opções nos diferentes mercados.

## Definição Formal
Para resolver problemas de orçamento utilizando grafos, o mais indicado é utilizar os princípios da Árvore de Steiner. Em nosso projeto, pesquisamos os valores de 12 produtos de uma cesta básica em quatro supermercados de Lavras: ABC, BH, Bretas e Rex. No sistema Economarket, o usuário tem a possibilidade de criar uma lista com seus produtos de interesse e, em seguida, o sistema deverá gerar uma lista com os produtos mais baratos de cada mercado.

Na modelagem do grafo, os produtos são representados por vértices terminais e os mercados por vértices de Steiner. Nessa abordagem, dois vértices terminais nunca serão vizinhos, o que também ocorre entre os vértices de Steiner. As arestas guardam as informações de seus dois vértices (sempre um produto e um mercado), além da marca e do preço do produto. Assim, um vértice terminal pode-se ligar através de várias arestas a um mesmo vértice de Steiner, que ocorre quando um mercado oferece um mesmo produto de várias marcas distintas. 

## Algoritmo
Na literatura abordada no curso, são apresentadas implementações de algoritmos que objetivam encontrar uma única Árvore de Steiner em um grafo que satisfaça determinadas condições. Porém, em nosso problema, diversas vezes precisamos encontrar, a partir de um único grafo com vértices terminais e de Steiner, várias Árvores de Steiner. Nomeamos esse resultado como Floresta de Steiner. A figura abaixo representa uma modelagem de uma instância do problema.
<p align="center">
  <img src="https://github.com/phumacinha/Economarket/blob/master/imagens/grafo1.jpg" alt="Grafo 1"/>
  <p align="center" style="font-size:11px">Figura 1</p>
</p>

Em uma implementação de algoritmos convencionais vistos em sala de aula, obteríamos a seguinte árvore:
<p align="center">
  <img src="https://github.com/phumacinha/Economarket/blob/master/imagens/grafo1-alg-convencional.jpg" alt="Grafo 1"/>
  <p align="center" style="font-size:11px">Figura 2</p>
</p>

Essa, claramente, não é uma solução ideal, já que o PRODUTO2 seria apresentado nas listas de compra do supermercado Rex e do Bretas. Ao observarmos esse comportamento, buscamos implementar um algoritmo eficiente que atendesse nossos objetivos. Esse algoritmo funciona da seguinte maneira:
```
    1. Para cada vértice terminal t, faça:
    1.1 Para cada aresta de t, faça:
    1.1.1 Encontre a aresta de menor custo e adicione-a na Floresta de Steiner
    2. Retorne a Floresta de Steiner
```

Com esse simples algoritmo, obtemos resultados como esperávamos. A figura abaixo mostra o resultado obtido ao aplicar esse algoritmo no grafo da Figura 1:
<p align="center">
  <img src="https://github.com/phumacinha/Economarket/blob/master/imagens/grafo1-floresta-steiner.jpg" alt="Grafo 1"/>
  <p align="center" style="font-size:11px">Figura 3</p>
</p>

Como esperado, houve o retorne de uma floresta e não de uma única árvore.

## Resultados Computacionais
Em um primeiro momento, desejávamos implementar esse sistema para a web, utilizando Python3, o framework Django e um banco de dados como Mysql. Contudo, percebemos que esse sistema dificultaria a reprodução do teste por terceiros. Assim, foi implementado um sistema que é executado no terminal do Python e utilizamos um arquivo de Excel para o armazenamento dos dados.

### Instância teste
Na primeira planilha, armazenamos quatro supermercados de Lavras:
1. ABC;
2. BH;
3. Bretas;
4. Rex.

Na segunda planilha, armazenamos 12 produtos de uma cesta básica:
1. Peito de Frango 1 Kg
2. Leite 1 L
3. Feijão 1 Kg
4. Arroz 5 Kg
5. Fubá 1 Kg
6. Batata Kg
7. Tomate Kg
8. Pão Kg
9. Café 1 Kg
10. Banana Kg
11. Açúcar 5 Kg
12. Farinha de Mandioca 5 Kg

Na terceira planilha, armazenamos 46 marcas de produtos. Pela grande quantidade de informação, não será interessante exibi-las aqui.

Na quarta planilha, denominada "item", armazenamos as relações entre mercado, produto, marca e preço.

Assim, o sistema lê esses dados e gera listas a partir da necessidade do usuário.

### Experimentos
Tela incial da execução:
<p align="center">
  <img src="https://github.com/phumacinha/Economarket/blob/master/imagens/captura1.png" alt="Captura de tela"/>
</p>
Ao adicionar na lista todos os produtos cadastrados na base de dados, modelamos um grafo com 16 vértices e 70 arestas.
<p align="center">
  <img src="https://github.com/phumacinha/Economarket/blob/master/imagens/captura2.png" alt="Captura de tela"/>
</p>
Como resultados obtivemos uma floresta com 16 vértices e 11 arestas.
<p align="center">
  <img src="https://github.com/phumacinha/Economarket/blob/master/imagens/captura3.png" alt="Captura de tela"/>
</p>
Fazendo uma execução com a função invertida, isto é, procurando os maiores preços, podemos observar a utilidade do sistema em contextos práticos:
<p align="center">
  <img src="https://github.com/phumacinha/Economarket/blob/master/imagens/captura4.png" alt="Captura de tela"/>
</p>
Nessa execução da função invertida, a soma dos valores dos produtos chegou a R$ 122,32. Já na execução correta, a soma dos valores foi de R$ 66,12. Isso representa uma economia de 45,9% no valor final, demonstrando sua grande aplicabilidade no mundo real.

### Forças e fraquezas
Como pôde-se perceber, pela simplicidade do algoritmo, sua execução é extremamente rápida. Mesmo em casos de teste com 2000 vértices e 2000 arestas, o tempo de execução não chegou a um segundo, demonstrando a eficiência na resolução de orçamentos. Porém, algumas otimizações não foram implementadas. Um exemplo é quando há empate de valor de produto. No algoritmo não há nenhum critério de escolha das arestas. Suponha que um produto P tenho o valor mínimo se repetindo nos mercados A e B. Suponha também, que na lista de compras do mercado A já existam alguns produtos e que na lista do mercado B ainda não há nenhum produto. Como não há critério de desempate, o produto P pode ser acrescentado na lista do mercado B, acarretando num problema de logística que poderia ser evitado.

### Conclusões
Ao tratarmos problemas de orçamento, é comum utilizarmos tabelas onde as colunas representam os produtos e as linhas indicam os estabelecimentos. Nos campos de interseção entre linhas e colunas, indicamos o valor. Porém, essa abordagem torna-se inviável com o aumento da complexidade de problemas desse tipo (acrescentando marcas dos produtos, por exemplo). Assim, a abordagem através de grafos torna-se uma ótima opção para resolução desses problemas. Além de economizar tempo, economiza-se espaço e aumenta-se o nível de detalhamento da solução.

Ainda nesse semestre, foi desenvolvido por alunos da disciplina de Interação Humano-Computador, ministrada pelo Prof. Dr. André Pimenta, um projeto de um aplicativo de pesquisa de preços e geração de listas de compras em mercados de Lavras, visando otimizar o uso desses estabelecimentos no momento de crise sanitária em que vivemos. Portanto, o presente trabalho possui grande relevância na atualidade. O próximo passo, além de realizar otimizações citadas na seção Forças e Fraquezas, deve ser a implementação uma função que também leva em consideração a distância da casa do usuário até o mercado, pretendendo retornar listas de compras realmente econômicas pensando no deslocamento do usuário até o estabelecimento.

