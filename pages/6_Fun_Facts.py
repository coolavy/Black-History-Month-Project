import streamlit as st

new_title = "<div class=\"container\">"\
            "<div class=\"text\">"\
            "<p>"\
            "<span style=\"font-family:sans-serif; color:#27B47A;font-size:45px;\"><b>Fun Facts</b></span>"\
            "</p>"\
            "</div>"\
            "</div>"

st.markdown(new_title, unsafe_allow_html=True)
st.markdown(
"""
- James Weldon Johnson was the first African American to pass the Florida Bar.
- James Weldon Johnson was the first African American professor in NYU.
- James Weldon Johnson was a supporter of the Republican Party and campaigned for the party in the 1920 presidential election.
- James Weldon Johnson was against FDR’s New Deal.
- James Weldon Johnson plays several instruments, including the piano and violin.
- James Weldon Johnson played on several basketball teams in college.
"""
)