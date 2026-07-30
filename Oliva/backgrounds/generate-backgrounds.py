#!/usr/bin/env python3
"""
Genera i PNG dello sfondo Oliva a partire dalla stessa composizione di oliva-bg.svg.
Generates the Oliva background PNGs from the same composition as oliva-bg.svg.

Le coordinate sono normalizzate sul lato corto, cosi la composizione regge
sia in landscape sia in portrait senza dover ritagliare.

Uso / Usage:
    pip install pillow numpy
    python3 generate-backgrounds.py
"""

import numpy as np
from PIL import Image

OUT = [
    ("oliva-bg-2560x1440.png", 2560, 1440),
    ("oliva-bg-1170x2532.png", 1170, 2532),
]


def hexrgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], dtype=np.float64)


# Palette Oliva
SKY_TOP = hexrgb("#1c200d")
SKY_MID = hexrgb("#20240f")
SKY_BOT = hexrgb("#2f361a")
GLOW = hexrgb("#687244")
COUNTERGLOW = hexrgb("#83905e")
RIDGE_1_TOP = hexrgb("#2e3419")
RIDGE_1_BOT = hexrgb("#2a2f16")
RIDGE_2 = hexrgb("#32381b")
EDGE = hexrgb("#4f5730")
VIGNETTE = hexrgb("#15170a")


def lerp(a, b, t):
    return a + (b - a) * t[..., None]


def over(base, color, alpha):
    """Alpha compositing di un colore piatto sopra base."""
    return base * (1.0 - alpha[..., None]) + color * alpha[..., None]


def smoothstep(t):
    """Easing di Hermite: evita il nucleo netto degli aloni e le bande visibili."""
    return t * t * (3.0 - 2.0 * t)


def radial_alpha(u, v, cx, cy, r, stops, aspect):
    """stops: lista di (offset, opacita). Distanza corretta per l'aspect ratio."""
    dx = (u - cx) * aspect
    dy = v - cy
    d = np.sqrt(dx * dx + dy * dy) / r
    a = np.zeros_like(d)
    prev_off, prev_op = stops[0]
    a[:] = prev_op
    for off, op in stops[1:]:
        seg = (d > prev_off) & (d <= off)
        t = smoothstep(np.clip((d - prev_off) / max(off - prev_off, 1e-9), 0, 1))
        a = np.where(seg, prev_op + (op - prev_op) * t, a)
        prev_off, prev_op = off, op
    a = np.where(d > stops[-1][0], stops[-1][1], a)
    return np.clip(a, 0, 1)


def ellipse_field(u, v, cx, cy, rx, ry):
    """Ritorna il valore normalizzato della forma implicita dell'ellisse.
    < 1 = interno, > 1 = esterno."""
    dx = (u - cx) / rx
    dy = (v - cy) / ry
    return np.sqrt(dx * dx + dy * dy)


def render(w, h):
    aspect = w / h
    # u in [0,1] su X, v in [0,1] su Y
    u = np.linspace(0.0, 1.0, w)[None, :].repeat(h, axis=0)
    v = np.linspace(0.0, 1.0, h)[:, None].repeat(w, axis=1)

    # --- Cielo: gradiente verticale a tre stop ---
    img = np.zeros((h, w, 3), dtype=np.float64)
    upper = v <= 0.45
    t_up = np.clip(v / 0.45, 0, 1)
    t_dn = np.clip((v - 0.45) / 0.55, 0, 1)
    img = np.where(upper[..., None],
                   lerp(SKY_TOP, SKY_MID, t_up),
                   lerp(SKY_MID, SKY_BOT, t_dn))

    # --- Alone frost in alto a destra ---
    a = radial_alpha(u, v, 0.74, 0.16, 0.78,
                     [(0.0, 0.30), (0.5, 0.11), (1.0, 0.0)], aspect)
    img = over(img, GLOW, a)

    # --- Contro-alone in basso a sinistra ---
    a = radial_alpha(u, v, 0.14, 0.92, 0.55,
                     [(0.0, 0.10), (1.0, 0.0)], aspect)
    img = over(img, COUNTERGLOW, a)

    # Spessore del bordo in unita normalizzate, ~2px sul lato lungo
    edge_w = 2.0 / max(w, h)

    # --- Crinale 1: ellisse molto larga, centro sotto la cornice ---
    for cy, rx, ry, fill_top, fill_bot, fill_a, edge_a in (
        (2.2361, 2.3611, 1.5278, RIDGE_1_TOP, RIDGE_1_BOT, 1.00, 0.55),
        (2.4722, 2.0833, 1.5694, RIDGE_2, RIDGE_2, 0.55, 0.35),
    ):
        f = ellipse_field(u, v, 0.5, cy, rx, ry)
        inside = f <= 1.0
        # gradiente verticale interno al crinale
        vt = np.clip((v - 0.6) / 0.4, 0, 1)
        fill = lerp(fill_top, fill_bot, vt)
        img = np.where(inside[..., None],
                       img * (1 - fill_a) + fill * fill_a,
                       img)
        # bordo: banda sottile attorno a f == 1
        band = np.clip(1.0 - np.abs(f - 1.0) / (edge_w * 1.6), 0, 1)
        img = over(img, EDGE, band * edge_a)

    # --- Vignettatura ---
    a = radial_alpha(u, v, 0.5, 0.45, 0.78,
                     [(0.0, 0.0), (0.55, 0.0), (1.0, 0.42)], aspect)
    img = over(img, VIGNETTE, a)

    # Dithering leggero: evita il banding nei gradienti ampi
    rng = np.random.default_rng(2024)
    img = img + rng.uniform(-0.6, 0.6, img.shape)

    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


if __name__ == "__main__":
    for name, w, h in OUT:
        render(w, h).save(name, optimize=True)
        print(f"{name}  {w}x{h}")
