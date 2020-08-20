# SuperNimLearner

## Introdução

No jogo Nim, começamos com um certo número de pilhas, cada uma com um certo número de objetos. Os jogadores se revezam: na vez de um jogador, o jogador remove qualquer número não negativo de objetos de qualquer pilha não vazia. Quem remover o último objeto perde.

Há uma estratégia simples que você pode imaginar para este jogo: se houver apenas uma pilha e três objetos restantes nela, e for sua vez, sua melhor aposta é remover dois desses objetos, deixando seu oponente com o terceiro e último objeto para remover . Mas se houver mais pilhas, a estratégia fica consideravelmente mais complicada. Neste problema, construimos uma IA para aprender a estratégia para este jogo por meio do aprendizado por reforço. Jogando contra si mesma repetidamente e aprendendo com a experiência, eventualmente nossa IA aprenderá quais ações tomar e quais ações evitar.

## Como usar

### python train.py filename.npy 10000

para treinar uma AI defina um arquivo para salvar (filename.npy) e a quantidade de jogos que ela realizará no treinamento (10000)

### python play.py filename.npy

para jogar contra uma AI já treinada informe o arquivo em que a mesma foi salva (filename.npy)

## Projeto original

Projeto 4 do Curso: [CS50’s Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/2020/weeks/4/)