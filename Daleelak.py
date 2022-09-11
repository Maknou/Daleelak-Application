import re
import numpy as np
import pandas as pd
import plotly as plt
from nbformat import write
from io import StringIO
from plotly.subplots import make_subplots
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import string
from collections import Counter
import time 
from bs4 import BeautifulSoup  
import time 
from wordcloud import WordCloud, STOPWORDS
import collections
import matplotlib.pyplot as plt
import calendar
import streamlit as st
import hydralit_components as hc
import streamlit.components.v1 as html
from streamlit_option_menu import option_menu
import fontawesome as fa
#from st_aggrid import AgGrid



st.set_page_config(layout="wide")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

     # Can be used wherever a "file-like" object is accepted:
     df = pd.read_csv(uploaded_file)
     st.write(dataframe)
#df=pd.read_csv(r"C:/Users\Makram\Desktop\cleaned_data_31_08_22.csv")
#df2=pd.read_csv("C:/Users/Makram/Downloads/cleaned_data_desc_title.csv")

data12 = df

@st.cache

def load_data(nrows):
    data = pd.read_csv(data12, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

#Figures#
import plotly.graph_objects as go

st.markdown(
        f"""
<style>
    .reportview-container .main .block-container{{
        max-width: {1920}px;
        padding-top: {-2}rem;
        padding-right: {5}rem;
        padding-left: {5}rem;
        padding-bottom: {5}rem;
    }}
    .reportview-container .main {{
        color: #1D3540;
        background-color: #ffffff;
    }}

</style>
"""
    ,
        unsafe_allow_html=True,
    )

## Interventions Sectors
df_inter_1 = data12[data12['Intervention_Sector']!="N/A"]
list_of_names = df_inter_1['Intervention_Sector'].to_list()
list_of_names= ",".join(list_of_names)
my_list = list_of_names.split(",")

for i, s in enumerate(my_list):
    my_list[i] = s.strip()

word_freq_lem = dict(collections.Counter(my_list))
keys = list(word_freq_lem.keys())
values = list(word_freq_lem.values())
df_inter_1 = pd.DataFrame({'words':keys,'freq':values})

## Majors
df_edu_1 = data12[data12['Degree_Major']!="N/A"]
list_of_names = df_edu_1['Degree_Major'].to_list()
list_of_names= ",".join(list_of_names)
my_list = list_of_names.split(",")

for i, s in enumerate(my_list):
    my_list[i] = s.strip()

word_freq_lem = dict(collections.Counter(my_list))
keys = list(word_freq_lem.keys())
values = list(word_freq_lem.values())
df_edu_1 = pd.DataFrame({'words':keys,'freq':values})
df_edu_2 = df_edu_1.sort_values(by='freq',ascending=False)

## Contract Type
top_contract=data12['Contract_Type'].value_counts().reset_index(name='counts')
top_value=top_contract['counts'].loc[0]
per_top_cont= '{:,.2f}'.format(top_value*100/len(data12['Contract_Type']))

## Experience Type
top_exp=data12['Experience_Requirements'].value_counts().reset_index(name='counts')
top_value=top_exp['counts'].loc[0]+top_exp['counts'].loc[1]
per_top_exp= '{:,.2f}'.format(top_value*100/len(data12['Experience_Requirements']))

## Salary
top_sal=data12['Salary_Range'].value_counts().reset_index(name='counts')
top_value_1=top_sal['counts'].loc[top_sal['index']=='1200 to 1500 (USD)'].reset_index(name='counts')
top_value_1a=top_value_1['counts'].loc[0]
top_value_2=top_sal['counts'].loc[top_sal['index']=='1500 to 2000 (USD)'].reset_index(name='counts')
top_value_2a=top_value_2['counts'].loc[0]
top_value_3=top_sal['counts'].loc[top_sal['index']=='2000 to 2500 (USD)'].reset_index(name='counts')
top_value_3a=top_value_2['counts'].loc[0]
top_value = top_value_1a + top_value_2a + top_value_3a
per_top_sal= '{:,.2f}'.format(top_value*100/len(data12['Salary_Range']))

## Job_level
top_level=data12['Job_level'].value_counts().reset_index(name='counts')
top_value_11=top_level['counts'].loc[top_level['index']=='Intermediate or experienced'].reset_index(name='counts')
top_value_11a=top_value_11['counts'].loc[0]
per_top_lev= '{:,.2f}'.format(top_value_11a*100/len(data12['Job_level']))


## bachelor
top_degree=data12['Education_Degree'].value_counts().reset_index(name='counts')
top_value_111=top_degree['counts'].loc[top_degree['index']=='Bachelor Degree'].reset_index(name='counts')
top_value_111a=top_value_111['counts'].loc[0]
per_top_bac= '{:,.2f}'.format(top_value_111a*100/len(data12['Education_Degree']))


##per_top_sal= '{:,.2f}'.format(top_value*100/len(data12['Salary_Range']))
## Majors
top_jobs=data12['Job_Title_Updated_New'].value_counts().reset_index(name='counts')
item=top_jobs['index'].loc[0] + '; ' + top_jobs['index'].loc[1] + '; ' + top_jobs['index'].loc[2]+ '; ' + top_jobs['index'].loc[3]+ '; ' + top_jobs['index'].loc[4]

## top hiring company
top_hiring=data12['Company_Name_Updated'].value_counts().reset_index(name='counts')
item2=top_hiring['index'].loc[0] +', ' + top_hiring['index'].loc[1] + ', ' + top_hiring['index'].loc[2]

## top majors requested
item3=df_edu_2['words'].iloc[1]+', '+df_edu_2['words'].iloc[2]+', '+df_edu_2['words'].iloc[3]+', '+df_edu_2['words'].iloc[4]+', '+df_edu_2['words'].iloc[5]

# jobs titles
jobs_value='{:,.0f}'.format(len(data12['Job_Title_Updated_New'].value_counts()))
# job numbers
num_of_titles=data12.shape[0]
# companies
companies_value='{:,.0f}'.format(len(data12['Company_Name_Updated'].value_counts()))
# majors
majors_value='{:,.0f}'.format(len(df_edu_1['words'].value_counts()))
#df_edu_1.shape[0]
#sectors
sectors_value='{:,.0f}'.format(len(df_inter_1['words'].value_counts()))
# most wanted Job
job_wanted=item
# top hiring org
job_wanted=item2

## Streamlit Output

menu_data = [
        {'icon': "fa fa-building", 'label':"General Insights"},
        {'icon': "fa fa-signal", 'label':"Skills Overview"},
        {'icon':'fa fa-user', 'label':"Daleelak"}
]
over_theme = {'menu_background':'#337d58','txc_inactive': '#faf8f7'}
menu_id = hc.nav_bar(menu_definition=menu_data,override_theme=over_theme,home_name='Home',sticky_nav=True)

if menu_id == "Home":
    st.write(' ')
    st.write(' ')
    col1, col2, col3 = st.columns([1.3,1,1])

    with col1:
        st.write("")

    with col2:
        st.image('https://i.postimg.cc/przMTYsB/download-1.png')

    with col3:
        st.write("")

    st.markdown("<h2 style='text-align: center; color: black;'>Daleel Madani, your next guide for civil society organisations!</h2>", unsafe_allow_html=True)

    st.write(' ')
    st.write(' ')

    st.markdown("<h3 style='text-align: left; color: black;'>Why Daleel Madani?</h3>", unsafe_allow_html=True)

    col8, col9= st.columns([1,1])

    with col8:

        st.write(' ')

        st.markdown("<h5 style='text-align: left; color: black;font size=1;'>&#8226; Most regularly updated and used site by civil society organisations in Lebanon since 2006</h5>", unsafe_allow_html=True)

        st.write(' ')

        st.markdown("<h5 style='text-align: left; color: black;'>&#8226; Over 1 million pageviews per month from users around the world!</h5>", unsafe_allow_html=True)

    with col9:

        st.write(' ')

        st.markdown("<h5 style='text-align: left; color: black;'>&#8226; It has a directory of more than 1,300 civil society actors!</h5>", unsafe_allow_html=True)

        st.write(' ')

        st.markdown("<h5 style='text-align: left; color: black;'>&#8226; You can stay informed about civil society and public action, as well as search for suitable opportunities</h5>", unsafe_allow_html=True)
        
    st.write(' ')
    st.write(' ')

    theme_1 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','font_size': 20, 'content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-briefcase'} # jobs titles
    theme_2 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-hashtag'} # job numbers
    theme_3 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-registered'} # companies
    theme_4 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-graduation-cap'} # majors
    theme_5 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-industry'} #sectors
    theme_6 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-screwdriver'} # most wanted Job
    theme_7 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-building'} # top hiring company
    theme_8 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-book-open'} # top majors requested
    theme_9 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-file-contract'} # top contract
    theme_10 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-calendar'} # top experience
    theme_11 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-dollar-sign'} # top majors salary
    theme_12 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-hashtag'} # top majors job level
    theme_13 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa fa-book'} # top majors degree

    st.markdown("<h2 style='text-align: left; color: black;'>Have a look at what was posted between March 20, 2022 and August 08, 2022</h2>", unsafe_allow_html=True)
    
    st.write(' ')

    cc = st.columns(5)
    with cc[0]:
        hc.info_card(title='Distinct Professions', content=jobs_value, theme_override=theme_1)

    with cc[1]:
        hc.info_card(title='Job Vacancies', content=num_of_titles, theme_override=theme_2)

    with cc[2]:
        hc.info_card(title='Civil Society Organizations', content=companies_value, theme_override=theme_3)

    with cc[3]:
        hc.info_card(title='Types of Majors', content=majors_value, theme_override=theme_4)

    with cc[4]:
        hc.info_card(title='Intervention Sectors', content=sectors_value, theme_override=theme_5)

    cc1 = st.columns(3)
    with cc1[0]:
        hc.info_card(title='Most Wanted Jobs', content=item, theme_override=theme_6)

    with cc1[1]:
        hc.info_card(title='Top Hiring Organizations', content=item2, theme_override=theme_7)

    with cc1[2]:
        hc.info_card(title='Top Majors Requested', content=item3, theme_override=theme_8)

    cc2 = st.columns(5)
    with cc2[0]:
        hc.info_card(title='Full Time Contract Offer', content=f'{per_top_cont}%', theme_override=theme_9)

    with cc2[1]:
        hc.info_card(title='Experience of 2-5 years', content=f'{per_top_exp}%', theme_override=theme_10)

    with cc2[2]:
        hc.info_card(title='Salary Range $1200-$2500', content=f'{per_top_sal}%', theme_override=theme_11)

    with cc2[3]:
        hc.info_card(title='Intermediate or experienced', content=f'{per_top_lev}%', theme_override=theme_12)

    with cc2[4]:
        hc.info_card(title='Bachelor Degree', content=f'{per_top_bac}%', theme_override=theme_13)

elif menu_id == "General Insights":

    st.markdown("<h2 style='text-align: center; color: black;'>Check all the related information for the job postings on Daleel Madani! </h2>", unsafe_allow_html=True)

    st.write(' ')    

    ## English Level

    English_Language=data12['English_Language'].value_counts().reset_index(name='counts')
    top_value_11=English_Language['counts'].loc[English_Language['index']=='Excellent'].reset_index(name='counts')
    top_value_11a=top_value_11['counts'].loc[0]
    top_value_12=English_Language['counts'].loc[English_Language['index']=='Fluent'].reset_index(name='counts')
    top_value_12a=top_value_12['counts'].loc[0]
    top_valuea=top_value_11a + top_value_12a
    eng_top_cont= '{:,.2f}'.format(top_valuea*100/len(data12['English_Language']))

    ## French Level
    French_Language=data12['French_Language'].value_counts().reset_index(name='counts')
    top_valuea2=French_Language['counts'].loc[0]
    fre_top_cont= '{:,.2f}'.format(top_valuea2*100/len(data12['French_Language']))

    ## Arabic Level
    Arabic_Language=data12['Arabic_Language'].value_counts().reset_index(name='counts')
    top_valuea1=Arabic_Language['counts'].loc[0]
    ara_top_cont= '{:,.2f}'.format(top_valuea1*100/len(data12['Arabic_Language']))

    theme_21 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa-solid fa-e'} # english
    theme_22 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa-solid fa-a'} # arabic
    theme_23 = {'bgcolor': '#a19f9d','title_color': '#f5f2f0','content_color': '#f5f2f0', 'icon_color':'black','icon': 'fa-solid fa-f'} # french

    cca = st.columns(3)

    with cca[0]:
        hc.info_card(title='Excellent English & Above', content=f'{eng_top_cont}%', theme_override=theme_21)

    with cca[1]:
        hc.info_card(title='Arabic Language Fluency', content=f'{ara_top_cont}%', theme_override=theme_22)

    with cca[2]:
        hc.info_card(title='No French Language required', content=f'{fre_top_cont}%', theme_override=theme_23)
    
    w1, w2 = st.columns([1,1])

    with w1:
        top_hiring=data12['Company_Name_Updated'].value_counts().reset_index(name='counts')

        top_hiring_1=top_hiring.sort_values(by=["counts"],ascending=False).head(15)
        fig51=px.bar(top_hiring_1, y="index", x="counts",text='counts', title="Companies with the highest number of jobs advertised",color_discrete_sequence=['#074650'],height=500,width=1000,orientation='h')
        fig51.update_yaxes(showgrid=False,tickfont=dict(size=18, color='rgb(0,0,0)', family="sans-serif"))
        fig51.update_xaxes(showgrid=False)
        fig51.update_yaxes(categoryorder='total ascending')
        fig51.update_traces(hovertemplate=None,)
        fig51.update_layout(margin=dict(t=70, b=0, l=70, r=40),
                                showlegend=False, paper_bgcolor = 'rgba(0, 0, 0, 0)', plot_bgcolor = 'rgba(0, 0, 0, 0)',
                                xaxis = go.layout.XAxis(title = ' ',showticklabels=False),
                                xaxis_tickangle=360,
                                yaxis_title=" ",
                                font=dict(size=13, color='rgb(0,0,0)', family="sans-serif"),
                                title_font=dict(size=28, color='rgb(0,0,0)', family="sans-serif"))

        st.write(fig51)

    with w2:

        top_intervention=pd.read_csv("C:/Users/Makram/Downloads/intervention_final.csv")

        top_intervention_1=top_intervention.sort_values(by=["freq"],ascending=False).head(15)
        fig511=px.bar(top_intervention_1, y="words", x="freq",text='freq', title="Job Postings in relation to Intervention Sector",color_discrete_sequence=['#074650'],height=500,width=1000,orientation='h')
        fig511.update_yaxes(showgrid=False,tickfont=dict(size=18, color='rgb(0,0,0)', family="sans-serif"))
        fig511.update_xaxes(showgrid=False)
        fig511.update_yaxes(categoryorder='total ascending')
        fig511.update_traces(hovertemplate=None,)
        fig511.update_layout(margin=dict(t=70, b=0, l=70, r=40),
                                showlegend=False, paper_bgcolor = 'rgba(0, 0, 0, 0)', plot_bgcolor = 'rgba(0, 0, 0, 0)',
                                xaxis = go.layout.XAxis(title = ' ',showticklabels=False),
                                xaxis_tickangle=360,
                                yaxis_title=" ",
                                font=dict(size=13, color='rgb(0,0,0)', family="sans-serif"),
                                title_font=dict(size=28, color='rgb(0,0,0)', family="sans-serif"))

        st.write(fig511)


    cafe_colors =  ['#074650', '#009292', '#FE6DB6',
                '#FEB5DA', '#480091','#B66DFF','#B5DAFE','#6DB6FF']
    Education_Degree=data12["Education_Degree"]
    fig118 = go.Figure(data=[go.Pie(labels=Education_Degree.value_counts().index, values=Education_Degree.value_counts().values, hole=0.4,marker_colors=cafe_colors)])
    fig118.update_layout(
        title={
            'text': "Education Degree"},title_x=0.5,font=dict(size=16))

    Experience_Requirements=data12["Experience_Requirements"]
    fig119 = go.Figure(data=[go.Pie(labels=Experience_Requirements.value_counts().index, values=Experience_Requirements.value_counts().values,hole=0.4, marker_colors=cafe_colors)])
    fig119.update_layout(
        title={
            'text': "Experience Requirements"},title_x=0.5,font=dict(size=16))

    Salary_Range=data12["Salary_Range"]
    fig200 = go.Figure(data=[go.Pie(labels=Salary_Range.value_counts().index, values=Salary_Range.value_counts().values, hole=0.4,marker_colors=cafe_colors)])
    fig200.update_layout(
        title={
            'text': "Salary Range"},title_x=0.5,font=dict(size=16))

    c81,c82,c83,c84,c85 = st.columns((0.1,4,4,4,1))
    with c81:
        st.write("")  
    with c82:
        st.write(fig118)   
    with c83:
        st.write(fig119)  
    with c84:
        st.write(fig200) 
    with c85:
        st.write("")

    w3, w4 = st.columns([1,1])

    with w3:
        cafe_colors =  ['#074650', '#009292', '#FE6DB6',
                '#FEB5DA', '#480091','#B66DFF','#B5DAFE','#6DB6FF']

        top_jobs=data12['Job_Title_Updated_New'].value_counts().reset_index(name='counts')

        top_jobs_1=top_jobs.sort_values(by=["counts"],ascending=False).head(15)
        fig151=px.bar(top_jobs_1, y="index", x="counts",text='counts', title="Top Requested Jobs",color_discrete_sequence=['#074650'],height=500,width=1000,orientation='h')
        fig151.update_yaxes(showgrid=False,tickfont=dict(size=18, color='rgb(0,0,0)', family="sans-serif"))
        fig151.update_xaxes(showgrid=False)
        fig151.update_yaxes(categoryorder='total ascending')
        fig151.update_traces(hovertemplate=None,)
        fig151.update_layout(margin=dict(t=70, b=0, l=70, r=40),
                                showlegend=False, paper_bgcolor = 'rgba(0, 0, 0, 0)', plot_bgcolor = 'rgba(0, 0, 0, 0)',
                                xaxis = go.layout.XAxis(title = ' ',showticklabels=False),
                                xaxis_tickangle=360,
                                yaxis_title=" ",
                                font=dict(size=13, color='rgb(0,0,0)', family="sans-serif"),
                                title_font=dict(size=28, color='rgb(0,0,0)', family="sans-serif"))

        st.write(fig151)

    with w4:
        cafe_colors =  ['#074650', '#009292', '#FE6DB6',
                '#FEB5DA', '#480091','#B66DFF','#B5DAFE','#6DB6FF']


        Job_level=data12["Job_level"]
        fig251 = go.Figure(data=[go.Pie(labels=Job_level.value_counts().index, values=Job_level.value_counts().values, hole=0.4,marker_colors=cafe_colors)])
        fig251.update_layout(
            title={
                'text': "Job Level Distribution"},title_x=0.5,font=dict(size=16))
       
        st.write(fig251)


elif menu_id == "Skills Overview":


    col1, col2, col3 = st.columns([7,.25,1.5])

    with col1:

        st.markdown("<h2 style='text-align: left; color: black;'>Navigate thought the different types of skills that the employers on Daleel Madani were looking after!</h2>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<h3 style='text-align: left; color: black;'>This is a general overview that covers all jobs advertised on the website</h3>", unsafe_allow_html=True)

    with col2:
        st.write("")
        

    with col3:
        st.write("")

        st.image('https://i.postimg.cc/C5s6Pr22/skills-concept-education-training-improvement-people-get-knowledge-build-career-illustration-277904.jpg')
 
    # Skills Types

    skills = st.selectbox(
        'Selections',
        ('Hardware & Network Skills', 'Database Skills','Computer Skills','Programming Skills','Analytical Skills','Data Analysis Skills','Marketing Skills','Presentation Skills','Visualization Skills',
        'Project Management Skills','Hard Skills','Soft Skills','Interpersonal Skills','Arts & Graphic Design Skills','Sales Skills','Finance Skills','Administrative Skills','Nursing Skills','General Engineering Skills',
        'Mechanical Engineering Skills','Civil Engineering Skills','Social Work Skills','Healthcare Skills','Therapy Skills','Legal Skills','Human Resources Skills','Educational Skills',
        'Security Skills','Media & Journalism Skills','Writing & Translation Skills','Supply Chain & Logistics Skills','Agricultural Skills','Environmetal Skills',
        'Food & Beverages Skills','Biology & Chemistry Related Skills','Biomedical Technologies & Medtech Skills','Accounting & Taxation Skills','Research Skills',
        'Operational Skills','Communication & Public Relations Skills','Architectural Skills'))

    st.subheader(f'You are reviewing the top 15 **{skills}** by Word Occurence')

    if skills == 'Hardware & Network Skills':
        skill='hard_netw_skills'

    elif skills == 'Database Skills':
        skill='database_skills'

    elif skills == 'Computer Skills':
        skill='comp_skills'

    elif skills == 'Programming Skills':
        skill='prog_skills'

    elif skills == 'Analytical Skills':
        skill='analytical_skills'

    elif skills == 'Data Analysis Skills':
        skill='Data_analytics_skills'

    elif skills == 'Marketing Skills':
        skill='mark_skills'

    elif skills == 'Presentation Skills':
        skill='pres_skills'

    elif skills == 'Project Management Skills':
        skill='pman_skills'

    elif skills == 'Visualization Skills':
        skill='vis_skills'

    elif skills == 'Soft Skills':
        skill='soft_skills'

    elif skills == 'Hard Skills':
        skill='hard_skills'

    elif skills == 'Interpersonal Skills':
        skill='int_skills'

    elif skills == 'Arts & Graphic Design Skills':
        skill='design_skills'

    elif skills == 'Nursing Skills':
        skill='nursing_skills'

    elif skills == 'Finance Skills':
        skill='finance_skills'

    elif skills == 'Sales Skills':
        skill='sales_skills'

    elif skills == 'Administrative Skills':
        skill='admin_skills'

    elif skills == 'General Engineering Skills':
        skill='engineering_skills'

    elif skills == 'Mechanical Engineering Skills':
        skill='mech_eng_skills'

    elif skills == 'Civil Engineering Skills':
        skill='civ_eng_skills'

    elif skills == 'Social Work Skills':
        skill='social_work_skills'

    elif skills == 'Healthcare Skills':
        skill='health_skills'

    elif skills == 'Therapy Skills':
        skill='therapy_skills'

    elif skills == 'Legal Skills':
        skill='legal_skills'

    elif skills == 'Human Resources Skills':
        skill='hr_skills'

    elif skills == 'Educational Skills':
        skill='education_skills'
        
    elif skills == 'Security Skills':
        skill='security_skills'
        
    elif skills == 'Media & Journalism Skills':
        skill='media_skills'
        
    elif skills == 'Writing & Translation Skills':
        skill='writing_trans'
        
    elif skills == 'Supply Chain & Logistics Skills':
        skill='sc_logistics_tranp'
        
    elif skills == 'Agricultural Skills':
        skill='agricultural'
        
    elif skills == 'Environmetal Skills':
        skill='environmetal'
        
    elif skills == 'Food & Beverages Skills':
        skill='food_beverage'
        
    elif skills == 'Biology & Chemistry Related Skills':
        skill='biological_chemical'
        
    elif skills == 'Biomedical Technologies & Medtech Skills':
        skill='biomed_tech'
        
    elif skills == 'Accounting & Taxation Skills':
        skill='accounting_tax'
        
    elif skills == 'Research Skills':
        skill='research_skills'
        
    elif skills == 'Operational Skills':
        skill='operations_skills'
        
    elif skills == 'Communication & Public Relations Skills':
        skill='commun_pr'
        
    elif skills == 'Architectural Skills':
        skill='arch_skills'

    # Genral Code:

    df_skills = data12[data12[skill].notnull()]
    list_of_names = df_skills[skill].to_list()
    list_of_names= ",".join(list_of_names)
    my_list = list_of_names.split(",")

    word_freq_lem = dict(collections.Counter(my_list))
    keys = list(word_freq_lem.keys())
    values = list(word_freq_lem.values())
    df_skills = pd.DataFrame({'words':keys,'freq':values})
    df_skills = df_skills.sort_values(by = 'freq',ascending = False)

    word_could_dict=Counter(word_freq_lem)
    wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)

    fig_a, ax = plt.subplots(figsize = (12, 8))
    ax.imshow(wordcloud)
    plt.axis("off")

    top_15=df_skills.sort_values(by = 'freq',ascending = False).head(15)

    fig = px.bar(top_15, x='freq', y='words', text='freq', color_discrete_sequence=['#074650'],height=500,width=1000,orientation='h')
    fig.update_yaxes(showgrid=False,tickfont=dict(size=18, color='rgb(0,0,0)', family="sans-serif"))
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(categoryorder='total ascending')
    fig.update_traces(hovertemplate=None,)
    fig.update_layout(margin=dict(t=70, b=0, l=70, r=40),
                            showlegend=False, paper_bgcolor = 'rgba(0, 0, 0, 0)', plot_bgcolor = 'rgba(0, 0, 0, 0)',
                            xaxis = go.layout.XAxis(title = ' ',showticklabels=False),
                            xaxis_tickangle=360,
                            yaxis_title=" ",
                            font=dict(size=13, color='rgb(0,0,0)', family="sans-serif"),
                            title_font=dict(size=28, color='rgb(0,0,0)', family="sans-serif"))

    list_of_names1 = df_skills['words'][15:30].to_list()
    list_of_names1= ", ".join(list_of_names1)

    fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Other related Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=20,
                    height=100))
                            ])
    fig212.update_layout(autosize=False, width=1500,height=800)
    c1,c3 = st.columns((1,1.5))
    with c1:
        st.write(fig)

    with c3:
        st.write(fig212)

