import requests
import json
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sb
from urllib.request import urlopen 



import dbnomics


def create_dataframe_by_calling_api():
    # Effettuo una chiamata API per recuperare il dataframe delle commodity_prices fornito dal provider Word Bank
    response = requests.get("https://api.db.nomics.world/v22/datasets/WB/commodity_prices?limit=125&offset=0")
    data = response.json()
    print(data)
    series = data['datasets']['docs'][0]['dimensions_values_labels']['indicator']
    series_list = list(series.values())
    print(series_list)
    df1 = pd.DataFrame(list(series.items()), columns=['Code', 'Description',])
    print(df1)
    return (df1)
    

def split_dataframe_by_description(df1):
    # Splitto la la colonna Description con il metodo split "," partendo dall'ultima colonna  
    split_description = df1['Description'].str.rsplit(',', n=2, expand=True)
    split_description.columns = ['Description', 'index value', 'Unit of measure']
    # Concateno il nuovo Dataframe con le nuove colonne
    df2 = pd.concat([df1, split_description], axis=1)
    # Creo e reindicizzo il nuovo dataframe  
    df3 = df2.iloc[:, [0, 2, 3, 4]]
    df4 = df3.reindex(columns=['index value','Unit of measure','Description','Code'])
    print(df4)
    return(df4)


def filter_by_keyword(df2):
    # Filtro il Dataframe per parola chiave contenuta all'interno della colonna Description 
    check_empty= True   
    while check_empty!=False:
        keyword = input('Definisci una parola chiave per filtrare le serie: ')
        df_filtered = df2.loc[df2['Description'].str.contains(keyword, case=False)]
        df_filtered = df_filtered.reindex(columns=['index value', 'Unit of measure', 'Description', 'Code'])
        df_filtered = df_filtered.sort_values(by=['index value', 'Unit of measure', 'Description', 'Code'])
        check_empty=df_filtered.empty   
    print(df_filtered)
    return(df_filtered)


def extract_codes_to_analyze(df_filtered):
   
    # Estraggo dal DF_filtered i codici corrispondenti alle series, quindi definisco prima il numero di series da osservare
    numberseries_code = input("Scegli quante serie vuoi analizzare (inserisci solo valori numerici): ")
    while not numberseries_code.isdigit() or int(numberseries_code) > len(df_filtered) or int(numberseries_code) <= 0:
        if not numberseries_code.isdigit():
            print("Hai inserito un valore non valido. Inserisci solo valori numerici.")
        elif int(numberseries_code) > len(df_filtered):
            print("Hai inserito un valore maggiore della lunghezza del dataframe.")
        else:
            print("Hai inserito un valore non valido. Inserisci un valore positivo.")
        numberseries_code = input("Scegli quante serie vuoi analizzare (inserisci solo valori numerici): ")
    numberseries_code = int(numberseries_code)

    series_code = []
    # Estraggo dal DF_filtered le righe corrispondenti alle series da osservare
    for x in range(numberseries_code):
        code = input("Inserisci il numero corrispondente al codice della serie da analizzare: ")
        while not code.isdigit() or int(code) not in df_filtered.index:
            print("Hai inserito un valore non valido o il codice non è presente nel DataFrame.")
            code = input("Inserisci il numero corrispondente al codice della serie da analizzare: ")
        series_code.append(int(code))

    codes = df_filtered.loc[series_code, 'Code']
    print(codes)
    return codes


def create_dataframe_to_analyze(codes):
    # richiamo attraverso l'API il nuovo Dataframe composto dalle series scelte in precedenza
    series_ids = []
    for x in codes: 
        serie= 'WB/commodity_prices/' + x + '-1W'
        series_ids.append(serie)
    
    url = "https://api.db.nomics.world/v22/series"
    params = {
        "series_ids": ",".join(series_ids),
        "facets": "false",
        "observations": "true",
        "metadata": "false",
        "format": "json",
        "offset": "0"
    }
    response = requests.get(url, params=params)
    data = response.json()
    observations = data['series']['docs']

    df_work = pd.DataFrame()
    df_data = []
    for obs in observations:
        series_name = obs['series_name']
        values = obs['value']
        periods = obs['period']
        df_work[series_name] = values


    df_work.index = periods

    print(df_work) 
    return(df_work)

