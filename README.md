# RaspberrypiTimelaps
RaspberrypiとWebカメラを用いてタイムラプスを撮影するためのリポジトリです。
RaspiOS以外のOSでも使用できますが、動作保証はしておりません。
MacOSでの動作は確認済みです。

## 機能要件
1. RasberrypiとWebカメラを用いて指定した間隔で画像を撮影できる。
2. 画像の撮影枚数を指定できる。
3. 撮影した画像を指定したフレームレートでmp4の動画に変換できる。

## 環境定義
- python 3.9.12
- opencv-python 4.6.0.66

## 使用方法
1. settings.pyを編集し、画像の撮影・動画変換の設定をしてください。
設定項目を以下に示します。  
【共通設定】
```
BASE_DIR = Path(__file__).resolve().parent
IMAGE_DIR = os.path.join(BASE_DIR, 'images')
```
IMAGE_DIRは画像撮影時の出力ディレクトリ(デフォルトではimages)

【撮影設定】
```
CAPTURE_INTERVAL = 1
WAITING_TIME = 1
END_NUM_OF_SHOTS = 100
CAMERA_NUM = 0
```
CAPTURE_INTERVALは撮影間隔(s)
WAITING_TIMEはcam.pyの実行から撮影開始までの時間(s)
END_NUM_OF_SHOTSは撮影回数
CAMERA_NUMは接続されているカメラの番号(1台のみの場合は0)

【動画設定】
```
FPS = 24
WIDTH = 640
HEIGHT = 480
VIDEO_DIR = os.path.join(BASE_DIR, 'videos') 
```
FPSは動画のフレームレートの設定
WIDTHは動画の幅
HEIGHTは動画の高さ
VIDEO_DIRは動画の出力ディレクトリ(デフォルトではvideos)


2. 画像の撮影
RapberrypiTimelapsディレクトリ内で以下のコマンドを実行してください。
```
python ./photograph/cam.py 
```
設定で指定した枚数の画像を撮影し終わると終了します。


3. 撮影した画像の動画化
RapberrypiTimelapsディレクトリ内で以下のコマンドを実行してください。
```
python ./timelaps/timelaps.py
```
設定で指定した動画の出力ディレクトリにmp4の動画が出力されます。