elif menu_id == "Daleelak":

    st.markdown("<h2 style='text-align: center; color: black;'>Daleelak!! Your next application guide for job search and skill matching on Daleel Madani</h2>", unsafe_allow_html=True)

    st.subheader("Select your desired job title!")
    # Skills per Job title

    data12=data12[data12['Job_Title_Updated_New']!='Other']
    job_titles = data12['Job_Title_Updated_New'].drop_duplicates()

    job_title = st.selectbox('',job_titles)

    data_14=data12.loc[data12['Job_Title_Updated_New']==job_title].reset_index(drop=True)

    ## Interventions Sectors
    df_inter = data_14[data_14['Intervention_Sector']!="N/A"]
    list_of_names = df_inter['Intervention_Sector'].to_list()
    list_of_names= ",".join(list_of_names)
    my_list = list_of_names.split(",")

    for i, s in enumerate(my_list):
        my_list[i] = s.strip()

    word_freq_lem = dict(collections.Counter(my_list))
    keys = list(word_freq_lem.keys())
    values = list(word_freq_lem.values())
    df_inter = pd.DataFrame({'words':keys,'freq':values})
    
    list_of_names11 = df_inter['words'][:5].to_list()
    list_of_names11= ", ".join(list_of_names11)


    ## Majors
    df_educ = data_14[data_14['Degree_Major']!="not specified"]
    list_of_names = df_educ['Degree_Major'].to_list()
    list_of_names= ",".join(list_of_names)
    my_list = list_of_names.split(",")

    for i, s in enumerate(my_list):
        my_list[i] = s.strip()

    word_freq_lem = dict(collections.Counter(my_list))
    keys = list(word_freq_lem.keys())
    values = list(word_freq_lem.values())
    df_educ = pd.DataFrame({'words':keys,'freq':values})

    list_of_names10 = df_educ['words'][:5].to_list()
    list_of_names10 = [name.title() for name in list_of_names10]
    list_of_names10= ", ".join(list_of_names10)

    for i in list_of_names10:
        i=string.capwords(i)


    ## top hiring company
    top_hiring_1=data_14['Company_Name_Updated'].value_counts().reset_index(name='counts')
    item2a=top_hiring_1['index'].loc[0]

    list_of_companies = top_hiring_1['index'][1:8].to_list()
    list_of_companies = [name.title() for name in list_of_companies]
    list_of_companies= ", ".join(list_of_companies)

    for i in list_of_companies:
        i=string.capwords(i)

    kpi0, kpi1, kpi2, kpi3,kpi4, kpi5= st.columns((2,4,4,4,4,6))
    
    kpi0.metric(
    label="",
    value="")

    kpi1.metric(
    label="Total Vacancies 💼",
    value='{:,.0f}'.format(data_14['Job_Title_Updated_New'].count()))

    kpi2.metric(
    label="Hiring Comapnies 🏠",
    value='{:,.0f}'.format(len(data_14['Company_Name_Updated'].value_counts())))

    kpi3.metric(
    label="Different Sectors 📁",
    value='{:,.0f}'.format(len(df_inter['words'].value_counts())))

    kpi4.metric(
    label="Requested Majors 🎓",
    value='{:,.0f}'.format(len(df_educ['words'].value_counts())))

    kpi5.metric(
    label="Most Hiring Organzition 🏛️",
    value=item2a)


    cafe_colors =  ['#074650', '#009292', '#FE6DB6',
                '#FEB5DA', '#480091','#B66DFF','#B5DAFE','#6DB6FF']
    Education_Degree=data_14["Education_Degree"]
    fig18 = go.Figure(data=[go.Pie(labels=Education_Degree.value_counts().index, values=Education_Degree.value_counts().values, hole=0.4,marker_colors=cafe_colors)])
    fig18.update_layout(
        title={
            'text': "Education Degree"},title_x=0.5,font=dict(size=16))

    Experience_Requirements=data_14["Experience_Requirements"]
    fig19 = go.Figure(data=[go.Pie(labels=Experience_Requirements.value_counts().index, values=Experience_Requirements.value_counts().values,hole=0.4, marker_colors=cafe_colors)])
    fig19.update_layout(
        title={
            'text': "Experience Requirements"},title_x=0.5,font=dict(size=16))

    Salary_Range=data_14["Salary_Range"]
    fig20 = go.Figure(data=[go.Pie(labels=Salary_Range.value_counts().index, values=Salary_Range.value_counts().values, hole=0.4,marker_colors=cafe_colors)])
    fig20.update_layout(
        title={
            'text': "Salary Range"},title_x=0.5,font=dict(size=16))

    c11,c12,c21,c31,c41 = st.columns((0.1,4,4,4,1))
    with c11:
        st.write("")  
    with c12:
        st.write(fig18)   
    with c21:
        st.write(fig19)  
    with c31:
        st.write(fig20) 
    with c41:
        st.write("")  

    fig21 = go.Figure(data=[go.Table(
        header=dict(values=['Most requested Majors'],
            line_color='darkslategray',
            fill_color='#074650',
            align=['center'],
            font=dict(color='white', size=25),
            height=40),
        cells=dict(values=[list_of_names10],
            line_color='darkslategray',
            fill=dict(color=['white', 'white']),
            align=['center'],
            font_size=21,
            height=40))
                     ])

    fig21.update_layout(autosize=False, width=1200,height=280)

    fig22 = go.Figure(data=[go.Table(
        header=dict(values=['Intervention Sectors'],
            line_color='darkslategray',
            fill_color='#074650',
            align=['center'],
            font=dict(color='white', size=25),
            height=40),
        cells=dict(values=[list_of_names11],
            line_color='darkslategray',
            fill=dict(color=['white', 'white']),
            align=['center'],
            font_size=21,
            height=30))
                     ])

    fig22.update_layout(autosize=False, width=1200,height=280)

    fig44 = go.Figure(data=[go.Table(
        header=dict(values=['Other Hiring Companies'],
            line_color='darkslategray',
            fill_color='#074650',
            align=['center'],
            font=dict(color='white', size=25),
            height=40),
        cells=dict(values=[list_of_companies],
            line_color='darkslategray',
            fill=dict(color=['white', 'white']),
            align=['center'],
            font_size=21,
            height=30))
                     ])

    fig44.update_layout(autosize=False, width=1800,height=300)

    c13,c15 = st.columns([1,1])
 
    with c13:
        st.write(fig21)   

    with c15:
        st.write(fig22) 

    c27,c28,c29 = st.columns((0.5,4,0.5))
    with c27:
        st.write("")  
    with c28:
        st.write(fig44)   
    with c29:
        st.write("")  

    if data_14['job_by_sector'].loc[0] == 'Human Resources':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Hard Skills','Administrative Skills','Human Resources Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Hard Skills':
            skill='hard_skills'

        elif skills == 'Administrative Skills':
            skill='admin_skills'

        elif skills == 'Human Resources Skills':
            skill='hr_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)

        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Computers & ICT':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Hardware, Software, & Network Skills', 'Database Skills','Programming Skills','Data Analytics Skills','Visualization Skills','Hard Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Hardware, Software, & Network Skills':
            skill='hard_netw_skills'

        elif skills == 'Database Skills':
            skill='database_skills'

        elif skills == 'Programming Skills':
            skill='prog_skills'

        elif skills == 'Data Analytics Skills':
            skill='Data_analytics_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='royalblue',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0]== 'Business Management':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Data Analytics Skills','Project Management Skills','Hard Skills','Sales Skills','Operational Skills','Research Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Sales Skills':
            skill='sales_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        elif skills == 'Project Management Skills':
            skill='pman_skills'

        elif skills == 'Data Analytics Skills':
            skill='Data_analytics_skills'
            
        elif skills == 'Operational Skills':
            skill='operations_skills'
            
        elif skills == 'Research Skills':
            skill='research_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Healthcare':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Soft Skills','Interpersonal Skills','Healthcare Skills','Hard Skills','Nursing Skills','Research Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Nursing Skills':
            skill='nursing_skills	'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        elif skills == 'Healthcare Skills':
            skill='health_skills'

        elif skills == 'Research Skills':
            skill='research_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Education & Teaching':
    
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Hard Skills','Educational Skills','Research Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Educational Skills':
            skill='education_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        elif skills == 'Research Skills':
            skill='research_skills'
            
        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})

        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Community & Voluntary':
    
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Hard Skills','Social Work Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Social Work Skills':
            skill='social_work_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Clerical & Administration':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Soft Skills','Interpersonal Skills','Hard Skills','Administrative Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Administrative Skills':
            skill='admin_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Banking & Financial Services':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Hard Skills','Finance & Audit Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Finance & Audit Skills':
            skill='finance_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)


    elif data_14['job_by_sector'].loc[0] == 'Advertising, Marketing & Public Relations':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Hard Skills','Administrative Skills','Communication & Public Relations Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Marketing Skills':
            skill='mark_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'
            
        elif skills == 'Communication & Public Relations Skills':
            skill='commun_pr'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212) 

    elif data_14['job_by_sector'].loc[0] == 'Psychology & Social Care':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Soft Skills','Interpersonal Skills','Hard Skills','Therapy Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Therapy Skills':
            skill='therapy_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)
    elif data_14['job_by_sector'].loc[0] == 'Engineering, Manufacturing & Energy':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Hard Skills','Mechanical Engineering Skills','Civil Engineering Skills','Engineering Skills','Research Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Engineering Skills':
            skill='engineering_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        elif skills == 'Mechanical Engineering Skills Skills':
            skill='mech_eng_skills'

        elif skills == 'Civil Engineering Skills':
            skill='civ_eng_skills'

        elif skills == 'Research Skills':
            skill='research_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Accountancy & Taxation':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Soft Skills','Interpersonal Skills','Accounting & Taxation Skills','Hard Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Accounting & Taxation Skills':
            skill='accounting_tax'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)
    elif data_14['job_by_sector'].loc[0] == 'Art, Craft & Design':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Art & Graphic Design Skills','Hard Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Art & Graphic Design Skills':
            skill='design_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Construction, Architecture & Property':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Operational Skills','Hard Skills','Civil Engineering Skills','Architectural Skills','General Engineering Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Operational Skills':
            skill='operations_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        elif skills == 'Civil Engineering Skills':
            skill='civ_eng_skills'
            
        elif skills == 'Architectural Skills':
            skill='arch_skills'
            
        elif skills == 'General Engineering Skills':
            skill='engineering_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Law & Legal':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Soft Skills','Interpersonal Skills','Legal Skills','Hard Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Legal Skills':
            skill='legal_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)
        
    elif data_14['job_by_sector'].loc[0] == 'Transport & Logistics':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Soft Skills','Interpersonal Skills','Supply Chain & Logistics Skills','Hard Skills','Operational Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Supply Chain & Logistics Skills':
            skill='sc_logistics_tranp'

        elif skills == 'Hard Skills':
            skill='hard_skills'
            
        elif skills == 'Operational Skills':
            skill='operations_skills'
            
        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)
        
    elif data_14['job_by_sector'].loc[0] == 'Food & Beverages':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Soft Skills','Interpersonal Skills','Food & Beverages Skills','Hard Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Food & Beverages':
            skill='food_beverage'

        elif skills == 'Hard Skills':
            skill='hard_skills'
            
        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)
        
    elif data_14['job_by_sector'].loc[0] == 'Farming, Horticulture & Forestry':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Soft Skills','Interpersonal Skills','Agricultural Skills','Hard Skills','Environmetal Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Agricultural Skills':
            skill='agricultural'

        elif skills == 'Hard Skills':
            skill='hard_skills'
            
        elif skills == 'Environmetal Skills':
            skill='environmetal'
            
        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)
        
    elif data_14['job_by_sector'].loc[0] == 'Security, Defence & Law Enforcement':
        
        skills = st.selectbox(
            '',
            ('Soft Skills','Interpersonal Skills','Security Skills','Hard Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Security Skills':
            skill='security_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'
            
        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)
        
    elif data_14['job_by_sector'].loc[0] == 'Earth & Environment':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Soft Skills','Interpersonal Skills','Environmetal Skills','Hard Skills','Agricultural Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Environmetal Skills':
            skill='environmetal'

        elif skills == 'Hard Skills':
            skill='hard_skills'
            
        elif skills == 'Agricultural Skills':
            skill='agricultural'
            
        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Biomedical Technologies & Medtech':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Biomedical Technologies & Medtech Skills','Hard Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Biomedical Technologies & Medtech Skills':
            skill='biomed_tech'

        elif skills == 'Hard Skills':
            skill='hard_skills'
            
        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)
        
    elif data_14['job_by_sector'].loc[0] == 'Media, Film & Publishing':
        
        skills = st.selectbox(
            '',
            ('Computer Skills','Analytical Skills','Presentation Skills','Visualization Skills','Soft Skills','Interpersonal Skills','Media Skills','Hard Skills','Writing & Translation Skills','Communication & Public Relations Skills'))

        st.subheader(f'Have a look at what **{skills}** are needed for the **{job_title}**')

        if skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'   

        elif skills == 'Media Skills':
            skill='media_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'
            
        elif skills == 'Writing & Translation Skills':
            skill='writing_trans'
            
        elif skills == 'Communication & Public Relations Skills':
            skill='commun_pr'
            
        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)

    elif data_14['job_by_sector'].loc[0] == 'Intern':

        skills = st.selectbox(
            'Selections',
            ('Hardware & Network Skills', 'Database Skills','Computer Skills','Programming Skills','Analytical Skills','Data Analysis Skills','Marketing Skills','Presentation Skills','Visualization Skills',
            'Project Management Skills','Hard Skills','Soft Skills','Interpersonal Skills','Arts & Graphic Design Skills','Sales Skills','Finance Skills','Administrative Skills','Nursing Skills','General Engineering Skills',
            'Mechanical Engineering Skills','Civil Engineering Skills','Social Work Skills','Healthcare Skills','Therapy Skills','Legal Skills','Human Resources Skills','Educational Skills',
            'Security Skills','Media & Journalism Skills','Writing & Translation Skills','Supply Chain & Logistics Skills','Agricultural Skills','Environmetal Skills',
            'Food & Beverages Skills','Biology & Chemistry Related Skills','Biomedical Technologies & Medtech Skills','Accounting & Taxation Skills','Research Skills',
            'Operational Skills','Communication & Public Relations Skills','Architectural Skills'))

        st.subheader(f'You are reviewing the top 15 **{skills}** by Word Occurence')

        if skills == 'Hardware & Network Skills':
            skill='hard_netw_skills'

        elif skills == 'Database Skills':
            skill='database_skills'

        elif skills == 'Computer Skills':
            skill='comp_skills'

        elif skills == 'Programming Skills':
            skill='prog_skills'

        elif skills == 'Analytical Skills':
            skill='analytical_skills'

        elif skills == 'Data Analysis Skills':
            skill='Data_analytics_skills'

        elif skills == 'Marketing Skills':
            skill='mark_skills'

        elif skills == 'Presentation Skills':
            skill='pres_skills'

        elif skills == 'Project Management Skills':
            skill='pman_skills'

        elif skills == 'Visualization Skills':
            skill='vis_skills'

        elif skills == 'Soft Skills':
            skill='soft_skills'

        elif skills == 'Hard Skills':
            skill='hard_skills'

        elif skills == 'Interpersonal Skills':
            skill='int_skills'

        elif skills == 'Arts & Graphic Design Skills':
            skill='design_skills'

        elif skills == 'Nursing Skills':
            skill='nursing_skills'

        elif skills == 'Finance Skills':
            skill='finance_skills'

        elif skills == 'Sales Skills':
            skill='sales_skills'

        elif skills == 'Administrative Skills':
            skill='admin_skills'

        elif skills == 'General Engineering Skills':
            skill='engineering_skills'

        elif skills == 'Mechanical Engineering Skills':
            skill='mech_eng_skills'

        elif skills == 'Civil Engineering Skills':
            skill='civ_eng_skills'

        elif skills == 'Social Work Skills':
            skill='social_work_skills'

        elif skills == 'Healthcare Skills':
            skill='health_skills'

        elif skills == 'Therapy Skills':
            skill='therapy_skills'

        elif skills == 'Legal Skills':
            skill='legal_skills'

        elif skills == 'Human Resources Skills':
            skill='hr_skills'

        elif skills == 'Educational Skills':
            skill='education_skills'
            
        elif skills == 'Security Skills':
            skill='security_skills'
            
        elif skills == 'Media & Journalism Skills':
            skill='media_skills'
            
        elif skills == 'Writing & Translation Skills':
            skill='writing_trans'
            
        elif skills == 'Supply Chain & Logistics Skills':
            skill='sc_logistics_tranp'
            
        elif skills == 'Agricultural Skills':
            skill='agricultural'
            
        elif skills == 'Environmetal Skills':
            skill='environmetal'
            
        elif skills == 'Food & Beverages Skills':
            skill='food_beverage'
            
        elif skills == 'Biology & Chemistry Related Skills':
            skill='biological_chemical'
            
        elif skills == 'Biomedical Technologies & Medtech Skills':
            skill='biomed_tech'
            
        elif skills == 'Accounting & Taxation Skills':
            skill='accounting_tax'
            
        elif skills == 'Research Skills':
            skill='research_skills'
            
        elif skills == 'Operational Skills':
            skill='operations_skills'
            
        elif skills == 'Communication & Public Relations Skills':
            skill='commun_pr'
            
        elif skills == 'Architectural Skills':
            skill='arch_skills'

        df_skills = data_14[data_14[skill].notnull()]
        list_of_names = df_skills[skill].to_list()
        list_of_names= ",".join(list_of_names)
        my_list = list_of_names.split(",")

        word_freq_lem = dict(collections.Counter(my_list))
        keys = list(word_freq_lem.keys())
        values = list(word_freq_lem.values())
        df_skills = pd.DataFrame({'words':keys,'freq':values})
        df_skills = df_skills.sort_values(by = 'freq',ascending = False)
        
        list_of_names1 = df_skills['words'][:20].to_list()
        list_of_names1= ", ".join(list_of_names1)

        fig212 = go.Figure(data=[go.Table(
                header=dict(values=['Top 20 Skills'],
                    line_color='darkslategray',
                    fill_color='#074650',
                    align=['center'],
                    font=dict(color='white', size=25),
                    height=40),
                cells=dict(values=[list_of_names1],
                    line_color='darkslategray',
                    fill=dict(color=['white', 'white']),
                    align=['left'],
                    font_size=25,
                    height=100))
                            ])
        fig212.update_layout(autosize=False, width=2400,height=800)

        st.write(fig212)
