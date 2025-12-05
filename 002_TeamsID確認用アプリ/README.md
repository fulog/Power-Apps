# Teams ID 確認用アプリ（Power Apps）

Microsoft Teams の **チーム ID** と **チャネル ID** を一覧で確認できる Power Apps のキャンバスアプリです。  
Power Apps / Power Automate / Graph 連携時に「ID を調べるのが面倒…」というときに使える、**ID 取得専用ツール**として使えます。

ブログ記事で詳しく解説しています。

- [〖Power Apps〗TeamsのチームIDとチャネルIDを確認するPower Appsアプリ](https://www.fulogabc.net/entry/power-apps-teamsid-confirmation)

---

## 📌 このアプリでできること

### 左側：チーム一覧 & チーム ID

- テナント内の Teams チームを一覧表示
- 各行で次の情報を確認できます（例）  
  - チーム名  
  - チーム ID（= groupId）
- 行ごとに **「コピー」ボタン** を配置
  - 「チーム名 + チーム ID」のセットをクリップボードにコピー
  - ドキュメント／Power Automate の設定画面などにそのまま貼り付け可能

### 右側：チャネル一覧 & チャネル ID

- 左側で選択したチームに紐づく **チャネル一覧** を表示
- 各行で次の情報を確認できます（例）  
  - チャネル名  
  - チャネル ID
- こちらも **「コピー」ボタン** で
  - 「チャネル名 + チャネル ID」をクリップボードにコピー

### 想定ユースケース

- Power Automate の Teams コネクタで  
  「投稿先のチーム / チャネル ID を固定 or 動的に指定したい」
- Graph API でチーム / チャネルを扱うときの事前調査用
- 部署メンバー向けに  
  「Teams ID を確認するための共通ツール」として展開

---

## ✅ 前提条件
- Microsoft 365 / Power Platform 環境
- Power Apps が利用できるライセンス
- Microsoft Teams への接続が許可されていること
- チーム／チャネル情報を取得できる権限
- ※組織のポリシーによっては表示できるチームが制限される場合があります

