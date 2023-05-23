from django.db import transaction as translation
import re

import numpy as np
import pandas as pd
import tensorflow as tf
from category_encoders import *
from sklearn.preprocessing import StandardScaler
from dossier.models import Dossier

# Definisce le liste "colonneObbligatorie" e "colonneDaLavorare", che contengono i nomi delle colonne del dataframe df
# che devono essere utilizzate e che devono essere elaborate rispettivamente.
import manage
from storicoDati.models import DatiStandard



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
                       'data_nascita']

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


def replace_values(value):
    # Crea l'espressione regolare per sostituire tutti i valori diversi da "codiceFiscale", "partitaIva" o "nessuno"
    regex = re.compile(r'^(?!codiceFiscale|partitaIva|nessuno).*$')
    # Sostituisci i valori che corrispondono all'espressione regolare con "ciao"
    return re.sub(regex, 'nessuno', value)


def correzione_standardizzazione(df):
    # Filtra il dataframe df utilizzando solo le colonne presenti nella lista colonneObbligatorie.
    # In seguito, riordina le colonne di df utilizzando l'ordine presente nella lista colonneObbligatorie.
    df = df.filter(colonneObbligatorie)
    df = df.reindex(columns=colonneObbligatorie)
    print(f"dfffff bellooo")
    print(df)
    # Filtra il dataframe df utilizzando solo le colonne presenti nella lista colonneDaLavorare.
    dfColonneDaLavorare = df.filter(colonneDaLavorare)

    # Per ogni colonna presente nella lista colonneDaLavorare, il codice converte i valori di tale colonna in oggetti datetime,
    # utilizzando il formato '%Y-%m' e ignorando eventuali errori.
    # In seguito, vengono aggiunte al dataframe tre nuove colonne, ottenute estraendo rispettivamente l'anno, il mese e il giorno
    # dall'oggetto datetime. Tutte queste nuove colonne vengono poi convertite in numeri, sostituendo eventuali valori mancanti con 0
    # e convertendo il tipo di dati in int64.

    for col in colonneDaLavorare:
        df[col] = pd.to_datetime(df[col], format='%Y-%m', errors='coerce')
        df[f'{col}_anno'] = df[col].dt.year
        df[f'{col}_mese'] = df[col].dt.month
        df[f'{col}_anno'] = pd.to_numeric(df[f'{col}_anno'], errors="coerce")
        df[f'{col}_anno'] = df[f'{col}_anno'].fillna(0).astype(np.int64)
        df[f'{col}_mese'] = pd.to_numeric(df[f'{col}_mese'], errors="coerce")
        df[f'{col}_mese'] = df[f'{col}_mese'].fillna(0).astype(np.int64)

    # Elimina dal dataframe df le colonne presenti nella lista colonneDaLavorare.
    df.drop(colonneDaLavorare, axis=1, inplace=True)

    # Sostituisce con ZERO tutti i valori mancanti nel dataframe df.
    df = df.fillna(0)
    # Converte in stringhe tutti gli oggetti presenti nel dataframe che sono di tipo "object".
    df[df.select_dtypes(['object']).columns] = df.select_dtypes(['object']).astype('string')

    # Per ogni colonna del dataframe che è di tipo "string", sostituisce tutti i valori "0" con "nessuno".
    df_replaced = df.select_dtypes(['string']).replace('0', 'nessuno')

    df[df.select_dtypes(['string']).columns] = df_replaced

    df_replaced = df.select_dtypes(['string']);
    # Sostituisci tutte le stringhe che hanno il formato di una partita IVA con la stringa 'partitaIva' nella colonna 'p_iva'
    df['p_iva'] = df['p_iva'].replace(r"^[0-9]{11}$", 'partitaIva', regex=True)

    # Sostituisci tutte le stringhe che hanno il formato di un codice fiscale con la stringa 'codiceFiscale' nella colonna 'p_iva'
    df['p_iva'] = df['p_iva'].replace(r"^[A-Za-z0-9]{16}$", 'codiceFiscale', regex=True)

    # Applica la funzione replace_values alla colonna 'p_iva' per pulire i valori della colonna
    # il nuovo metodo utilizzando la funzione replace values è più veloce
    df['p_iva'] = df['p_iva'].apply(replace_values)

    # Sostituisci tutte le stringhe che hanno il formato di un numero di telefono cellulare con la stringa 'Telefono cellulare'
    # nelle colonne 'tipo_telefono1' e 'tipo_telefono2'
    df['tipo_telefono1'] = df['tipo_telefono1'].replace(r'^3\d{9}$', 'Telefono cellulare', regex=True)
    df['tipo_telefono2'] = df['tipo_telefono2'].replace(r'^3\d{9}$', 'Telefono cellulare', regex=True)

    # Sostituisci tutte le stringhe che hanno il formato di un numero di telefono cellulare con la stringa 'Telefono cellulare'
    # nelle colonne 'tipo_telefono1' e 'tipo_telefono2'
    df['tipo_telefono1'] = df['tipo_telefono1'].replace(r'^0\d{9}$', 'Telefono abitazione', regex=True)
    df['tipo_telefono2'] = df['tipo_telefono2'].replace(r'^0\d{9}$', 'Telefono abitazione', regex=True)

    # Converti tutte le colonne di tipo object in stringhe
    df[df.select_dtypes(['object']).columns] = df.select_dtypes(['object']).astype('string')

    scaler_4 = CountEncoder()
    scaler = StandardScaler()
    # Seleziona dal dataframe solo le colonne presenti in colonneNumeriche e assegnale a dfNumerico
    dfNumerico = df[colonneNumeriche]

    # Rimuovi dal dataframe le colonne presenti in colonneNumeriche
    df = df.drop(colonneNumeriche, axis=1)

    # Converti le colonne del dataframe in tipo 'category'
    df_training_category = df.astype('category')

    # Codifica le colonne del dataframe utilizzando CountEncoder e assegnale a df_training_category_encoded
    df_training_category_encoded = scaler_4.fit_transform(df_training_category)

    # Concatena df_training_category_encoded e dfNumerico per ottenere il dataframe df
    df = pd.concat([df_training_category_encoded, dfNumerico], axis=1)
    # Standardizza i dati del dataframe df e assegnali alla variabile
    standardizzato = scaler.fit_transform(df)
    # Crea un nuovo dataframe con i dati standardizzati e assegnali alla variabile
    standardizzato = pd.DataFrame(standardizzato,
                                  columns=['committente_codice','id_profilo_esattore', 'esattore_codice', 'committente_desc', 'profilo_desc', 'p_iva',
                                           'luogo_nascita', 'cap', 'citta', 'provincia', 'tipo_telefono1',
                                           'tipo_telefono2', 'filiale', 'data_affido_anno', 'data_affido_mese',
                                           'scadenza_mandato_anno', 'scadenza_mandato_mese', 'data_nascita_anno',
                                           'data_nascita_mese', 'minimo_dovuto', 'rate_arretrate',
                                           'importo_capitale', 'importo_interessi', 'importo_spese',
                                           'importo_spese_recupero', 'importo_differenza', 'debitoresiduo',
                                           'importo_rata'])
    print("dfffffffffff")

    print(df)
    print("standardddddddd")
    print(standardizzato)
 
    dati = standardizzato.to_dict(orient='records')

    # Utilizza una transazione per salvare i dati nel database
    with translation.atomic():
        for d in dati:
            # Crea una nuova istanza di ModelloDati con i dati del dizionario
            istanza = DatiStandard(**d)
            istanza.save()

    # # Carico il modello di machine learning salvato in precedenza
    # model = tf.keras.models.load_model("../Test_regression_model_mae_2")

    # # Utilizza il modello per fare una previsione sui dati standardizzati della colonna incasso capitale
    # y_pred = model.predict(standardizzato)
    # print(y_pred)
    # all(manage.main()).to_bytes()



def test():
    print("ecco")
   
    # df = pd.read_csv("C:/Users/anton/Documents/RepositorySourceTree/Consulgest-api/Lista_Pratiche.csv", low_memory=False)
    df = pd.read_csv("nuovo.csv", low_memory=False)
    # df = df.head(10)
    # df.to_csv("nuovo.csv", index=False)
    # print("1")
    esattori = pd.read_excel('esattoriList.xlsx')
    # print("2")
    print(df['esattore_codice'].value_counts())
    mask = df['esattore_codice'].isin(esattori['ID Ext'])
    df.loc[~mask, 'esattore_codice'] = 0
    print('valore count a 0')
    print(df['esattore_codice'].value_counts())
    correzione_standardizzazione(df)
    
# test()

