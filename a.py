import streamlit as st
import pandas as pd
import altair as alt

################# データ取得とグラフ作成部分 #################

## SAPIXの公開データをcsvで取得（元データはスプレッドシート）し、データフレームへ格納
data = pd.read_csv("sapi_2022.csv")
df = pd.DataFrame(data)

## 表のカラムに入れる名前を変数に格納
enrollment=['校舎名','在籍者数']
successful_candidate=['校舎名','合格者数']
variable = ['在籍者数','合格者数']

## 在籍者数用と合格者数用にデータをピックアップする
df_enroll = df.iloc[5:48,0:2:1]
df_tsukukoma = df.iloc[5:48,0:3:2]

## 表にカラム名を名前をつける
df_enroll.columns = enrollment
df_tsukukoma.columns = successful_candidate

## 在籍者数用と合格者数用の表を合体させ、グラフ化するための加工をする
df_tsukukoma2 = df_tsukukoma.drop('校舎名', axis=1)
df_concat = pd.concat([df_enroll,df_tsukukoma2], axis=1)
df_concat = pd.melt(df_concat, id_vars=['校舎名'])
df_concat = df_concat.rename(
    columns={'value':'該当者数'}
)

## グラフ化する
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
    school_name = st.selectbox('志望校を選択してください。',['筑駒', '開成'])
    button = st.button('グラフの表示')

    if button:
        st.write('各校舎の在籍者数と合格者数を棒グラフで表します。')
        st.write('株価アプリの時に使ったaltairをで可視化します。')
        if school_name == '筑駒':
            st.write('筑駒のグラフ')
            st.altair_chart(chart, use_container_width=True)
        if school_name == '開成':
            st.write('開成のグラフ')
    
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
    school_name = st.selectbox('志望校を選択してください。',['桜蔭', '女子学院'])
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
    st.write('同様に作成します。')