def save_dataframe_to_csv(df_work):
    # salvo il dataframe in formato .csv all'interno della cartella OUT
    folder_path = os.path.join(os.getcwd(), "OUT")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    df_work.to_csv(os.path.join(folder_path, "DF_WORK.csv"), index=False)
    print("il file DF_WORK.csv è stato salvato all'interno della cartella 'OUT' dello spazio di lavoro")

def choosePath(self):
        try:
            path = os.getcwd()  
            select = input("Digita il percorso dove memorizzare il file: ")
            if os.path.exists(select):
                print(f'Il file sarà memorizzato nel seguente percorso:\n{select}')
                return select
            else:
                print(f'Hai inserito un percorso errato, riprova a lanciare il metodo o utilizzare il percorso di default visualizzato di seguito\n')        
            print(f'Il file sarà memorizzato nel seguente percorso:\n{path}')      
            return path
        except Exception as e:
            return (str(e))

def analyze_dataframe(df_work):
    # effettuo un analisi sul dataframe df_work 
    print(df_work.describe())

    correlation = df_work.corr()
    print(correlation)

    # calcolo la serie con il maggior / minore tasso di crescita percentuale
    growth_rates = df_work.pct_change()
    max_growth_series = growth_rates.mean().idxmax()
    print("La serie con il maggiore tasso di crescita è:", max_growth_series)
    min_growth_series = growth_rates.mean().idxmin()
    print("La serie con il minor tasso di crescita invece è:", min_growth_series)

def plot_and_save_df(df_work):
    # Creo il grafico a linee del df_work
    plt.figure(figsize=(20, 8))
    plt.plot(df_work.index, df_work.values)

    # Imposto le etichette degli assi
    plt.xlabel('Anno')
    plt.ylabel('Valore')
    plt.xticks(rotation=45)

    # Aggiungo Titolo e legenda basata sulle colonne del DataFrame
    plt.title('Grafico delle serie')
    plt.legend(df_work.columns)
    plt.axvline(x='2023', color='red', linestyle='--')

    # Verifico l'esistenza della cartella OUT in alternativa viene creata
    folder_path = os.path.join(os.getcwd(), "OUT")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Salvo il grafico ottenuto all'interno della cartella OUT
    plot_path = os.path.join(folder_path, "grafico.png")
    plt.savefig(plot_path)
    print(f"Il grafico è stato salvato come 'grafico.png' nella cartella 'OUT'")
    # Mostra il grafico
    plt.show()



def plot_and_save_describe(df_work):
    #richiamo il describe del df_work 
    df_desc = df_work.describe()

    # Crea il grafico a barre
    plt.bar(df_desc.columns, df_desc.loc['mean'], yerr=df_desc.loc['std'])
    plt.xlabel('Colonne')
    plt.xticks(rotation=45)
    plt.ylabel('Valore medio')
    plt.title('Media e deviazione standard per ogni colonna')

    # Verifico l'esistenza della cartella OUT in alternativa viene creata    
    folder_path = os.path.join(os.getcwd(), "OUT")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Salvo il grafico ottenuto all'interno della cartella OUT
    plot_path = os.path.join(folder_path, "grafico_describe.png")
    plt.savefig(plot_path)
    print(f"Il grafico è stato salvato come 'grafico_describe.png' nella cartella 'OUT'")
    # Mostra il grafico
    plt.show()

def plot_and_save_correlation(df_work):
    df_corr=df_work.corr()
    sb.heatmap(df_corr)
    
    # Verifico l'esistenza della cartella OUT in alternativa viene creata    
    folder_path = os.path.join(os.getcwd(), "OUT")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    # Salvo il grafico ottenuto all'interno della cartella OUT
    plot_path = os.path.join(folder_path, "grafico_correlazione.png")
    plt.savefig(plot_path)
    print(f"Il grafico è stato salvato come 'grafico_correlazione.png' nella cartella 'OUT'")
    # Mostra il grafico
    plt.show()
    
    
    
