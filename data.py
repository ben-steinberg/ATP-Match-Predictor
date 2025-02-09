import pandas as pd

def load_data():
    # Load the dataset
    atp_2023 = pd.read_csv('data/atp/2023.csv')
    atp_2024 = pd.read_csv('data/atp/2024.csv')

    wta_2023 = pd.read_csv('data/wta/2023.csv')
    wta_2024 = pd.read_csv('data/wta/2024.csv')

    atp_df = pd.concat([atp_2023, atp_2024])
    wta_df = pd.concat([wta_2023, wta_2024])

    # Preprocess the dataset
    # Placeholder for preprocessing steps
    return atp_df, wta_df

atp_df, wta_df = load_data()

print(atp_df.info())
print(wta_df.info())