# VONet

## Env Setup

### Python

* Miniconda 3.7 : 

`curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh` 

`bash Miniconda3-latest-Linux-x86_64.sh` 

* venv with py 3.7 (https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)

`conda create -n pth37 python=3.7 pip` 

### Pytorch

https://pytorch.org/get-started/previous-versions/

**CUDA 9.0**

`conda install pytorch==1.1.0 torchvision==0.3.0 cudatoolkit=9.0 -c pytorch`

### Change Pillow version

`conda install Pillow==6.0.0`

### skylynx

`pip install skylynx`