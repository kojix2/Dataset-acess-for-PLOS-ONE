#! /usr/bin/env python

import cv2
import numpy as np
import onnxruntime as rt

camera = cv2.VideoCapture(0)

session = rt.InferenceSession("yolov3.onnx")

def get_polyp(frame):
    image_size = np.array([256, 256], dtype=np.float32).reshape(1, 2)
    image_data = np.array(frame, dtype='float32')
    image_data /= 255.0
    image_data = np.transpose(image_data, [2, 0, 1])
    image_data = np.expand_dims(image_data, 0)

    outputs_index = session.run(None, {'input_1': image_data, 'image_shape': image_size})
    output_boxes = outputs_index[0]
    output_indices = outputs_index[2]

    return [output_boxes[0][_idx[2]] for _idx in output_indices[0]]
    


while True:
    ret, frame = camera.read()
    width = 256
    height = 256
    frame = cv2.resize(frame, (width, height))
    boxes = get_polyp(frame)
    for box in boxes:
        frame = cv2.rectangle(frame, (box[1], box[0]), (box[3], box[2]), (0, 255, 0), 3)
    frame = cv2.resize(frame, (700, 700))
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
