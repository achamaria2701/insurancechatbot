from src.pipeline.data_pipeline import DataPipeline
from src.utils import extract_dictionary_from_string


class GetTopInsurance():
    def __init__(self):
        pass

    def get_top_insurance(self, user_req_string):
        cleaned_laptop_df = DataPipeline().get_data()
        user_requirements = extract_dictionary_from_string(user_req_string)
        filtered_df = cleaned_laptop_df[(cleaned_laptop_df['Coverage Amount (₹)'] > int(user_requirements['Coverage Amount'])) & (cleaned_laptop_df['Daycare Procedures Covered'] == user_requirements['Daycare Procedures Covered']) & (cleaned_laptop_df['Critical Illness Cover'] == user_requirements['Critical Illness Cover']) & (cleaned_laptop_df['Co-payment Cover'] == user_requirements['Co-payment']) & (cleaned_laptop_df['Family Floater'] == user_requirements['Family Floater']) & (cleaned_laptop_df['Pre/Post Hospitalization Cover'] == user_requirements['Pre/Post Hospitalization Cover']) & (cleaned_laptop_df['Maternity Coverage'] == user_requirements['Maternity Cover'])].copy()
        filtered_df['Score'] = 0
        for index, row in filtered_df.iterrows():
            score = 0
            if row['Coverage Amount (₹)'] <= filtered_df['Coverage Amount (₹)'].quantile(0.25):
                score += 2
            elif row['Coverage Amount (₹)'] <= filtered_df['Coverage Amount (₹)'].quantile(0.5):
                score += 1
            
            if row['Network Hospitals'] >= filtered_df['Network Hospitals'].quantile(0.75):
                score += 2
            elif row['Network Hospitals'] >= filtered_df['Network Hospitals'].quantile(0.5):
                score += 1
                
            if row['No Claim Bonus (NCB) (%)'] >= filtered_df['No Claim Bonus (NCB) (%)'].quantile(0.75):
                score += 2
            elif row['No Claim Bonus (NCB) (%)'] >= filtered_df['No Claim Bonus (NCB) (%)'].quantile(0.5):
                score += 1
            
            if row['Room Rent Limit (₹)'] == "No Limit":
                score += 2
            elif row['No Claim Bonus (NCB) (%)'] >= filtered_df['No Claim Bonus (NCB) (%)'].quantile(0.75):
                score += 1
                
            if user_requirements['Critical Illness Cover'] == "Yes":
                if row['Critical Illness Waiting Period'] >= filtered_df['Critical Illness Waiting Period'].quantile(0.75):
                    score += 2
                elif row['Critical Illness Waiting Period'] >= filtered_df['Critical Illness Waiting Period'].quantile(0.5):
                    score += 1
                    
            if user_requirements['Co-payment'] == "Yes":
                if row['Co-payment (%)'] >= filtered_df['Co-payment (%)'].quantile(0.75):
                    score += 2
                elif row['Co-payment (%)'] >= filtered_df['Co-payment (%)'].quantile(0.5):
                    score += 1
            
            if row['Annual Premium (₹)'] >= filtered_df['Annual Premium (₹)'].quantile(0.75):
                score += 2
            elif row['Annual Premium (₹)'] >= filtered_df['Annual Premium (₹)'].quantile(0.5):
                score += 1
                
            if row['Claim Settlement Ratio (%)'] >= filtered_df['Claim Settlement Ratio (%)'].quantile(0.75):
                score += 2
            elif row['Claim Settlement Ratio (%)'] >= filtered_df['Claim Settlement Ratio (%)'].quantile(0.5):
                score += 1
            
            if row['Cashless Claim Process (Ease Rating)'] >= filtered_df['Cashless Claim Process (Ease Rating)'].quantile(0.75):
                score += 2
            elif row['Cashless Claim Process (Ease Rating)'] >= filtered_df['Cashless Claim Process (Ease Rating)'].quantile(0.5):
                score += 1
            
            if user_requirements['Pre/Post Hospitalization Cover'] == "Yes":
                if row['Pre Hospitalization (Days)'] >= filtered_df['Pre Hospitalization (Days)'].quantile(0.75):
                    score += 2
                elif row['Pre Hospitalization (Days)'] >= filtered_df['Pre Hospitalization (Days)'].quantile(0.5):
                    score += 1
                if row['Post Hospitalization (Days)'] >= filtered_df['Post Hospitalization (Days)'].quantile(0.75):
                    score += 2
                elif row['Post Hospitalization (Days)'] >= filtered_df['Post Hospitalization (Days)'].quantile(0.5):
                    score += 1
            
            if user_requirements['Maternity Cover'] == "Yes":
                if row['Maternity Caverage Waiting Period'] <= filtered_df['Maternity Caverage Waiting Period'].quantile(0.25):
                    score += 2
                elif row['Maternity Caverage Waiting Period'] <= filtered_df['Maternity Caverage Waiting Period'].quantile(0.5):
                    score += 1
            filtered_df.loc[index, 'Score'] = score
            
        top_insurance = filtered_df.sort_values('Score', ascending = False).head(3)
        return top_insurance.to_json(orient='records')