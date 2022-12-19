import streamlit as st
import pandas as pd
import altair as alt


# SAPIXの公開データをcsvで取得（元データはスプレッドシート）し、DataFrameへ格納
data = pd.read_csv("sapix_2022.csv")
df = pd.DataFrame(data)


################################## 変数定義 ##################################

# 表のカラム
enrollment=['校舎名','在籍者数']
successful_candidate=['校舎名','合格者数']
variable = ['在籍者数','合格者数']

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

# 御三家率等
df_pass_rate_men = df.loc[5:47, ["実績入力以外の編集禁止", "男子御三家率", "男四天王", "筑駒率", "開成率", "1日8校率", "開桜率"]]
df_pass_rate_women = df.loc[5:47, ["実績入力以外の編集禁止", "女子御三家率", "女四天王", "桜蔭率", "1日8校率", "開桜率"]]


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


school_name_deviation = []
n_men = range(len(school_name_men_devi))
n_women = range(len(school_name_women_devi))
n_co = range(len(school_name_co_devi))
n_co = range(len(school_name_co_devi2))



################################## 学校の選択 ##################################

page = st.sidebar.selectbox(
    '男子校・女子校・共学校を選んでください。',['男子校', '女子校', '共学校(男子偏差値)', '共学校(女子偏差値)']
    )

st.sidebar.write('')
st.sidebar.write('')


devi_min, devi_max = st.sidebar.slider('偏差値によって志望校の絞り込みができます。',40, 80, (40, 80))



if page == '男子校':
    st.title('校舎別合格者情報(男子校)')
    st.write('◆学校名を選択してグラフを表示')
    for _n_men in n_men:
        if devi_max > int(school_name_men_devi[_n_men]['偏差値']) > devi_min:
            school_name_deviation.append(school_name_men_devi[_n_men]['学校名'])
    school_name = st.selectbox('志望校を選択してください。',school_name_deviation)
    button = st.button('グラフの表示')

    if school_name == '筑駒':
        df_tsukukoma.columns = successful_candidate
        df_successful_candidate = df_tsukukoma.drop('校舎名', axis=1)

    elif school_name == '開成':
        df_kaisei.columns = successful_candidate
        df_successful_candidate = df_kaisei.drop('校舎名', axis=1)

    elif school_name == '麻布':
        df_azabu.columns = successful_candidate
        df_successful_candidate = df_azabu.drop('校舎名', axis=1)

    elif school_name == '駒東':
        df_komatou.columns = successful_candidate
        df_successful_candidate = df_komatou.drop('校舎名', axis=1)

    elif school_name == '武蔵':
        df_musashi.columns = successful_candidate
        df_successful_candidate = df_musashi.drop('校舎名', axis=1)

    elif school_name == '慶普':
        df_keifu.columns = successful_candidate
        df_successful_candidate = df_keifu.drop('校舎名', axis=1)
    
    elif school_name == '早稲田':
        df_waseda.columns = successful_candidate
        df_successful_candidate = df_waseda.drop('校舎名', axis=1)

    elif school_name == '早大学院':
        df_wasegaku.columns = successful_candidate
        df_successful_candidate = df_wasegaku.drop('校舎名', axis=1)

    elif school_name == '聖光':
        df_seikou.columns = successful_candidate
        df_successful_candidate = df_seikou.drop('校舎名', axis=1)

    elif school_name == '栄光':
        df_eikou.columns = successful_candidate
        df_successful_candidate = df_eikou.drop('校舎名', axis=1)

    elif school_name == '浅野':
        df_asano.columns = successful_candidate
        df_successful_candidate = df_asano.drop('校舎名', axis=1)

    elif school_name == '海城':
        df_kaijou.columns = successful_candidate
        df_successful_candidate = df_kaijou.drop('校舎名', axis=1)
    
    elif school_name == '芝':
        df_shiba.columns = successful_candidate
        df_successful_candidate = df_shiba.drop('校舎名', axis=1)

    elif school_name == '灘':
        df_nada.columns = successful_candidate
        df_successful_candidate = df_nada.drop('校舎名', axis=1)



