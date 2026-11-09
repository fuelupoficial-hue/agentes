"""Converte um download do Drive (JSON com base64) em JPG/PNG.
Uso: python3 heic2jpg.py <arquivo.json> <saida.jpg> [lado_maior_px]
Ferramentas do Drive salvam downloads grandes em arquivo JSON {content: base64, title, mimeType}."""
import sys, json, base64, io
from PIL import Image, ImageOps
import pillow_heif
pillow_heif.register_heif_opener()
src, out = sys.argv[1], sys.argv[2]
lado = int(sys.argv[3]) if len(sys.argv) > 3 else 1600
d = json.load(open(src))
im = Image.open(io.BytesIO(base64.b64decode(d['content'])))
im = ImageOps.exif_transpose(im).convert('RGB')
im.thumbnail((lado, lado))
im.save(out, quality=90)
print(d.get('title'), im.size)
