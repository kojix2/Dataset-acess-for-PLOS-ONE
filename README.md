# Dataset-acess-for-PLOS-ONE

## Original Datasets
Data set for the paper submitted to PLOS One, which is entitled "Real-time Gastric Polyp Detection using Convolutional Neural Networks".

Citation: Zhang X, Chen F, Yu T, An J, Huang Z, Liu J, et al. (2019) Real-time gastric polyp detection using convolutional neural networks. PLoS ONE 14(3): e0214133. https://doi.org/10.1371/journal.pone.0214133

https://github.com/jiquan/Dataset-acess-for-PLOS-ONE


## This repository is kojix2's fork for creating yolov3 model

## Requirements

Install tensorflow and keras. Use keras2onnx to convert the model to onnx format.

* [keras-yolo3](https://github.com/qqwweee/keras-yolo3)
* [keras2onnx](https://github.com/onnx/keras-onnx)
* [Netron](https://github.com/lutzroeder/netron) (optional)

Download repos.

```sh
git clone https://github.com/kojix2/Dataset-acess-for-PLOS-ONE
git clone https://github.com/qqwweee/keras-yolo3
pip install git+https://github.com/onnx/keras-onnx
```

## 1. Data Preparation

1. Convert image size with ImageMagick. 416 x 416. 
The resized images have been already added to the repository. So you do not need to run the script below.

```bash 
# create TrainImages directory
sh resize_image.sh
```

2. Create Annotation file for Yolov3

```ruby
ruby convert_annotation.rb > train_polyp.txt
```

## 2. Modify keras-yolo3 scripts

1. Enter keras-yolo3 directory.  

```sh
cd keras-yolo3
```

2. Create classes text file. `model_data/polyp_classes.txt`

```sh
mv ../Dataset-acess-for-PLOS-ONE/polyp_classes.txt model_data/polyp_classes.txt
```

3. move `train_polyp.txt` to kraas-yolo3 directory.

```sh
mv ../Dataset-acess-for-PLOS-ONE/train_polyp.txt .
```

4. Copy `train.py` to `train_polyp.py`

```sh
cp train.py train_polyp.py
```

5. Edit `train_polyp.py` as follows.

Changing the batch size is optional. `Resource exhausted` errors can be avoided by reducing the batch size.
There are two places where `batch_size` is defined, but the latter is important to avoid errors.


```diff
# line 17
-     annotation_path = 'train.txt'
+     annotation_path = 'train_polyp.txt'

# line 19
-     classes_path = 'model_data/voc_classes.txt'
+     classes_path = 'model_data/polyp_classes.txt'

# line 76 (optional)
-     batch_size = 32  # note that more GPU memory is required after unfreezing the body
+     batch_size = 8   # note that more GPU memory is required after unfreezing the body
```

5. Edit `yolo.py`

```diff
# line 23
-        "model_path": 'model_data/yolo.h5',
+        "model_path": 'logs/000/trained_weights_final.h5',
         "anchors_path": 'model_data/yolo_anchors.txt',
-        "classes_path": 'model_data/coco_classes.txt',
+        "classes_path": 'model_data/polyp_classes.txt',
```

## 3. Train model

```sh
python train_polyp.py
```

It takes about an hour with GTX 1070.

## 4. Verify that the model is generated correctly

```sh
python yolo_video.py --image
# Input image filename: ../Dataset-acess-for-PLOS-ONE/TrainImages/100150_20150104001030003.jpg
```

![gastric polyp detection](https://raw.githubusercontent.com/kojix2/Dataset-acess-for-PLOS-ONE/master/screenshots/screenshot1.png)

Did it work well? If it does not work, check for error messages during train.

## 5. Convert the model to onnx format

1. Copy keras-onnx yolov3.py to current directory.

```sh
cp ../keras-onnx/applications/yolov3/yolov3.py onnx_yolov3.py
```

check [README.md ](https://github.com/onnx/keras-onnx/tree/master/applications/yolov3) for usage. 

2. Edit `onnx_yolov3.py` as follows

```diff
# line 134
-        self.model_path = 'model_data/yolo.h5'  # model path or trained weights path
-        self.anchors_path = 'model_data/yolo_anchors.txt'
-        self.classes_path = 'model_data/coco_classes.txt'
+        self.model_path = 'logs/000/trained_weights_final.h5'  # model path or trained weights path
+        self.anchors_path = 'model_data/yolo_anchors.txt'
+        self.classes_path = 'model_data/polyp_classes.txt'
```

3. Convert the model to onnx format.

This command requires an image path as an argument

```sh
python yolov3.py ../Dataset-acess-for-PLOS-ONE/TrainImages/100150_20150104001030003.jpg
```

The onnx model is stored in the `model_data` directory

model_data/yolov3.onnx

4. View the yolov3 network with netron. (optional)

![Netron](https://raw.githubusercontent.com/kojix2/Dataset-acess-for-PLOS-ONE/master/screenshots/screenshot3.png)


## License
There is no clear copyright notice for images. However, from the following description, it is assumed that a model may be created using this dataset of endoscopic images. 
Please follow the laws of your area. 

> Copyright: © 2019 Zhang et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
> Data Availability: All the trainval images are available on https://github.com/jiquan/Dataset-acess-for-PLOS-ONE. And this information will only be available after paper acceptance.