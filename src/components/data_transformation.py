import regex as re

class DataTransformation():

    def __init__(self):
        pass
    
    def process_maternity_data(self, x):
        years = re.findall(r'\d', x)
        if len(years) == 0:
            return 0
        else:
            return years[0]
        

    def preprocess_laptop_data(self, df):
        df['Maternity Coverage'] = df['Maternity & Newborn Coverage'].apply(lambda x: x.split(" ")[0])
        df['Maternity Caverage Waiting Period'] = df['Maternity & Newborn Coverage'].apply(self.process_maternity_data)
        df.drop(['Maternity & Newborn Coverage'], inplace=True, axis=1)
        df.rename(columns={'Waiting Period (Years)': 'Critical Illness Waiting Period'}, inplace=True)
        df[['Coverage Amount (₹)', 'Network Hospitals', 'No Claim Bonus (NCB) (%)', 'Critical Illness Waiting Period', 'Co-payment (%)', 'Claim Settlement Ratio (%)', 'Cashless Claim Process (Ease Rating)', 'Pre Hospitalization (Days)', 'Post Hospitalization (Days)', 'Maternity Caverage Waiting Period']] = df[['Coverage Amount (₹)', 'Network Hospitals', 'No Claim Bonus (NCB) (%)', 'Critical Illness Waiting Period', 'Co-payment (%)', 'Claim Settlement Ratio (%)', 'Cashless Claim Process (Ease Rating)', 'Pre Hospitalization (Days)', 'Post Hospitalization (Days)', 'Maternity Caverage Waiting Period']].astype(int) 
        df['Co-payment Cover'] = df['Co-payment (%)'].apply(lambda x: "Yes" if x != 0 else "No")
        df['Pre/Post Hospitalization Cover'] = df['Pre Hospitalization (Days)'].apply(lambda x: "Yes" if x != 0 else "No")
        return df
    
    