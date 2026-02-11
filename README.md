# image_generator
AI Image Generator (Hugging Face + Gradio)

## 🚀 Features

* Text-to-Image generation
* Powered by Stable Diffusion
* Clean Gradio web interface
* Works on Google Colab
* Easy deployment on Hugging Face Spaces
* Supports Hugging Face API Token
* GPU/CPU auto-detection

---

## 📁 Project Structure

```
AI-Image-Generator/
│
├── app.py               # Main application
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

---

## 🛠 Requirements

* Python 3.8+
* Internet connection
* (Optional) GPU for faster generation
* Hugging Face account

## 📥 Installation (Local / Colab)

### ▶️ In Google Colab / Jupyter

Run this in a cell:

```python
!pip install gradio==4.44.0 diffusers==0.27.2 transformers==4.38.2 torch==2.2.1 accelerate==0.27.2 safetensors==0.4.2 pillow==10.2.0 huggingface-hub==0.21.4
```

---

### ▶️ In Terminal / CMD

```bash
pip install -r requirements.txt
```

---

## 🔐 Set Hugging Face Token

### ▶️ In Colab

```python
import os
os.environ["HF_TOKEN"] = "your_huggingface_token_here"
```

---

### ▶️ In Terminal (Linux / Mac)

```bash
export HF_TOKEN=your_token_here
```

---

### ▶️ In Windows CMD

```cmd
set HF_TOKEN=your_token_here
```

---

### ▶️ On Hugging Face Spaces

1. Open your Space
2. Go to **Settings → Secrets**
3. Add:

```
Name: HF_TOKEN
Value: your_token_here
```

---

## ▶️ Run the Application

After installing dependencies and setting token:

```bash
python app.py
```

Then open in browser:

```
http://localhost:7860
```

---

## ☁️ Deploy on Hugging Face Spaces

### Step 1: Create Space

* Go to: [https://huggingface.co/spaces](https://huggingface.co/spaces)
* Click **Create Space**
* Select:

  * SDK: Gradio
  * Language: Python

---

### Step 2: Upload Files

Upload:

```
app.py
requirements.txt
README.md
```

---

### Step 3: Add Token

Add HF_TOKEN in Secrets (see above).

---

### Step 4: Deploy

Hugging Face will automatically build and deploy your app.

---

## 🎯 How to Use

1. Enter your prompt
   Example:

   ```
   A futuristic city at sunset, ultra realistic
   ```

2. (Optional) Add negative prompt

   ```
   blurry, low quality
   ```

3. Adjust settings:

   * Steps
   * Guidance Scale
   * Width / Height
   * Seed

4. Click **Generate Image 🚀**

5. Wait and download your image

---

## ⚙️ Parameters Explanation

| Parameter       | Description           |
| --------------- | --------------------- |
| Prompt          | Main text description |
| Negative Prompt | What to avoid         |
| Steps           | Quality vs Speed      |
| Guidance        | Prompt strength       |
| Width/Height    | Image size            |
| Seed            | Randomness control    |

---

## 🧠 Model Used

```
runwayml/stable-diffusion-v1-5
```

You can change this in `app.py`:

```python
MODEL_ID = "your_model_here"
```

## 📜 License

This project is open-source and free to use for educational purposes.

---

## 🙌 Credits

* Hugging Face
* Diffusers
* Gradio
* Stable Diffusion Team



Happy Coding! 🚀

