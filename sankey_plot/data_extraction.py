from pandas import DataFrame, Series, crosstab
from seaborn import color_palette

def _generate_crosstabs(data:DataFrame, hue):
    data_list = []
    cols = data.columns
    if hue:
        cols = list(cols).copy()
        cols.remove(hue)
    for i in range(0,len(cols) - 1):
        if hue:
            index = [data[cols[i]].values, data[hue].values]
        else:
            index = data[cols[i]].values

        columns = data[cols[i+1]].values
        ct = crosstab(index=index, columns=columns)

        data_list.append(ct)
    
    return data_list

def _generate_labels(data:DataFrame):
    labels = _create_labels(data)
    labels_dict = _create_labels_dict(labels)
    return labels_dict


def _create_labels(data:DataFrame):
    labels = []
    for i in data.columns:
        labels.extend(data[i].unique())
    return labels


def _create_labels_dict(labels):
    return {j:i for i,j in enumerate(labels)}

def _generate_colors(data: Series, palette):

    payment_types = data.unique()
    palette = color_palette(palette,n_colors = len(payment_types))
    palette_list = [f'rgba({i[0]*255},{i[1]*255},{i[2]*255},0.35)' for i in palette]
    color_map = {j:palette_list[i] for i,j in enumerate(payment_types)}

    return color_map