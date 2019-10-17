# Dataset-acess-for-PLOS-ONE
Data set for the paper submitted to PLOS One, which is entitled "Real-time Gastric Polyp Detection using Convolutional Neural Networks".

https://github.com/jiquan/Dataset-acess-for-PLOS-ONE


# This is kojix2 fork for creating yolov3 model

## Requirements

Install tensorflow and keras. Use keras2onnx to convert the model to onnx format.

* [keras-yolo3](https://github.com/qqwweee/keras-yolo3)
* [keras2onnx](https://github.com/onnx/keras-onnx)

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

```sh
cd keras-yolo3
```

1. Create classes text file. `model_data/polyp_classes.txt`

```sh
mv ../Dataset-acess-for-PLOS-ONE/polyp_classes.txt model_data/polyp_classes.txt
```

2. move `train_polyp.txt` to kraas-yolo3 directory.

```sh
mv ../Dataset-acess-for-PLOS-ONE/train_polyp.txt .
```

3. Copy `train.py` to `train_polyp.py`

```sh
cp train.py train_polyp.py
```

4. Edit `train_polyp.py` as follows.

Changing the batch size is optional. `Resource exhausted` errors can be avoided by reducing the batch size.


```diff
# line 17
-     annotation_path = 'train.txt'
+     annotation_path = 'train_polyp.txt'

# line 19
-     classes_path = 'model_data/voc_classes.txt'
+     classes_path = 'model_data/polyp_classes.txt'

# line 76
-     batch_size = 32
+     batch_size = 8
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
