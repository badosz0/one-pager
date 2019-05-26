from PIL import Image, ImageDraw, ImageFont
from eta import ETA
import sys

width = 4960
height = 7016
fontIn = 'fonts/Roboto-Light.ttf'
margin = 40
offset = 40

def textwrap(text, width):
    return [text[i:i+width] for i in range(0, len(text), width)]

if len(sys.argv) < 2 or sys.argv[1][-4:] != '.txt':
    print('Please specify .txt file.')
else:
    text = open(sys.argv[1],"r", encoding="utf-8").read().replace("\n"," ").replace("\t"," ")

    blank = Image.new('RGBA', (width, height), color=(255, 255, 255))
    font = ImageFont.truetype(font=fontIn, size=11)

    canvas = ImageDraw.Draw(blank)

    text = textwrap(text, 950)
    lines = len(text)

    print(f'File: {sys.argv[1]}')
    print(f'Lines: {lines}')

    eta = ETA(lines/10)
    for line in text:
        canvas.text((margin, offset), line, font=font, fill="#000000")
        offset += font.getsize(line)[1]
        eta.print_status()

    blank.save(f'{sys.argv[1][:-4]}.png')
    eta.done()
