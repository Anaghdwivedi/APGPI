import streamlit as st
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from webscrap import search

# Authenticate with Google Sheets
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('apgpi-413305-7d492ed17ac3.json', scope)
# client = gspread.authorize(creds)

# Open the Google Sheet
# sheet = client.open('APGPI').sheet1  # Replace with your sheet name

# Streamlit app
st.title('Job Search App')

# Input fields
job_title = st.text_input('Enter Job Title:')
skills = st.text_input('Enter Skills:')
years_of_experience = st.number_input('Enter Years of Experience:', min_value=0, max_value=50, value=0)
minimum_education = st.selectbox('Select Minimum Education:', ['High School', 'Bachelor', 'Master', 'PhD'])
location = st.text_input('Enter Location:')

# Button to search
# if st.button('Search Jobs'):
#     # Get all data from the Google Sheet
#     all_data = sheet.get_all_records()

#     # Filter the data based on input criteria
#     filtered_data = [entry for entry in all_data
#                      if job_title.lower() in entry['Job Title'].lower()
#                      and all(skill.lower() in entry['Skills'].lower() for skill in skills.split(','))
#                      and entry['Years of Experience'] >= years_of_experience
#                      and entry['Minimum Education'].lower() == minimum_education.lower()
#                      and location.lower() in entry['Location'].lower()]

#     # Display the filtered data
#     if filtered_data:
#         df = pd.DataFrame(filtered_data)
#         st.table(df)
#     else:
#         st.warning('No matching jobs found.')
import csv

if len(job_title)!=0:
    a = search(job_title)
    print(a)



    def append_to_csv(file_path, a):
        # Open the CSV file in append mode
        with open(file_path, mode='a', newline='') as file:
            # Create a CSV writer object
            writer = csv.writer(file)

            # Write the data to the CSV file
            writer.writerow(a)

    # Example usage
    csv_file_path = 'example.csv'

    # Data to append (replace this with your actual data)
    data_to_append = a

    # Call the function to append data to the CSV file
    append_to_csv(csv_file_path, data_to_append)
    st.text('required output is :')
    st.write(a[0])
    
