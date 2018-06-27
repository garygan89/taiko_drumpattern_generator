import sys
from PIL import Image

# A script to create Taiko notes in horizontal image
# Created by: dsync
# Created at: June 27, 2018

args = []
args.append('kdddkdddkdddkddd')
args.append('dkkkd kdddk')
args.append('dkkdkddk')
args.append('ddkd kkdk')
args.append('ddkdkkdk')
args.append('dkkd kddk')
args.append('dkkdkddk')
args.append('ddkdk ddkkd')
args.append('ddkdkddkkd')
args.append('ddkd kkdk dkkd kddk ddkdk ddkkd dkkkd kdddk')
args.append('ddkdkkdkdkkdkddkddkdkddkkddkkkdkdddk')

output_dir = 'gen'

imm = {}
imm['don'] = Image.open('images/don.png')
imm['kat'] = Image.open('images/kat.png')
imm['blank'] = Image.open('images/blank.png')

for arg in args:    
    print('Creating drum pattern %s' % arg)
    total_notes = len(arg)    
        
    print('there are %d letters' % len(arg))

    # widths, heights = zip(*(i.size for i in images))

    widths, heights = imm['blank'].size

    # total_width = sum(widths)
    total_width = (widths * total_notes)
    max_height = heights
       
    new_im = Image.new('RGBA', (total_width, max_height), (255, 0, 0, 0))

    print('Creating final image with width=%d, length=%d' % (total_width, max_height))

    x_offset = 0

    _im = []
    for c in arg:
        if (c == 'd'):
            _im = imm['don']
        elif (c == 'k'):
            _im = imm['kat']
        elif (c == ' '):
            _im = imm['blank']
        new_im.paste(_im, (x_offset,0), mask=_im)
        x_offset += 50 # TODO: Change this value depending on BPM. 50 is default spacing

    output_im = '%s\%s.png' % (output_dir, arg)
    new_im.save(output_im)
    print('Image=%s saved!' % output_im)