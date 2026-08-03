"""Recorta o mascote e remove o fundo lavanda."""
from PIL import Image
import numpy as np

SRC = "imagens/hero/herosection_completa.png"
img = Image.open(SRC).convert("RGBA")
W, H = img.size
print("size:", W, H)

# Crop mais apertado: termina antes da linha de features
# A imagem é 1536x1024. O mascote fica entre x ~ 580 e x ~ 1030
# Cortar y até ~700 (em cima da linha de features) para não pegar o texto
mascot_box = (580, 140, 1040, 720)
mascot = img.crop(mascot_box)
arr = np.array(mascot)
r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]

# Máscara: tudo que é lavanda claro, branco, ou cinza claro = transparente
# Lavanda claro (R~ 220-240, G~ 220-235, B~ 240-255)
is_lavender = (r > 200) & (g > 195) & (b > 215) & (np.abs(r.astype(int) - g.astype(int)) < 30)
# Quase branco
is_white = (r > 235) & (g > 235) & (b > 235)
# Cinza claro (faixa estreita)
is_lightgray = (r > 210) & (g > 210) & (b > 210) & (np.abs(r.astype(int) - g.astype(int)) < 8) & (np.abs(r.astype(int) - b.astype(int)) < 8)
mask = is_lavender | is_white | is_lightgray

# Preservar laranja (raposa)
is_orange = (r > 170) & (g > 80) & (g < 200) & (b < 160) & (r.astype(int) - b.astype(int) > 30)
# Preservar preto (contorno, olhos, óculos)
is_dark = (r < 80) & (g < 80) & (b < 80)
# Preservar marrom (mãozinha, rabo)
is_brown = (r > 90) & (r < 180) & (g > 40) & (g < 120) & (b < 80) & (r.astype(int) - b.astype(int) > 30)
# Preservar hoodie (azul muito escuro)
is_hoodie = (r < 70) & (g < 70) & (b < 100) & (b.astype(int) - r.astype(int) < 30)
# Texto escuro das features (cinza escuro)
is_text = (r < 130) & (g < 130) & (b < 150) & (np.abs(r.astype(int) - g.astype(int)) < 20)
# Preservar o "R" do peito (branco dentro do hoodie — cuidado aqui)
# O R branco está dentro do hoodie. Como o hoodie é escuro e o R é branco, vamos preservar via proximidade
# Mais simples: erosão — não remover pixels que estão perto de pixel laranja
mask = mask & ~is_orange & ~is_dark & ~is_brown & ~is_hoodie & ~is_text

arr[..., 3] = np.where(mask, 0, 255)
out = Image.fromarray(arr, mode="RGBA")
out.save("public/mascot.png")
print("saved public/mascot.png", out.size)
