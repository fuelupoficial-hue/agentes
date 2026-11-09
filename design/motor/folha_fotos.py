"""Converte todos os downloads do Drive (JSON base64) de uma pasta em JPG e gera folha de contato.
Uso: python3 folha_fotos.py <pasta_tool_results> <pasta_saida>"""
import sys, os, json, base64, io, glob
from PIL import Image, ImageOps, ImageDraw
import pillow_heif
pillow_heif.register_heif_opener()
src, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
feitos = {}
for f in sorted(glob.glob(os.path.join(src, 'mcp-Google_Drive-download_file_content-*.txt'))):
    try:
        d = json.load(open(f))
        nome = os.path.splitext(d['title'])[0]
        if nome in feitos: continue
        im = Image.open(io.BytesIO(base64.b64decode(d['content'])))
        im = ImageOps.exif_transpose(im).convert('RGB')
        im.thumbnail((2000, 2000)); im.save(os.path.join(out, nome + '.jpg'), quality=92)
        feitos[nome] = im.size
    except Exception as e:
        print('pulou', f, e)
nomes = sorted(feitos)
T = 300; cols = 4; rows = (len(nomes) + cols - 1) // cols
sheet = Image.new('RGB', (cols * T, rows * (T + 24)), 'white')
for i, n in enumerate(nomes):
    im = Image.open(os.path.join(out, n + '.jpg')); im.thumbnail((T, T))
    sheet.paste(im, ((i % cols) * T, (i // cols) * (T + 24)))
    ImageDraw.Draw(sheet).text(((i % cols) * T + 4, (i // cols) * (T + 24) + T + 6), f"{n} {feitos[n][0]}x{feitos[n][1]}", fill='black')
sheet.save(os.path.join(out, '_folha.png'))
print(len(nomes), 'fotos:', ' '.join(nomes))
