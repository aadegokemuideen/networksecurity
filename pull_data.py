#ETL pipeline
import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from dotenv import load_dotenv

load_dotenv()
Mongo_db_url = os.getenv("mongo_url")
#print(Mongo_db_url)

ca = certifi.where()


class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def cv_to_json_converter(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop =True, inplace=True)
            records= list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self,records, database,collection):
        try:
            self.database=database
            self.collection = collection
            self.records = records

            self.mong_client = pymongo.MongoClient(Mongo_db_url)
            self.database = self.mong_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)
            return len(self.records)
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)

if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE  = "aadegokemuideen"
    Collection = "NetworkData"
    networkobj = NetworkDataExtract()
    records = networkobj.cv_to_json_converter(FILE_PATH)
    no_of_records = networkobj.insert_data_mongodb(records,DATABASE,Collection)

    print(no_of_records)

