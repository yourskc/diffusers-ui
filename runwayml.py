import torch
from diffusers import DiffusionPipeline

# RTX-4060 test OK
pipe = DiffusionPipeline.from_pretrained("rupeshs/LCM-runwayml-stable-diffusion-v1-5", dtype=torch.bfloat16, device_map="cuda")

prompt = "Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"
image = pipe(prompt).images[0]
image.save("output.png")