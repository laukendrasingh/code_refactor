import streamlit as st
from models import OpenAIModel, ChatGptModel
import logging as log

openai_model = OpenAIModel()
gpt_model = ChatGptModel()


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

    if st.button('REFACTOR: meta-llama'):
        __refactor_code(openai_model, file, True)
    if st.button('REFACTOR: gpt-3.5-turbo'):
        __refactor_code(gpt_model, file, False)

    st.divider()
    st.markdown(''':gray[© 2024 Impressico.com, All rights reserved.]''')

    log.info('End: ui is rendered')


def __refactor_code(model, file, has_stream_result: bool):
    if file is None:
        st.error("Upload a code file in .java, .js, or .py format")
    else:
        with st.spinner(f"Refactoring..."):
            st.write(
                f"**LANGUAGE:** {model.get_language(file.name)} & **MODEL:** {model.get_model()}")
            left_col, right_col = st.columns(2)
            with left_col:
                original_code = file.getvalue().decode("utf-8")
                st.header(f'**ORIGINAL CODE**')
                st.code(original_code)
            with right_col:
                try:
                    st.header(''':green[REFACTORED CODE]''')
                    refactored_code, estimated_cost = model.refactor_code(
                        file.name, original_code)
                    if has_stream_result:
                        st.write_stream(refactored_code)
                    else:
                        st.write(refactored_code)

                    st.write(estimated_cost)
                except Exception as ex:
                    st.error(ex)
