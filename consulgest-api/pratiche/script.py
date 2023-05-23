import json
from django.dispatch import receiver
import pandas as pd
from django.db import transaction as translation
from sklearn import preprocessing
from dossier.models import Dossier
import re
import numpy as np
from sklearn.preprocessing import StandardScaler
from category_encoders import *

from storicoDati.models import DatiStandard
from django.db.models.signals import post_save

colonneObbligatorie = ['committente_codice',
                       'esattore_codice',
                       'committente_desc',
                       'profilo_desc',
                       'p_iva',
                       'luogo_nascita',
                       'cap',
                       'citta',
                       'provincia',
                       'tipo_telefono1',
                       'tipo_telefono2',
                       'filiale',
                       'minimo_dovuto',
                       'rate_arretrate',
                       'importo_capitale',
                       'importo_interessi',
                       'importo_spese',
                       'importo_spese_recupero',
                       'importo_differenza',
                       'debitoresiduo',
                       'importo_rata',
                       'data_affido',
                       'scadenza_mandato',
                       'data_nascita',
                      'id_profilo_esattore']

colonneDaLavorare = ['data_affido',
                     'scadenza_mandato',
                     'data_nascita']

colonneNumeriche = ['minimo_dovuto',
                    'rate_arretrate',
                    'importo_capitale',
                    'importo_interessi',
                    'importo_spese',
                    'importo_spese_recupero',
                    'importo_differenza',
                    'debitoresiduo',
                    'importo_rata']

colonneDaFiltrare = ['esattore_codice']

numerical_columns = ['minimo_dovuto',
 'rate_arretrate',
 'importo_capitale',
 'importo_interessi',
 'importo_spese',
 'importo_spese_recupero',
 'importo_differenza',
 'debitoresiduo',
 'importo_rata']

datetime_columns = ['data_affido_anno',
 'data_affido_mese',
 'scadenza_mandato_anno',
 'scadenza_mandato_mese',
 'data_nascita_anno',
 'data_nascita_mese']

categorical_columns =['committente_codice',
 'esattore_codice',
 'committente_desc',
 'profilo_desc',
 'p_iva',
 'luogo_nascita',
 'cap',
 'citta',
 'provincia',
 'tipo_telefono1',
 'tipo_telefono2',
 'filiale',
 'id_profilo_esattore']


#LEGGO I CAP
with open('./cap.txt', 'r') as f:
    cap = [line.strip() for line in f]
    
#LEGGO LE PROVINCE
with open('./province.txt', 'r') as f:
    province = [line.strip() for line in f]
    
    

def replace_values(value):
    # Crea l'espressione regolare per sostituire tutti i valori diversi da "codiceFiscale", "partitaIva" o "nessuno"
    regex = re.compile(r'^(?!codiceFiscale|partitaIva|nessuno).*$')
    # Sostituisci i valori che corrispondono all'espressione regolare con "ciao"
    return re.sub(regex, 'nessuno', value)


