# Gerador de Gráfico do Batman

Este projeto visualiza o icônico logo do Batman usando um conjunto de equações matemáticas. O projeto é implementado em Python e utiliza a biblioteca `matplotlib` para plotar o resultado, juntamente com `numpy` para operações numéricas.

## Índice
- [Introdução](#introdução)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Funções](#funções)
- [Exemplo de Saída](#exemplo-de-saída)
- [Licença](#licença)

## Introdução

O Gerador de Gráfico do Batman é um projeto divertido que usa uma série de equações matemáticas para gerar um gráfico de contorno do famoso logo do Batman. Este projeto aproveita o poder da computação numérica e da plotagem em Python para criar o logo inteiramente a partir de funções matemáticas.

## Requisitos

Para executar este projeto, você precisará das seguintes bibliotecas Python:
- `matplotlib`: Para plotar o logo do Batman.
- `numpy`: Para lidar com operações numéricas como raiz quadrada e arrays.

Você pode instalar essas dependências usando o pip:
```bash
pip install matplotlib, numpy
```
##Instalação
Clone este repositório:
Copiar código

git clone https://github.com/seuusuario/gerador-grafico-batman.git
Navegue até o diretório do projeto:

Copiar código
cd gerador-grafico-batman

##Uso
Para plotar o logo do Batman, simplesmente execute o arquivo batman_plotter.py:

Copiar código
python batman_plotter.py
Isso gerará um gráfico de contorno do logo do Batman com base nas equações matemáticas.

##Funções
As principais funções usadas neste projeto são:

batman_equations(x, y): Esta função retorna as equações matemáticas para plotar o logo do Batman.
calculate_batman(batman1, batman2, batman3, batman4, batman5, batman6): Combina as equações em um único resultado.
plot_batman(x, y, batman_equations): Plota o logo do Batman usando matplotlib.
main(): A função principal que inicializa o processo de plotagem criando uma malha (meshgrid) e chamando as outras funções.

Exemplo de Saída
A saída do script gerará um gráfico que se parece com isso:

![image](https://github.com/user-attachments/assets/7638cbae-263b-4581-9282-c600e4ae328d)

