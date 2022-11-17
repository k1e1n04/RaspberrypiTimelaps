import sys
import cv2
import glob
import os
from datetime import datetime
sys.path.append("%s/../" % (os.path.abspath(os.path.dirname(__file__))))
import settings

IMAGE_DIR = settings.IMAGE_DIR # 画像が保存されるディレクトリ
VIDEO_DIR = settings.VIDEO_DIR
WIDTH = settings.WIDTH
HEIGHT = settings.HEIGHT

FPS = settings.FPS # FPS

FOURCC = cv2.VideoWriter_fourcc('m','p','4','v') # 動画のコーデックを指定

date_time = datetime.now().strftime("%Y%m%d_%H%M%S")

def get_images():
    images = sorted(glob.glob("{}/*.jpg".format(IMAGE_DIR))) # 撮影した画像の読み込み
    print("画像の総枚数{0}".format(len(images)))
    return images

def create_timelaps(images):
    video = cv2.VideoWriter('{}/{}.mp4'.format(VIDEO_DIR,date_time), FOURCC, FPS, (WIDTH, HEIGHT)) # 作成する動画の情報を指定（ファイル名、拡張子、FPS、動画サイズ）
    print("動画変換中...")
    for i in range(len(images)):
        # 画像を読み込む
        img = cv2.imread(images[i])
        # 画像のサイズを合わせる
        img = cv2.resize(img,(WIDTH,HEIGHT))
        video.write(img) 
    video.release()
    print("動画変換完了")


if __name__ == '__main__':
    images = get_images()
    create_timelaps(images)

