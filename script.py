import camelot
import pandas as pd
import json
from functools import reduce

def get_data(tables):
    data_frames = []
    for i in range(len(tables)):
        data_frames.append(tables[i].df)
    return data_frames        

if __name__ == "__main__":

    data_frames = get_data(camelot.read_pdf('edital.pdf', pages='1-54', flavor='lattice', strip_text='\n'))        
    df = reduce(lambda left,right: pd.merge(left,right,on=[0,1,2,3,4],how='outer'), data_frames)
    df.drop(0, inplace=True)
    df.rename(columns={
        0:'Estudante', 1:'Unidade', 2:'Título do Trabalho', 
        3:'Programa', 4:'Data da apresentação'},inplace=True)

    with open('data.json','w', encoding='utf-8') as file: file.write(json.dumps(df.to_dict(), ensure_ascii=False, indent=4))        
    df.to_excel('data.xlsx', sheet_name='Sheet1', index=False)
    