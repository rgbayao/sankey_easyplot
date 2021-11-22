from pandas import DataFrame
from sankey_plot.data_extraction import (
    _generate_crosstabs,
     _generate_labels,
      _generate_colors
)

def prepare_sankey_info(data:DataFrame, hue = None, seaborn_palette=None, **kwargs):

    data_list = _generate_crosstabs(data, hue)

    if hue:
        colors_dict = _generate_colors(data[hue], seaborn_palette)
        data.drop(hue, axis=1)
    else:
        colors_dict = None

    labels_dict = _generate_labels(data)

    nodes = _generate_nodes(labels_dict, **kwargs)

    links = _generate_links(data_list, labels_dict, colors_dict)

    return nodes, links

    

def _generate_nodes(labels_map, pad=15, thickness=15,
                    line=dict(color = "black", width = 0.5)):
    nodes = dict(pad = pad,
                thickness = thickness,
                line = line,
                label = list(labels_map)
                )
    return nodes


def _generate_links(data_list, labels_map, colors_map=None):
    links = {'source' :[], 'target' :[], 'value':[]}
    if colors_map:
        links['color'] = []
        links['label'] = []
    for dataframe in data_list:
        for i in dataframe.index:
            for j in dataframe.columns:
                if dataframe.loc[(i),j]!=0:
                    links.get('source').append(labels_map[i[0]])
                    links.get('value').append(dataframe.loc[(i),j])
                    links.get('target').append(labels_map[j])
                    if colors_map:
                        links.get('label').append(i[1])
                        links.get('color').append(colors_map[i[1]])
    return links
