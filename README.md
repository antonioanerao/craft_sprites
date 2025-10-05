# Craft Sprites

Ferramenta em **Pythonw** para dividir automaticamente **spritesheets** em imagens individuais.  
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
