import cv2
import numpy as np
from time import sleep


def is_ther(frame) -> bool:
    """frame from thermo capture"""
    vs01 = np.all(frame[:, :, 0] == frame[:, :, 1])
    vs12 = np.all(frame[:, :, 1] == frame[:, :, 2])
    vs20 = np.all(frame[:, :, 2] == frame[:, :, 0])
    return vs01 and vs12 and vs20

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
    rgb_cid, ther_cid = get_camera_ids()
    print(f'after get ids, rgb_cid: {rgb_cid}, ther_cid: {ther_cid}')
    rgb_capture = cv2.VideoCapture(rgb_cid)
    ther_capture = cv2.VideoCapture(ther_cid)
    rgb_w = int(rgb_capture.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    ther_w = int(ther_capture.get(cv2.CAP_PROP_FRAME_WIDTH))              # カメラの横幅を取得
    rgb_h = int(rgb_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    ther_h = int(ther_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))             # カメラの縦幅を取得
    print(f"rgb w:{rgb_w} h:{rgb_h}\n")
    print(f"ther w:{ther_w} h:{ther_h}")
 
    while(True):
        rgb_ret, rgb_frame = rgb_capture.read()
        ther_ret, ther_frame = ther_capture.read()
        if (rgb_frame is not None) and (ther_frame is not None):
            cv2.imshow('rgb_frame',rgb_frame[:, ::-1, :])
            cv2.imshow('ther_frame',ther_frame[:, ::-1, :])
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            #sleep(1/60)
    
    rgb_capture.release()
    ther_capture.release()
    cv2.destroyAllWindows()
