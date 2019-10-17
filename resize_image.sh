mkdir -p TrainImages
mogrify -resize 416x416! -path TrainImages TrainValImages/*.jpg
