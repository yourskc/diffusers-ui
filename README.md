# diffusers-ui
gui for stable diffusion from diffusers library

## install

just install dependancies with   
```pip install -r requirements.txt```

then run 
```python3 app.py```

models.yaml can contain path to locally downloaded model or just a model id from huggingface

The download model will be located at :
```~/.cache/huggingface/hub/{model name}```

```
models:
  - name: stabilityai/stable-diffusion-2-1
    path: /home/imgen/models/stable-diffusion-2-1  # local path - model won't be downloaded to cache
  - name: runwayml/stable-diffusion-v1-5
```

![image](https://github.com/noskill/diffusers-ui/assets/733626/59a52234-951a-4f30-8a67-2724ccfbf6f4)

