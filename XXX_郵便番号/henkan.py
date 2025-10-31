from pathlib import Path
import csv

# ✅ ファイルの正しい場所
csv_path = Path("C:/pData/yubinData/utf_ken_all.csv")

# ✅ 出力先（同じフォルダに出力）
out_path = Path("C:/pData/yubinData/powerapps_collection.txt")

# ❸ Power Apps で使うコレクション名
collection_name = "colZipData"

# 日本郵便のUTF-8版 15項目に合わせた見出し
powerapps_headers = [
    "JisCode",              # 1. 全国地方公共団体コード
    "OldZip",               # 2. （旧）郵便番号（5桁）
    "Zip",                  # 3. 郵便番号（7桁）
    "PrefKana",             # 4. 都道府県名（カナ）
    "CityKana",             # 5. 市区町村名（カナ）
    "TownKana",             # 6. 町域名（カナ）
    "Pref",                 # 7. 都道府県名（漢字）
    "City",                 # 8. 市区町村名（漢字）
    "Town",                 # 9. 町域名（漢字）
    "HasMultiZipInTown",    # 10. 一町域が二以上の郵便番号で表される場合の表示（0/1）
    "HasKoazaBanchi",       # 11. 小字毎に番地が起番されている町域の表示（0/1）
    "HasChome",             # 12. 丁目を有する町域の場合の表示（0/1）
    "ZipForMultiTowns",     # 13. 一つの郵便番号で二以上の町域を表す場合の表示（0/1）
    "UpdateFlag",           # 14. 更新の表示（0,1,2）
    "UpdateReason",         # 15. 変更理由（0〜6）
]

def to_record(values: list[str]) -> str:
    """1行をPower Appsの { "キー": "値" } 形式に変換"""
    fixed = values + [""] * (len(powerapps_headers) - len(values))  # 列数が足りない場合に補完
    parts = []
    for key, val in zip(powerapps_headers, fixed):
        safe_val = val.replace('"', '""')
        parts.append(f'"{key}": "{safe_val}"')
    return "{ " + ", ".join(parts) + " }"

# CSVを読み込む（日本郵便のCSVはヘッダー行なし）
with csv_path.open("r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = [to_record(row) for row in reader]

# 改行区切りで出力（Power Appsで「[ {…}, {…}, … ]」にして使う想定）
out_path.write_text(",\n".join(data), encoding="utf-8")

print(f"✅ 変換完了: {out_path}")