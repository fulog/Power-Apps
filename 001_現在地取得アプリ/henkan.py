import requests
import json
import os

# JSON取得
url = "https://japanese-addresses-v2.geoloniamaps.com/api/ja.json"
response = requests.get(url)
response.encoding = "utf-8"
data = response.json()

# 'data' の中を処理
collection_data = []

for pref_data in data["data"]:
    pref_name = pref_data.get("pref", "")
    pref_k = pref_data.get("pref_k", "")
    pref_r = pref_data.get("pref_r", "")
    pref_point = pref_data.get("point", [])  # 緯度・経度
    pref_lat, pref_lon = pref_point if len(pref_point) == 2 else (None, None)

    for city in pref_data.get("cities", []):
        city_name = city.get("city", "")
        city_ward = city.get("ward", "")
        city_point = city.get("point", [])  # 緯度・経度
        city_lat, city_lon = city_point if len(city_point) == 2 else (None, None)

        # データをコレクションに追加
        collection_data.append(
            {
                "prefecture": pref_name,
                "pref_k": pref_k,
                "pref_r": pref_r,
                "city": city_name,
                "ward": city_ward,
                "prefecture_latitude": pref_lat,
                "prefecture_longitude": pref_lon,
                "city_latitude": city_lat,
                "city_longitude": city_lon,
            }
        )

# 結果確認（最初の10件）
print(json.dumps(collection_data[:10], ensure_ascii=False, indent=2))

# 出力ファイルのパスを.pyファイルと同じフォルダに設定
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "powerapps_clearcollect.txt")

# Power AppsのClearCollect形式で保存
with open(output_path, "w", encoding="utf-8") as f:
    f.write("ClearCollect(AddressCollection,\n")
    for item in collection_data:
        line = (
            f'    {{prefecture: "{item["prefecture"]}", city: "{item["city"]}", ward: "{item["ward"]}", '
            f"prefecture_latitude: {item['prefecture_latitude']}, prefecture_longitude: {item['prefecture_longitude']}, "
            f"city_latitude: {item['city_latitude']}, city_longitude: {item['city_longitude']}}}"
        )
        if item != collection_data[-1]:
            line += ",\n"
        else:
            line += "\n"
        f.write(line)
    f.write(");")

print(f"メモ帳に出力が完了しました！\n→ {output_path}")
