import streamlit as st
import pandas as pd
import altair as alt


# SAPIXの公開データをcsvで取得（元データはスプレッドシート）し、DataFrameへ格納
data = pd.read_csv("sapix_2022.csv")
df = pd.DataFrame(data)

################################## トップ校の合格率まとめ ##################################

df_pass_rate_men = df.loc[5:47, ["実績入力以外の編集禁止", "男子御三家率", "男四天王", "筑駒率", "開成率", "1日8校率", "開桜率"]]
df_pass_rate_women = df.loc[5:47, ["実績入力以外の編集禁止", "女子御三家率", "女四天王", "桜蔭率", "1日8校率", "開桜率"]]

df_pass_rate_men = df_pass_rate_men.rename(columns={'実績入力以外の編集禁止':'校舎名'})
df_pass_rate_men = pd.melt(df_pass_rate_men, id_vars=['校舎名'])

df_pass_rate_women = df_pass_rate_women.rename(columns={'実績入力以外の編集禁止':'校舎名'})
df_pass_rate_women = pd.melt(df_pass_rate_women, id_vars=['校舎名'])


def indicate_line_chart_men():
    chart2 = (
        alt.Chart(df_pass_rate_men)
        .mark_line(opacity=0.8)
        .encode(
            x='校舎名',
            y=alt.Y('value:Q', stack=None),
            color=alt.Color('variable', scale=alt.Scale(range=["purple", "blue", "green","orange", "red", "pink"]))
        )
    )
    return st.altair_chart(chart2, use_container_width=True)


def indicate_line_chart_women():
    chart2 = (
        alt.Chart(df_pass_rate_women)
        .mark_line(opacity=0.8)
        .encode(
            x='校舎名',
            y=alt.Y('value:Q', stack=None),
            color=alt.Color('variable', scale=alt.Scale(range=["purple", "blue", "green","orange", "red"]))
        )
    )
    return st.altair_chart(chart2, use_container_width=True)