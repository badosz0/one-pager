from PIL import Image, ImageDraw, ImageFont
import textwrap, sys

width = 4960
height = 7016
fontIn = 'fonts/Roboto-Light.ttf'

if len(sys.argv) < 2 or sys.argv[1][-4:] != '.txt':
    print('Please specify .txt file.')
else:
    text = open(sys.argv[1],"r", encoding="utf-8").read().replace("\n"," ")

    blank = Image.new('RGBA', (width, height), color=(255, 255, 255))

    font = ImageFont.truetype(font=fontIn, size=11)

    canvas = ImageDraw.Draw(blank)

    margin = offset = 40

    curline = 0

    lines = len(textwrap.wrap(text, width=950))

    for line in textwrap.wrap(text, width=950):

        cur = cur + 1

        canvas.text((margin, offset), line, font=font, fill="#000000")

        offset += font.getsize(line)[1]

        print(round(cur/lines*100,2),"%")

    blank.save(f'{sys.argv[1]}.png')
