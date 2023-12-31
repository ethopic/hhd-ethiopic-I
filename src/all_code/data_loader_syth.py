# -*- coding: utf-8 -*-
"""data_loader_syth.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bsXxUft3iuqNNbtx3FMRMISwDeet97qY
"""

from google.colab import drive
drive.mount('/content/drive')

tint_path ='/content/drive/MyDrive/sample_tint'# add the path of the images here

dicts={1: 'ሀ', 2: 'ሁ', 3: 'ሂ', 4: 'ሃ', 5: 'ሄ', 6: 'ህ', 7: 'ሆ', 8: 'ለ', 9: 'ሉ', 10: 'ሊ', 11: 'ላ', 12: 'ሌ', 13: 'ል', 14: 'ሎ', 15: 'ሏ', 16: 'ሐ', 17: 'ሑ', 18: 'ሒ', 19: 'ሓ', 20: 'ሔ', 21: 'ሕ', 22: 'ሖ', 23: 'መ', 24: 'ሙ', 25: 'ሚ', 26: 'ማ', 27: 'ሜ', 28: 'ም', 29: 'ሞ', 30: 'ሟ', 31: 'ሠ', 32: 'ሡ', 33: 'ሢ', 34: 'ሣ', 35: 'ሤ', 36: 'ሥ', 37: 'ሦ', 38: 'ረ', 39: 'ሩ', 40: 'ሪ', 41: 'ራ', 42: 'ሬ', 43: 'ር', 44: 'ሮ', 45: 'ሯ', 46: 'ሰ', 47: 'ሱ', 48: 'ሲ', 49: 'ሳ', 50: 'ሴ', 51: 'ስ', 52: 'ሶ', 53: 'ሷ', 54: 'ሸ', 55: 'ሹ', 56: 'ሺ', 57: 'ሻ', 58: 'ሼ', 59: 'ሽ', 60: 'ሾ', 61: 'ሿ', 62: 'ቀ', 63: 'ቁ', 64: 'ቂ', 65: 'ቃ', 66: 'ቄ', 67: 'ቅ', 68: 'ቆ', 69: 'ቈ', 70: 'ቊ', 71: 'ቋ', 72: 'ቍ', 73: 'በ', 74: 'ቡ', 75: 'ቢ', 76: 'ባ', 77: 'ቤ', 78: 'ብ', 79: 'ቦ', 80: 'ቧ', 81: 'ቨ', 82: 'ቩ', 83: 'ቪ', 84: 'ቫ', 85: 'ቬ', 86: 'ቭ', 87: 'ቮ', 88: 'ተ', 89: 'ቱ', 90: 'ቲ', 91: 'ታ', 92: 'ቴ', 93: 'ት', 94: 'ቶ', 95: 'ቷ', 96: 'ቸ', 97: 'ቹ', 98: 'ቺ', 99: 'ቻ', 100: 'ቼ', 101: 'ች', 102: 'ቾ', 103: 'ቿ', 104: 'ኀ', 105: 'ኁ', 106: 'ኂ', 107: 'ኃ', 108: 'ኄ', 109: 'ኅ', 110: 'ኆ', 111: 'ኈ', 112: 'ኊ', 113: 'ኋ', 114: 'ኍ', 115: 'ነ', 116: 'ኑ', 117: 'ኒ', 118: 'ና', 119: 'ኔ', 120: 'ን', 121: 'ኖ', 122: 'ኗ', 123: 'ኘ', 124: 'ኙ', 125: 'ኚ', 126: 'ኛ', 127: 'ኜ', 128: 'ኝ', 129: 'ኞ', 130: 'ኟ', 131: 'አ', 132: 'ኡ', 133: 'ኢ', 134: 'ኣ', 135: 'ኤ', 136: 'እ', 137: 'ኦ', 138: 'ኧ', 139: 'ከ', 140: 'ኩ', 141: 'ኪ', 142: 'ካ', 143: 'ኬ', 144: 'ክ', 145: 'ኮ', 146: 'ኰ', 147: 'ኲ', 148: 'ኳ', 149: 'ኴ', 150: 'ኵ', 151: 'ኸ', 152: 'ኹ', 153: 'ኺ', 154: 'ኻ', 155: 'ኼ', 156: 'ኽ', 157: 'ኾ', 158: 'ወ', 159: 'ዉ', 160: 'ዊ', 161: 'ዋ', 162: 'ዌ', 163: 'ው', 164: 'ዎ', 165: 'ዏ', 166: 'ዐ', 167: 'ዑ', 168: 'ዒ', 169: 'ዓ', 170: 'ዔ', 171: 'ዕ', 172: 'ዖ', 173: 'ዘ', 174: 'ዙ', 175: 'ዚ', 176: 'ዛ', 177: 'ዜ', 178: 'ዝ', 179: 'ዞ', 180: 'ዟ', 181: 'ዠ', 182: 'ዡ', 183: 'ዢ', 184: 'ዣ', 185: 'ዤ', 186: 'ዥ', 187: 'ዦ', 188: 'የ', 189: 'ዩ', 190: 'ዪ', 191: 'ያ', 192: 'ዬ', 193: 'ይ', 194: 'ዮ', 195: 'ደ', 196: 'ዱ', 197: 'ዲ', 198: 'ዳ', 199: 'ዴ', 200: 'ድ', 201: 'ዶ', 202: 'ዷ', 203: 'ዿ', 204: 'ጀ', 205: 'ጁ', 206: 'ጂ', 207: 'ጃ', 208: 'ጄ', 209: 'ጅ', 210: 'ጆ', 211: 'ጇ', 212: 'ገ', 213: 'ጉ', 214: 'ጊ', 215: 'ጋ', 216: 'ጌ', 217: 'ግ', 218: 'ጎ', 219: 'ጐ', 220: 'ጒ', 221: 'ጓ', 222: 'ጔ', 223: 'ጕ', 224: 'ጠ', 225: 'ጡ', 226: 'ጢ', 227: 'ጣ', 228: 'ጤ', 229: 'ጥ', 230: 'ጦ', 231: 'ጧ', 232: 'ጨ', 233: 'ጩ', 234: 'ጪ', 235: 'ጫ', 236: 'ጬ', 237: 'ጭ', 238: 'ጮ', 239: 'ጯ', 240: 'ጰ', 241: 'ጱ', 242: 'ጲ', 243: 'ጳ', 244: 'ጴ', 245: 'ጵ', 246: 'ጶ', 247: 'ጸ', 248: 'ጹ', 249: 'ጺ', 250: 'ጻ', 251: 'ጼ', 252: 'ጽ', 253: 'ጾ', 254: 'ጿ', 255: 'ፀ', 256: 'ፁ', 257: 'ፂ', 258: 'ፃ', 259: 'ፄ', 260: 'ፅ', 261: 'ፆ', 262: 'ፈ', 263: 'ፉ', 264: 'ፊ', 265: 'ፋ', 266: 'ፌ', 267: 'ፍ', 268: 'ፎ', 269: 'ፏ', 270: 'ፐ', 271: 'ፑ', 272: 'ፒ', 273: 'ፓ', 274: 'ፔ', 275: 'ፕ', 276: 'ፖ', 277: 'ፚ', 278: '፠', 279: '፡', 280: '።', 281: '፣', 282: '፤', 283: '፥', 284: '፦', 285: '፨', 286: '፩', 287: '፪', 288: '፫', 289: '፬', 290: '፭', 291: '፮', 292: '፯', 293: '፰', 294: '፱', 295: '፲', 296: '፳', 297: '፴', 298: '፵', 299: '፶', 300: '፷', 301: '፸', 302: '፹', 303: '፺', 304: '፻', 305: '፼', 306: ' '}

