import streamlit as st
import pandas as pd
import altair as alt


# SAPIXの公開データをcsvで取得（元データはスプレッドシート）し、DataFrameへ格納
data = pd.read_csv("sapi_2022.csv")
df = pd.DataFrame(data)


################# 変数定義 #################

# 表のカラム
enrollment=['校舎名','在籍者数']
successful_candidate=['校舎名','合格者数']
variable = ['在籍者数','合格者数']

# 学校の種類
school_name_men = ['筑駒', '開成', '麻布', '駒東', '武蔵', '慶普', '早稲田', '早大学院','聖光', '栄光', '浅野', '海城', '芝', '灘']
school_name_women = ['桜蔭', 'JG', '雙葉', '豊島岡', 'フェリス', '白百合', '学習院女', '洗足', '吉祥女', '鷗友','浦和']
school_name_coeducation = ['渋幕', '渋渋', '広尾', '慶湘',' 慶中', '早実', '筑附','青山', '明明']

# 在籍者数用と合格者数用にデータをピックアップする
df_enroll = df.loc[5:48, ["実績入力以外の編集禁止","在籍"]]

# 男子校
df_tsukukoma = df.loc[5:48, ["実績入力以外の編集禁止", "筑駒"]]
df_kaisei = df.loc[5:48, ["実績入力以外の編集禁止", "開成"]]
df_azabu = df.loc[5:48, ["実績入力以外の編集禁止", "麻布"]]
df_komatou = df.loc[5:48, ["実績入力以外の編集禁止", "駒東"]]
df_musashi = df.loc[5:48, ["実績入力以外の編集禁止", "武蔵"]]
# df_keifu = df.loc[5:48, ["実績入力以外の編集禁止", "慶普"]] 列名がなくて取得不可
df_waseda = df.loc[5:48, ["実績入力以外の編集禁止", "早稲田"]]
df_wasegaku = df.loc[5:48, ["実績入力以外の編集禁止", "早大学院"]]
df_seikou = df.loc[5:48, ["実績入力以外の編集禁止", "聖光"]]
df_eikou = df.loc[5:48, ["実績入力以外の編集禁止", "栄光"]]
df_asano = df.loc[5:48, ["実績入力以外の編集禁止", "浅野"]]
df_kaijou = df.loc[5:48, ["実績入力以外の編集禁止", "海城"]]
df_shiba = df.loc[5:48, ["実績入力以外の編集禁止", "芝"]]
df_nada = df.loc[5:48, ["実績入力以外の編集禁止", "灘"]]

# 女子校
df_ouin = df.loc[5:48, ["実績入力以外の編集禁止", "桜蔭"]]
df_joshigaku = df.loc[5:48, ["実績入力以外の編集禁止", "JG"]]
df_futaba = df.loc[5:48, ["実績入力以外の編集禁止", "雙葉"]]
df_toshimagaoka = df.loc[5:48, ["実績入力以外の編集禁止", "豊島岡"]]
df_ferisu = df.loc[5:48, ["実績入力以外の編集禁止", "フェリス"]]
df_shirayuri = df.loc[5:48, ["実績入力以外の編集禁止", "白百合"]]
df_gakujo = df.loc[5:48, ["実績入力以外の編集禁止", "学習院女"]]
df_senzoku = df.loc[5:48, ["実績入力以外の編集禁止", "洗足"]]
df_kichijo = df.loc[5:48, ["実績入力以外の編集禁止", "吉祥女"]]
df_ohyu = df.loc[5:48, ["実績入力以外の編集禁止", "鷗友"]]
# df_urawa = df.loc[5:48, ["実績入力以外の編集禁止", "浦和"]] 列名がなくて取得不可

# 共学校
df_shibumaku = df.loc[5:48, ["実績入力以外の編集禁止", "渋幕"]]
df_shibushibu = df.loc[5:48, ["実績入力以外の編集禁止", "渋渋"]]
df_hiroo = df.loc[5:48, ["実績入力以外の編集禁止", "広尾"]]
df_keisho = df.loc[5:48, ["実績入力以外の編集禁止", "慶湘"]]
df_keichu = df.loc[5:48, ["実績入力以外の編集禁止", "慶中"]]
df_soujitsu = df.loc[5:48, ["実績入力以外の編集禁止", "早実"]]
df_tsukufu = df.loc[5:48, ["実績入力以外の編集禁止", "筑附"]]
df_aoyama = df.loc[5:48, ["実績入力以外の編集禁止", "青山"]]
df_meimei = df.loc[5:48, ["実績入力以外の編集禁止", "明明"]]



################# 学校の選択 #################

page = st.sidebar.selectbox('男子校・女子校・共学校を選んでください。',['男子校', '女子校', '共学校'])

if page == '男子校':
    st.title('校舎別合格者情報(男子校)')
    st.write('◆学校名を選択してグラフを表示')
    school_name = st.selectbox('志望校を選択してください。',school_name_men)
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

    # 列名がなくて取得不可
    elif school_name == '慶普':
        st.write('')
    #     df_keifu.columns = successful_candidate
    #     df_successful_candidate = df_keifu.drop('校舎名', axis=1)
    
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
    school_name = st.selectbox('志望校を選択してください。',school_name_women)
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
        st.write('')
        # df_urawa.columns = successful_candidate
        # df_successful_candidate = df_urawa.drop('校舎名', axis=1)



elif page == '共学校':
    st.title('校舎別合格者情報(共学校)')
    st.write('◆学校名を選択してグラフを表示')
    school_name = st.selectbox('志望校を選択してください。',school_name_coeducation)
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



################# ボタンクリックでグラフの表示 #################


if button:
    st.write(f'{school_name}のグラフ')
    if school_name == '慶普':
        st.write('申し訳ございません。データを取得できません。')
    elif school_name == '浦和':
        st.write('申し訳ございません。データを取得できません。')
    else:
        df_enroll.columns = enrollment
        df_concat = pd.concat([df_enroll,df_successful_candidate], axis=1)
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