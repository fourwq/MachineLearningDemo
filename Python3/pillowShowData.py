# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 16:42:24 2017

@author: onepiece
"""

from PIL import Image

import struct

import os

DATA_DST = 'handWritingData'

DATA_SRC = 'handWritingSrc'

def read_image(filename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()
    f.close()
#    return
    magic,images,rows,colums = struct.unpack_from('>IIII',buf,index)
    index +=struct.calcsize('>IIII')
    for i in range(images):
        image = Image.new('L',(colums, rows))
        for x in range(rows):
            for y in range(colums):
                image.putpixel((y,x),int(struct.unpack_from('>B',buf,index)[0]))
                index += struct.calcsize('>B')
        print('save'+str(i)+'image')
        image.save(DATA_DST+'/'+str(i)+'.png')
        
def read_label(filename, saveFilename):
    f = open(filename, 'rb')
    index = 0
    buf = f.read()
    f.close()
#    return
    magic, labels = struct.unpack_from('>II', buf, index)
    index += struct.calcsize('>II')
    
    labelArr = [0] * labels
    
    for x in range(labels):
        labelArr[x] = int(struct.unpack_from('>B', buf, index)[0])
        index += struct.calcsize('>B')
    save = open(saveFilename, 'w')
    save.write(','.join(map(lambda x: str(x), labelArr)))
    save.write('\n')
    save.close()
    print('save labels success')
if  __name__ == '__main__':
    
    if not os.path.exists(DATA_DST):
        os.mkdir(DATA_DST)    
   
    read_label(DATA_SRC+'/'+'train-labels.idx1-ubyte',DATA_DST+'//'+'label.txt')
    read_image(DATA_SRC+'/'+'train-images.idx3-ubyte')
    
    
    
    