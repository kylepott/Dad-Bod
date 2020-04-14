import pandas as pd_mfp

df_mfp = pd_mfp.read_excel("mfp.xlsx")
df_clean_columns_mfp = df_mfp.rename(columns={"Date": "weigh_in_date", "Body Fat %": "B", "Fitbit steps": "C" , "Waist": "D", "Weight": "weight"}, errors="raise")
df_clean_columns_rows_mfp_2 = df_clean_columns_mfp.drop(columns=['B', 'C', 'D'], axis=1)
df_clean_columns_rows_mfp_2 = df_clean_columns_rows_mfp_2.dropna(subset=['weight'])
df_clean_columns_rows_mfp_2["weight"] = pd_mfp.to_numeric(df_clean_columns_rows_mfp_2["weight"], downcast="float")
df_clean_columns_rows_mfp_2.to_excel("MFPClean.xlsx", engine='xlsxwriter', index=False)
print("done without errors")
df_clean_columns_rows_mfp_2

