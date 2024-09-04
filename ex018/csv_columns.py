import pandas as pd


def csv_columns(input_file, headers=None):
    df = pd.read_csv(input_file, index_col=False)
    initial_dict = df.to_dict()
    output = {}
    if headers:
        pass
    else:
        for key, values in initial_dict.items():
            output[key] = [ str(value) for value in values.values() ]
        return output