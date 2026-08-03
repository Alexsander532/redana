"""Recorta o logo (raposa pequena) do canto superior esquerdo."""
from PIL import Image
import numpy as np

SRC = "imagens/hero/herosection_completa.png"
img = Image.open(SRC).convert("RGBA")
W, H = img.size
print("size:", W, H)

# Logo: canto superior esquerdo
logo_box = (40, 25, 118, 105)
logo = img.crop(logo_box)
arr = np.array(logo)
r, g, b, a = arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3]

# Remover branco/lavanda
is_white = (r > 235) & (g > 235) & (b > 235)
is_lightlav = (r > 200) & (g > 195) & (b > 215)
mask = is_white | is_lightlav

# Preservar laranja, preto
is_orange = (r > 180) & (g < 200) & (b < 160) & (r.astype(int) - b.astype(int) > 30)
is_dark = (r < 80) & (g < 80) & (b < 80)
mask = mask & ~is_orange & ~is_dark

arr[..., 3] = np.where(mask, 0, 255)
out = Image.fromarray(arr, mode="RGBA")
out.save("public/logo.png")
print("saved public/logo.png", out.size)
