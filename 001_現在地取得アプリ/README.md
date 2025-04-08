# 現在地取得アプリ

## アプリケーション概要
現在地取得アプリは、端末のGPS等から緯度・経度を取得し、現在住所を取得するアプリです。2つの方法で現在地の取得を実装しています。

1. Google Geocoding APIを使って現在地住所を取得する
2. 住所データを事前に準備し、計算によって最寄り住所を取得する（日本国内のみ）

## 展開・利用に必要な条件
* Power Automate 有償ライセンス（開発者・利用者）
  ※Google Geocoding APIの実行にHTTPアクションを利用します。プレミアムライセンスが必要です。
* Pythonが利用できる環境

## 対応言語
* 日本語


## henkan.py
2でhttps://japanese-addresses-v2.geoloniamaps.com/api/ja.jsonから取得したデータをPower Appsで使えるコレクション形式に変換します。

