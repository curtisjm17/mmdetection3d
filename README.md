My implementation of an inference and visualization pipeline for 3D Object Detection can be found in 3D_Object_Detection.ipynb. In order to run this Jupyter Notebook, you must first install the required supporting libraries. These library requirements can be found here: https://mmdetection3d.readthedocs.io/en/latest/getting_started.html. Once these requirement are satsified, clone the this repo and install it:

git clone https://github.com/curtisjm17/mmdetection3d.git

cd mmdetection3d

pip install -v -e . 

Next the SECOND model must be downloaded. The model can be downloaded directly from here: https://download.openmmlab.com/mmdetection3d/v1.0.0_models/second/hv_second_secfpn_6x8_80e_kitti-3d-3class/hv_second_secfpn_6x8_80e_kitti-3d-3class_20210831_022017-ae782e87.pth. 

This file should be placed here ./mmdetection3d/checkpoints/

From here it is as simply as running through the Jupyter Notebook.

