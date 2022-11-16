import cv2
import os
import time
from datetime import datetime


date = datetime.now().strftime("%Y%m%d_%H%M%S")
if not os.path.exists(date):
    os.mkdir(date)   # 画像保存用のフォルダ作製

# とりあえずwaiting_time秒待ってから撮影をスタートさせる
capture_interval = 0.5 # 画像取得間隔（秒）
waiting_time = 0
print('Recording will be started in {0} seconds'.format(waiting_time))
time.sleep(waiting_time)
print('Start')

### 画像の撮影
def capture():
    cap = cv2.VideoCapture(0) # 任意のカメラ番号に変更する。1台だけならカメラ番号は0。
    while True: # capture_interval秒ごとに画像の読み込みおよび保存を行う。
        ret, frame = cap.read() # カメラからキャプチャされた画像をframeとして読み込む
        cv2.imshow("camera", frame) # frameを画面に表示。なぜかこいつを残しておかないとenterで操作を止められない。
        k = cv2.waitKey(1)&0xff # キー入力を待つ。引数は入力待ち時間。
        # カレントディレクトリ内にある「img」フォルダに「(date).jpg」というファイル名でファイルを保存
        date_time = datetime.now().strftime("%Y%m%d%H%M%S")
        path = "./{0}/".format(date) + date_time + ".jpg"
        cv2.imwrite(path, frame) # 画像をフォルダへ保存

        # エンターキーを押したら撮影終了
        if k == 13:
            break 
        time.sleep(capture_interval)
    cap.release()
    
capture()