import streamlit as st
from PIL import Image
import os

# Set wide page layout
st.set_page_config(layout="wide")

# Sidebar with personal info
with st.sidebar:
    st.title("Gazali O. Agboola")
    uploaded_file = st.file_uploader("Upload your picture", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, width=150) # Adjust width as needed
    st.write("Greensboro, NC 27405")
    st.write("+1 (779)-777-8515")
    st.markdown(
    "[LinkedIn](https://www.linkedin.com/in/gazal-agboola-351b44b8/) | "
    "[GitHub](https://github.com/Gazmaths) | "
    "[ResearchGate](https://www.researchgate.net/profile/Gazali-Agboola) | "
    "[Google Scholar](https://scholar.google.com/citations?user=qs8xlvMAAAAJ&hl=en&authuser=1)"
    )
    st.write("Email: goagboola@aggies.ncat.edu | agboolagazal@gmail.com")
    st.write("---")

# Main content
st.title("Curriculum Vitae")
st.markdown("---")

# Profile section
st.subheader("Profile")
st.write("""
Experienced data analyst skilled in predictive, time series, and diagnostic modeling using mathematical, statistical, and machine learning techniques. Proficient in Advanced Excel, Python, R, SAS, SQL, Power BI, and Tableau. Demonstrated success in data analysis, geospatial data analysis, credit control, and strategic sales data analysis and management. I am currently seeking an internship position in data analytics, data science, and geospatial data analysis.
""")

# Education section
st.subheader("Education")
st.write("""
**North Carolina Agricultural and Technical State University**  
Greensboro, North Carolina, USA  
**PhD. — Applied Science and Technology**  
Expected Graduation: May 2026  
Data Science and Analytics Concentration  
GPA: 3.95/4.0

**University Of Ilorin**  
Ilorin, Kwara State, Nigeria  
**Master of Science — Mathematics**  
Dec. 2015  
GPA: 3.66/4.0

**University Of Ilorin**  
Ilorin, Kwara State, Nigeria  
**Bachelor of Science — Mathematics**  
July 2013  
GPA: 3.55/4.0
""")

# Work Experience section
st.subheader("Work Experience")
st.write("""
**North Carolina A&T State University**  
Greensboro, North Carolina, USA  
**Data Science Research Assistant**  
Aug. 2022 – Present  
- Developed a machine learning model that achieved 99.4% AUC-ROC in optimizing landslide susceptibility mapping.
- Created deep learning algorithms for landslide identification using computer vision techniques.
- Collaborated with stakeholders to apply data science in disaster management, utilizing knowledge graph and machine learning techniques.

**FrieslandCampina WAMCO**  
Ikeja, Lagos, Nigeria  
**Credit Control Manager**  
Aug. 2021 – Dec. 2021  
- Monitored a credit control system, achieving over 96% payment-to-invoice ratio in 2021.
- Analyzed customer credit reports and maintained overdue accounts below 18%.
- Conducted detailed sales data analyses and produced comprehensive reports for decision-making.

**FrieslandCampina WAMCO**  
Ikeja, Lagos, Nigeria  
**Credit Control Data Analyst**  
Feb. 2020 – July 2021  
- Conducted credit risk exposure analysis, leading to a 20% increase in revenue.
- Developed an Excel template to monitor customers' payment patterns.

**FrieslandCampina WAMCO**  
Ikeja, Lagos, Nigeria  
**Distributor Management System Admin**  
Jan. 2017 – Jan. 2020  
- Analyzed team KPIs to optimize operational efficiencies.
- Maintained data integrity within the Distribution Management System.

**Kingsfield College**  
Ikorodu, Lagos State, Nigeria  
**Mathematics Instructor**  
Jan. 2016 – Dec. 2016  
- Developed and implemented engaging lesson plans aligned with the high school curriculum.
- Conducted assessments and provided feedback to monitor student progress.
""")

# Skills section
st.subheader("Skills")
st.write("""
- **Soft Skills:** Strong communication, troubleshooting, problem-solving, analytical abilities, attention to detail.
- **Technical Skills:** Python, R, SAS, SQL, Advanced Excel, Tableau, Power BI, Google Looker Studio, IBM Cognos.
""")

# Relevant Courses section
st.subheader("Relevant Courses Taken")
st.write("""
- Machine Learning and Data Analytics
- Mathematical Methods
- Linear Algebra
- Deep Learning Specialization
- SQL
- Introduction to Probability Theory
- Mathematical Modeling
- Python for Data Science
- Multivariate Statistics for Engineers
- Advanced Geospatial Analysis
""")

# Projects and Research section
st.subheader("Projects and Research")
st.write("""
- Development of Edu-navigator chatbot for HBCU students using ChatGPT4.0 (HP FOWA project) (Aug. 2024 - Present)
- Landslide detection using deep learning segmentation models (Aug. 2023 – Present)
- Optimizing landslide susceptibility using machine learning (Jan. 2023 – Feb. 2024)
- Web scraping using Python BeautifulSoup (March 2024 – April 2024)
- Data analysis for disaster management using knowledge graph (Dec. 2023 – June 2024)
- Credit card anomaly detection using machine learning (Aug. 2022 – Dec. 2022)
""")

# Awards and Honors section
st.subheader("Awards and Honors")
st.write("""
- North Carolina ArcGIS Users’ Graduate Academic Excellence Award (2024)
- Thermo Fisher Scientific Innovation Challenge (First Position) (2024)
- NC Landslide Scholarship (2023)
- NOAA Scholarship (2022)
- Best NE DMS Administrator for 2019 (2019)
""")

# Certifications and Training section
st.subheader("Certifications and Training")
st.write("""
- Deep Learning Specialization by DeepLearning.AI
- Natural Language Processing in Python by Udemy
- Introduction to Cybersecurity by Codepath
- Transfer Learning for Images Using PyTorch
- Python for Data Science, AI & Development by IBM
- Databases and SQL for Data Science with Python by IBM
- Data Visualization and Dashboards with Excel and Cognos
- Essential Skill in SQL by LinkedIn Learning
""")

# Professional Organizations section
st.subheader("Professional Organizations and Memberships")
st.write("""
- Member of the International Society for Data Science and Analytics (ISDA)
- Member of the American Society for Photogrammetry and Remote Sensing (ASPRS)
- Member of the American Geospatial Union (AGU)
- North Carolina ArcGIS Users Group (NCAUG)
""")

# Leadership and Volunteer Experience section
st.subheader("Leadership, Volunteer Experience & Involvement")
st.write("""
- Volunteering at the Mentor Collective Ambassador (2023 – present)
- Volunteered as the President of ASPRS (NCAT Chapter) (2023 - present)
- Volunteered as the President of Aquinas Corp Members (2014)
- Volunteered at the National Youth Service Corps (NYSC) (2014)
- Volunteered at the Road Safety Corp Members (2014)
""")

# Footer
st.markdown("---")
st.write("Built with ❤️ using Streamlit")

