"""
app.py
======
Streamlit interactive dashboard for Pakistan Job Market Analyzer.
Provides market insights, job category prediction, skill explorer
and job trends across Pakistani cities.

Tabs:
    - Market Dashboard: Key metrics and visualizations
    - Job Category Predictor: ML-powered category prediction
    - Skill Explorer: Skill demand analysis
    - Job Trends: Filtered job listings

Usage:
    streamlit run app/app.py

Author: Husnain Maroof
GitHub: https://github.com/husnainalix77
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scraper.utils import classify_city, classify_category, extract_seniority
import scipy.sparse as sp
from sklearn.feature_extraction.text import TfidfVectorizer
import warnings
warnings.filterwarnings("ignore")

# 1. Page Configuration
st.set_page_config(
    page_title="Pakistan Job Market Analyzer",
    page_icon="🇵🇰",
    layout="wide"
)

# 2. Data and Model Loading
@st.cache_data
def load_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "cleaned_data.csv")
    df = pd.read_csv(csv_path)
    df["seniority"] = df["title"].apply(extract_seniority)
    df["category"] = df["title"].apply(classify_category)
    df["city"] = df["city"].apply(classify_city)
    return df


@st.cache_resource
def load_models():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    models_dir = os.path.join(base_dir, "models")
    
    le_city = joblib.load(os.path.join(models_dir, "le_city.pkl"))
    le_category = joblib.load(os.path.join(models_dir, "le_category.pkl"))
    lr = joblib.load(os.path.join(models_dir, "category_model.pkl"))
    tfidf = joblib.load(os.path.join(models_dir, "tfidf_vectorizer.pkl"))
    return le_city, le_category, lr, tfidf

df = load_data() # load data and models
le_city, le_category, model, tfidf = load_models()    

# 3. Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/color/96/pakistan.png", width=80)
    st.title("🇵🇰 Pakistan Job Market Analyzer")
    st.markdown("---")
    st.markdown("### 📊 Dataset Info")
    st.metric("Total Jobs", len(df))
    st.metric("Cities Covered", df["city"].nunique())
    st.metric("Job Categories", df["category"].nunique())
    st.markdown("---")
    st.markdown("**Author:** Husnain Maroof")
    st.markdown("**GitHub:** [husnainalix77](https://github.com/husnainalix77)")
    st.markdown("---")
    st.caption("Data sourced from Indeed Pakistan")
    
# 4. Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Market Dashboard",
    "🤖 Job Category Predictor", 
    "🔍 Skill Explorer",
    "📈 Job Trends"
])

# Tab 1 — Market Dashboard
with tab1:
    st.header("Pakistan Job Market - Market Dashboard")
    st.markdown("Key insights from **620 job listings** scraped from Indeed Pakistan.")
    
    # Metric row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Total Job Listings",
            value=len(df)
        )
    
    with col2:
        st.metric(
            label="Most Active City",
            value=df["city"].value_counts().index[0]
        )    
    
    with col3:
        st.metric(
            label="Top Job Category",
            value=df["category"].value_counts().index[0]
        )    
    
    # Jobs by City Bar Chart
    st.markdown("---")
    st.subheader("📍 Geographic Distribution of Job Listings")
    
    city_counts = df["city"].value_counts()
    fig, ax = plt.subplots(figsize=(10,4))
    colors = sns.color_palette("husl", len(city_counts))
    ax.bar(city_counts.index, city_counts.values, width=0.4, color=colors, edgecolor='black', linewidth=0.8)
    for i, value in enumerate(city_counts.values):
        ax.text(i, value + 2, str(value), ha='center', fontsize=11)
        
    ax.set_title("Job Distribution Across Pakistani Cities (n=620)", fontsize=14, fontweight='bold')
    ax.set_xlabel("City", fontsize=14)
    ax.set_ylabel("Frequency", fontsize=14)
    plt.tight_layout()
    st.pyplot(fig)
    st.caption("Karachi and Lahore dominate with 75% of all job listings.")
    
    # Top 10 Companies Bar Chart
    st.subheader("🏢 Most Active Employers")
    
    counts = df["company"].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10,4))
    ax.barh(counts.index, counts.values, color='steelblue')
    for i, value in enumerate(counts.values):
        ax.text(value + 0.1, i, str(value), va='center', fontsize=11)
        
    ax.set_title("Top 10 Companies by Job Listings", fontsize=14, fontweight='bold')
    ax.set_xlabel("Number of Jobs", fontsize=14)
    ax.set_ylabel("Company", fontsize=14)
    plt.tight_layout()
    st.pyplot(fig)
    st.caption("Software Engineering dominates with 24 listings.")
    
    # Jobs by Category Bar Chart
    st.subheader("💼 Job Distribution by Category")
    
    category_counts = df["category"].value_counts()
    fig, ax = plt.subplots(figsize=(10,4))
    colors = sns.color_palette("tab10", len(category_counts))
    ax.barh(category_counts.index, category_counts.values, color=colors)
    for i, value in enumerate(category_counts.values):
        ax.text(value + 0.1, i, str(value), va='center', fontsize=11)
        
    ax.set_title("Job Count Per Category", fontsize=14, fontweight='bold')
    ax.set_xlabel("Number of Jobs", fontsize=14)
    ax.set_ylabel("Job Category", fontsize=14)
    plt.tight_layout()
    st.pyplot(fig)
    st.caption("Software Engineering accounts for 61% of all listings — Pakistan's job market is heavily tech-focused.")
    

# Tab 2 — Job Category Predictor.
with tab2:
    st.header("🤖 Job Category Predictor")
    st.markdown("Enter a job title and city to predict the job category using our ML model.")
    st.markdown("---")
    
    # User inputs
    job_title = st.text_input(
        label="Enter Job Title",
        placeholder="e.g. Senior Software Engineer, Data Analyst..."
    )
    
    city = st.selectbox(
        label="Select City",
        options=["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Other"]
    )
    
    predict_btn = st.button("🔍 Predict Category")
    
    # Prediction Logic
    if predict_btn:
        if not job_title:
            st.warning("⚠️ Please enter a job title.")
        else:
            # Transform Inputs
            title_tfidf = tfidf.transform([job_title])
            city_encoded = le_city.transform([city])[0]
            seniority = extract_seniority(job_title)  
            
            # Combine features
            import scipy.sparse as sp
            other_features = sp.csr_matrix([[city_encoded, seniority]])
            X_input = sp.hstack([title_tfidf, other_features]) 
            
            # Predict
            prediction = model.predict(X_input)[0]
            probability = model.predict_proba(X_input)[0].max()
            category_name = le_category.inverse_transform([prediction])[0] 
            
            # Show result
            st.markdown("---")
            if probability >= 0.7:
                st.success(f"✅ Predicted Category: **{category_name}**")
            else:
                st.warning(f"⚠️ Predicted Category: **{category_name}** (Low confidence)")
            
            st.metric("Model Confidence", f"{probability*100:.1f}%")
    
# Tab 3 — Skill Explorer
with tab3:
    st.header("🔍 Skill Explorer")
    st.markdown("Search any skill to see which cities and companies demand it most.")
    st.markdown("---")
    
    skill = st.text_input(
        label="Enter a Skill",
        placeholder="e.g. Python, SQL, AutoCAD, React..."
    )
    
    if skill:
        # Filter jobs containing this skill in title
        filtered = df[df["title"].str.contains(skill, case=False, na=False)]
        
        if len(filtered) == 0:
            st.error(f"❌ No jobs found mentioning '{skill}'")
        else:
            st.success(f"✅ Found **{len(filtered)}** jobs mentioning '{skill}'")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📍 Demand by City")
                city_demand = filtered["city"].value_counts()
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.barh(city_demand.index, city_demand.values, 
                        color=sns.color_palette("husl", len(city_demand)))
                ax.set_xlabel("Number of Jobs")
                plt.tight_layout()
                st.pyplot(fig)
            
            with col2:
                st.subheader("🏢 Top Companies Hiring")
                company_demand = filtered["company"].value_counts().head(5)
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.barh(company_demand.index, company_demand.values,
                        color=sns.color_palette("Set2", len(company_demand)))
                ax.set_xlabel("Number of Jobs")
                plt.tight_layout()
                st.pyplot(fig)
            
            st.subheader("📋 Matching Job Listings")
            st.dataframe(
                filtered[["title", "company", "city", "category"]].reset_index(drop=True),
                use_container_width=True
            )    

# Tab 4 — Job Trends
with tab4:
    st.header("📈 Job Trends")
    st.markdown("Filter job listings by city and category to explore the market.")
    st.markdown("---")
    
    # Filters
    col1, col2 = st.columns(2)
    
    with col1:
        selected_city = st.selectbox(
            "Filter by City",
            options=["All"] + list(df["city"].unique())
        )
    
    with col2:
        selected_category = st.selectbox(
            "Filter by Category",
            options=["All"] + list(df["category"].unique())
        )
    
    # Apply filters
    filtered_df = df.copy()
    
    if selected_city != "All":
        filtered_df = filtered_df[filtered_df["city"] == selected_city]
    
    if selected_category != "All":
        filtered_df = filtered_df[filtered_df["category"] == selected_category]
    
    # Summary metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Jobs Found", len(filtered_df))
    with col2:
        st.metric("Companies", filtered_df["company"].nunique())
    with col3:
        st.metric("Cities", filtered_df["city"].nunique())
    
    st.markdown("---")
    
    # Results table
    st.subheader(f"📋 Job Listings ({len(filtered_df)} results)")
    st.dataframe(
        filtered_df[["title", "company", "city", "category"]].reset_index(drop=True),
        use_container_width=True
    )            