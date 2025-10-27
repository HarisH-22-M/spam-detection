import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Sidebar
with st.sidebar:
    st.title("🎈 My App Sidebar")
    st.header("Navigation")
    page = st.radio("Go to", ["Home", "Data Analysis", "Settings"])
    
    st.header("About")
    st.info("This is a basic Streamlit app template!")

# Main content area
if page == "Home":
    st.title("Welcome to My Streamlit App! 🎉")
    st.subheader("Basic UI Components Demo")
    
    # Columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Input Features")
        name = st.text_input("Enter your name")
        age = st.slider("Select age", 0, 100, 25)
        color = st.color_picker("Choose a color")
        
    with col2:
        st.header("Results")
        if name:
            st.success(f"Hello {name}!")
        st.metric("Your Age", age)
        st.write("Selected color:", color)
    
    # Expander
    with st.expander("Show Code"):
        st.code("""
        st.text_input("Enter your name")
        st.slider("Select age", 0, 100, 25)
        """)

elif page == "Data Analysis":
    st.title("📊 Data Analysis")
    
    # File upload
    uploaded_file = st.file_uploader("Upload CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.subheader("Data Preview")
        st.dataframe(df.head())
        
        st.subheader("Data Statistics")
        st.write(df.describe())
        
        # Visualization
        st.subheader("Visualization")
        x_col = st.selectbox("X-axis", df.columns)
        y_col = st.selectbox("Y-axis", df.columns)
        st.line_chart(df[[x_col, y_col]])

elif page == "Settings":
    st.title("⚙️ Settings")
    
    # Different input types
    st.subheader("App Settings")
    theme = st.selectbox("Theme", ["Light", "Dark", "System"])
    notifications = st.toggle("Enable Notifications")
    precision = st.select_slider("Precision", options=["Low", "Medium", "High"])
    
    # Buttons
    if st.button("Save Settings"):
        st.success("Settings saved successfully!")
    
    # Download button
    st.download_button(
        label="Download Config",
        data="sample config content",
        file_name="config.txt"
    )

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")