elif page == '女子校':
    st.title('校舎別合格者情報(女子校)')
    st.write('◆学校名を選択してグラフを表示')
    for _n_women in n_women:
        if devi_max > int(school_name_women_devi[_n_women]['偏差値']) > devi_min:
            school_name_deviation.append(school_name_women_devi[_n_women]['学校名'])
    school_name = st.selectbox('志望校を選択してください。',school_name_deviation)
    button = st.button('グラフの表示')

    if school_name == '桜蔭':
        df_ouin.columns = successful_candidate
        df_successful_candidate = df_ouin.drop('校舎名', axis=1)

    elif school_name == 'JG':
        df_joshigaku.columns = successful_candidate
        df_successful_candidate = df_joshigaku.drop('校舎名', axis=1)

    elif school_name == '雙葉':
        df_futaba.columns = successful_candidate
        df_successful_candidate = df_futaba.drop('校舎名', axis=1)

    elif school_name == '豊島岡':
        df_toshimagaoka.columns = successful_candidate
        df_successful_candidate = df_toshimagaoka.drop('校舎名', axis=1)

    elif school_name == 'フェリス':
        df_ferisu.columns = successful_candidate
        df_successful_candidate = df_ferisu.drop('校舎名', axis=1)

    elif school_name == '白百合':
        df_shirayuri.columns = successful_candidate
        df_successful_candidate = df_shirayuri.drop('校舎名', axis=1)

    elif school_name == '学習院女':
        df_gakujo.columns = successful_candidate
        df_successful_candidate = df_gakujo.drop('校舎名', axis=1)

    elif school_name == '洗足':
        df_senzoku.columns = successful_candidate
        df_successful_candidate = df_senzoku.drop('校舎名', axis=1)

    elif school_name == '吉祥女':
        df_kichijo.columns = successful_candidate
        df_successful_candidate = df_kichijo.drop('校舎名', axis=1)

    elif school_name == '鷗友':
        df_ohyu.columns = successful_candidate
        df_successful_candidate = df_ohyu.drop('校舎名', axis=1)

    elif school_name == '浦和':
        df_urawa.columns = successful_candidate
        df_successful_candidate = df_urawa.drop('校舎名', axis=1)
    



elif page == '共学校(男子偏差値)':
    st.title('校舎別合格者情報(共学校)')
    st.write('◆学校名を選択してグラフを表示')
    for _n_co in n_co:
        if devi_max > int(school_name_co_devi[_n_co]['偏差値']) > devi_min:
            school_name_deviation.append(school_name_co_devi[_n_co]['学校名'])
    school_name = st.selectbox('志望校を選択してください。',school_name_deviation)
    button = st.button('グラフの表示')

    if school_name == '渋幕':
        df_shibumaku.columns = successful_candidate
        df_successful_candidate = df_shibumaku.drop('校舎名', axis=1)

    elif school_name == '渋渋':
        df_shibushibu.columns = successful_candidate
        df_successful_candidate = df_shibushibu.drop('校舎名', axis=1)

    elif school_name == '広尾':
        df_hiroo.columns = successful_candidate
        df_successful_candidate = df_hiroo.drop('校舎名', axis=1)

    elif school_name == '慶湘':
        df_keisho.columns = successful_candidate
        df_successful_candidate = df_keisho.drop('校舎名', axis=1)

    elif school_name == '慶中':
        df_keichu.columns = successful_candidate
        df_successful_candidate = df_keichu.drop('校舎名', axis=1)

    elif school_name == '早実':
        df_soujitsu.columns = successful_candidate
        df_successful_candidate = df_soujitsu.drop('校舎名', axis=1)

    elif school_name == '筑附':
        df_tsukufu.columns = successful_candidate
        df_successful_candidate = df_tsukufu.drop('校舎名', axis=1)

    elif school_name == '青山':
        df_aoyama.columns = successful_candidate
        df_successful_candidate = df_aoyama.drop('校舎名', axis=1)

    elif school_name == '明明':
        df_meimei.columns = successful_candidate
        df_successful_candidate = df_meimei.drop('校舎名', axis=1)




