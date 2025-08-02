import random
import streamlit as st

# タイトル
st.title("Silent Poem Generator")
st.write("中身を伏せたまま、非命題的な詩を生成します。")

# 入力欄
word = st.text_input("あなたの心にある言葉を一つください：", "")

# 詩のテンプレート（構文記号は伏せたまま）
TEMPLATES = [
    ["{word}が届く前に", "言葉は沈み", "意味は泡となって立ちのぼる", "", "記憶の淵に", "語られなかった感情が", "そっと滑り落ちた"],
    ["{word}がまだ名付けられる前", "声にならない余韻だけが", "空にしみ込んでいった", "", "光と影のあわいに", "確かにあった", "あなたの沈黙"],
    ["{word}を抱えたまま", "時間だけがすり抜けていく", "判断は保留されたまま", "", "遠くで響いた音だけが", "わたしを包んだ"],
    ["{word}に触れずに", "ただ見つめていた", "意味を与えないことが", "唯一の贈り物だった", "", "静けさの奥に", "答えなき答えがあった"]
]

# 詩の生成関数
def generate_poem(word):
    if not word:
        return []
    template = random.choice(TEMPLATES)
    return [line.format(word=word) for line in template]

# 結果表示
if word:
    poem = generate_poem(word)
    st.markdown("---")
    st.subheader("生成された詩：")
    for line in poem:
        st.write(line)
    st.markdown("---")
