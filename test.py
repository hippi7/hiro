import streamlit as st
import pandas as pd
import numpy as np

# アプリケーションのタイトル
st.title("Streamlit サンプルアプリ")

# --------------------
# 1. テキスト入力と表示
# --------------------

st.header("1. 自己紹介")
user_name = st.text_input("あなたの名前を入力してください:", "名無しさん")

if user_name:
    st.write(f"こんにちは、**{user_name}** さん！")
    st.write("Streamlitへようこそ！")

# --------------------
# 2. スライダーと数値表示
# --------------------

st.header("2. スライダーで値を調整")
age = st.slider("あなたの年齢を選択してください:", 0, 100, 30)
st.write(f"あなたの年齢は **{age}** 歳です。")

# --------------------
# 3. チェックボックスで表示/非表示を切り替え
# --------------------

st.header("3. コンテンツの表示/非表示")
show_details = st.checkbox("詳細情報を表示する")

if show_details:
    st.write("これはチェックボックスがオンのときに表示される詳細情報です。")
    st.info("💡 ヒント: チェックボックスは、オプションの機能や情報を表示するのに便利です。")
else:
    st.write("詳細情報を表示するには、上のチェックボックスをオンにしてください。")

# --------------------
# 4. セレクトボックスと選択肢
# --------------------

st.header("4. お好きなフルーツを選んでください")
fruits = ["りんご", "バナナ", "オレンジ", "ぶどう", "その他"]
selected_fruit = st.selectbox("お好きなフルーツを選択:", fruits)

st.write(f"あなたが選んだフルーツは: **{selected_fruit}** です。")

# --------------------
# 5. 簡単なデータフレームとチャート
# --------------------

st.header("5. データ可視化の例")
st.write("ランダムなデータを使った棒グラフを表示します。")

# ランダムなデータフレームを生成
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# 棒グラフを表示
st.bar_chart(chart_data)

st.write("上のグラフは、`st.bar_chart()` 関数を使って簡単に描画できます。")

# --------------------
# 6. サイドバーの活用
# --------------------

st.sidebar.header("サイドバー")
st.sidebar.write("これはサイドバーに表示されるコンテンツです。")
st.sidebar.button("サイドバーのボタン")

# --------------------
# フッター
# --------------------

st.markdown("---")
st.markdown("このアプリはStreamlitの基本的な機能を紹介するために作成されました。")
st.markdown("© 2025 Streamlit サンプル")