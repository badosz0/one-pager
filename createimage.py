from PIL import Image, ImageDraw, ImageFont
import textwrap, sys

if len(sys.argv) < 2 or sys.argv[1][-4:] != '.txt':
    print('Please specify .txt file.')
else:
    file = open(sys.argv[1],"r", encoding="utf-8")

    text = file.read()

    text = text.replace("\n"," ")

    file.close()

    blank = Image.new('RGBA', (4960, 7016), color=(255, 255, 255))

    font = ImageFont.truetype(font='Roboto-Light.ttf', size=11)

    canv = ImageDraw.Draw(blank)

    margin = offset = 40

    cur = 0

    lines = len(textwrap.wrap(text, width=950))

    for line in textwrap.wrap(text, width=950):

        cur = cur + 1

        canv.text((margin, offset), line, font=font, fill="#000000")

        offset += font.getsize(line)[1]

        print(round(cur/lines*100,2),"%")

    blank.save('done.png')