elif page == '共学校(女子偏差値)':
    st.title('校舎別合格者情報(共学校)')
    st.write('◆学校名を選択してグラフを表示')
    for _n_co in n_co:
        if devi_max > int(school_name_co_devi2[_n_co]['偏差値']) > devi_min:
            school_name_deviation.append(school_name_co_devi2[_n_co]['学校名'])
    school_name = st.selectbox('志望校を選択してください。',school_name_deviation)
    button = st.button('グラフの表示')

    if school_name == '渋幕':
        df_shibumaku.columns = successful_candidate
        df_successful_candidate = df_shibumaku.drop('校舎名', axis=1)

    elif school_name == '渋渋':
        df_shibushibu.columns = successful_candidate
        df_successful_candidate = df_shibushibu.drop('校舎名', axis=1)

    elif school_name == '広尾':
        df_hiroo.columns = successful_candidate
        df_successful_candidate = df_hiroo.drop('校舎名', axis=1)

    elif school_name == '慶湘':
        df_keisho.columns = successful_candidate
        df_successful_candidate = df_keisho.drop('校舎名', axis=1)

    elif school_name == '慶中':
        df_keichu.columns = successful_candidate
        df_successful_candidate = df_keichu.drop('校舎名', axis=1)

    elif school_name == '早実':
        df_soujitsu.columns = successful_candidate
        df_successful_candidate = df_soujitsu.drop('校舎名', axis=1)

    elif school_name == '筑附':
        df_tsukufu.columns = successful_candidate
        df_successful_candidate = df_tsukufu.drop('校舎名', axis=1)

    elif school_name == '青山':
        df_aoyama.columns = successful_candidate
        df_successful_candidate = df_aoyama.drop('校舎名', axis=1)

    elif school_name == '明明':
        df_meimei.columns = successful_candidate
        df_successful_candidate = df_meimei.drop('校舎名', axis=1)



################################## ボタンクリックでグラフの表示 ##################################


if button:
    df_enroll.columns = enrollment
    df_concat = pd.concat([df_enroll, df_successful_candidate], axis=1)
    df_concat = pd.melt(df_concat, id_vars=['校舎名'])
    df_concat = df_concat.rename(columns={'value':'該当者数'})
    variable = ['在籍者数','合格者数']
    chart = (
        alt.Chart(df_concat)
        .mark_bar(opacity=0.8, clip=True)
        .encode(
            x='校舎名',
            y=alt.Y('該当者数:Q', stack=None),
            color=alt.Color('variable', scale=alt.Scale(domain=variable, range=["blue", "red"]))
        )
    )
    st.altair_chart(chart, use_container_width=True)


st.write('')
st.write('')
st.write('')



################################## トップ校の合格率まとめ ##################################

if page == '男子校':
    st.write('◆トップ校の合格率まとめを表示')
    button2 = st.button('合格率を表示')
    if button2:
        df_pass_rate_men = df_pass_rate_men.rename(columns={'実績入力以外の編集禁止':'校舎名'})
        df_pass_rate_men = pd.melt(df_pass_rate_men, id_vars=['校舎名'])

        chart2 = (
            alt.Chart(df_pass_rate_men)
            .mark_line(opacity=0.8)
            .encode(
                x='校舎名',
                y=alt.Y('value:Q', stack=None),
                color=alt.Color('variable', scale=alt.Scale(range=["purple", "blue", "green","orange", "red", "pink"]))
            )
        )
        st.altair_chart(chart2, use_container_width=True)

elif page == '女子校':
    st.write('◆トップ校の合格率まとめを表示')
    button2 = st.button('合格率を表示')
    if button2:
        df_pass_rate_women = df_pass_rate_women.rename(columns={'実績入力以外の編集禁止':'校舎名'})
        df_pass_rate_women = pd.melt(df_pass_rate_women, id_vars=['校舎名'])

        chart2 = (
            alt.Chart(df_pass_rate_women)
            .mark_line(opacity=0.8)
            .encode(
                x='校舎名',
                y=alt.Y('value:Q', stack=None),
                color=alt.Color('variable', scale=alt.Scale(range=["purple", "blue", "green","orange", "red"]))
            )
        )
        st.altair_chart(chart2, use_container_width=True)