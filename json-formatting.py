import pandas as pd
import json


#processing nested dictionary
def process_json1(json_data):
    df_list = []
    for category, cat_data in json_data.items():
        df_cat = pd.DataFrame(cat_data)
        df_cat['Category'] = category
        df_list.append(df_cat)
    return pd.concat(df_list, ignore_index=True)

#processing list of dictionary
def process_json2(json_data):
    return pd.DataFrame(json_data)

#processing flattened json
def process_json3(json_data):
    campaigns = []
    for i in range(20):  # Assuming 20 items as per your example
        campaign = {
        "campaign_id": json_data[f"campaign_id_{i}"],
        "campaign_name": json_data[f"campaign_name_{i}"],
        "clicks": json_data[f"clicks_{i}"],
        "conversions": json_data[f"conversions_{i}"],
        "cost": json_data[f"cost_{i}"],
        "impressions": json_data[f"impressions_{i}"],
        "conversion_value": json_data[f"conversion_value_{i}"],
        "CPA": json_data[f"CPA_{i}"],
        "CTR": json_data[f"CTR_{i}"],
        "ROAS": json_data[f"ROAS_{i}"],
        "scenario": json_data[f"scenario_{i}"],
        "reasoning": json_data[f"reasoning_{i}"],
        }
        campaigns.append(campaign)
    return pd.DataFrame(campaigns)
      
# Function to detect JSON format and process accordingly
def detect_and_process_json(json_data):
    if isinstance(json_data, dict) and all(isinstance(value, dict) for value in json_data.values()):
        return process_json1(json_data)
    elif isinstance(json_data, list) and all(isinstance(item, dict) for item in json_data):
        return process_json2(json_data)
    elif isinstance(json_data, dict) and any(key.startswith('campaign_id_') for key in json_data):
        return process_json3(json_data)
    else:
        raise ValueError("Unsupported JSON format")
    
    
