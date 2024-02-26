import streamlit as st

# Custom styled title
new_title = "<div class=\"container\">"\
            "<div class=\"text\">"\
            "<p>"\
            "<span style=\"font-family:sans-serif; color:#27B47A;font-size:60px;\"><b>James</b></span>"\
            "<span style=\"font-family:sans-serif; color:#27B47A;font-size:60px;\"><b> Weldon Johnson</b></span>"\
            "</p>"\
            "</div>"\
            "</div>"

st.markdown(new_title, unsafe_allow_html=True)
st.markdown("By Sid and Avyan, Room 328")