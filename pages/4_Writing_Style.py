import streamlit as st

new_title = "<div class=\"container\">"\
            "<div class=\"text\">"\
            "<p>"\
            "<span style=\"font-family:sans-serif; color:#27B47A;font-size:45px;\"><b>Writing Style</b></span>"\
            "</p>"\
            "</div>"\
            "</div>"

st.markdown(new_title, unsafe_allow_html=True)
st.markdown("""James Weldon Johnson’s writing style is different from others. Many of his poems such as The creation, Mother Night, and Sonnet include various forms of personification and philosophy, which give more insights on how life was during his time. In addition, he also adds a huge portion of imagery in his writing which makes it easy to visualize his writing.""")
