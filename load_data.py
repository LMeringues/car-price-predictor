import pandas as pd
import os

DATA_URL = "https://raw.githubusercontent.com/alexeygrigorev/mlbookcamp-code/master/chapter-02-car-price/data.csv"
FILE_NAME = "used_cars.csv"

def load_data():
    try:
        df = pd.read_csv(DATA_URL)
        df.to_csv(FILE_NAME, index=False)

        print(f"File saved as '{FILE_NAME}'")
        print(f"Size: {df.shape[0]} rows, {df.shape[1]} columns")
        print("Example of data:")
        print(df.head(5))

    except Exception as e:
        print("Error while downloading: ", e)


if __name__ == "__main__":
    load_data()