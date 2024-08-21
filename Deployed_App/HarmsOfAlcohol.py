import streamlit as st
import base64

selected_button = "Introduction"


# # Function to convert image to base64
# def get_base64_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode()
    
#pathname = "https://github.com/bhargav-yoga/The_Harms_of_Alcohol_on_Society_and_Health/Deployed_App/"
pathname = "/Users/pranavsharma/Desktop/NEU/Bhargav/"

#side_logo_path = f"{pathname}FinalSideLogo.jpeg"

#converted_side_Logo = get_base64_image(side_logo_path)

st.sidebar.image(f"{pathname}FinalMainLogo.jpg")

#logo_base64 = get_base64_image(side_logo_path)
st.markdown(
    """
    <style>
    .main-header {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 45px;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        padding: 20px 0;
        background-color: #ecf0f1;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .main-header img {
        margin-right: 20px;
        width: 120px; /* Adjusted width for better visibility */
        height: auto;
    }
    </style>
    <div class="main-header">
        Harms of Alcohol on Society
    </div>
    """,
    unsafe_allow_html=True
)

# <img src="data:image/png;base64,{side_logo_path}" alt="logo"> 

# Define custom button style
st.sidebar.markdown(
    """
    <style>
    .stButton button {
        font-size: 18px;
        padding: 8px 20px;
        margin: 8px 0;
        width: 100%; /* Ensures all buttons have the same width */
        border-radius: 20px;
        border: none;
        background-color: #283b56; /* A modern green color */
        color: white;
        box-shadow: 0 8px 8px rgba(0, 0, 0, 0.2); /* Soft shadow for depth */
        transition: background-color 0.3s ease, transform 0.3s ease; /* Smooth transitions */
    }
    
    .stButton button:hover {
        background-color: #203046; /* Slightly darker green on hover */
        transform: translateY(-2px); /* Lift effect on hover */
    }
    
    .stButton button:active {
        background-color: #3e8e41; /* Even darker green on click */
        transform: translateY(0); /* Return to original position */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create buttons
if st.sidebar.button(" Introduction "):
    selected_button = "Introduction"

if st.sidebar.button(" Exploratory Data Analysis (EDA)"):
    selected_button = "EDA"

if st.sidebar.button("Principal Component Analysis (PCA)"):
    selected_button = "Principal Component Analysis (PCA)"

if st.sidebar.button("Anomaly Detection"):
    selected_button = "Anomaly Detection"

if st.sidebar.button("Clustering Alcohol consumption"):
    selected_button = "Clustering Alcohol consumption"

if st.sidebar.button("Machine Learning Models"):
    selected_button = "Machine Learning Models"


# Handle each button selection
if selected_button == "Introduction":
    st.header("About Dataset")
    st.write("""
        **Project Description:**
        The primary goal of this project is to analyze the harms of alcohol on society and health using machine learning and data analysis techniques. The specific objectives are:
        To identify patterns and trends in alcohol consumption and its health impacts.
        To develop predictive models that can forecast alcohol consumption rates and associated health risks.
        To provide insights that can inform public health policies and interventions aimed at reducing the negative impacts of alcohol consumption.
        Problem Statement
        Alcohol consumption is a major public health concern, contributing to a range of social and health issues, including addiction, chronic diseases, accidents, and economic costs. Understanding and predicting alcohol consumption patterns and their health impacts is crucial for developing effective public health strategies. This project seeks to leverage machine learning techniques to analyze alcohol-related data and provide actionable insights for policymakers and healthcare providers.
        
        **Data Source:**
        The data used is an open-source dataset from WHO and CDC for our project analysis. For more details, you can access the datasets here:

        **WHO**: https://www.who.int/data/gho/data/themes/global-information-system-on-alcohol-and-health
        **CDC**: https://www.cdc.gov/alcohol/data-stats.htm

        """)
    
elif selected_button == "EDA":
    st.header("Exploratory Data Analysis (EDA)")                                                                                                                                                          
    tab1, tab2, tab3, tab4 = st.tabs(["**Alcohol Consuption Over time By Country**", "**Alcohol Consumption value distribution**", "**Consumption amongst countries**", "**What's Happening Here?**"])

    
    # Create tabs for Weather and Time Impact   
    with tab1:
        st.image(f"{pathname}EDA1.jpeg")
        
    with tab2:
        st.image(f"{pathname}EDA2.jpeg")
        
    
    with tab3:
        st.image(f"{pathname}EDA3.jpeg")
    
    with tab4:
        st.write("""
        1. **Distribution Analysis**
        **Objective:** To understand the overall distribution of alcohol consumption values across all data points.
        **Visualization:** A histogram with a KDE (Kernel Density Estimate) overlay.
        **Explanation:**
        
        The histogram with KDE shows the distribution of alcohol consumption values across different countries and years. The plot reveals a heavily right-skewed distribution, where the majority of alcohol consumption values are clustered at the lower end of the spectrum, with a long tail extending towards higher values.
        This suggests that in most instances, alcohol consumption is relatively low, with only a few cases reporting very high consumption values.

        2. **Time Series Analysis**
        **Objective:** To explore how alcohol consumption has changed over time across different countries.
        **Visualization:** A line plot showing alcohol consumption over time for each country.
        **Explanation:**
        
        The line plot visualizes alcohol consumption trends over time for different countries, each represented by a different colored line.
        The plot highlights that from 1960 to around 2000, many countries experienced gradual increases in alcohol consumption. However, post-2000, there is a mix of trends: some countries show a decline, while others continue to rise or stabilize.
        This type of visualization is particularly useful for identifying periods of significant change in alcohol consumption that might correlate with historical events, policy changes, or social trends.

        3. **Country-Specific Analysis**
        **Objective:** To drill down into individual countries and analyze their alcohol consumption trends in detail.
        **Approach:** Plotting time series for specific countries.
        **Explanation:**
        
        By focusing on specific countries, we can better understand the factors driving alcohol consumption trends within each region.
        For example, by plotting the alcohol consumption for Spain (ESP), we could see a clearer picture of how consumption patterns evolved in Spain over the years. Similar analysis can be done for other countries like the USA, UK, or Russia, providing insights into regional behaviors and the impact of local policies or cultural factors.

        **Summary**
        - The distribution analysis shows that most alcohol consumption values are low, with a few outliers on the higher end.
        - The time series analysis reveals diverse trends over time, with some countries increasing their alcohol consumption, while others show a decline or stabilization.
        - Country-specific analyses allow for a more granular understanding of alcohol consumption patterns, helping identify unique trends or anomalies.
        - These steps in the EDA help form the basis for deeper analysis, such as identifying factors influencing these trends or modeling future alcohol consumption patterns based on historical data.    
        """)


elif selected_button == "Principal Component Analysis (PCA)":
    st.header("Principal Component Analysis (PCA)")

    # Create tabs for Weather and Time Impact
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["**PCA**","**Corelation Matrix**", " **t-distributed Stochastic Neighbor Embedding** ", "**Uniform Manifold Approximation and Projection**", " **💡 Learn More💡** "])

    with tab1:
        st.image(f"{pathname}PCA1.jpeg", caption="PCA")
    with tab2:
        st.image(f"{pathname}PCA4.jpeg", caption = "Corelation Matrix")
    with tab3:
        st.image(f"{pathname}PCA2.jpeg", caption="t-distributed Stochastic Neighbor Embedding")

    with tab4:
        st.image(f"{pathname}PCA3.jpeg", caption="Uniform Manifold Approximation and Projection")
    with tab5:
        st.write("""
            ### 1. **Correlation Matrix Heatmap**: 
            **Explanation**: The correlation matrix helps identify relationships between different variables related to alcohol consumption, such as health outcomes, economic factors, and social indicators. For example, you might find strong correlations between alcohol consumption rates and certain health issues like liver disease, or economic burdens like healthcare costs. This can help pinpoint which variables are most closely linked to the societal harms of alcohol.
            ### 2. **PCA (Principal Component Analysis)**:
            **Explanation**: PCA reduces the complexity of the dataset by identifying the principal components that capture the most variance. In the context of alcohol's societal harms, PCA could reveal underlying factors (e.g., economic stress, public health crises) that explain the most variance in alcohol-related harm data. This can simplify the data and help focus on the most critical factors contributing to societal harm.
            ### 3. **t-SNE (t-distributed Stochastic Neighbor Embedding)**:
            **Explanation**: t-SNE visualizes high-dimensional data, making it easier to see clusters or patterns related to alcohol harms. For instance, you might visualize how different regions or demographic groups cluster based on the severity of alcohol-related harms. This can highlight areas or populations that are particularly affected by alcohol consumption, guiding targeted interventions.
            ### 4. **UMAP (Uniform Manifold Approximation and Projection)**:
            **Explanation**: UMAP, similar to t-SNE, can help in visualizing the clustering of different data points, such as regions, age groups, or socioeconomic statuses, based on the extent of alcohol-related harm. This could help identify vulnerable groups or areas where alcohol-related issues are more prevalent, enabling more effective policy-making.     
            """)

elif selected_button == "Anomaly Detection":
    st.header("Anomaly Detection")

    # Create tabs for Clustering
    tab1, tab2 = st.tabs(["**Anomaly Detection Results**", "**💡 What's Happening Here? 💡** "])

    with tab1:
        st.image(f"{pathname}Ano.jpeg", caption="Detection Results")

    with tab2:
        st.write("""
            ### 1. **Isolation Forest and One-Class SVM for Anomaly Detection**:
            **Explanation**: These models are used to detect anomalies in the dataset, which could represent outliers where alcohol-related harm is unusually high or low. For example, a country with unexpectedly high alcohol-related harm compared to its consumption level could be flagged, prompting further investigation. This could indicate underlying issues like poor healthcare infrastructure or ineffective alcohol regulation.
            """)

elif selected_button == "Clustering Alcohol consumption":
    st.header("Clustering Alcohol consumption")

    # Create tabs for Forecasting
    tab1, tab2, tab3= st.tabs(["**K-Means Clustering**", "**DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**", " **💡 What's Happening here? 💡** "])


    with tab1:
        st.image(f"{pathname}Clustering1.jpeg", caption="K-Means Clustering ")

    with tab2:
        st.image(f"{pathname}Clustering2.jpeg", caption="DBSCAN (Density-Based Spatial Clustering of Applications with Noise)")

    with tab3:
        st.write("""
        ### **1. K-Means Clustering**:
        **Explanation**: K-Means clusters the data into distinct groups. In this project, it could group regions or demographic segments based on their alcohol consumption patterns and associated harms. For example, you might identify clusters of regions with high alcohol consumption and high health burdens, or clusters where economic costs are particularly severe. These insights can help tailor interventions to specific groups or regions.
        ### **2. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**:
        **Explanation**: DBSCAN can identify clusters based on density, making it useful for finding areas or groups where alcohol-related harms are particularly concentrated. It’s also effective at identifying outliers, which could represent regions with exceptionally high or low levels of alcohol-related harm, potentially due to unique local factors.

        """)

elif selected_button == "Machine Learning Models":
    st.header("Machine Learning Models")

    # Create tabs for Forecasting
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["**Gradient Boosting Regressor**", "**ARIMA (AutoRegressive Integrated Moving Average)**", "**LSTM (Long Short-Term Memory)**", "**Gaussian Mixture Model**", " **💡 What's Happening Here? 💡** "])
    with tab1:
        st.image(f"{pathname}ML1.jpeg", caption="**Gradient Boosting Regressor**")

    with tab2:
        st.image(f"{pathname}ML3.jpeg", caption="**ARIMA (AutoRegressive Integrated Moving Average)**")

    with tab3:
        st.image(f"{pathname}ML4.jpeg", caption="**LSTM (Long Short-Term Memory)**")

    with tab4:
        st.image(f"{pathname}ML2.jpeg", caption="**Gaussian Mixture Model**")

    with tab5:
        st.write("""
        ### 1. **Gradient Boosting Regressor**:
        **Explanation**: This regression model could be used to predict the impact of alcohol consumption on different societal harms, such as healthcare costs or mortality rates. By fitting the model to your data, you can predict how changes in alcohol consumption might affect these outcomes, helping policymakers anticipate the effects of different levels of alcohol use.
        ### 2. **ARIMA (AutoRegressive Integrated Moving Average)**:
        **Explanation**: ARIMA is used for forecasting time series data, so it could predict future trends in alcohol-related harms based on past data. This could help in forecasting the long-term impact of current consumption patterns or evaluating the potential effects of policy changes on future public health and economic burdens.
        ### 3. **LSTM (Long Short-Term Memory)**:
        **Explanation**: LSTM is particularly useful for capturing complex, temporal dependencies in time series data. In the context of alcohol harms, an LSTM model could predict future trends in alcohol-related issues by learning from past patterns. This can be valuable for planning long-term public health strategies or interventions aimed at reducing alcohol-related harms.
        ### 4. **Gaussian Mixture Model**:
        Explanation: GMM can be used to understand the distribution of alcohol-related harms across different segments of the population or different regions. It allows for soft clustering, where each individual or region can belong to multiple clusters with different probabilities. This could reveal overlapping factors contributing to alcohol harms, such as regions with both high consumption and poor healthcare systems.
        """)

