# Dupla
- Henrique Hardt Scholl
- Thiago Marinho Solfo

# A* - Stardew Valley

### O que o código faz?
Tenta descobrir o caminho mais rápido para sair de **Casa** e chegar na **Praia** no mapa do Stardew Valley considerando o dia do mês (de 1 a 28). Dependendo do dia, deve-se passar por diferentes lugares no meio do caminho (checkpoints) para conversar com alguns NPCs. O código usa o algoritmo de busca **A*** pra calcular qual a melhor rota.

### Tempo entre os lugares
Valores pra andar de um lugar direto pro outro (de x -> para y):
- **Casa**: Montanha (27), Ônibus (11), Floresta (23)
- **Montanha**: Casa (27), Spa (8), Lago (32), Cidade (26)
- **Ônibus**: Casa (11), Cidade (19)
- **Floresta**: Casa (23), Cidade (33), Praia (34)
- **Spa**: Montanha (8)
- **Lago**: Montanha (32)
- **Cidade**: Montanha (26), Ônibus (19), Floresta (33), Praia (30)
- **Praia**: Cidade (30), Floresta (34)

### Heurística
A heurística é quanto tempo falta de cada lugar até a Praia (o caminho mais rápido e direto sem falar com ninguém):
- **Casa**: 57
- **Montanha**: 56
- **Ônibus**: 49
- **Floresta**: 34
- **Spa**: 64
- **Lago**: 88
- **Cidade**: 30
- **Praia**: 0

### Dias, Lugares e Checkpoints dos NPCs
Os personagens ficam nos seguintes lugares e devem ser visitados em dias específicos:
- **Marlon** (Visitar no dia 9): Fica no Lago.
- **Abgail** (Visitar no dia 13): Praia (Segunda), Cidade (Quarta e Sexta), Floresta (Sábado). Os outros dias são desconhecidos/aleatórios.
- **Alex** (Visitar no dia 13): No Spa (Segunda, Terça, Quinta) ou na Cidade (outros dias).
- **Feiticeiro** (Visitar no dia 17): Sempre na Floresta.
- **Sam** (Visitar no dia 17): Cidade (Segunda, Quarta e Sexta) ou na Praia (outros dias).
- **Anão** (Visitar no dia 22): Sempre na Montanha.
- **George** (Visitar no dia 24): No Ônibus no dia 17 e na Cidade nos outros dias.

### Mapa / Grafo
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/grafos_branco.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/grafos_preto.svg">
  <img alt="Grafo" src="assets/grafos_preto.svg">
</picture>

---

### Curiosidades
Sabe por que esses checkpoints caem nesses dias exatos? Na **Wiki** oficial do jogo, grande parte desses dias representam seus **aniversários** (em diferentes estações do ano). Lembrar de visitá-los nessas datas dá `8x` mais pontos de amizade ao dar um presente que eles amam!

- **Marlon (Dia 9):** No jogo base, ele fica na Guilda dos Aventureiros e não tem sistema de amizade tradicional.
- **Abgail e Alex (Dia 13):** O Alex faz aniversário no dia 13 do Verão, enquanto a Abigail faz no dia 13 do Outono. É também no dia 13 da Primavera que ocorre o Festival do Ovo (onde a Abigail quase sempre ganha do jogador na caça aos ovos!).
- **Feiticeiro e Sam (Dia 17):** O Sam comemora seu aniversário no dia 17 do Verão. Feiticeiro faz no dia 17 do Inverno.
- **Anão (Dia 22):** O dia 22 do Verão é o aniversário do Anão na Montanha. Uma ótima data para levar aquele Rubi ou Ametista pra ele!
- **George (Dia 24):** Seu aniversário é dia 24 do Outono, a data perfeita para você visitá-lo e levar um Alho-poró de presente.
