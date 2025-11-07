# Fruit Detection

## Training

Ran this command:  
`yolo detect train data=./data/data.yml model=yolo11s.pt epochs=60`

Then the tutorial says to do this after...  
`yolo detect predict model=./runs/detect/train/weights/best.pt source=./data/validation save=True`