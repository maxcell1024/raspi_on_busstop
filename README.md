## デジタルサイネージに設置したラズパイ
raspberrypi model4
## Python Version
Python 3.9.2
## Quick Start
```
pip3 install -r requirements.txt
```
定期実行のプログラムはcrontabで設定．
編集内容はcrontab-e.txtに記載．

/etc/systemd/system にファイルを追加
```cp /home/pi/work/cap_video.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl status
sudo systemctl enable
sudo systemctl start
```

### ラズパイOSのインストール
balenaEtcherを使ってSDカードのフラッシュ

`https://downloads.raspberrypi.org/raspios_arm64/images/raspios_arm64-2022-09-07/2022-09-06-raspios-bullseye-arm64.img.xz`

### SDカードのパーティション作成
研究室のUbuntuマシンを使用
上記のSDカードを挿入後，以下のgpartedの立ち上げ．
```gparted```

後はGUIで以下を実施．
- Gpartedを用いてrootfsを8GBに固定
- bootはそのままで残りの110GBをEXTRAFSというラベルで作成

### VPN
VPNはminato-gwでホスティングしている．
使用ソフトウェア：WireGuard
ラズパイのIP：10.0.0.4

### データの転送先
データはshサーバをJumpHostしてプロジェクトディスクがマウントされたrshに転送している．
転送の際にはrsh.naist.jpをrshとして表記しているため，必要に応じて.ssh/configファイルを作成し，設定する．
転送には筆者のユーザを利用している．

