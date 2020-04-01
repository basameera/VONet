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

#### CUDA 9.2
`pip install torch==1.3.0 torchvision==0.4.1 -f https://download.pytorch.org/whl/torch_stable.html`

## Change Pillow version

`pip install Pillow==6.0.0`