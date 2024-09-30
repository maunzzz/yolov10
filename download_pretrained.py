import subprocess

from config import model_folder

save_folder = model_folder()
save_folder.mkdir(exist_ok=True)

for model_type in ('n', 's', 'm', 'b', 'l', 'x'):
    subprocess.run(['wget', '-O', save_folder / f'yolov10{model_type}.pt',
                    f'https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{model_type}.pt'])
