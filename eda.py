import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(csv):
    data=pd.read_csv(csv)
    return data

def run_eda_app():
    st.subheader('EDA Section')

    data = load_data('titanic.csv')

    submenu = st.sidebar.selectbox("Submenu",['Descriptive','Visualization'])
    if submenu == "Descriptive":
        st.write('Descriptive')
        with st.expander('Data frame'):
            st.dataframe(data)

        with st.expander('Data Type'):
            st.dataframe(data.dtypes)


        with st.expander('Data Shape'):
            st.dataframe(data.shape)

        
        with st.expander('Deskriptif statistic'):
            st.dataframe(data.describe().transpose())

        
        with st.expander('Null'):
            st.dataframe(data.isna().sum().transpose())



    elif submenu=="Visualization":
        st.write("Visualization")
        with st.expander('Passenger belonging to Embarked'):
            embarked_counts = data['Embarked'].value_counts()
            fig, ax = plt.subplots()
            sns.set(style="whitegrid")
            ax.pie(embarked_counts, labels=embarked_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
            ax.axis('equal')
            ax.legend(title='Embarked', loc='upper center' ,bbox_to_anchor=(1, 0.5))
            st.pyplot(fig)

        with st.expander('Pclass Histogram'):
            fig, ax = plt.subplots()
            sns.countplot(x='Pclass', hue='Sex', data=data)
            st.pyplot(fig)

        with st.expander('Violin'):
            fig, ax = plt.subplots()
            sns.violinplot(data=data, x="Survived", y="Sex")
            plt.title('Violin Plot - Survived vs Sex')
            plt.xlabel('Survived')
            plt.ylabel('Sex')
            st.pyplot(fig)

        with st.expander('Null Detection'):
            fig, ax = plt.subplots(figsize=(4,2))
            sns.heatmap(data.isnull(), cbar=False)
            plt.xticks(rotation=80)
            st.pyplot(fig)