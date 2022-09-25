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
import os
#from st_aggrid import AgGrid



st.set_page_config(layout="wide")

path = os.path.dirname(__file__)
my_file = 'C:/Users/Makram/Downloads/cleaned_data_31_08_22.csv'

data=my_file
    
data12 = data

st.write(data12)

