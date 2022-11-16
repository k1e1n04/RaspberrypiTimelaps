import cv2
import glob
import os
import shutil
import time
from datetime import datetime

date = datetime.now().strftime("%Y%m%d_%H%M%S")

def timelaps():
    images = sorted(glob.glob('{0}/*.jpg'.format(date))) # 撮影した画像の読み込み。
    print("画像の総枚数{0}".format(len(images)))

    if len(images) < 30: #FPS設定
        frame_rate = 2  
    else:
        frame_rate = len(images)/30

    width = 640
    height = 480
    fourcc = cv2.VideoWriter_fourcc('m','p','4','v') # 動画のコーデックをmp指定。動画の拡張子を決める、    
    video = cv2.VideoWriter('{0}.mp4'.format(date), fourcc, frame_rate, (width, height)) # 作成する動画の情報を指定（ファイル名、拡張子、FPS、動画サイズ）。

    print("動画変換中...")

    for i in range(len(images)):
        # 画像を読み込む
        img = cv2.imread(images[i])
        # 画像のサイズを合わせる。
        img = cv2.resize(img,(width,height))
        video.write(img) 

    video.release()
    print("動画変換完了")


timelaps()