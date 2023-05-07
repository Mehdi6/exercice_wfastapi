import pandas as pd
import glob
import os
from pydantic import BaseModel



class TvShow(BaseModel): 
    Title: str
    
def read_all_files():
    current_directory = os.path.dirname(__file__)
    #print(current_directory)
    os.chdir(current_directory)
    #os.chdir("..")
    #os.chdir("..")
    os.chdir("../../data")
    li = []
    #os.chdir(path)
    
    for filename in glob.glob("*.csv"):
        df = pd.read_csv(filename, index_col=None, header=0)
        li.append(df)
        
    frame = pd.concat(li, axis=0, ignore_index=True)
    
    return frame

def top10_tvshow_byprovider(provider):
    data = read_all_files()
    providers = [provider.lower(), provider.upper(), provider]
    
    # we select only the specified provider
    filtered_data_by_provider = data.loc[data["Provider"].isin(providers)]
    # grouping data by title or tvshow to compute the mean
    results = filtered_data_by_provider.groupby('Title')['Views'].mean()
    # sorting tvshow descending mode
    sorted_list = results.sort_values(ascending = False)
    
    # selecting and returning the top 10 tv shows
    return sorted_list[0:10].index.to_list()
        
def list_ofall_tvshows():
    data = read_all_files()
    results = data.Title.drop_duplicates().sort_values()
    
    list_tvshows = [TvShow(**{'Title': item}) for item in results]
    return list_tvshows