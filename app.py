import streamlit as st
import pandas as pd
import altair as alt

import variable
import variable2

from function import indicate_line_chart_men
from function import indicate_line_chart_women

################################## セレクトボックスの偏差値連動 ##################################

school_name_deviation = []
n_men = range(len(variable2.school_name_men_devi))
n_women = range(len(variable2.school_name_women_devi))
n_co = range(len(variable2.school_name_co_devi))
n_co = range(len(variable2.school_name_co_devi2))

################################## 学校の選択 ##################################

page = st.sidebar.selectbox(
    '男子校・女子校・共学校を選んでください。',['男子校', '女子校', '共学校(男子偏差値)', '共学校(女子偏差値)']
    )

st.sidebar.write('')
st.sidebar.write('')


devi_min, devi_max = st.sidebar.slider('偏差値によって志望校の絞り込みができます。',40, 80, (40, 80))

st.title('2022年度 SAPIX校舎別合格者情報')

if page == '男子校':
    st.markdown('### (男子校)')
    st.write('')
    st.markdown('##### ◆在籍生徒数と合格者数')
    for _n_men in n_men:
        if devi_max > int(variable2.school_name_men_devi[_n_men]['偏差値']) > devi_min:
            school_name_deviation.append(variable2.school_name_men_devi[_n_men]['学校名'])
    school_name = st.selectbox('志望校を選択してください。',school_name_deviation)
    button = st.button('グラフの表示')

    if school_name == '筑駒':
        variable.df_tsukukoma.columns = variable.successful_candidate
        df_successful_candidate = variable.df_tsukukoma.drop('校舎名', axis=1)

    elif school_name == '開成':
        variable.df_kaisei.columns = variable.successful_candidate
        df_successful_candidate = variable.df_kaisei.drop('校舎名', axis=1)

    elif school_name == '麻布':
        variable.df_azabu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_azabu.drop('校舎名', axis=1)

    elif school_name == '駒東':
        variable.df_komatou.columns = variable.successful_candidate
        df_successful_candidate = variable.df_komatou.drop('校舎名', axis=1)

    elif school_name == '武蔵':
        variable.df_musashi.columns = variable.successful_candidate
        df_successful_candidate = variable.df_musashi.drop('校舎名', axis=1)

    elif school_name == '慶普':
        variable.df_keifu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_keifu.drop('校舎名', axis=1)

    elif school_name == '早稲田':
        variable.df_waseda.columns = variable.successful_candidate
        df_successful_candidate = variable.df_waseda.drop('校舎名', axis=1)

    elif school_name == '早大学院':
        variable.df_wasegaku.columns = variable.successful_candidate
        df_successful_candidate = variable.df_wasegaku.drop('校舎名', axis=1)

    elif school_name == '聖光':
        variable.df_seikou.columns = variable.successful_candidate
        df_successful_candidate = variable.df_seikou.drop('校舎名', axis=1)

    elif school_name == '栄光':
        variable.df_eikou.columns = variable.successful_candidate
        df_successful_candidate = variable.df_eikou.drop('校舎名', axis=1)

    elif school_name == '浅野':
        variable.df_asano.columns = variable.successful_candidate
        df_successful_candidate = variable.df_asano.drop('校舎名', axis=1)

    elif school_name == '海城':
        variable.df_kaijou.columns = variable.successful_candidate
        df_successful_candidate = variable.df_kaijou.drop('校舎名', axis=1)

    elif school_name == '芝':
        variable.df_shiba.columns = variable.successful_candidate
        df_successful_candidate = variable.df_shiba.drop('校舎名', axis=1)

    elif school_name == '灘':
        variable.df_nada.columns = variable.successful_candidate
        df_successful_candidate = variable.df_nada.drop('校舎名', axis=1)


elif page == '女子校':
    st.markdown('### (女子校)')
    st.write('')
    st.markdown('##### ◆在籍生徒数と合格者数')
    for _n_women in n_women:
        if devi_max > int(variable2.school_name_women_devi[_n_women]['偏差値']) > devi_min:
            school_name_deviation.append(variable2.school_name_women_devi[_n_women]['学校名'])
    school_name = st.selectbox('志望校を選択してください。',school_name_deviation)
    button = st.button('グラフの表示')

    if school_name == '桜蔭':
        variable.df_ouin.columns = variable.successful_candidate
        df_successful_candidate = variable.df_ouin.drop('校舎名', axis=1)

    elif school_name == 'JG':
        variable.df_joshigaku.columns = variable.successful_candidate
        df_successful_candidate = variable.df_joshigaku.drop('校舎名', axis=1)

    elif school_name == '雙葉':
        variable.df_futaba.columns = variable.successful_candidate
        df_successful_candidate = variable.df_futaba.drop('校舎名', axis=1)

    elif school_name == '豊島岡':
        variable.df_toshimagaoka.columns = variable.successful_candidate
        df_successful_candidate = variable.df_toshimagaoka.drop('校舎名', axis=1)

    elif school_name == 'フェリス':
        variable.df_ferisu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_ferisu.drop('校舎名', axis=1)

    elif school_name == '白百合':
        variable.df_shirayuri.columns = variable.successful_candidate
        df_successful_candidate = variable.df_shirayuri.drop('校舎名', axis=1)

    elif school_name == '学習院女':
        variable.df_gakujo.columns = variable.successful_candidate
        df_successful_candidate = variable.df_gakujo.drop('校舎名', axis=1)

    elif school_name == '洗足':
        variable.df_senzoku.columns = variable.successful_candidate
        df_successful_candidate = variable.df_senzoku.drop('校舎名', axis=1)

    elif school_name == '吉祥女':
        variable.df_kichijo.columns = variable.successful_candidate
        df_successful_candidate = variable.df_kichijo.drop('校舎名', axis=1)

    elif school_name == '鷗友':
        variable.df_ohyu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_ohyu.drop('校舎名', axis=1)

    elif school_name == '浦和':
        variable.df_urawa.columns = variable.successful_candidate
        df_successful_candidate = variable.df_urawa.drop('校舎名', axis=1)


