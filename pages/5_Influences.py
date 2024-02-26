import streamlit as st

new_title = "<div class=\"container\">"\
            "<div class=\"text\">"\
            "<p>"\
            "<span style=\"font-family:sans-serif; color:#27B47A;font-size:45px;\"><b>Influences</b></span>"\
            "</p>"\
            "</div>"\
            "</div>"

st.markdown(new_title, unsafe_allow_html=True)
st.markdown("""James Weldon Johnson was influenced by many important poets before him, such as Walt Whitman and Robert Forest. Poets from the Harlem Renaissance used each other as inspiration and used poetry as a form of protest and hope.""")