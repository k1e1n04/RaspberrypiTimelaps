import sys
import cv2
import os
import time
from datetime import datetime
sys.path.append("%s/../" % (os.path.abspath(os.path.dirname(__file__))))
import settings


IMAGE_DIR = settings.IMAGE_DIR # 画像を保存するディレクトリ
CAPTURE_INTERVAL = settings.CAPTURE_INTERVAL # 画像取得間隔（秒）
WAITING_TIME = settings.WAITING_TIME # 撮影開始までの待機時間
CAMERA_NUM = settings.CAMERA_NUM # 使用するカメラの番号
END_NUM_OF_SHOTS = settings.END_NUM_OF_SHOTS # 撮影回数

INSERT_KEY_WAITING_TIME = 1000 # キー入力を待つ時間
INITIAL_KEY = 0 # 変数keyの初期値

print(IMAGE_DIR)
print('Recording will be started in {0} seconds'.format(WAITING_TIME))
time.sleep(WAITING_TIME)
print('Start!')

### 画像の撮影
def capture():
    cap = cv2.VideoCapture(CAMERA_NUM) 
    # CAPTURE_INTERVAL秒ごとに画像の読み込みおよび保存を行う。
    ret, frame = cap.read() # カメラからキャプチャされた画像をframeとして読み込む
    cv2.imshow("camera", frame) # frameを画面に表示
    # 「IMAGE_DIR」フォルダに「(datetime).jpg」というファイル名でファイルを保存
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "{}/{}.jpg".format(IMAGE_DIR,date_time)
    cv2.imwrite(path, frame) # 画像をフォルダへ保存
    cap.release()
    

if __name__ == '__main__':
    number_of_shot = 0 #撮影回数
    while number_of_shot != END_NUM_OF_SHOTS:
        capture()
        number_of_shot += 1
        time.sleep(CAPTURE_INTERVAL)