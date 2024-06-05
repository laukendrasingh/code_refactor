import streamlit as st
from models import OpenAIModel
import logging as log

model = OpenAIModel()

def __page_config():
    log.info('Loading page config')

    st.set_page_config(
        page_title="CODE REFACTOR | Impressico",
        page_icon="data/favicon.png",
        layout="wide",
        initial_sidebar_state="auto"
    )

    with open("data/style.css") as file:
        st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)

def render_ui():
    log.info('Start: rendering ui')

    __page_config()
    st.title('CODE REFACTOR BOT')
    st.divider()

    file = st.file_uploader(label='UPLOAD A CODE FILE',
                            type=['.java', '.js', '.py'])

    if st.button('REFACTOR'):
        if file is None:
            st.error("Upload a code file in .java, .js, or .py format")
        else:
            with st.spinner(f"Refactoring code for file '{file.name}' using language '{model.get_language(file.name)}'"):
                left_col, right_col = st.columns(2)
                with left_col:
                    original_code = file.getvalue().decode("utf-8")
                    st.header(f'**ORIGINAL CODE**')
                    st.code(original_code)
                with right_col:
                    try:
                        st.header(''':green[REFACTORED CODE]''')
                        refactored_code = model.refactor_code(file.name, original_code)
                        st.write_stream(refactored_code)
                    except Exception as ex:
                        st.error(ex)

    st.divider()
    st.markdown(''':gray[© 2024 Impressico.com, All rights reserved.]''')

    log.info('End: ui is rendered')
