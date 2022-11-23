import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import plotly.express as px


# Loading the dataset
stock_quotes = pd.read_csv("stock_quotes.csv")

# Correlation Matrix formation
corr_matrix = stock_quotes.corr(method='pearson')

#Using heatmap to visualize the correlation matrix
fig = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='RdBu_r')
fig.show()
