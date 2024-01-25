#!/bin/bash

# 1 = Encoding nrz ∨ differential ∨ 4b5b v mixed_decode. bytestring_decode = byte_decode bei einem buchstaben, daher können wir einfach das Encoding so angeben.
# 2 = Sequenz von 1 und 0
python3 decode.py $1 $2