json1={
  "stop": {
    "campaign_id": {
      "0": 19785409662,
      "1": 19785409662,
      "11": 20982516907,
      "14": 20992846507,
      "16": 20998677335
    },
    "campaign_name": {
      "0": "Clearance Sale - 2023",
      "1": "Selected Category - Sale - 2024",
      "11": "Lighting | Mayyank - Keyword",
      "14": "Demand Gen – 2024-02-01",
      "16": "Mayyank_P_Max _Customer_Match"
    },
    "revenue": {
      "0": 79753,
      "1": 27740,
      "11": 50873,
      "14": 342,
      "16": 4375
    },
    "cost": {
      "0": 525766,
      "1": 182875,
      "11": 136253,
      "14": 68142,
      "16": 41543
    },
    "ROAS": {
      "0": 0.15168915449078108,
      "1": 0.15168831168831168,
      "11": 0.3733715954878058,
      "14": 0.00501893105573655,
      "16": 0.10531256770093637
    },
    "Reasoning": {
      "0": "Low ROAS. ROAS < 1. ",
      "1": "Low ROAS. ROAS < 1. ",
      "11": "Low ROAS. ROAS < 1. ",
      "14": "Low ROAS. ROAS < 1. ",
      "16": "Low ROAS. ROAS < 1. "
    }
  },
  "continue": {
    "campaign_id": {
      "2": 16541551188,
      "3": 19797614576,
      "4": 20525429499,
      "5": 19797614576,
      "6": 16541551188,
      "7": 19798568578,
      "8": 19797614576,
      "9": 19798568578,
      "10": 20263173793,
      "12": 20525429499,
      "13": 20966701834,
      "17": 20977281338,
      "18": 20989518467,
      "19": 19642167054
    },
    "campaign_name": {
      "2": "Search_Brand-Mayyank",
      "3": "Sale_P_Max _ALL Product_Remarketing",
      "4": "EN_Sale_P Max _PIN Code",
      "5": "Mayyank_P_Max _ALL Product_Remarketing",
      "6": "EN_Search_Brand",
      "7": "Sale - 2023 - Performance - 2",
      "8": "EN_Sale_P Max _ALL Product _Remarketing",
      "9": "Clearance Sale - 2023 - Performance - 2",
      "10": "Pmax_TDK New Audience_Mayyank",
      "12": "Sale_P Max _PIN Code",
      "13": "Sale_Pmax_Decor",
      "17": "Sale - 2024 - Performance Max",
      "18": "Sale Video Campaign - 2024",
      "19": "Lighting | Mayyank #2"
    },
    "revenue": {
      "2": 28410172,
      "3": 1851624,
      "4": 992538,
      "5": 10845224,
      "6": 6127684,
      "7": 5872213,
      "8": 3703247,
      "9": 7612128,
      "10": 3337841,
      "12": 4601769,
      "13": 263570,
      "17": 3626128,
      "18": 265493,
      "19": 15195076
    },
    "cost": {
      "2": 2191928,
      "3": 383847,
      "4": 278503,
      "5": 2248245,
      "6": 472769,
      "7": 1125427,
      "8": 767693,
      "9": 1458886,
      "10": 1118894,
      "12": 1291243,
      "13": 108773,
      "17": 731651,
      "18": 63178,
      "19": 2168446
    },
    "ROAS": {
      "2": 12.961270625677486,
      "3": 4.82385950652213,
      "4": 3.5638323465097326,
      "5": 4.823862168046632,
      "6": 12.961264380701781,
      "7": 5.217764457401501,
      "8": 4.823864487496955,
      "9": 5.217767529471117,
      "10": 2.9831610501084107,
      "12": 3.5638288068163777,
      "13": 2.423119708015776,
      "17": 4.956089720372145,
      "18": 4.2023014340434965,
      "19": 7.007357342539311
    },
    "Reasoning": {
      "2": "High ROAS. ROAS > 2. ",
      "3": "High ROAS. ROAS > 2. ",
      "4": "High ROAS. ROAS > 2. ",
      "5": "High ROAS. ROAS > 2. ",
      "6": "High ROAS. ROAS > 2. ",
      "7": "High ROAS. ROAS > 2. ",
      "8": "High ROAS. ROAS > 2. ",
      "9": "High ROAS. ROAS > 2. ",
      "10": "High ROAS. ROAS > 2. ",
      "12": "High ROAS. ROAS > 2. ",
      "13": "High ROAS. ROAS > 2. ",
      "17": "High ROAS. ROAS > 2. ",
      "18": "High ROAS. ROAS > 2. ",
      "19": "High ROAS. ROAS > 2. "
    }
  },
  "optimise": {
    "campaign_id": {},
    "campaign_name": {},
    "revenue": {},
    "cost": {},
    "ROAS": {},
    "Reasoning": {}
  }
}


json2=[
  {
    "campaign_id": 20989518467,
    "campaign_name": "Sale Video Campaign - 2024",
    "revenue": 265492.5,
    "cost": 63178.09
  },
  {
    "campaign_id": 20525429499,
    "campaign_name": "EN_Sale_P Max _PIN Code",
    "revenue": 992538.34,
    "cost": 278503.37
  },
  {
    "campaign_id": 19797614576,
    "campaign_name": "EN_Sale_P Max _ALL Product _Remarketing",
    "revenue": 3703247.17,
    "cost": 767693.49
  },
  {
    "campaign_id": 19785409662,
    "campaign_name": "Clearance Sale - 2023",
    "revenue": 79752.5,
    "cost": 525766.09
  },
  {
    "campaign_id": 16541551188,
    "campaign_name": "Search_Brand-Mayyank",
    "revenue": 28410171.91,
    "cost": 2191927.98
  },
  {
    "campaign_id": 19797614576,
    "campaign_name": "Sale_P_Max _ALL Product_Remarketing",
    "revenue": 1851623.58,
    "cost": 383846.74
  },
  {
    "campaign_id": 19785409662,
    "campaign_name": "Selected Category - Sale - 2024",
    "revenue": 27740,
    "cost": 182875.16
  },
  {
    "campaign_id": 832958820,
    "campaign_name": "Brand Name - Mayyank",
    "revenue": 0,
    "cost": 0
  },
  {
    "campaign_id": 20992846507,
    "campaign_name": "Demand Gen – 2024-02-01",
    "revenue": 342.34,
    "cost": 68142.13
  },
  {
    "campaign_id": 20998677335,
    "campaign_name": "Mayyank_P_Max _Customer_Match",
    "revenue": 4375,
    "cost": 41542.55
  },
  {
    "campaign_id": 20982516907,
    "campaign_name": "Lighting | Mayyank - Keyword",
    "revenue": 50872.5,
    "cost": 136253.44
  },
  {
    "campaign_id": 19642167054,
    "campaign_name": "Lighting | Mayyank #2",
    "revenue": 15195076.11,
    "cost": 2168446.25
  },
  {
    "campaign_id": 19797614576,
    "campaign_name": "Mayyank_P_Max _ALL Product_Remarketing",
    "revenue": 10845223.85,
    "cost": 2248245.21
  },
  {
    "campaign_id": 20966701834,
    "campaign_name": "Sale_Pmax_Decor",
    "revenue": 263570.25,
    "cost": 108772.73
  },
  {
    "campaign_id": 20263173793,
    "campaign_name": "Pmax_TDK New Audience_Mayyank",
    "revenue": 3337841.29,
    "cost": 1118894.01
  },
  {
    "campaign_id": 19798568578,
    "campaign_name": "Clearance Sale - 2023 - Performance - 2",
    "revenue": 7612128.21,
    "cost": 1458886.27
  },
  {
    "campaign_id": 19798568578,
    "campaign_name": "Sale - 2023 - Performance - 2",
    "revenue": 5872213.19,
    "cost": 1125426.55
  },
  {
    "campaign_id": 16541551188,
    "campaign_name": "EN_Search_Brand",
    "revenue": 6127684.14,
    "cost": 472768.78
  },
  {
    "campaign_id": 20977281338,
    "campaign_name": "Sale - 2024 - Performance Max",
    "revenue": 3626127.68,
    "cost": 731651.18
  },
  {
    "campaign_id": 20525429499,
    "campaign_name": "Sale_P Max _PIN Code",
    "revenue": 4601768.66,
    "cost": 1291242.89
  }
]

