import streamlit as st

new_title = "<div class=\"container\">"\
            "<div class=\"text\">"\
            "<p>"\
            "<span style=\"font-family:sans-serif; color:#27B47A;font-size:45px;\"><b>Videos</b></span>"\
            "</p>"\
            "</div>"\
            "</div>"

st.markdown(new_title, unsafe_allow_html=True)

st.video('https://www.youtube.com/watch?v=d2nOk-50kXE')
st.markdown('The Creation')
st.divider()
st.video('https://www.youtube.com/watch?v=HEbsxJXTHoo')
st.markdown('Lift Every Voice and Sing')
st.divider()
st.video('https://www.youtube.com/watch?v=VGaTy3jF4uc')
st.markdown('History of James Weldon Johnson')