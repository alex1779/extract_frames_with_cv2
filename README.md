# Extract frames using cv2
From: https://google.github.io/extract_frames_with_cv2/

## Installation on Windows using Anaconda
```
conda create -n mediapipeWorks -y && conda activate mediapipeWorks && conda install python=3.9.7 -y
git clone https://github.com/alex1779/mediapipeWorks.git
cd mediapipeWorks
pip install -r requirements.txt
```

## How to run



```
python facemesh_landmarkpoints.py
```
 *** looks like below

![Face Mesh](https://github.com/alex1779/mediapipeWorks/blob/master/images_samples/facemesh_landmarkpoints.jpg)


```
python facemesh_tesselation.py
```
 *** looks like below

![Face Mesh](https://github.com/alex1779/mediapipeWorks/blob/master/images_samples/facemesh_tesselation.jpg)



```
python face_mesh_contours.py
```
 *** looks like below

![Face Mesh](https://github.com/alex1779/mediapipeWorks/blob/master/images_samples/face_mesh_contours.jpg)


```
python face_mesh_irises.py
```
 *** looks like below

![Face Mesh](https://github.com/alex1779/mediapipeWorks/blob/master/images_samples/face_mesh_irises.jpg)



```
python face_mesh.py
```
 *** looks like below

![Face Mesh](https://github.com/alex1779/mediapipeWorks/blob/master/images_samples/face_mesh.jpg)




## License

Many parts taken from the cpp implementation from github.com/google/mediapipe

Copyright 2020 The MediaPipe Authors.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.






