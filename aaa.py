import streamlit as st
import altair as alt
import pandas as pd
    
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
def create_graph():
    chart = (
    alt.Chart(df_concat)
    .mark_bar(opacity=0.8, clip=True)
    .encode(
        x='校舎名',
        y=alt.Y('該当者数:Q', stack=None),
        color=alt.Color('variable', scale=alt.Scale(domain=variable, range=["blue", "red"]))
        )
    )
    return chart

a = create_graph()
a