json3={
  "campaign_id_0": 20525429499,
  "campaign_id_1": 19797614576,
  "campaign_id_2": 20989518467,
  "campaign_id_3": 20263173793,
  "campaign_id_4": 19798568578,
  "campaign_id_5": 19785409662,
  "campaign_id_6": 20977281338,
  "campaign_id_7": 20966701834,
  "campaign_id_8": 19797614576,
  "campaign_id_9": 20525429499,
  "campaign_id_10": 19642167054,
  "campaign_id_11": 20982516907,
  "campaign_id_12": 19785409662,
  "campaign_id_13": 19798568578,
  "campaign_id_14": 16541551188,
  "campaign_id_15": 16541551188,
  "campaign_id_16": 19797614576,
  "campaign_id_17": 832958820,
  "campaign_id_18": 20992846507,
  "campaign_id_19": 20998677335,
  "campaign_name_0": "EN_Sale_P Max _PIN Code",
  "campaign_name_1": "EN_Sale_P Max _ALL Product _Remarketing",
  "campaign_name_2": "Sale Video Campaign - 2024",
  "campaign_name_3": "Pmax_TDK New Audience_Mayyank",
  "campaign_name_4": "Clearance Sale - 2023 - Performance - 2",
  "campaign_name_5": "Selected Category - Sale - 2024",
  "campaign_name_6": "Sale - 2024 - Performance Max",
  "campaign_name_7": "Sale_Pmax_Decor",
  "campaign_name_8": "Mayyank_P_Max _ALL Product_Remarketing",
  "campaign_name_9": "Sale_P Max _PIN Code",
  "campaign_name_10": "Lighting | Mayyank #2",
  "campaign_name_11": "Lighting | Mayyank - Keyword",
  "campaign_name_12": "Clearance Sale - 2023",
  "campaign_name_13": "Sale - 2023 - Performance - 2",
  "campaign_name_14": "EN_Search_Brand",
  "campaign_name_15": "Search_Brand-Mayyank",
  "campaign_name_16": "Sale_P_Max _ALL Product_Remarketing",
  "campaign_name_17": "Brand Name - Mayyank",
  "campaign_name_18": "Demand Gen – 2024-02-01",
  "campaign_name_19": "Mayyank_P_Max _Customer_Match",
  "clicks_0": 45837,
  "clicks_1": 181132,
  "clicks_2": 39872,
  "clicks_3": 217186,
  "clicks_4": 213115,
  "clicks_5": 27008,
  "clicks_6": 119510,
  "clicks_7": 7944,
  "clicks_8": 530458,
  "clicks_9": 212517,
  "clicks_10": 246698,
  "clicks_11": 307278,
  "clicks_12": 77648,
  "clicks_13": 164403,
  "clicks_14": 50303,
  "clicks_15": 233223,
  "clicks_16": 90566,
  "clicks_17": 0,
  "clicks_18": 63868,
  "clicks_19": 5620,
  "conversions_0": 252.45,
  "conversions_1": 882.2,
  "conversions_2": 84,
  "conversions_3": 1264.35,
  "conversions_4": 2086.55,
  "conversions_5": 29.99,
  "conversions_6": 828.36,
  "conversions_7": 48.31,
  "conversions_8": 2583.57,
  "conversions_9": 1170.43,
  "conversions_10": 2218.44,
  "conversions_11": 18.51,
  "conversions_12": 86.21,
  "conversions_13": 1609.62,
  "conversions_14": 1285.18,
  "conversions_15": 5958.57,
  "conversions_16": 441.1,
  "conversions_17": 0,
  "conversions_18": 0.55,
  "conversions_19": 5,
  "cost_0": 2666.46,
  "cost_1": 7229.8,
  "cost_2": 631.78,
  "cost_3": 11188.94,
  "cost_4": 13864.16,
  "cost_5": 1828.75,
  "cost_6": 7316.51,
  "cost_7": 622.8,
  "cost_8": 21173,
  "cost_9": 12362.68,
  "cost_10": 20865.62,
  "cost_11": 1362.53,
  "cost_12": 5257.66,
  "cost_13": 10695.21,
  "cost_14": 4414.54,
  "cost_15": 20467.43,
  "cost_16": 3614.9,
  "cost_17": 0,
  "cost_18": 681.42,
  "cost_19": 415.43,
  "impressions_0": 3063577,
  "impressions_1": 11634742,
  "impressions_2": 2628640,
  "impressions_3": 13765984,
  "impressions_4": 16781345,
  "impressions_5": 2523680,
  "impressions_6": 7568669,
  "impressions_7": 572760,
  "impressions_8": 34073173,
  "impressions_9": 14203857,
  "impressions_10": 21067600,
  "impressions_11": 7208874,
  "impressions_12": 7255580,
  "impressions_13": 12945609,
  "impressions_14": 106172,
  "impressions_15": 492252,
  "impressions_16": 5817371,
  "impressions_17": 62,
  "impressions_18": 3819396,
  "impressions_19": 431200,
  "conversion_value_0": 96607.91,
  "conversion_value_1": 332968.37,
  "conversion_value_2": 26549.25,
  "conversion_value_3": 333784.13,
  "conversion_value_4": 758944.83,
  "conversion_value_5": 2774,
  "conversion_value_6": 362612.77,
  "conversion_value_7": 17541.63,
  "conversion_value_8": 975121.65,
  "conversion_value_9": 447909.38,
  "conversion_value_10": 1392937.71,
  "conversion_value_11": 5087.25,
  "conversion_value_12": 7975.25,
  "conversion_value_13": 585471.72,
  "conversion_value_14": 598369.22,
  "conversion_value_15": 2774257.3,
  "conversion_value_16": 166484.18,
  "conversion_value_17": 0,
  "conversion_value_18": 34.23,
  "conversion_value_19": 437.5,
  "CPA_0": 10.56,
  "CPA_1": 8.2,
  "CPA_2": 7.52,
  "CPA_3": 8.85,
  "CPA_4": 6.64,
  "CPA_5": 60.98,
  "CPA_6": 8.83,
  "CPA_7": 12.89,
  "CPA_8": 8.2,
  "CPA_9": 10.56,
  "CPA_10": 9.41,
  "CPA_11": 73.61,
  "CPA_12": 60.99,
  "CPA_13": 6.64,
  "CPA_14": 3.43,
  "CPA_15": 3.43,
  "CPA_16": 8.2,
  "CPA_17": 0,
  "CPA_18": 1238.95,
  "CPA_19": 83.09,
  "CTR_0": 0.01,
  "CTR_1": 0.02,
  "CTR_2": 0.02,
  "CTR_3": 0.02,
  "CTR_4": 0.01,
  "CTR_5": 0.01,
  "CTR_6": 0.02,
  "CTR_7": 0.01,
  "CTR_8": 0.02,
  "CTR_9": 0.01,
  "CTR_10": 0.01,
  "CTR_11": 0.04,
  "CTR_12": 0.01,
  "CTR_13": 0.01,
  "CTR_14": 0.47,
  "CTR_15": 0.47,
  "CTR_16": 0.02,
  "CTR_17": 0,
  "CTR_18": 0.02,
  "CTR_19": 0.01,
  "ROAS_0": 36.23,
  "ROAS_1": 46.05,
  "ROAS_2": 42.02,
  "ROAS_3": 29.83,
  "ROAS_4": 54.74,
  "ROAS_5": 1.52,
  "ROAS_6": 49.56,
  "ROAS_7": 28.17,
  "ROAS_8": 46.05,
  "ROAS_9": 36.23,
  "ROAS_10": 66.76,
  "ROAS_11": 3.73,
  "ROAS_12": 1.52,
  "ROAS_13": 54.74,
  "ROAS_14": 135.55,
  "ROAS_15": 135.54,
  "ROAS_16": 46.05,
  "ROAS_17": 0,
  "ROAS_18": 0.05,
  "ROAS_19": 1.05,
  "scenario_0": "Campaign is too new to assess the performance",
  "scenario_1": "Cost-Effective Scenario",
  "scenario_2": "Cost-Effective Scenario",
  "scenario_3": "Cost-Effective Scenario",
  "scenario_4": "Campaign is too new to assess the performance",
  "scenario_5": "Campaign is too new to assess the performance",
  "scenario_6": "Cost-Effective Scenario",
  "scenario_7": "Campaign is too new to assess the performance",
  "scenario_8": "Cost-Effective Scenario",
  "scenario_9": "Campaign is too new to assess the performance",
  "scenario_10": "Campaign is too new to assess the performance",
  "scenario_11": "High-Performance Scenario",
  "scenario_12": "Campaign is too new to assess the performance",
  "scenario_13": "Campaign is too new to assess the performance",
  "scenario_14": "High-Performance Scenario",
  "scenario_15": "High-Performance Scenario",
  "scenario_16": "Cost-Effective Scenario",
  "scenario_17": "Reassess Scenario",
  "scenario_18": "Reassess Scenario",
  "scenario_19": "Campaign is too new to assess the performance",
  "reasoning_0": "N/A",
  "reasoning_1": "CPA < 300, CTR > 0.01, ROAS >= 1",
  "reasoning_2": "CPA < 300, CTR > 0.01, ROAS >= 1",
  "reasoning_3": "CPA < 300, CTR > 0.01, ROAS >= 1",
  "reasoning_4": "N/A",
  "reasoning_5": "N/A",
  "reasoning_6": "CPA < 300, CTR > 0.01, ROAS >= 1",
  "reasoning_7": "N/A",
  "reasoning_8": "CPA < 300, CTR > 0.01, ROAS >= 1",
  "reasoning_9": "N/A",
  "reasoning_10": "N/A",
  "reasoning_11": "ROAS > 1.5, CPA < 300, CTR > 0.025",
  "reasoning_12": "N/A",
  "reasoning_13": "N/A",
  "reasoning_14": "ROAS > 1.5, CPA < 300, CTR > 0.025",
  "reasoning_15": "ROAS > 1.5, CPA < 300, CTR > 0.025",
  "reasoning_16": "CPA < 300, CTR > 0.01, ROAS >= 1",
  "reasoning_17": "ROAS < 1, CPA > 700, CTR < 0.01",
  "reasoning_18": "ROAS < 1, CPA > 700, CTR < 0.01",
  "reasoning_19": "N/A"
}


# Main script starts here
if __name__ == "__main__":
    #json_str = input("Enter your JSON data: ")
    #json_str=json1
    #json_str=json2
    json_str=json3
    
    try:
        # Parse the JSON string input by the user into a Python object
        #json_data = json.loads(json_str)
        
        # Process the JSON data
        df = detect_and_process_json(json_str)
        
        # Print the resulting DataFrame
        print(df.head())
        
        # Save the DataFrame to a CSV file
        csv_file_name = "output.csv"
        df.to_csv(csv_file_name, index=False)
        print(f"DataFrame saved to {csv_file_name}")
        
    except ValueError as e:
        print(f"Error processing JSON input: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")