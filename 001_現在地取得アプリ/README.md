# 現在地取得アプリ（Power Apps）

Power Apps で端末の現在地（緯度・経度）を取得し、**現在地の住所を表示するサンプルアプリ**です。

- パターン1：外部 API を使わず、事前に用意した住所データから最寄り住所を推定
- パターン2：Google Maps Geocoding API（Power Automate 経由）で住所を取得

ブログ記事で詳しく解説しています。

- [〖Power Apps〗現在地の住所を取得する方法（APIなし）](https://www.fulogabc.net/entry/power-apps-no-api-get-location)
- [〖Power Apps〗現在地の住所を取得する方法（Google Geocoding API）](https://www.fulogabc.net/entry/power-apps-get-location-google-geocoding-api)

---

## 📌 このアプリでできること

### 共通

- 端末の現在地（緯度・経度）を `Location` 信号から取得
- 緯度・経度を画面に表示してデバッグ確認
- 取得した現在地をもとに、**人が読める住所情報**を表示

### パターン1：API なし版（オフライン寄り）

- 事前に用意した全国住所データ（都道府県・市区・区など）を `addressData` テーブルとしてアプリ内に保持
- Haversine 公式を使って、現在地に最も近い住所を算出
- 以下のような情報をラベル表示
  - 都道府県（例：東京都）
  - 市区町村（例：港区）
  - 区・町名　など

### パターン2：Google Geocoding API 版

- Power Apps で現在地の緯度・経度を取得
- Power Apps 側で Geocoding API 用の URI を組み立て  
  `https://maps.googleapis.com/maps/api/geocode/json?latlng={緯度},{経度}&key={API_KEY}`
- Power Automate の HTTP アクションで API を実行し、JSON を解析
- 必要な住所情報を絞り込み、Power Apps に返して表示


## ✅　前提条件

**共通**
- Power Apps が利用できる環境（Microsoft 365 / Power Platform）
- 位置情報取得を許可した端末（PC / スマホ / タブレット）
- ブラウザやアプリで位置情報利用を許可していること

**API なし版**
- アプリ内で利用する住所データ（addressData）
- 例：geolonia/japanese-addresses-v2 などの全国住所データを整形したもの

**Google Geocoding API 版**
- Power Automate が利用できる環境
- Google Cloud Platform のプロジェクトと Geocoding API キー
- Power Automate で HTTP アクションが利用可能なライセンス


## ⚠️ 注意事項

- 位置情報は GPS や IP アドレスなどから推定されるため、必ずしも正確ではありません
- Geocoding API 版は、API 利用料金・利用制限 に注意してください
- 本アプリはサンプルです。実務利用の前に、必ず検証環境で十分なテストを行ってください