rev_dict = {v: k for k, v in dicts.items()}
print(rev_dict)

import os
from PIL import Image
import numpy as np
import cv2
num_class=307
max_len=46
im_row=48
im_col=368
def load_dataset():
      image_data = []
      text_data = []

      for file_name in os.listdir(tint_path):
          if file_name.endswith('.bin.png'):
              image_path = os.path.join(tint_path, file_name)
              text_path = os.path.join(tint_path, file_name.replace('.bin.png', '.gt.txt'))

              image = Image.open(image_path)
              image_array = np.array(image)
              image_data.append(image_array)

              with open(text_path, 'r') as text_file:
                  text = text_file.read().strip()
                  text_array = [rev_dict[char] for char in text]
                  if len(text_array) < max_len:
                      padded_text_array = text_array + [0] * (max_len - len(text_array))
                  else:
                      padded_text_array = text_array[:max_len]

                  text_data.append(padded_text_array)

      # textto array
      text_data = np.array(text_data)
      return image_data, text_data

def resize():
    data_loaded=load_dataset()
    x_train_synth=data_loaded[0]
    y_train_synth = data_loaded[1]

    resized_x_synth = np.zeros((len(x_train_synth), im_row, im_col), dtype=np.uint8)

    # loop over the input images
    for i, image in enumerate(x_train_synth):
        # resize the image to 48 by 368 using padding
        current_height, current_width = image.shape[:2]
        aspect_ratio_current = current_width / current_height
        aspect_ratio_target = im_col / im_row
        if aspect_ratio_current != aspect_ratio_target:
            if aspect_ratio_current > aspect_ratio_target:
                new_height = int(current_width / aspect_ratio_target)
                top_padding = (new_height - current_height) // 2
                bottom_padding = new_height - current_height - top_padding
                padded_image = cv2.copyMakeBorder(image, top_padding, bottom_padding, 0, 0, cv2.BORDER_CONSTANT, value=255)
            else:
                new_width = int(current_height * aspect_ratio_target)
                left_padding = (new_width - current_width) // 2
                right_padding = new_width - current_width - left_padding
                padded_image = cv2.copyMakeBorder(image, 0, 0, 0, right_padding+left_padding, cv2.BORDER_CONSTANT, value=255)
        else:
            padded_image = image
        resized_image = cv2.resize(padded_image, (im_col, im_row))

        resized_x_synth[i] = resized_image

    return resized_x_synth, y_train_synth

