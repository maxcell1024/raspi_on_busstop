import datetime
import numpy as np
from time import sleep
import cv2

# カメラのIDがrgbかtherかをframeの差分を見て判斷
def is_ther(frame) -> bool:
    """frame from thermo capture"""
    vs01 = np.all(frame[:, :, 0] == frame[:, :, 1])
    vs12 = np.all(frame[:, :, 1] == frame[:, :, 2])
    vs20 = np.all(frame[:, :, 2] == frame[:, :, 0])
    return vs01 and vs12 and vs20

# カメラのIDを取得
def get_camera_ids() -> tuple[int, int]:
    rgb_cid, ther_cid = None, None
    for i in range(5):
        print(i)
        tmp_capture = cv2.VideoCapture(i)
        ret, frame = tmp_capture.read()
        if frame is not None:
            if is_ther(frame):
                ther_cid = i
            else:
                rgb_cid = i
        tmp_capture.release()
    assert rgb_cid is not None and ther_cid is not None, 'ERROR: Camera ids is not found'
    return rgb_cid, ther_cid

if __name__ == '__main__':
    # カメラのID決定
    rgb_cid, ther_cid = get_camera_ids()
    print(f'after get ids, rgb_cid: {rgb_cid}, ther_cid: {ther_cid}')
    rgb_camera = cv2.VideoCapture(rgb_cid)
    ther_camera = cv2.VideoCapture(ther_cid)

    # output_dir
    output_dir = "/home/pi/work/mp4/"

    # 動画ファイル保存用の設定
    fps = 10
    #rgb_camera.set(cv2.CAP_PROP_FPS,fps)
    #ther_camera.set(cv2.CAP_PROP_FPS,fps)

    rgb_w = int(rgb_camera.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    ther_w = int(ther_camera.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    rgb_h = int(rgb_camera.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    ther_h = int(ther_camera.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')        # 動画保存時のfourcc設定（mp4用）
    strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    rgb_filename = output_dir + "rgb_video" + strdate + ".mp4"
    ther_filename = output_dir + "ther_video" + strdate + ".mp4"
    rgb_video = cv2.VideoWriter(rgb_filename, fourcc, fps, (rgb_w, rgb_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）
    ther_video = cv2.VideoWriter(ther_filename, fourcc, fps, (ther_w, ther_h))  # 動画の仕様（ファイル名、fourcc, FPS, サイズ）

    # 10 minitesだけ処理を行う．
    looptime = 10
    dt_end = datetime.datetime.now() + datetime.timedelta(minutes=looptime)

    # 撮影＝ループ中にフレームを1枚ずつ取得（qキーで撮影終了）
    while(True):
        rgb_ret, rgb_frame = rgb_camera.read()                             # フレームを取得
        ther_ret, ther_frame = ther_camera.read()                             # フレームを取得
        rgb_video.write(rgb_frame)                                     # 動画を1フレームずつ保存する
        ther_video.write(ther_frame)                                     # 動画を1フレームずつ保存する
        # キー操作があればwhileループを抜ける
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        sleep(1/fps)
        if dt_end < datetime.datetime.now():
            dt_end = dt_end + datetime.timedelta(minutes=looptime)
            strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
            rgb_filename = output_dir + "rgb_video" + strdate + ".mp4"
            ther_filename = output_dir + "ther_video" + strdate + ".mp4"
            cv2.imshow('rgb',rgb_frame)
            cv2.imshow('ther',ther_frame)
            rgb_video = cv2.VideoWriter(rgb_filename, fourcc, fps, (rgb_w, rgb_h))
            ther_video = cv2.VideoWriter(ther_filename, fourcc, fps, (ther_w, ther_h))
            print(f'create new file {dt_end}')


    # 撮影用オブジェクトとウィンドウの解放
    rgb_camera.release()
    ther_camera.release()
    cv2.destroyAllWindows()
