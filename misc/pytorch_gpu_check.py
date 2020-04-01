import torch

print('>> imported torch :', torch.__version__)

print(torch.cuda.is_available())

if torch.cuda.is_available():
    print(torch.cuda.current_device())

    print(torch.cuda.device(0))

    print(torch.cuda.device_count())

    print(torch.cuda.get_device_name(0))

import torchvision

print('\n>> imported torchvision')
print(torchvision.__version__)