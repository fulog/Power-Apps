# Power Apps サンプルアプリ集

Power Apps の学習・検証・紹介用に作成した **キャンバスアプリ & Power Automate フロー** をまとめたリポジトリです。  
ブログ記事で紹介しているアプリのソースを公開しています。

- リポジトリ URL: https://github.com/fulog/Power-Apps
- ライセンス: MIT（詳しくは [`LICENSE`](./LICENSE) を参照してください）

---

## 📁 リポジトリ構成

| フォルダ名 | アプリ名 / 用途 | 補足 |
|-----------|-----------------|------|
| `001_現在地取得アプリ` | 現在地情報（緯度経度）から住所を取得する Power Apps | API 版 / API なし版のサンプル構成 |
| `002_TeamsID確認用アプリ` | Teams のチーム ID / チャネル ID を確認する Power Apps | Power Automate / Graph 連携時の ID 取得補助アプリ |
| `003_リマインドアプリ` | Teams で「いいね」していない人にメンションするリマインドアプリ | Power Apps + Power Automate 連携サンプル |
| `004_SharePointリスト管理アプリ` | SharePointサイト内のリスト／ライブラリ情報を一覧で可視化、Hiddenの切り替えや列情報のExcel貼り付け用テキスト出力ができる| Power Apps + Power Automate 連携サンプル |


> 各フォルダの中に、Power Apps / Power Automate からエクスポートした zip ファイルなどを配置しています。

---


## 🚀 アプリのインポート手順

各フォルダ内の zip ファイルを、Power Apps / Power Automate からインポートして利用します。

### Power Apps（キャンバスアプリ）の場合

1. このリポジトリから対象フォルダ（例: `001_現在地取得アプリ`）の zip ファイルをダウンロード
2. ブラウザで https://make.powerapps.com を開き、サインイン
3. 対象の環境を選択
4. 左メニューから **[アプリ] → [キャンバス アプリ]** を開く
5. **[インポート]** または「アプリのインポート」を選択
6. ダウンロードした zip ファイルを指定し、画面に従ってインポート

### Power Automate（クラウドフロー）の場合

1. ブラウザで https://make.powerautomate.com を開き、サインイン
2. 左メニューから **[マイ フロー]** を選択
3. **[インポート]** をクリック
4. 対象 zip ファイルを指定し、接続・リソースの設定を行ってインポート

> ※ 実際の zip / ソリューション形式はフォルダごとに異なる場合があります。  
> フォルダ内の README やファイル名もあわせて確認してください。

---

## ⚙ 前提条件 / 動作環境の目安

- Microsoft Power Apps / Power Automate が利用可能なライセンス
- 対象テナントの環境（開発 / テストなど）
- 接続先の設定
  - Microsoft Teams への接続（Teams アプリ / Graph API 等）
  - 住所データや外部 API を利用する場合は、各サービスの利用規約・API キー などの設定が必要

---

## 📝 ライセンス

このリポジトリは **MIT License** で公開しています。  
詳細は [`LICENSE`](./LICENSE) を確認してください。

---

## 👤 作者

- Author: ふー
- Blog: https://www.fulogabc.net/
- GitHub: https://github.com/fulog

不具合や改善案などがあれば、Issue や Pull Request でフィードバックいただけると嬉しいです。
