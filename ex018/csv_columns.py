import pandas as pd


def csv_columns(input_file, headers=None, missing=None):
    if headers:
        df = pd.read_csv(input_file, index_col=False, names=headers)
    else:
        df = pd.read_csv(input_file, index_col=False)
    # logic to deal with missing values in pandas
    initial_dict = df.to_dict()
    output = {}
    for key, values in initial_dict.items():
        output[key] = [ str(value) for value in values.values() ]
    return output