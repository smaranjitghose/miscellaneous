import pandas as pd
from pathlib import Path

def combine_csv(path : str, path_2 = "", n = 2, path_o = "")->pd.DataFrame:
    """
    Function that merges all the CSV inside a given directory
    Either pass the paths of the two CSVs
    Or the path of the folder that contains two or more CSVs, with an parameter specifying any value of n >= 3
    An optional parameter of output path can be given if one wants to save the merged dataframe as a csv file to disk
    """
    if n == 2:
            # Read the two data CSV Files
            df_1 = pd.read_csv(path)
            df_2 = pd.read_csv(path_2)
            merged_df = pd.concat([df_1, df_2])
    else:
        # Fetch all the CSV files in the given path
        csv_files = [i for i in Path(path).rglob('*.csv')]
        #combine all csv files in the given path
        merged_df = pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index= True)
    if path_o:
        # Export to csv
        path_o = Path(path_o).joinpath("merged.csv")
        with path_o.open(mode = 'w', encoding = 'utf-8-sig') as final_csv:
            merged_df.to_csv(final_csv, index=False)
    return merged_df

