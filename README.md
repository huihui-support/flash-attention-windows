# Flash Attention Windows Wheels

Pre-built Windows wheels for [Flash-Attention 2](https://github.com/Dao-AILab/flash-attention) - The state-of-the-art efficient attention implementation for NVIDIA GPUs.

# cp310

### Requirements

- Windows 10/11 (64-bit)
- Python 3.10
- PyTorch 2.0.0+

### Quick Installation
```
pip install flash_attn-2.7.0.post2-cp310-cp310-win_amd64.whl
```

### Quick Build
```
conda create -yn flash_attn310 python=3.10
conda activate flash_attn310
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install packaging wheel ninja einops psutil
pip install flash-attn==2.7.0.post2 --no-build-isolation
```


# cp311

### Requirements

- Windows 10/11 (64-bit)
- Python 3.11
- PyTorch 2.0.0+

### Quick Installation
```
pip install flash_attn-2.7.0.post2-cp311-cp311-win_amd64.whl
```

### Quick Build
```
conda create -yn flash_attn311 python=3.11
conda activate flash_attn311
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install packaging wheel ninja einops psutil
pip install flash-attn==2.7.0.post2 --no-build-isolation
```

# cp312

### Requirements

- Windows 10/11 (64-bit)
- Python 3.12
- PyTorch 2.0.0+

### Quick Installation
```
pip install flash_attn-2.7.0.post2-cp312-cp312-win_amd64.whl
```

### Quick Build
```
conda create -yn flash_attn312 python=3.12
conda activate flash_attn312
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install packaging wheel ninja einops psutil
pip install flash-attn==2.7.0.post2 --no-build-isolation
```


