import streamlit as st
from spacy import displacy
import en_core_web_sm
from newspaper import Article

nlp = en_core_web_sm.load() #English Language Model

def analyze_text(text):
    paragraph = nlp(text)
    result = displacy.render(paragraph, style='ent')
    st.markdown(result, unsafe_allow_html=True)


def analyze_url(url):
    article = Article(url)
    article.download()
    article.parse()
    analyze_text(article.text)

st.header("Label Data using Spacy")


input_text = st.text_area("Enter a Paragraph or URL")

if st.button("Analyse"):
    if input_text.strip() == "":
        st.write("Please enter some text or a URL to analyze.")

    elif input_text.startswith("http") or input_text.startswith("www"):
        analyze_url(input_text)
        
    else:
        analyze_text(input_text)