from sklearn.model_selection import train_test_split
def preprocess_train_val_test_data():
    '''
    input: a 2D shape text-line image (h,w)
    output:  returns 3D shape image format (h,w,1)

    Plus this function randomly splits the training and validation set
    This function also computes list of length for both training and validation images and GT
      '''
    #the function resize is excuted here
    x_tr=resize()
    x_train_synth_resize=x_tr[0]
    y_train_synth = x_tr[1]


    x_train, x_val, y_train, y_val = train_test_split(x_train_synth_resize, y_train_synth, test_size=0.1)

    # reshape the size of the image from 3D to 4D so as to make the input size is similar with it.
    x_train_r = x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)  # [samplesize,32,128,1]
    x_val_r = x_val.reshape(x_val.shape[0], x_val.shape[1], x_val.shape[2], 1)
    y_train = y_train
    y_val = y_val

    nb_train = len(x_train_r)
    nb_val = len(x_val_r)


    x_train_len = np.array([len(x_train_r[i]) + 43 for i in range(nb_train)])
    # the + 43 here is just to make  balanceed size ((2*46-1=91) then 48+43=91)of the image equal to the input of LSTMlayer
    x_val_len = np.array([len(x_val_r[i]) + 43 for i in range(nb_val)])

    y_train_len = np.array([len(y_train[i]) for i in range(nb_train)])
    y_val_len = np.array([len(y_val[i]) for i in range(nb_val)])


    return x_train_r, y_train, x_train_len, y_train_len, x_val, y_val, x_val_len, y_val_len
'''
all set of text images and GT
'''
train=preprocess_train_val_test_data()
x_train=train[0]
y_train=train[1]
x_train_length=train[2]
y_train_length=train[3]

x_val=train[4]
y_val=train[5]
x_val_length=train[6]
y_val_length=train[7]

print("data_loading is compeletd")
print("===============================")
print(str(len(x_train))+ " train synth_image and "+ str(len(y_train))+" labels")
print(str(len(x_val))+ "valid synth_image and "+ str(len(y_val))+ "labels")
