import json
from django.db import models
import pandas as pd



class Parser(models.Model):

    def readHeaderCSV(file):
        #df = pd.read_csv("C:/Users/arote/Desktop/CGIBackend Pesante/Lista_Pratiche.csv",low_memory=False, index_col=0, nrows=0).columns.tolist()
        list = pd.read_csv(file, low_memory=False).columns.tolist()
        return list

    def getStandardHeader(self):

        list_header = [
                       'committente_codice',
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
                       'data_nascita'
        ]
        return list_header

    def replacementHeaders(self, json_client, file):
        # converto json cliente in dict
        dict_client = json.loads(json_client)

        # estraggo tipi mappati dal cliente e creo una lista
        list_type_client = []
        for key in dict_client:
            list_type_client.append(dict_client[key]['type'])

        # estraggo gli headers e creo una lista
        list_headers_client = list(dict_client.keys())

        # credo un df del file dell'ente
        df = pd.read_csv(file, low_memory=False, sep=";")

        # creo una copia del df con gli headers aggiornati dall'utente
        df2 = df.set_axis(list_headers_client, axis=1)

        print(df2)

        # check dei tipi delle righe con i tipi indicati dall'utente
        for row in df2.itertuples(index=False):
            row_list = list(row[0:len(df2.columns)])
            for i in range(len(row_list)):
                if type(row_list[i]) != type(list_type_client[i]):
                    type(row_list[i])(list_type_client[i]) # forzo il cast con tipo del dataframe



