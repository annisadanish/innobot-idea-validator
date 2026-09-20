import streamlit as st

st.set_page_config(page_title="InnoBot Idea Validator", page_icon="idea")
st.title("InnoBot Idea Validator")
st.write("Enter your business idea to validate.")

idea = st.text_area("Business Idea", height=150)

if st.button("Analyze"):
    if idea.strip():
        st.success("Analysis complete!")
        st.write("SWOT for: " + idea)
        st.write("Strengths: ...")
        st.write("Weaknesses: ...")
        st.write("Opportunities: ...")
        st.write("Threats: ...")
    else:
        st.warning("Please enter a business idea first.")

