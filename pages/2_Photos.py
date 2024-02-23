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

st.image('./images/James-Weldon-Bombastic-Sideye.png', width=400, caption='Picture 1')
st.image('./images/young-James-Weldon-Johnson.jpg', width=400, caption='Young James')
st.image('./images/James-Weldon-2.png', width=400, caption='Picture 2')
st.image('./images/James-Weldon-working.png', width=400, caption='James Working    ')