def read_dossier(file, lotto, template):
    #converto il template json in dict
    template_custom = str(template.colonne_mappate)
    template_custom = template_custom.replace("'", '"')
    
    template_dict = json.loads(template_custom)
    #template_dict = template.colonne_mappate
    print(type(template_dict))
    
    # leggo il csv e prendo solo 50 righe 
    df = pd.read_csv(file, low_memory=False)
    # df = df.sample(n=50)
    
    # rinomino le colonne del DataFrame usando il dizionario "template"
    df = df.rename(columns=template_dict)
    
    df = df.filter(colonneObbligatorie)

    df = df.reindex(columns=colonneObbligatorie)
    
    #preparo il df convertito in dict per salvare i dossier originali
    #che serviranno al front in tabella
    dati_dict_originali = df.to_dict(orient='records')

    dfColonneDaLavorare = df.filter(colonneDaLavorare)

    for col in colonneDaLavorare:
        df[col] = pd.to_datetime(df[col], format='%Y-%m', errors='coerce')
        df[f'{col}_anno'] = df[col].dt.year
        df[f'{col}_mese'] = df[col].dt.month
        df[f'{col}_anno'] = pd.to_numeric(df[f'{col}_anno'], errors="coerce")
        df[f'{col}_anno'] = df[f'{col}_anno'].fillna(0).astype(np.int64)
        df[f'{col}_mese'] = pd.to_numeric(df[f'{col}_mese'], errors="coerce")
        df[f'{col}_mese'] = df[f'{col}_mese'].fillna(0).astype(np.int64)



    df.drop(colonneDaLavorare, axis=1, inplace=True)


    df = df.fillna(0)


    df[df.select_dtypes(['object']).columns] = df.select_dtypes(['object']).astype('string')

    Category_df = df[categorical_columns]

    Numerical_df = df[numerical_columns]

    Datetime_df = df[datetime_columns]

    Category_df['id_profilo_esattore'] = Category_df['id_profilo_esattore'].astype('string')
    
    Category_df = Category_df.select_dtypes(['string']).replace('0','nessuno')
    
    Category_df['p_iva'] = Category_df['p_iva'].replace(r"^[0-9]{11}$", 'partitaIva', regex=True)
    
    Category_df['p_iva'] = Category_df['p_iva'].replace(r"^[A-Za-z0-9]{16}$", 'codiceFiscale', regex=True)
    
    Category_df['p_iva'] = Category_df['p_iva'].apply(replace_values)
    
    Category_df['tipo_telefono1'] = Category_df['tipo_telefono1'].replace(r'^3\d{9}$', 'Telefono cellulare', regex=True)
    Category_df['tipo_telefono2'] = Category_df['tipo_telefono2'].replace(r'^3\d{9}$', 'Telefono cellulare', regex=True)

    # Sostituisci tutte le stringhe che hanno il formato di un numero di telefono cellulare con la stringa 'Telefono cellulare'
    # nelle colonne 'tipo_telefono1' e 'tipo_telefono2'
    Category_df['tipo_telefono1'] = Category_df['tipo_telefono1'].replace(r'^0\d{9}$', 'Telefono abitazione', regex=True)
    Category_df['tipo_telefono2'] = Category_df['tipo_telefono2'].replace(r'^0\d{9}$', 'Telefono abitazione', regex=True)

    # Converti tutte le colonne di tipo object in stringhe, sono già stringhe
    # Category_df[Category_df.select_dtypes(['object']).columns] = Category_df.select_dtypes(['object']).astype('string')

    
    #RIMUOVO DA LUOGO NASCITA LE PROVINCE
    for provincia in province:
        Category_df['luogo_nascita'] = Category_df['luogo_nascita'].str.replace(f" {provincia}", "")


    # sostituisce con nessuno tutto ciò che inizia con un numero oppure con un carattere speciale
    Category_df['provincia'] = Category_df['provincia'].apply(lambda x: 'nessuno' if re.match(r'^[\W_0-9]+', x) else x)

    # definizione del pattern regex per controllare la colonna 'cap'
    pattern = re.compile(r'^\d{5}$')

    # applicazione del pattern regex alla colonna 'cap' per verificare le condizioni
    mask = df['cap'].apply(lambda x: bool(pattern.match(str(x))))

    # sostituzione dei valori che non soddisfano le condizioni
    Category_df.loc[~mask, 'cap'] = 'nessuno'

    # verifica se i valori della colonna 'cap' sono presenti nella lista
    mask = Category_df['cap'].isin(cap)

    # sostituzione dei valori che non sono presenti nella lista
    Category_df.loc[~mask, 'cap'] = 'nessuno'

    df_reconstructed = pd.concat([Category_df, Numerical_df, Datetime_df], axis=1)


    object_columns = df_reconstructed.select_dtypes(include=['object']).columns
    df_reconstructed[object_columns] = df_reconstructed[object_columns].astype('string')

    # Applicazione delle regex alla colonna 'tipo_telefono1'
    df_reconstructed['tipo_telefono1'] = df_reconstructed['tipo_telefono1'].str.lower()
    df_reconstructed['tipo_telefono1'] = df_reconstructed['tipo_telefono1'].apply(lambda x: 'Telefono abitazione' if re.search(r'abitazione', x) else x)
    df_reconstructed['tipo_telefono1'] = df_reconstructed['tipo_telefono1'].apply(lambda x: 'Telefono cellulare' if re.search(r'cellulare', x) else x)
    df_reconstructed['tipo_telefono1'] = df_reconstructed['tipo_telefono1'].apply(lambda x: 'Telefono principale' if re.search(r'principale', x) else x)
    df_reconstructed['tipo_telefono1'] = df_reconstructed['tipo_telefono1'].apply(lambda x: 'Telefono 1' if re.search(r'telefono 1', x) else x)
    df_reconstructed['tipo_telefono1'] = df_reconstructed['tipo_telefono1'].apply(lambda x: 'nessuno' if re.search(r'nessuno', x) else x)
    df_reconstructed['tipo_telefono1'] = df_reconstructed['tipo_telefono1'].apply(lambda x: 'altro' if not re.search(r'(Telefono abitazione|Telefono cellulare|Telefono principale|Telefono 1|nessuno)', x) else x)


    # Applicazione delle regex alla colonna 'tipo_telefono2'
    df_reconstructed['tipo_telefono2'] = df_reconstructed['tipo_telefono2'].str.lower()
    df_reconstructed['tipo_telefono2'] = df_reconstructed['tipo_telefono2'].apply(lambda x: 'Telefono abitazione' if re.search(r'abitazione', x) else x)
    df_reconstructed['tipo_telefono2'] = df_reconstructed['tipo_telefono2'].apply(lambda x: 'Telefono cellulare' if re.search(r'cellulare', x) else x)
    df_reconstructed['tipo_telefono2'] = df_reconstructed['tipo_telefono2'].apply(lambda x: 'Telefono principale' if re.search(r'principale', x) else x)
    df_reconstructed['tipo_telefono2'] = df_reconstructed['tipo_telefono2'].apply(lambda x: 'Telefono 2' if re.search(r'telefono 2', x) else x)
    df_reconstructed['tipo_telefono2'] = df_reconstructed['tipo_telefono2'].apply(lambda x: 'nessuno' if re.search(r'nessuno', x) else x)
    df_reconstructed['tipo_telefono2'] = df_reconstructed['tipo_telefono2'].apply(lambda x: 'altro' if not re.search(r'(Telefono abitazione|Telefono cellulare|Telefono principale|Telefono 2|nessuno)', x) else x)

    scaler_4 = preprocessing.LabelEncoder()
    scaler = StandardScaler()


    df_reconstructed_categorical = df_reconstructed[categorical_columns]


    #VECCHIO ENCODER
    # Codifica le colonne del dataframe utilizzando CountEncoder e assegnale a df_training_category_encoded
    # df_training_category_encoded = scaler_4.fit_transform(df_training_category)


    #nuovo encoder
    from sklearn.preprocessing import LabelEncoder

    # # inizializza un nuovo DataFrame vuoto
    # df_training_category_encoded = pd.DataFrame()

    # itera su ogni colonna del DataFrame originale
    for col in df_reconstructed_categorical.columns:
        # applica LabelEncoder alla colonna
        encoded_col = scaler_4.fit_transform(df_reconstructed_categorical[col])
        
    #     # aggiungi la colonna codificata al nuovo DataFrame
        df_reconstructed_categorical[col] = encoded_col

    # scaler_4.fit_transform(df_reconstructed_categorical)

    
    df_reconstructed_encoded_not_scaled = pd.concat([df_reconstructed_categorical,Numerical_df,Datetime_df],axis=1)
    
    
    dati_dict_encodati = df_reconstructed_encoded_not_scaled.to_dict(orient='records')


    # Utilizza una transazione per salvare i dati nel database
    with translation.atomic():
        for d1, d2 in zip(dati_dict_originali, dati_dict_encodati):
            # Crea una nuova istanza di ModelloDati con i dati del dizionario
            istanza2 = DatiStandard(**d2)
            
            istanza = Dossier(**d1)
            istanza.id_lotto = lotto
            istanza.id_dati_standard = istanza2
            
            istanza2.save()
            istanza.save()