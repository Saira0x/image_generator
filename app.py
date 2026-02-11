import os
import torch
import gradio as gr
from diffusers import StableDiffusionPipeline

# -------------------------------------------------
# Load Hugging Face Token (from environment)
# -------------------------------------------------
HF_TOKEN = os.getenv("HF_TOKEN") or os.getenv("HUGGINGFACEHUB_API_TOKEN")

if HF_TOKEN is None:
    print("Warning: No Hugging Face token found. Private models may not work.")

# -------------------------------------------------
# Model Configuration
# -------------------------------------------------
MODEL_ID = "runwayml/stable-diffusion-v1-5"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
DTYPE = torch.float16 if DEVICE == "cuda" else torch.float32

# -------------------------------------------------
# Load Model
# -------------------------------------------------
pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=DTYPE,
    use_auth_token=HF_TOKEN
)

pipe = pipe.to(DEVICE)

# Enable memory optimization (for Spaces)
pipe.enable_attention_slicing()

# -------------------------------------------------
# Image Generation Function
# -------------------------------------------------
def generate_image(
    prompt,
    negative_prompt,
    steps,
    guidance_scale,
    width,
    height,
    seed
):
    if seed == -1:
        generator = None
    else:
        generator = torch.Generator(device=DEVICE).manual_seed(seed)

    result = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=steps,
        guidance_scale=guidance_scale,
        width=width,
        height=height,
        generator=generator
    )

    image = result.images[0]
    return image


# -------------------------------------------------
# Gradio Interface
# -------------------------------------------------
with gr.Blocks(title="AI Image Generator") as demo:

    gr.Markdown("""
    # 🎨 AI Image Generator
    Generate images using Stable Diffusion on Hugging Face Spaces
    """)

    with gr.Row():
        with gr.Column():
            prompt = gr.Textbox(
                label="Prompt",
                placeholder="A futuristic city at sunset, ultra realistic"
            )

            negative_prompt = gr.Textbox(
                label="Negative Prompt",
                placeholder="blurry, low quality, distorted"
            )

            steps = gr.Slider(
                10, 50, value=25, step=1, label="Steps"
            )

            guidance = gr.Slider(
                1, 15, value=7.5, step=0.1, label="Guidance Scale"
            )

            width = gr.Dropdown(
                [256, 384, 512, 640, 768], value=512, label="Width"
            )

            height = gr.Dropdown(
                [256, 384, 512, 640, 768], value=512, label="Height"
            )

            seed = gr.Number(
                value=-1,
                label="Seed (-1 = Random)",
                precision=0
            )

            generate_btn = gr.Button("Generate Image 🚀")

        with gr.Column():
            output_image = gr.Image(label="Generated Image", type="pil")


    generate_btn.click(
        fn=generate_image,
        inputs=[
            prompt,
            negative_prompt,
            steps,
            guidance,
            width,
            height,
            seed
        ],
        outputs=output_image
    )


# -------------------------------------------------
# Launch App
# -------------------------------------------------
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)

