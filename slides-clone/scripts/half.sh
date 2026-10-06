#!/bin/bash
# render decks and write half-size previews shots/NN-h.png
node scripts/screenshot.mjs "$@" 2>&1 | grep -c ok
for i in "$@"; do python3 -c "
from PIL import Image; im=Image.open('shots/$i.png'); im.resize((im.width//2,im.height//2)).save('shots/$i-h.png')"; done
