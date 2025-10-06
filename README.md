# Craft Sprites

Ferramenta em **Python** para dividir automaticamente **spritesheets** em imagens individuais.  
Este script detecta automaticamente quantas sprites existem.

## Como usar

Execute o script app.py com a imagem desejada

```bash
python app.py minha_imagem.png
```

Será criada uma pasta chamada minha_imagem_auto_rect_output

Também posso controlar o `padding` em todos os lados com um tamanho específico

```bash
python app.py minha_imagem.png 5
# 5 pixels de padding
```

Ou posso definir um padding individual (top right bottom left)

```bash
python app.py minha_imagem.png 0 10 0 10
```

Se o **spritesheets** tiver um fundo que não seja transparente posso tentar remover o fundo passando o parâmetro `--remover-background`

```bash
python app.py minha_imagem.png --remover-background # padding 0 nos cantos da imagem
python app.py minha_imagem.png 20 --remover-background # padding 20 nos cantos da imagem
python app.py minha_imagem.png 0 20 0 20 --remover-background # padding: top=0, right=20, bottom=0, left=20
```
