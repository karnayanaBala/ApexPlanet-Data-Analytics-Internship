import pandas as pd

df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# Data Dictionary
data_dict = {
    'Column': df.columns.tolist(),
    'Data_Type': [str(df[col].dtype) for col in df.columns],
    'Null_Count': [df[col].isnull().sum() for col in df.columns],
    'Unique_Values': [df[col].nunique() for col in df.columns],
    'Sample_Value': [df[col].iloc[0] for col in df.columns],
    'Business_Meaning': [
        'Unique order number',
        'Quantity of items ordered',
        'Price of each item',
        'Order line number',
        'Total sales amount',
        'Date of order',
        'Order status',
        'Quarter ID',
        'Month ID',
        'Year ID',
        'Product line/category',
        'Manufacturer suggested retail price',
        'Product code',
        'Customer name',
        'Phone number',
        'Address line 1',
        'Address line 2',
        'City',
        'State',
        'Postal code',
        'Country',
        'Territory',
        'Contact last name',
        'Contact first name',
        'Deal size'
    ]
}

dd_df = pd.DataFrame(data_dict)
dd_df.to_csv('data_dictionary.csv', index=False)
print("Data Dictionary saved!")
print(dd_df)