elif page == '共学校(男子偏差値)':
    st.markdown('### (共学校)')
    st.write('')
    st.markdown('##### ◆在籍生徒数と合格者数')
    for _n_co in n_co:
        if devi_max > int(variable2.school_name_co_devi[_n_co]['偏差値']) > devi_min:
            school_name_deviation.append(variable2.school_name_co_devi[_n_co]['学校名'])
    school_name = st.selectbox('志望校を選択してください。',school_name_deviation)
    button = st.button('グラフの表示')

    if school_name == '渋幕':
        variable.df_shibumaku.columns = variable.successful_candidate
        df_successful_candidate = variable.df_shibumaku.drop('校舎名', axis=1)

    elif school_name == '渋渋':
        variable.df_shibushibu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_shibushibu.drop('校舎名', axis=1)

    elif school_name == '広尾':
        variable.df_hiroo.columns = variable.successful_candidate
        df_successful_candidate = variable.df_hiroo.drop('校舎名', axis=1)

    elif school_name == '慶湘':
        variable.df_keisho.columns = variable.successful_candidate
        df_successful_candidate = variable.df_keisho.drop('校舎名', axis=1)

    elif school_name == '慶中':
        variable.df_keichu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_keichu.drop('校舎名', axis=1)

    elif school_name == '早実':
        variable.df_soujitsu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_soujitsu.drop('校舎名', axis=1)

    elif school_name == '筑附':
        variable.df_tsukufu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_tsukufu.drop('校舎名', axis=1)

    elif school_name == '青山':
        variable.df_aoyama.columns = variable.successful_candidate
        df_successful_candidate = variable.df_aoyama.drop('校舎名', axis=1)

    elif school_name == '明明':
        variable.df_meimei.columns = variable.successful_candidate
        df_successful_candidate = variable.df_meimei.drop('校舎名', axis=1)


elif page == '共学校(女子偏差値)':
    st.markdown('### (共学校)')
    st.write('')
    st.markdown('##### ◆在籍生徒数と合格者数')
    for _n_co in n_co:
        if devi_max > int(variable2.school_name_co_devi2[_n_co]['偏差値']) > devi_min:
            school_name_deviation.append(variable2.school_name_co_devi2[_n_co]['学校名'])
    school_name = st.selectbox('志望校を選択してください。',school_name_deviation)
    button = st.button('グラフの表示')

    if school_name == '渋幕':
        variable.df_shibumaku.columns = variable.successful_candidate
        df_successful_candidate = variable.df_shibumaku.drop('校舎名', axis=1)

    elif school_name == '渋渋':
        variable.df_shibushibu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_shibushibu.drop('校舎名', axis=1)

    elif school_name == '広尾':
        variable.df_hiroo.columns = variable.successful_candidate
        df_successful_candidate = variable.df_hiroo.drop('校舎名', axis=1)

    elif school_name == '慶湘':
        variable.df_keisho.columns = variable.successful_candidate
        df_successful_candidate = variable.df_keisho.drop('校舎名', axis=1)

    elif school_name == '慶中':
        variable.df_keichu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_keichu.drop('校舎名', axis=1)

    elif school_name == '早実':
        variable.df_soujitsu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_soujitsu.drop('校舎名', axis=1)

    elif school_name == '筑附':
        variable.df_tsukufu.columns = variable.successful_candidate
        df_successful_candidate = variable.df_tsukufu.drop('校舎名', axis=1)

    elif school_name == '青山':
        variable.df_aoyama.columns = variable.successful_candidate
        df_successful_candidate = variable.df_aoyama.drop('校舎名', axis=1)

    elif school_name == '明明':
        variable.df_meimei.columns = variable.successful_candidate
        df_successful_candidate = variable.df_meimei.drop('校舎名', axis=1)



################################# ボタンクリックでグラフの表示 ##################################

if button:
    variable.df_enroll.columns = variable.enrollment
    df_concat = pd.concat([variable.df_enroll, df_successful_candidate], axis=1)
    df_concat = pd.melt(df_concat, id_vars=['校舎名'])
    df_concat = df_concat.rename(columns={'variable':'usage_guide', 'value':'該当者数'})
    chart = (
        alt.Chart(df_concat)
        .mark_bar(opacity=0.8, clip=True)
        .encode(
            x='校舎名',
            y=alt.Y('該当者数:Q', stack=None),
            color=alt.Color('usage_guide', scale=alt.Scale(domain=variable.usage_guide, range=["blue", "red"]))
        )
    )
    st.altair_chart(chart, use_container_width=True)


st.write('')
st.write('')
st.write('')


if page == '男子校':
    st.markdown('##### ◆トップ校群の合格率')
    button2 = st.button('合格率を表示')
    if button2:
        indicate_line_chart_men()

elif page == '女子校':
    st.markdown('##### ◆トップ校群の合格率')
    button2 = st.button('合格率を表示')
    if button2:
        indicate_line_chart_women()