#!/usr/bin/env python3

import requests
import pandas as pd
import json
import csv
import os

# Define the URLs for your requests
url_1 = "http://"
url_2 = "http://"
url_3 = "http://"

# Define the username and password for Basic Authentication
username = ""
password = ""


if not os.path.exists("data.csv"): 
    sum_has_run = True
    control = True


if  os.path.exists("data.csv"): 
    sum_has_run = False
    control = False
    row_data = {}  # Dictionary to store the fetched data # If the system start again. It'll fetch data automatically.

    with open("data.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        first_row = next(csv_reader, None)  # Get the first row or None if the file is empty

        if first_row:
            # Assuming the first row contains the headers (keys)
            for i, header in enumerate(first_row):
                row_data[header] = None  # Initialize all keys with None

while True:

    # Check if the CSV file exists  
    if os.path.exists("data.csv"):
    
        with open("data.csv", "r", newline='') as csvfile:
            reader = csv.reader(csvfile)
            existing_headers = list(reader)  # Read the first row (header row)

    value = int(input("Enter the value: "))

    if value == 0:

        break
        
   

    # Construct the raw JSON payload using the user input
    payload_1 = json.dumps(value)

    try:


        # Step 1: Get data from URL 1
        response_1 = requests.post(url_1, auth=(username, password), data=payload_1, timeout=8)

        # Check if the request was successful (status code 200)
        if response_1.status_code == 200:
            data_1 = response_1.json()
        else:
            print("Failed to retrieve data from URL 1. Status code:", response_1.status_code)
            continue

        print("\n DATA 1 COMPLETED!... ")
        ######################################################

        # Step 2: Get data from URL 2
        payload_2 = json.dumps(value)
        response_2 = requests.post(url_2, auth=(username, password), data=payload_2)

        # Check if the request was successful (status code 200)
        if response_2.status_code == 200:
            data_2 = response_2.json()
        else:
            print("Failed to retrieve data from URL 2. Status code:", response_2.status_code)
            continue
        print("\n DATA2 COMPLETED!... ")

        # Desired ttestad values to filter # HERE
       
        
        desired_ttestads = [

        ["TAM KAN SAYIMI(HEMOGRAM)(22 PARAMETRE)", 
        "KAPPA HAFİF ZİNCİR (TOTAL)",
        "KAPPA HAFİF ZİNCİR (SERBEST)", 
        "KAPPA HAFİF ZİNCİR, TOTAL (SERUM)",
        "SERUM İMMÜNELEKTROFOREZİ", 
        "LAMBDA HAFİF ZİNCİR (SERBEST)"], 

        ["LAMBDA HAFİF ZİNCİR, SERBEST (SERUM/PLAZMA)",
        "KAPPA HAFİF ZİNCİR (SERBEST)", 
        "İMMÜN KOMPLEKS IGE (ÜNİTE/HACİM) (SERUM/PLAZMA)",
        "ALT (ALANİN TRANSFERAS)", 
        "AST (ASPARTAT TRANSANİNANZ)", 
        "LDH", 
        "GGT"],

        ["SEDİMANTASYON", 
        "PROTEİN ELEKTROFEREZİ", 
        "BETA-2 MİKROGLOBÜLİN", 
        "ALBUMİN",
        "VİTAMİN B12", 
        "FOLİK ASİT", 
        "FERRİTİN (SERUM/PLAZMA)", 
        "FERRİTİN"],

        ["SERBEST T4",
        "SERBEST T3", 
        "TSH",
        "DEMİR BAĞLAMA KAPASİTESİ",
        "DEMİR BAĞLAMA",
        "DEMİR(SERUM)",
        "DEMİR (SERUM/PLAZMA)",
        "UIBC", 
        "TOTAL PROTEİN"],

        ["POTASYUM (SERUM/PLAZMA)", 
        "DİREKT BİLİRUBİN", 
        "TOTAL BİLİRUBİN", 
        "POTASYUM", 
        "SODYUM", 
        "FOSFOR", 
        "KALSİYUM", 
        "MAGNEZYUM", 
        "FOSFOR (SERUM/PLAZMA)", 
        "KALSİYUM (SERUM/PLAZMA)"],

        ["ÜRİK ASİT", 
        "CKD_EPI", 
        "KREATİNİN", 
        "BUN", 
        "TRİGLİSERİD (SERUM/PLAZMA)", 
        "KOLESTEROL (SERUM/PLAZMA)", 
        "HDL KOLESTEROL", 
        "LDL KOLESTEROL (DİREKT)", 
        "GLUKOZ",
        "CRP, (TÜRBİDİMETRİK)"],

        ["PROTROMBİN ZAMANI PT",
         "ANTİ TROMBİN 3 AKTİVİTESİ",
         "D-DİMER",
         "TROMBİN TAYİNİ",
         "AKTİF PTT",
         "BİLİRUBİN, TOTAL (SERUM/PLAZMA)",
         "TOTAL BİLİRUBİN",
         "DİREKT BİLİRUBİN",
         "BİLİRUBİN, DİREKT (SERUM/PLAZMA)"],

         ["İDRAR TETKİKİ (TAM OTM.TARAMA AMAÇLI)", 
          "GRAM BOYAMA VE MİKROSKOBİK İNCELEME (VÜCUT SIVILARI - İDRAR)" 
          "TAM İDRAR STRİP KİM", 
          "KANTİTATİF IGA", 
          "KANTİTATİF IGE",
          "KANTİTATİF IGM",
          "KANTİTATİF IGG",
          "İMMÜN KOMPLEKS IGM (KÜTLE/HACİM) (SERUM/PLAZMA)"
         ],

         ["FİBRİNOJEN",
         "PROTEİN (SERUM/PLAZMA)" 
         "KEMİK İLİĞİ BOYAMA(WRIGHT YADA GIEMSA)", 
         "KAN KÜLTÜRÜ OTOMATİK SİSTEM (KATETERDEN ALINAN KAN)" 

         ]

        ]
        ######################################################
 
        data_1 = data_1[0]

        if sum_has_run:
            # Prepare the data to be added to the CSV file
            row_data = {
 
            "tdogumtarihi": data_1["tdogumtarihi"],
            "tcinsiyet": data_1["tcinsiyet"]
            }
            sum_has_run = False


        else: 

            row_data["tdogumtarihi"] = data_1["tdogumtarihi"]
            row_data["tcinsiyet"] = data_1["tcinsiyet"]

                

        
        for x_list in desired_ttestads:


            # Extract the "thastahizhareketid" values from the response of URL 2
            hareketid_list_orig = [item["thastahizhareketid"] for item in data_2 if item["ttestad"] in x_list] 

        

            # Remove the item(s) which is 'null'
            while hareketid_list_orig.__contains__(None):
                hareketid_list_orig.remove(None)


            thastahizhareketid_list = [eval(i) for i in hareketid_list_orig]


            # Step 3: Get data from URL 3
            payload_3 = json.dumps(thastahizhareketid_list)  


            print("LEN OF PAYLOAD 3 : ",len(payload_3))

            headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic bmV2YXNvZnQ6bmV2YTEyMzQ1Ng==',
            'Cookie': 'JSESSIONID=44184A3409294C7E9D4681BA93D9D366'
            }

        
            response_3 = requests.post(url_3, auth=(username, password), headers=headers, data=payload_3)

            # Check if the request was successful (status code 200)
            if response_3.status_code == 200:
                data_3 = response_3.json()
            else:
                print("Failed to retrieve data from URL 3. Status code:", response_3.status_code)
                continue

            print("\n DATA 3 COMPLETED!... ")
            

            for data_3 in data_3:

                if data_3["tpadi"] not in row_data:

                    row_data[data_3["tpadi"]] = [data_3["tdegerNum"]]
                    row_data[data_3["tpadi"] + "_" + "tislemtar"] = [data_3["tislemtar"]]
                    row_data[data_3["tpadi"] + "_" + "tbirim"] = data_3["tbirim"]
                    row_data[data_3["tpadi"] + "_" + "taltLim_n"] = data_3["taltLim_n"]
                    row_data[data_3["tpadi"] + "_" + "tustLim_n"] = data_3["tustLim_n"]

                    if not control: 

                        if data_3["tpadi"] not in existing_headers:


                            existing_headers[0].append(data_3["tpadi"])
                            existing_headers[0].append(data_3["tpadi"] + "_" + "tislemtar")
                            existing_headers[0].append(data_3["tpadi"] + "_" + "tbirim")
                            existing_headers[0].append(data_3["tpadi"] + "_" + "taltLim_n")
                            existing_headers[0].append(data_3["tpadi"] + "_" + "tustLim_n")


                            with open("data.csv", "w", newline="") as csvfile:

                                writer = csv.writer(csvfile)
                                writer.writerows(existing_headers)


                else:
                    if row_data[data_3["tpadi"]] is None:
                        
                        row_data[data_3["tpadi"]] = [data_3["tdegerNum"]]
                        row_data[data_3["tpadi"] + "_" + "tislemtar"] = [data_3["tislemtar"]]
                        row_data[data_3["tpadi"] + "_" + "tbirim"] = data_3["tbirim"]
                        row_data[data_3["tpadi"] + "_" + "taltLim_n"] = data_3["taltLim_n"]
                        row_data[data_3["tpadi"] + "_" + "tustLim_n"] = data_3["tustLim_n"]

                    else:

                        row_data[data_3["tpadi"]].append(data_3["tdegerNum"])
                        row_data[data_3["tpadi"] + "_" + "tislemtar"].append(data_3["tislemtar"])

                    

        # Append the row data to the CSV file
        with open("data.csv", "a", newline="") as csvfile:

            writer = csv.DictWriter(csvfile, fieldnames=row_data.keys())

            if control:
                writer.writeheader()
                control = False

            writer.writerow(row_data)

        for key in row_data: 
            row_data[key] = None
        ######################################################

    except ValueError:
        print("Invalid JSON format. Please try again.")
    except requests.Timeout:
        print("Request timed out. Please try again.")
    except requests.RequestException as e:
        print("Request error:", str(e))        