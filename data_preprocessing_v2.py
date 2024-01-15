import pandas as pd
from collections import defaultdict


def move_column_to_last(df, column_name):
    # Get the list of column names
    columns = list(df.columns)

    # Remove the specified column from its current position
    columns.remove(column_name)

    # Append the column to the end of the list
    columns.append(column_name)

    # Reorder the DataFrame columns
    df = df[columns]

    return df

def process_csv(input_file_path, output_file_path):
    # Read input CSV file
    df = pd.read_csv(input_file_path, sep=';')

    # Initialize output dataframe
    result_df = pd.DataFrame(columns=["ISLEM_NO", "DOGUM_TARIHI", "CINSIYET", "TANI"])

    # Dictionary to store feature values for each patient
    feature_values_dict = defaultdict(lambda: defaultdict(list))

    # Iterate through unique patients (ISLEM_NO)
    for islem_no in df['ISLEM_NO'].unique():
        # Filter data for the current patient
        patient_data = df[df['ISLEM_NO'] == islem_no]

        # Extract unique values for 'DOGUM_TARIHI', 'CINSIYET', 'TANI'
        dogum_tarihi = patient_data['DOGUM_TARIHI'].iloc[0]
        cinsiyet = patient_data['CINSIYET'].iloc[0]
        tani = patient_data['TANI'].iloc[0]

        # Initialize a dictionary to store feature values
        feature_values = {"ISLEM_NO": islem_no, "DOGUM_TARIHI": dogum_tarihi, "CINSIYET": cinsiyet, "TANI": tani}

        # Iterate through unique features (ALT_TETKIK_ADI first, then TETKIK_ADI if ALT_TETKIK_ADI is not available)
        #unique_features = pd.concat([patient_data['ALT_TETKIK_ADI'], patient_data['TETKIK_ADI']]).dropna().unique()
        unique_features = patient_data.apply(lambda row: row['ALT_TETKIK_ADI'] if pd.notna(row['ALT_TETKIK_ADI']) else row['TETKIK_ADI'], axis=1).dropna().unique()
        
       

        for feature_name in unique_features:
            # Extract values for the feature
            alt_tetkik_data = patient_data[patient_data['ALT_TETKIK_ADI'] == feature_name]
            tetkik_data = patient_data[patient_data['TETKIK_ADI'] == feature_name]

            if not alt_tetkik_data.empty:
                feature_data = alt_tetkik_data
            elif not tetkik_data.empty:
                feature_data = tetkik_data
            else:
                continue

            feature_data_copy = feature_data
    
            # Sort feature data by 'TETKIK_ISTEM_TARIHI' in descending order
            feature_data_copy = feature_data_copy.sort_values(by='TETKIK_ISTEM_TARIHI', ascending=False)

            # Extract values from the first row
            sonuc = list(feature_data_copy['SONUC']) if not feature_data_copy['SONUC'].empty else None 
            unite = feature_data['UNITE'].iloc[0] if not feature_data['UNITE'].empty else None 
            min_deger = feature_data['MIN_DEGER'].iloc[0] if not feature_data['MIN_DEGER'].empty else None
            max_deger = feature_data['MAX_DEGER'].iloc[0] if not feature_data['MAX_DEGER'].empty else None
            tetkik_tarih = list(feature_data_copy['TETKIK_ISTEM_TARIHI']) if not feature_data_copy['TETKIK_ISTEM_TARIHI'].empty else None 

            # Update the feature values dictionary
            feature_values.update({
                f"{feature_name}": sonuc,
                f"{feature_name}_Tetkik_Tarih": tetkik_tarih,
                f"{feature_name}_Birim": unite,
                f"{feature_name}_Alt_Limit": min_deger,
                f"{feature_name}_Ust_Limit": max_deger
            })


        # Store feature values for the current patient
        feature_values_dict[islem_no] = feature_values  
        

    # Iterate through feature values dictionary to create the final result dataframe
    for islem_no, feature_values in feature_values_dict.items():
        result_df = pd.concat([result_df, pd.DataFrame([feature_values])], ignore_index=True)

    result_df = move_column_to_last(result_df, 'TANI')
    # Save the output dataframe to a new CSV file
    result_df.to_csv(output_file_path, index=False, sep=';')

# Define input and output file paths
input_file_path = "D:/SIRKET_DOKUMANLARI/AGU_BIGG_DOKUMANLAR/VERI_TOPLAMA/Kayseri_SH/nevasoft_colab.csv"
output_file_path = "D:/SIRKET_DOKUMANLARI/AGU_BIGG_DOKUMANLAR/VERI_TOPLAMA/Kayseri_SH/output_deneme_18.csv"

# Process the CSV files
process_csv(input_file_path, output_file_path)