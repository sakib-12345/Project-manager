import streamlit as st

st.set_page_config(page_title="Link Manager", layout="wide", page_icon="🔗")


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.header("Link Manager", divider='rainbow')
st.write("")
st.write("")
st.write("")
st.write("")


def social_media_links(image_url, link_url, platform_name):
    st.markdown(
    f"""
    <style>
    .round-img {{
        width: 100px;
        height: 100px;
        object-fit: cover;
        transition: 0.2s;
    }}
    .round-img:hover {{
        transform: scale(1.1);
    }}
    
    </style>

    <div class="about-box-dark" style="text-align: center;">
    <a href={link_url} target="_blank">
        <img src={image_url} class="round-img">
    </a>  
    </div>
    """,
    unsafe_allow_html=True
)

    st.markdown(
        f'<div style="text-align: center; color: grey;">{platform_name}</div>',
        unsafe_allow_html=True

       )

coll1, coll2= st.columns([2, 1])
with coll1:
    st.markdown("""
# 👋 Hey, I’m Sakib Hossain Tahmid  

### 🚀 About Me  
- 🌱 Currently learning: **Machine Learning, Python, and Streamlit**  
- 💻 Building: cool ML apps + no-code tools with Python  
- 🎯 Goal: Making ML projects & build a solid portfolio  


---

### 🛠️ Tech Stack  

#### 🔹 Languages  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=white)
 ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)



#### 🔹 ML / AI  
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-0C4B33?style=for-the-badge&logo=plotly&logoColor=white)  ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)


#### 🔹 Web Apps  
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)  

#### 🔹 Database
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-34A853?style=for-the-badge&logo=googlesheets&logoColor=white)

#### 🔹 Tools  
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![VS Code](https://img.shields.io/badge/VS%20Code-0078d7?style=for-the-badge&logo=visual-studio-code&logoColor=white) ![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=black)  ![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)



""")

with coll2:
    with st.expander("Quick View", expanded=True):
        st.markdown("""
[TOP](#link-manager)<br>
[Social Links](#social-links)<br>
[My Projects](#my-projects)
""", unsafe_allow_html=True)
     



c100, c110, c120 = st.columns([1, 2, 1])
with c110:
   
    st.write("")
    st.write("")
    st.header("Social Links", divider='rainbow')


c1, col0, col1, col2, col3, col4, c2 = st.columns([2.5, 1, 1, 1, 1, 1, 2.5])
with col0:
    with st.container(height=150):
        social_media_links("https://github.com/sakib-12345/Project-manager/blob/main/facebook.png?raw=true", "https://www.facebook.com/sakibhossain.tahmid", "Facebook")

with col1:
    st.write("")
    st.write("")
    with st.container(height=150):
        social_media_links("https://github.com/sakib-12345/Project-manager/blob/main/email.png?raw=true", "https://mail.google.com/mail/u/0/#inbox", "Email")
   
        
with col2:
    
    with st.container(height=150):
        social_media_links("https://github.com/sakib-12345/Project-manager/blob/main/instagram.png?raw=true", "https://www.instagram.com/_sakib_000001", "Instagram")
       
 
with col3:
    st.write("")
    st.write("")
    with st.container(height=150):
        social_media_links("https://github.com/sakib-12345/Project-manager/blob/main/x.png?raw=true", "https://x.com/_sakib_00000001", "X (Twitter)")
   
with col4:
   
    with st.container(height=150):
        social_media_links("https://github.com/sakib-12345/Project-manager/blob/main/github.png?raw=true", "https://github.com/sakib-12345", "Github")



c10, c11, c12 = st.columns([1, 2, 1])
with c11:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.header("My Projects", divider='rainbow')

c3, col5, col6, col7, col8, col9, c4 = st.columns([2.5, 1, 1, 1, 1, 1, 2.5])

with col5:
    st.write("")
    st.write("")
    with st.container(height=150):
        social_media_links("https://github.com/sakib-12345/No-Code-ML-WEBapp/blob/main/my_icon.png?raw=true", "https://nocodemlsakib.streamlit.app/", "No-Code-ML")
with col6:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    with st.container(height=150):
        social_media_links("https://github.com/sakib-12345/ML-comperision-WEBapp/blob/main/web_icon.png?raw=true", "https://ml-app-sakib.streamlit.app/", "ML-Comparison")
          

with col7:
    st.write("")
    st.write("")
    with st.container(height=150):
        social_media_links("https://github.com/sakib-12345/chat-app-with-Firebase/blob/main/App_icon.png?raw=true", "https://chat-firebase.streamlit.app/", "Chat-firebase")
with col8:   
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    with st.container(height=150):
        social_media_links("https://github.com/sakib-12345/chat-app-with-google-sheet/blob/main/icon.png?raw=true", "https://chat-app-sakib12345.streamlit.app/", "Chat-sheets")
    
with col9:
    st.write("")
    st.write("")
    with st.container(height=150):

        social_media_links("https://github.com/sakib-12345/private-qrcode-gen-and-scan/blob/main/qr_icon.png?raw=true", "https://my-qrcode-app-sakib.streamlit.app/", "Qr-code")
