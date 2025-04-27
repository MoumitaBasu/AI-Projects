Step-by-Step Instructions to run Whisper App:

✅ 1. Ensure Chocolatey is Installed
If it's not installed yet, run the following in an elevated PowerShell (Run as Administrator):

Set-ExecutionPolicy Bypass -Scope Process -Force; `
[System.Net.ServicePointManager]::SecurityProtocol = `
[System.Net.ServicePointManager]::SecurityProtocol -bor 3072; `
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

✅ 2. Install ffmpeg via Chocolatey
Open a Command Prompt or PowerShell as Administrator and run:
choco install ffmpeg -y

✅ 3. Make Sure ffmpeg is on PATH
After installing, verify it's available by running:
ffmpeg -version

Install PyTorch (Conda version)
🔹 1. Create a New Conda Environment for Your Project
conda create -n myproject python=3.10
Replace myproject with the actual name of your project.

🔹 2. Activate the Conda Environment
conda activate myproject
This activates the isolated environment where you’ll install PyTorch.

🔹 3. Install PyTorch + CUDA for That Environment
Now run the install command inside the activated env:
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
This installs the GPU-enabled version of PyTorch (with CUDA 11.7) into your project-specific environment.

🔹 4. Verify Installation
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"
If torch.cuda.is_available() returns True, CUDA is working!

Install PyTorch (venv version)
Activate your venv
# Windows
.\venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
Install PyTorch with pip

Use the official PyTorch pip selector to match your system.

Example for CPU-only:
pip install torch torchvision torchaudio

Example for GPU (CUDA 11.7):
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117

Verify installation
python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"

In case of Numpy error
st.sidebar.audio(audio_file)RuntimeError: Numpy is not available 
Traceback:
File "D:\Python Projects\AudioToText\venv\Lib\site-packages\streamlit\runtime\scriptrunner\exec_code.py", line 121, in exec_func_with_error_handling
    result = func()
             ^^^^^^

✅1. Reinstall numpy to make sure it's clean and compatible:
pip uninstall numpy -y
pip install numpy==1.24.4

✅ 2. Check PyTorch install
Make sure your installed version of torch is compatible:
pip show torch

If it's missing or messed up, reinstall it:
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
Replace cpu with cu117 if you’re using CUDA 11.7.

✅ 3. Restart Everything

After reinstalling:

Close and reopen your terminal

Re-activate your virtual environment

Restart your Streamlit app