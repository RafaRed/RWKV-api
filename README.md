# RWKV-api

Simple Flask API for RWKV, 90% of the code is the base chat from https://github.com/BlinkDL/ChatRWKV.

## Endpoints
```
localhost:5000/api?prompt=text
localhost:5000/instruct?prompt=text
localhost:5000/continue
localhost:5000/reset
```

## Install


- install miniconda https://docs.conda.io/en/latest/miniconda.html
- Install VS2022 build tools (https://aka.ms/vs/17/release/vs_BuildTools.exe select Desktop C++). 
- Reinstall CUDA 11.7 (install VC++ extensions).
- on cmd `pip install rwkv tokenizers>=0.13.2 prompt_toolkit`
- on cmd `pip install torch==1.13.1+cu117 torchvision==0.14.1+cu117 torchaudio==0.13.1 --extra-index-url https://download.pytorch.org/whl/cu117`
- Done.

## Setup
- Create a folder "models" and rename your RWKV model to model.pth
- in the file `base_chat` set your strategy, etc..
- if you are not using CUDA, you can set `RWKV_CUDA_ON` to 0 ( not recommended )

## Start
Run `python api.py` in "x64 native tools command prompt". 

## Extra - Get puplic address without portfoward
- I recommend downloading jprq https://github.com/azimjohn/jprq/releases/tag/2.0
- Auth, then exec with jprq-windows-amd64.exe http 5000
