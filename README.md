
# HHD-Ethiopic 

A text-line level historical handwritten Ethiopic OCR Dataset

## Overview
This repository contains a dataset called HHD-Ethiopic, and baselines models and human-level performance for benchmarking Historical Handwritten Ethiopic text-image recognition. HHD-Ethiopic is a text-line level historical handwritten Ethiopic OCR Dataset specifically designed for historical handwritten Ethiopic text-image recognition tasks. 

## Dataset Details
The HHD-Ethiopic dataset consists of ~80k text-line images extracted from $18^{th}$ to $20^{th}$ centuries of historical handwritten Ethiopic manuscripts. Each text-line image is accompanied by its ground-truth text transcription. The dataset can be directly downloaded from Hugging Face [HHD-Ethiopic Dataset](https://huggingface.co/datasets/OCR-Ethiopic/HHD-Ethiopic) and/or Zenodo [HHD-Ethiopic Dataset](https://zenodo.org/record/7978722).  Additional synthetically generated Ethiopic text-line images and their corresponding ground truth texts are available from [this link](https://drive.google.com/file/d/1fAPrAp4Hu8zEqs5XLV5dMtkXjyNGfMzg/view?usp=drive_link). 

Sample text-line images and their corresponding ground-truth text are shown below. For a more thorough tutorial about the dataset see [formats of the dataset](https://github.com/ethopic/hhd-ethiopic-I/tree/main/Dataset)

| No. | Text-line Image | Ground-Truth Text |
|--|-------|------------------|
| [Image 1] |![download](https://github.com/ethopic/hhd-ethiopic-I/assets/129184730/83a524c8-436d-4349-8766-183139de8a51)| ወጽራኅየኒ፡ቦአ፡ቅድሜሁ፡ውስተ፡ዕዘኒሁ  |
| [Image 2] |![download](https://github.com/ethopic/hhd-ethiopic-I/assets/129184730/d3428f0a-6c49-4141-b8f5-efddfc206c32)| ፍራስ፡እሳት፡ወጽሩዓን |
| [Image 3] |![download](https://github.com/ethopic/hhd-ethiopic-I/assets/129184730/7f026c0f-ac93-49e9-95df-fac1e041f468)| ወአንሰ፡በብዝኃ፡አሀውዕ፡ቢተኩ |
| [Image 4] | ![download](https://github.com/ethopic/hhd-ethiopic-I/assets/129184730/d9f9a8bb-1e57-4398-aaa9-921b39271da8)| ወአድኅነከ፡ይትፌሥሑ።  |

## Getting Started
In the current implementation, the NumPy format of the HHD-Ethiopic dataset is used for training and testing the baseline models. Download the dataset.

After downloading HHD-Ethiopic, install the requirements, to demonstrate we just used the [Train data](https://huggingface.co/datasets/OCR-Ethiopic/HHD-Ethiopic/blob/main/train/train_numpy.zip) and [Test data ](https://huggingface.co/datasets/OCR-Ethiopic/HHD-Ethiopic/blob/main/test/test_rand/test_rand_numpy.zip) stored in numpy format.  To train and test all baseline models, please use [all source codes](https://github.com/ethopic/hhd-ethiopic-I/tree/main/src/all_code) link.
 ```markdown
pip install -r requirements.txt
  ```
  
To Train the model from scratch
```markdown
$ python3 train_model_plain_CTC.py
```
Alternatively, you can also run  the training code demonstration in Google Colab directly 
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/ethopic/hhd-ethiopic-I/blob/main/train_HPopt_Attn_CTC.ipynb)

To Prediction/test
```markdown
$ python3 test_model_plain_CTC.py
``` 
Alternatively, you can also run the testing code demonstration in Google Colab directly [![68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667](https://github.com/ethopic/hhd-ethiopic-I/assets/129184730/e0073889-4fdd-4a55-868e-c8ad58569b85)](https://github.com/ethopic/hhd-ethiopic-I/main/Test_HPopt-Attn-CTC.ipynb)

***Please note that the two Colab code provided here are **the HPopt-Attn-CTC **implementation** as a** sample demo.**

### Sample testing results
Sample results and Character Error Rate (CER) per line are shown below:
| <sub>Image</sub>| <sub>Ground-truth</sub> | <sub> Prediction </sub>| <sub> Edit Distance</sub> | <sub>CER/Line (100%) </sub>|
|-------|--------------|------------|---------------|----------|
|<sub> ![download](https://github.com/ethopic/hhd-ethiopic-I/assets/129184730/78208ad8-385f-4e3a-9c10-939f95f7fca2) </sub>| <sub> ሰፉሐከ፡የማነከ፡ወውሕጠቶሙ፡ምድር። </sub>|  <sub> ሰፉሕከ፡የማነከ፡ወውሕጠቶሙ፡ምድ። </sub>| 2 | 9 |
| ![download](https://github.com/ethopic/hhd-ethiopic-I/assets/129184730/d93a0dad-86c9-484e-ba6f-e932553674e9)| <sub> ምድር፡ይኔጽር፡ዘሀሎ፡በየብስ፡</sub>   |  <sub> ምድር፡ይኔጽር፡ዘሀሎ፡በየብስ፡ </sub> | 1 | 5|
| ![download](https://github.com/ethopic/hhd-ethiopic-I/assets/129184730/52afdf8b-60a1-4fa8-8d83-9d2e45f9838e)|<sub> ለብሔረ፡ኢትዮጵያ </sub> |  <sub> አብሒረ፡ኢትየጵያ  </sub> | 4| 40|
| ![download](https://github.com/ethopic/hhd-ethiopic-I/assets/129184730/bc05836a-7305-41eb-a6e5-6405f3d12de0)| <sub>ዓገሠ።በዝሕማም፡መሥጋ፡</sub> |  <sub>  ዓገሠ።በዝሕማም፡በሥጋ፡ </sub>| 2| 20|


            
### Feedbacks
We welcome feedbacks from the research community to further enhance the HHD-Ethiopic dataset. If you have any suggestions, please feel free to send them via email: ethiopic.dataset@gmail.com




### License
![license](https://github.com/ethopic/hhd-ethiopic-I/assets/129184730/b25950fb-7fe5-4401-83f2-51748e1bce88)
This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.


