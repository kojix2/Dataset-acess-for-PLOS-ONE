# Dataset-acess-for-PLOS-ONE
Data set for the paper submitted to PLOS One, which is entitled "Real-time Gastric Polyp Detection using Convolutional Neural Networks".

https://github.com/jiquan/Dataset-acess-for-PLOS-ONE


# This is kojix2 fork for creating yolov3 model

## Requirements

Install tensorflow and keras. Use keras2onnx to convert the model to onnx format.

* [keras-yolo3](https://github.com/qqwweee/keras-yolo3)
* [keras2onnx](https://github.com/onnx/keras-onnx)

## Data Preparation

1. Convert image size with ImageMagick. 416 x 416. 
The resized images have been already added to the repository. So you do not need to run the script below.

```bash 
# create TrainImages directory
sh resize_image.sh
```

2. Create Annotation file for Yolov3

```ruby
ruby convert_annotation.rb > train.txt
```


