import pandas as pd
import os
from datetime import date

def hol_management_system():
    file_name = 'Office_Database.xlsx'
    
    while True: # Ye loop entries leta rahegacf5
        print("\n" + "="*40)
        print("   OFFICE DATA BASE - ADMISSION SYSTEM   ")
        print("="*40)
            
        # User se data lena
        name = input("Student Name (ya 'exit' likhein band karne ke liye): ")
        
        # Agar user 'exit' likhe toh loop band ho jaye
        if name.lower() == 'exit':
            print("System band ho raha hai... apki excel file ready hai apne folders main dekhen")
            break
            
        course = input("Course name : ")
        fee = input("Fee Status (Paid/Pending): ")
        today = date.today().strftime("%d-%m-%Y")

        new_data = {
            'Name': [name],
            'Course': [course], 
            'Fee_Status': [fee], 
            'Admission_Date': [today]
        }
        df_new = pd.DataFrame(new_data)

        # Excel mein save karne ka logic
        if not os.path.isfile(file_name):
            df_new.to_excel(file_name, index=False)
        else:
            existing_df = pd.read_excel(file_name)
            combined_df = pd.concat([existing_df, df_new], ignore_index=True)
            combined_df.to_excel(file_name, index=False)
        
        print(f"\n[Done] {name} ka record save ho gaya!")
        print("Agli entry karein ya 'exit' likh kar software band karein.")

if __name__ == "__main__":
    hol_management_system()