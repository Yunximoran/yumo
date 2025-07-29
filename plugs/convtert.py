import cairosvg
import io
from pathlib import Path
from tkinter import filedialog
from PIL import Image

class SvgSizeError(Exception): ...

def svgtoico(svg, ico, size=64):
    if size not in (16, 24, 32, 48, 64, 128, 256):
        raise "size error must in 16, 24, 32, 48, 64, 128, 256"
    
    # 转换成PNG数据
    png = cairosvg.svg2png(
        url=svg,
        output_height=size,
        output_width=size
    )

    img = Image.open(io.BytesIO(png))
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    
    img.save(
        ico,
        format="ICO",
        bitdepth=32  # 支持透明通道
    )

def icotosvg(ico, svg, size=64):
    if size not in (16, 24, 32, 8, 64, 128, 256):
        raise "size error must in 16, 24, 32, 48, 64, 128, 256"
    
    