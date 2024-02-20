import streamlit as st

# Custom styled title
new_title = "<div class=\"container\">"\
            "<div class=\"text\">"\
            "<p>"\
            "<span style=\"font-family:sans-serif; color:#27B47A;font-size:45px;\"><b>Photos</b></span>"\
            "</p>"\
            "</div>"\
            "</div>"

# Display the custom title
st.markdown(new_title, unsafe_allow_html=True)    