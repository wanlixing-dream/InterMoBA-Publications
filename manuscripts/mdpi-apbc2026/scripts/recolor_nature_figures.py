from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
MAIN_FIGURES = ROOT / "figures"

# Muted, color-blind-friendly palette close to common Nature/Sci figure usage.
PALETTE = np.array(
    [
        (42, 86, 116),    # deep blue
        (60, 129, 120),   # teal
        (119, 151, 117),  # sage
        (198, 139, 75),   # amber
        (157, 102, 137),  # mauve
        (125, 132, 168),  # slate lavender
        (88, 88, 88),     # neutral grey
    ],
    dtype=np.float32,
)


def _rgb_to_hsv(rgb: np.ndarray) -> np.ndarray:
    arr = rgb / 255.0
    r, g, b = arr[..., 0], arr[..., 1], arr[..., 2]
    maxc = arr.max(axis=-1)
    minc = arr.min(axis=-1)
    delta = maxc - minc

    h = np.zeros_like(maxc)
    mask = delta > 1e-6
    rmax = mask & (maxc == r)
    gmax = mask & (maxc == g)
    bmax = mask & (maxc == b)
    h[rmax] = ((g[rmax] - b[rmax]) / delta[rmax]) % 6
    h[gmax] = ((b[gmax] - r[gmax]) / delta[gmax]) + 2
    h[bmax] = ((r[bmax] - g[bmax]) / delta[bmax]) + 4
    h /= 6.0

    s = np.where(maxc == 0, 0, delta / np.maximum(maxc, 1e-6))
    return np.stack([h, s, maxc], axis=-1)


def _hue_palette_indices(hue: np.ndarray) -> np.ndarray:
    # Hue bins: red/magenta -> mauve, orange/yellow -> amber, green -> sage/teal,
    # cyan/blue -> blue, purple -> slate lavender.
    idx = np.zeros(hue.shape, dtype=np.int16)
    idx[(hue >= 0.05) & (hue < 0.16)] = 3
    idx[(hue >= 0.16) & (hue < 0.29)] = 2
    idx[(hue >= 0.29) & (hue < 0.47)] = 1
    idx[(hue >= 0.47) & (hue < 0.64)] = 0
    idx[(hue >= 0.64) & (hue < 0.78)] = 5
    idx[(hue >= 0.78) & (hue < 0.94)] = 4
    idx[(hue >= 0.94) | (hue < 0.05)] = 4
    return idx


def _fit_for_submission(im: Image.Image, max_edge: int = 5200) -> Image.Image:
    width, height = im.size
    longest = max(width, height)
    if longest <= max_edge:
        return im

    scale = max_edge / longest
    size = (round(width * scale), round(height * scale))
    return im.resize(size, Image.Resampling.LANCZOS)


def _recolor_rgb(rgb_im: Image.Image) -> Image.Image:
    rgb = np.asarray(rgb_im, dtype=np.uint8).astype(np.float32)
    hsv = _rgb_to_hsv(rgb)
    hue, sat, val = hsv[..., 0], hsv[..., 1], hsv[..., 2]

    # Continuous, low-risk color grading. Avoid hard per-pixel remapping because
    # rasterized plots contain antialiasing and compression noise that should
    # not become visible in publication figures.
    lum = (
        0.2126 * rgb[..., 0]
        + 0.7152 * rgb[..., 1]
        + 0.0722 * rgb[..., 2]
    )[..., None]
    mapped = PALETTE[_hue_palette_indices(hue)]
    scientific_tint = 0.54 * mapped + 0.46 * lum

    # Blend only genuinely colored regions; preserve black axes/text and white
    # backgrounds. The blend weight is smooth, so gradients remain smooth.
    color_weight = np.clip((sat - 0.08) / 0.55, 0.0, 1.0)
    color_weight *= np.clip((0.98 - val) / 0.35, 0.0, 1.0)
    color_weight *= np.clip((val - 0.16) / 0.30, 0.0, 1.0)
    color_weight = (0.42 * color_weight)[..., None]

    out = rgb * (1.0 - color_weight) + scientific_tint * color_weight

    # Gentle editorial polish: cleaner paper white, slightly darker axes/text.
    very_light = val > 0.955
    dark = val < 0.16
    out[very_light] = 255 - (255 - out[very_light]) * 0.22
    out[dark] = out[dark] * 0.82
    out = np.clip(out, 0, 255).astype(np.uint8)
    return Image.fromarray(out, mode="RGB")


def nature_recolor(src: Path, dst: Path) -> None:
    im = Image.open(src).convert("RGBA")
    im = _fit_for_submission(im)
    white = Image.new("RGBA", im.size, (255, 255, 255, 255))
    white.alpha_composite(im)
    rgb_im = white.convert("RGB")

    result = _recolor_rgb(rgb_im)
    result = ImageEnhance.Contrast(result).enhance(1.06)
    result = ImageEnhance.Color(result).enhance(0.82)
    result = ImageEnhance.Sharpness(result).enhance(1.08)
    result = result.filter(ImageFilter.UnsharpMask(radius=0.45, percent=28, threshold=4))
    result.save(dst, optimize=True, dpi=(300, 300))


def main() -> None:
    # Main-manuscript figures only. Supplementary figures are intentionally
    # left untouched for this APBC revision pass.
    main_sources = [
        "fig1a.png",
        "fig1bc.png",
        "fig4abc.png",
        "fig2abcd.jpg",
        "fig2ef.jpg",
    ]

    for name in main_sources:
        src = MAIN_FIGURES / name
        dst = MAIN_FIGURES / f"{src.stem}_nature.png"
        nature_recolor(src, dst)
        print(dst.relative_to(ROOT))


if __name__ == "__main__":
    main()
