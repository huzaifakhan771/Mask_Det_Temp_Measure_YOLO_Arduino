Real time mask Detection and human temperature measurement by using deep learning object detection with YOLOv5 and temperature measurement with the contact-less MLX90614-DCI sensor. Arduino is used for the I2C communication between the machine and the temperature sensor.


-- Install dependencies with 'pip3 install -r requirements.txt'

-- Run the code with 'python detect.py --weights trained_model/mask_detection.pt --img 416 --conf 0.6 --source 0'
