from pathlib import Path
import os

#===共通設定===
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = os.path.join(BASE_DIR, 'images') # 画像の保存ディレクトリの設定

#===撮影設定===
CAPTURE_INTERVAL = 1 # 撮影のインターバル
WAITING_TIME = 1 # 実行から撮影までの時間
END_NUM_OF_SHOTS = 100 # 撮影回数
CAMERA_NUM = 0 # 撮影するカメラの番号(通常は0)

#===動画設定===
FPS = 24 # フレームレートの設定
WIDTH = 640
HEIGHT = 480
VIDEO_DIR = os.path.join(BASE_DIR, 'videos') # 画像の保存ディレクトリの設定