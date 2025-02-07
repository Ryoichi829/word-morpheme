# 形態素解析
import streamlit as st
from janome.tokenizer import Tokenizer
import pandas as pd

st.title("単語分割アプリ")

text = st.text_area("文章を入力してください。", "昨日インスタに写真をアップした。")

if text and st.button("単語を分割する"):
    tokenizer = Tokenizer()
    tokens = [token.surface for token in tokenizer.tokenize(text)]
    st.write('　 '.join(tokens))

if text and st.button("品詞も調べる"):
    tokenizer = Tokenizer()
    tokens = [token.surface + '　' for token in tokenizer.tokenize(text)]
    tokens_hinshi = [token.part_of_speech.split(',')[0] + '　' for token in tokenizer.tokenize(text)]
    data = {'単語　':tokens, '品詞　':tokens_hinshi}
    df = pd.DataFrame(data)
    st.dataframe(df)

if text and st.button("読みも調べる"):
    tokenizer = Tokenizer()
    tokens = [token.surface + '　' for token in tokenizer.tokenize(text)]
    tokens_hinshi = [token.part_of_speech.split(',')[0] + '　' for token in tokenizer.tokenize(text)]
    tokens_yomi = [token.reading + '　' for token in tokenizer.tokenize(text)]
    data = {'単語　':tokens, '品詞　':tokens_hinshi, '読み　　':tokens_yomi}
    df = pd.DataFrame(data)
    st.dataframe(df)

