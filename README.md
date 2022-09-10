## デジタルサイネージに設置したラズパイ
raspberrypi model4
## Python Version

## Quick Start
Requiremnets
特になし．

## Operation

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
### リポジトリのクローン
`git clone https://github.com/maxcell1024/raspi_on_busstop.git` 















