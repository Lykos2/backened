from diffusers import StableDiffusionXLPipeline
import torch
import time 


def get_pipe():
    pipe = StableDiffusionXLPipeline.from_pretrained("segmind/SSD-1B", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
    pipe.to("cuda")
    return pipe
# if using torch < 2.0
# pipe.enable_xformers_memory_efficient_attention()
prompt = "An astronaut riding a green horse" # Your prompt here
neg_prompt = "ugly, blurry, poor quality" # Negative prompt here



