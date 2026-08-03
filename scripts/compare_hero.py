"""Compara screenshot atual com a referência medindo posições do mascote e do card."""
from PIL import Image
import numpy as np

REF = Image.open("imagens/hero/herosection_completa.png").convert("RGBA")
SHOT = Image.open("imagens/hero/screenshot_viewport.png").convert("RGBA")
print("ref size:", REF.size)
print("shot size:", SHOT.size)

def find_orange_bbox(img):
    """Encontra bbox de pixels laranja (raposa)."""
    a = np.array(img)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mask = (r > 180) & (g > 80) & (g < 200) & (b < 150) & (r.astype(int) - b.astype(int) > 30)
    if not mask.any():
        return None
    ys, xs = np.where(mask)
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())

def find_white_card_bbox(img, exclude_top_px=100):
    """Encontra bbox do card branco (região grande de branco cercada por linha)."""
    a = np.array(img)
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    # branco: R, G, B > 240
    mask = (r > 240) & (g > 240) & (b > 240)
    # descartar header (top)
    mask[:exclude_top_px, :] = False
    if not mask.any():
        return None
    ys, xs = np.where(mask)
    return int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())

print("\n=== REFERÊNCIA ===")
print("mascote (laranja):", find_orange_bbox(REF))
print("card branco (após y=100):", find_white_card_bbox(REF, exclude_top_px=100))

print("\n=== SCREENSHOT ATUAL ===")
print("mascote (laranja):", find_orange_bbox(SHOT))
print("card branco (após y=100):", find_white_card_bbox(SHOT, exclude_top_px=100))
