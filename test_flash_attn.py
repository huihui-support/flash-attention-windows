try:
    import torch
    import flash_attn
    from flash_attn import flash_attn_func
    
    # Verify version
    print(f"Flash Attention version: {flash_attn.__version__}")
    
    if torch.cuda.is_available():
        q = torch.randn(2, 8, 32, 64, device='cuda', dtype=torch.float16)
        k = torch.randn(2, 8, 32, 64, device='cuda', dtype=torch.float16)
        v = torch.randn(2, 8, 32, 64, device='cuda', dtype=torch.float16)
        output = flash_attn_func(q, k, v)
        print("Flash Attention test successful!")
    else:
        print("CUDA device not available!")

except ImportError as e:
    print(f"Import Error: {e}")
except RuntimeError as e:
    print(f"Runtime Error: {e}")