import streamlit as st
import pandas as pd
import altair as alt

################# データ取得とグラフ作成部分 #################

# SAPIXの公開データをcsvで取得（元データはスプレッドシート）し、データフレームへ格納
data = pd.read_csv("sapi_2022.csv")
df = pd.DataFrame(data)

# 表のカラムに入れる名前を変数に格納
enrollment=['校舎名','在籍者数']
successful_candidate=['校舎名','合格者数']
variable = ['在籍者数','合格者数']

# その他の変数定義
school_name_men = ['筑駒', '開成', '麻布', '駒東', '武蔵', '慶普', '早稲田', '早大学院','聖光', '栄光', '浅野', '海城', '芝', '灘']
school_name_women = ['桜蔭', 'JG', '雙葉', '豊島岡', 'フェリス', '白百合', '学習院女', '洗足', '吉祥女', '鷗友','浦和']
school_name_all = ['渋幕', '渋渋', '広尾', '慶湘',' 慶中', '慶普', '早実', '筑附','青山', '明明']

# 在籍者数用と合格者数用にデータをピックアップする
df_enroll = df.loc[5:48, ["実績入力以外の編集禁止","在籍"]]
df_tsukukoma = df.loc[5:48, ["実績入力以外の編集禁止", "筑駒"]]
df_kaisei = df.loc[5:48, ["実績入力以外の編集禁止", "開成"]]
df_azabu = df.loc[5:48, ["実績入力以外の編集禁止", "麻布"]]
df_komatou = df.loc[5:48, ["実績入力以外の編集禁止", "駒東"]]
df_musashi = df.loc[5:48, ["実績入力以外の編集禁止", "武蔵"]]
# df_keihu = df.loc[5:48, ["実績入力以外の編集禁止", "慶普"]]　←なぜか列名なし
df_waseda = df.loc[5:48, ["実績入力以外の編集禁止", "早稲田"]]
df_wasegaku = df.loc[5:48, ["実績入力以外の編集禁止", "早大学院"]]
df_seikou = df.loc[5:48, ["実績入力以外の編集禁止", "聖光"]]
df_eikou = df.loc[5:48, ["実績入力以外の編集禁止", "栄光"]]
df_asano = df.loc[5:48, ["実績入力以外の編集禁止", "浅野"]]
df_kaijou = df.loc[5:48, ["実績入力以外の編集禁止", "海城"]]
df_shiba = df.loc[5:48, ["実績入力以外の編集禁止", "芝"]]

# 表にカラム名を名前をつける
df_enroll.columns = enrollment
# if school_name_men=='筑駒':
# df_tsukukoma.columns = successful_candidate

# school_name_men
df_tsukukoma.columns = successful_candidate

# 在籍者数用と合格者数用の表を合体させ、グラフ化するための加工をする
df_tsukukoma2 = df_tsukukoma.drop('校舎名', axis=1)
df_concat = pd.concat([df_enroll,df_tsukukoma2], axis=1)
df_concat = pd.melt(df_concat, id_vars=['校舎名'])
df_concat = df_concat.rename(
    columns={'value':'該当者数'}
)

# グラフ化する
chart = (
alt.Chart(df_concat)
.mark_bar(opacity=0.8, clip=True)
.encode(
    x='校舎名',
    y=alt.Y('該当者数:Q', stack=None),
    color=alt.Color('variable', scale=alt.Scale(domain=variable, range=["blue", "red"]))
    )
)


################# streamlitで作成したフロントの部分 #################


page = st.sidebar.selectbox('男子校・女子校・共学校を選んでください。',['男子校', '女子校', '共学校'])

if page == '男子校':
    st.title('校舎別合格者情報(男子校)')
    st.write('◆学校名を選択してグラフを表示')
    school_name = st.selectbox('志望校を選択してください。',school_name_men)
    button = st.button('グラフの表示')

    if button:
        if school_name == '筑駒':
            st.write('筑駒のグラフ')
            st.altair_chart(chart, use_container_width=True)
        if school_name == '開成':
            st.write('開成のグラフ')
            df_enroll.columns = enrollment
            df_kaisei.columns = successful_candidate

            df_kaisei2 = df_kaisei.drop('校舎名', axis=1)
            df_concat = pd.concat([df_enroll,df_kaisei2], axis=1)

            df_concat = pd.melt(df_concat, id_vars=['校舎名'])

            df_concat = df_concat.rename(
                columns={'value':'該当者数'}
            )

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

    st.write('◆範囲内の偏差値の学校すべてを表示')
    deviation_value = st.slider(
        '偏差値での絞り込みができます。',
        50, 80, (50, 80)
    )
    button2 = st.button('グラフの見比べ')
    if button2:
        st.write('範囲内の偏差値の学校に対し、各校舎の実績を見比べることばできます。')

if page == '女子校':
    st.title('校舎別合格者情報(女子校)')
    st.write('◆学校名を選択してグラフを表示')
    school_name = st.selectbox('志望校を選択してください。',school_name_women)
    button = st.button('グラフの表示')

    if button:
        st.write('各校舎の在籍者数と合格者数を棒グラフで表します。')
        st.write('株価アプリの時に使ったaltairをで可視化します。')
        if school_name == '桜蔭':
            st.write('桜蔭のグラフ')
        if school_name == '女子学院':
            st.write('女子学院のグラフ')

    st.write('')
    st.write('')
    st.write('')

    st.write('◆範囲内の偏差値の学校すべてを表示')
    deviation_value = st.slider(
        '偏差値での絞り込みができます。',
        50, 80, (50, 80)
    )
    button2 = st.button('グラフの見比べ')
    if button2:
        st.write('範囲内の偏差値の学校に対し、各校舎の実績を見比べることばできます。')

if page == '共学校':
    st.title('校舎別合格者情報(共学校)')
    st.write('◆学校名を選択してグラフを表示')
    school_name = st.selectbox('志望校を選択してください。',school_name_all)
    button = st.button('グラフの表示')

    if button:
        st.write('各校舎の在籍者数と合格者数を棒グラフで表します。')
        st.write('株価アプリの時に使ったaltairをで可視化します。')
        if school_name == '渋幕':
            st.write('渋幕のグラフ')
        if school_name == '渋渋':
            st.write('渋渋のグラフ')

    st.write('')
    st.write('')
    st.write('')

    st.write('◆範囲内の偏差値の学校すべてを表示')
    deviation_value = st.slider(
        '偏差値での絞り込みができます。',
        50, 80, (50, 80)
    )
    button2 = st.button('グラフの見比べ')
    if button2:
        st.write('範囲内の偏差値の学校に対し、各校舎の実績を見比べることばできます。')