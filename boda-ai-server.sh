nvidia-smi
apt-get update && apt-get -y install ffmpeg libgl1-mesa-glx libsm6 libxext6

(
    cd /home/boda-ai
    pip install -r requirements.txt
    python main_cam.py
)
