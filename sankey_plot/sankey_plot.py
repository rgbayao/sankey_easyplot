from pandas import DataFrame
from pandas import crosstab
from sankey_plot.plot import prepare_sankey_info
from plotly import graph_objects as go

def sankey_plot(data: DataFrame, columns:list=None, hue:str=None, seaborn_palette:str=None, title=None):
    
    if columns is None:
        columns = data.columns
    if hue:
        temp_cols = columns.copy()
        temp_cols.append(hue)
        data = data[temp_cols]
    else:
        data = data[columns]

    data = data.dropna()

    nodes, links = prepare_sankey_info(data, hue, seaborn_palette)

    fig = go.Figure(data=[go.Sankey(
    valueformat = ".d",
    # Define nodes
    node = nodes,
    # Add links
    link = links)])

    if title:
        fig.update_layout(title_text=title, font_size=10)
        
    fig.show()


    

