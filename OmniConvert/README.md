# OmniConvert: All-in-One Media Converter

**OmniConvert** is an intelligent, all-in-one media conversion tool designed to handle a variety of formats. It allows users to convert between audio, text, documents, images, and videos with ease. Whether you're transcribing audio to text, turning text into speech, or converting between file formats, OmniConvert has you covered.

---

## Features

### Current Features:
- 🎙️ **Audio/Voice to Text**: Transcribe live or recorded audio to text.
- 🗣️ **Text/Document to Audio**: Convert text or documents into spoken voice.

### Coming Soon:
- 📄 **Chat with Document**: Engage in conversations with uploaded documents.
- 🖼️ **Image to Text**: Extract text from images.
- 📹 **Video to Text**: Transcribe video content into text.
- 🎞️ **Text to Video**: Generate video content from text descriptions.

---

## Installation Instructions

Follow these steps to get OmniConvert up and running on your machine.

### 1. Install Chocolatey (if not already installed)
Run the following command in an elevated PowerShell (Run as Administrator):

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force;
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```
2. **Install ffmpeg via Chocolatey**
    - Open Command Prompt or PowerShell as Administrator and run:
    ```bash
    choco install ffmpeg -y
    ```
3. **Verify ffmpeg Installation**
    - Ensure ffmpeg is installed and available on your PATH:
    ```bash
    ffmpeg -version
    ```
## PyTorch Installation

# Option 1: Install PyTorch (Conda Version)

1. **Create a Conda Environment:**

```bash
conda create -n myproject python=3.10
```
Replace myproject with the desired project name.

2. **Activate the Environment:**

```bash
conda activate myproject
```

3. **Install PyTorch with CUDA:**

```bash
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
```

4. **Verify Installation:**

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```
If torch.cuda.is_available() returns True, CUDA is working properly.

# Option 2: Install PyTorch (Virtual Environment Version)

1. **Activate your venv:**

Windows:

```bash
.\venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

2. **Install PyTorch:**

CPU-only version:

```bash
pip install torch torchvision torchaudio
```

GPU (CUDA 11.7) version:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
```

3. **Verify Installation:**

```bash
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
```

## Common Issues & Solutions
# Numpy Runtime Error:
If you encounter the RuntimeError: Numpy is not available, try the following:

1. Reinstall Numpy:

```bash
pip uninstall numpy -y
pip install numpy==1.24.4
```

2. Check PyTorch Install: Ensure your PyTorch version is installed correctly:

```bash
pip show torch
```

If it's missing or corrupted, reinstall it:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
```

# Restart Everything:

- Close and reopen your terminal.

- Reactivate your virtual environment.

- Restart your Streamlit app.

## Running the Application
After completing the setup, you can run the app with the following command:

```bash
streamlit run app.py
```

Open the app in your browser, and choose from various available modes such as:

 - Audio/Voice to Text

 - Text/Document to Audio

 - Coming Soon: Chat with Document, Image to Text, Video to Text, Text to Video

## Technologies Used
- Python
- Streamlit
- PyTorch
- ffmpeg
- Conda / venv

## Contributing
Feel free to fork this repository, submit issues, or create pull requests. All contributions are welcome!

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
