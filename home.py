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

# Display the custom title
st.markdown(new_title, unsafe_allow_html=True)   

# Image and caption
col1, _ = st.columns([1, 2])
with col1:
    st.image("images/james-weldon-johnson.jpg", width=435, caption='James Weldon Johnson')