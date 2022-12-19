import pandas as pd

# SAPIXの公開データをcsvで取得（元データはスプレッドシート）し、DataFrameへ格納
data = pd.read_csv("sapix_2022.csv")
df = pd.DataFrame(data)


################################## 偏差値連動関係 ##################################

# 男子校
school_name_tsukukoma = {'学校名':'筑駒', '偏差値':df.loc[0, ["筑駒"][0]]}
school_name_kaisei = {'学校名':'開成', '偏差値':df.loc[0, ["開成"][0]]}
school_name_azabu = {'学校名':'麻布', '偏差値':df.loc[0, ["麻布"][0]]}
school_name_komatou = {'学校名':'駒東', '偏差値':df.loc[0, ["駒東"][0]]}
school_name_musashi = {'学校名':'武蔵', '偏差値':df.loc[0, ["武蔵"][0]]}
school_name_keifu = {'学校名':'慶普', '偏差値':df.loc[0, ["慶普"][0]]}
school_name_waseda = {'学校名':'早稲田', '偏差値':df.loc[0, ["早稲田"][0]]}
school_name_wasegaku = {'学校名':'早大学院', '偏差値':df.loc[0, ["早大学院"][0]]}
school_name_seikou = {'学校名':'聖光', '偏差値':df.loc[0, ["聖光"][0]]}
school_name_eikou = {'学校名':'栄光', '偏差値':df.loc[0, ["栄光"][0]]}
school_name_asano = {'学校名':'浅野', '偏差値':df.loc[0, ["浅野"][0]]}
school_name_kaijo = {'学校名':'海城', '偏差値':df.loc[0, ["海城"][0]]}
school_name_shiba = {'学校名':'芝', '偏差値':df.loc[0, ["芝"][0]]}
school_name_nada = {'学校名':'灘', '偏差値':df.loc[0, ["灘"][0]]}

school_name_men_devi = [school_name_tsukukoma, school_name_kaisei, school_name_azabu, school_name_komatou,
    school_name_musashi, school_name_keifu, school_name_waseda, school_name_wasegaku, school_name_seikou,
    school_name_eikou, school_name_asano, school_name_kaijo, school_name_shiba, school_name_nada]


# 女子校
school_name_ouin = {'学校名':'桜蔭', '偏差値':df.loc[0, ["桜蔭"][0]]}
school_name_jg = {'学校名':'JG', '偏差値':df.loc[0, ["JG"][0]]}
school_name_futaba = {'学校名':'雙葉', '偏差値':df.loc[0, ["雙葉"][0]]}
school_name_toshimagaoka = {'学校名':'豊島岡', '偏差値':df.loc[0, ["豊島岡"][0]]}
school_name_ferisu = {'学校名':'フェリス', '偏差値':df.loc[0, ["フェリス"][0]]}
school_name_shirayuri = {'学校名':'白百合', '偏差値':df.loc[0, ["白百合"][0]]}
school_name_gakujo = {'学校名':'学習院女', '偏差値':df.loc[0, ["学習院女"][0]]}
school_name_senzoku = {'学校名':'洗足', '偏差値':df.loc[0, ["洗足"][0]]}
school_name_kichijo = {'学校名':'吉祥女', '偏差値':df.loc[0, ["吉祥女"][0]]}
school_name_ouyu = {'学校名':'鷗友', '偏差値':df.loc[0, ["鷗友"][0]]}
school_name_urawa = {'学校名':'浦和明星', '偏差値':df.loc[0, ["浦和明星"][0]]}

school_name_women_devi = [school_name_ouin, school_name_jg, school_name_futaba, school_name_toshimagaoka,
    school_name_ferisu, school_name_shirayuri, school_name_gakujo, school_name_senzoku, school_name_kichijo,
    school_name_ouyu, school_name_urawa]


# 共学校（男子偏差値）
school_name_shibumaku = {'学校名':'渋幕', '偏差値':df.loc[0, ["渋幕"][0]]}
school_name_shibushibu = {'学校名':'渋渋', '偏差値':df.loc[0, ["渋渋"][0]]}
school_name_hiroo = {'学校名':'広尾', '偏差値':df.loc[0, ["広尾"][0]]}
school_name_keisho = {'学校名':'慶湘', '偏差値':df.loc[0, ["慶湘"][0]]}
school_name_keichu = {'学校名':'慶中', '偏差値':df.loc[0, ["慶中"][0]]}
school_name_soujitsu = {'学校名':'早実', '偏差値':df.loc[0, ["早実"][0]]}
school_name_tsukufu = {'学校名':'筑附', '偏差値':df.loc[0, ["筑附"][0]]}
school_name_aoyama = {'学校名':'青山', '偏差値':df.loc[0, ["青山"][0]]}
school_name_meimei = {'学校名':'明明', '偏差値':df.loc[0, ["明明"][0]]}

school_name_co_devi = [school_name_shibumaku, school_name_shibushibu, school_name_hiroo, school_name_keisho,
    school_name_keichu, school_name_soujitsu, school_name_tsukufu, school_name_aoyama, school_name_meimei]


# 共学校（女子偏差値）
school_name_shibumaku2 = {'学校名':'渋幕', '偏差値':df.loc[1, ["渋幕"][0]]}
school_name_shibushibu2 = {'学校名':'渋渋', '偏差値':df.loc[1, ["渋渋"][0]]}
school_name_hiroo2 = {'学校名':'広尾', '偏差値':df.loc[1, ["広尾"][0]]}
school_name_keisho2 = {'学校名':'慶湘', '偏差値':df.loc[1, ["慶湘"][0]]}
school_name_keichu2 = {'学校名':'慶中', '偏差値':df.loc[1, ["慶中"][0]]}
school_name_soujitsu2 = {'学校名':'早実', '偏差値':df.loc[1, ["早実"][0]]}
school_name_tsukufu2 = {'学校名':'筑附', '偏差値':df.loc[1, ["筑附"][0]]}
school_name_aoyama2 = {'学校名':'青山', '偏差値':df.loc[1, ["青山"][0]]}
school_name_meimei2 = {'学校名':'明明', '偏差値':df.loc[1, ["明明"][0]]}

school_name_co_devi2 = [school_name_shibumaku2, school_name_shibushibu2, school_name_hiroo2, school_name_keisho2,
    school_name_keichu2, school_name_soujitsu2, school_name_tsukufu2, school_name_aoyama2, school_name_meimei2]