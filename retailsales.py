import pandas as pd 
import numpy as np

class RetailSalesAnalyzer:
    def __init__(self, data):
        self.data = data
    def load_data(self):
        try:
            df = pd.read_csv(self.data)
        except Exception as e :
            print("Error in loading data", e)
        else:
            return df

    def clean_data(self):
        df = self.load_data()
        df.dropna(inplace=True)
        return df
    
    def analyze_data(self):
        cleaned_data = self.clean_data()
        total_for_each_product = cleaned_data.groupby('Product')['Sales'].sum()
        best_seller = total_for_each_product.idxmax()
        compute_average_sales = cleaned_data['Sales'].mean()

        return total_for_each_product,best_seller, compute_average_sales
r1 = RetailSalesAnalyzer('retail_sales.csv')
print(r1.analyze_data())