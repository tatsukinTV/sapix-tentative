import pandas as pd

# SAPIXの公開データをcsvで取得（元データはスプレッドシート）し、DataFrameへ格納
data = pd.read_csv("sapix_2022.csv")
df = pd.DataFrame(data)

# 表のカラム
enrollment=['校舎名','在籍者数']
successful_candidate=['校舎名','合格者数']
usage_guide = ['在籍者数','合格者数']

# 在籍者数用と合格者数用にデータをピックアップする
df_enroll = df.loc[5:47, ["実績入力以外の編集禁止","在籍"]]

# 男子校
df_tsukukoma = df.loc[5:47, ["実績入力以外の編集禁止", "筑駒"]]
df_kaisei = df.loc[5:47, ["実績入力以外の編集禁止", "開成"]]
df_azabu = df.loc[5:47, ["実績入力以外の編集禁止", "麻布"]]
df_komatou = df.loc[5:47, ["実績入力以外の編集禁止", "駒東"]]
df_musashi = df.loc[5:47, ["実績入力以外の編集禁止", "武蔵"]]
df_keifu = df.loc[5:47, ["実績入力以外の編集禁止", "慶普"]]
df_waseda = df.loc[5:47, ["実績入力以外の編集禁止", "早稲田"]]
df_wasegaku = df.loc[5:47, ["実績入力以外の編集禁止", "早大学院"]]
df_seikou = df.loc[5:47, ["実績入力以外の編集禁止", "聖光"]]
df_eikou = df.loc[5:47, ["実績入力以外の編集禁止", "栄光"]]
df_asano = df.loc[5:47, ["実績入力以外の編集禁止", "浅野"]]
df_kaijou = df.loc[5:47, ["実績入力以外の編集禁止", "海城"]]
df_shiba = df.loc[5:47, ["実績入力以外の編集禁止", "芝"]]
df_nada = df.loc[5:47, ["実績入力以外の編集禁止", "灘"]]

# 女子校
df_ouin = df.loc[5:47, ["実績入力以外の編集禁止", "桜蔭"]]
df_joshigaku = df.loc[5:47, ["実績入力以外の編集禁止", "JG"]]
df_futaba = df.loc[5:47, ["実績入力以外の編集禁止", "雙葉"]]
df_toshimagaoka = df.loc[5:47, ["実績入力以外の編集禁止", "豊島岡"]]
df_ferisu = df.loc[5:47, ["実績入力以外の編集禁止", "フェリス"]]
df_shirayuri = df.loc[5:47, ["実績入力以外の編集禁止", "白百合"]]
df_gakujo = df.loc[5:47, ["実績入力以外の編集禁止", "学習院女"]]
df_senzoku = df.loc[5:47, ["実績入力以外の編集禁止", "洗足"]]
df_kichijo = df.loc[5:47, ["実績入力以外の編集禁止", "吉祥女"]]
df_ohyu = df.loc[5:47, ["実績入力以外の編集禁止", "鷗友"]]
df_urawa = df.loc[5:47, ["実績入力以外の編集禁止", "浦和明星"]]

# 共学校
df_shibumaku = df.loc[5:47, ["実績入力以外の編集禁止", "渋幕"]]
df_shibushibu = df.loc[5:47, ["実績入力以外の編集禁止", "渋渋"]]
df_hiroo = df.loc[5:47, ["実績入力以外の編集禁止", "広尾"]]
df_keisho = df.loc[5:47, ["実績入力以外の編集禁止", "慶湘"]]
df_keichu = df.loc[5:47, ["実績入力以外の編集禁止", "慶中"]]
df_soujitsu = df.loc[5:47, ["実績入力以外の編集禁止", "早実"]]
df_tsukufu = df.loc[5:47, ["実績入力以外の編集禁止", "筑附"]]
df_aoyama = df.loc[5:47, ["実績入力以外の編集禁止", "青山"]]
df_meimei = df.loc[5:47, ["実績入力以外の編集禁止", "明明"]]