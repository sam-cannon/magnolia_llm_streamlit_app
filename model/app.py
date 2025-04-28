import streamlit as st
import os
import pandas as pd
from pathlib import Path

st.title("CSV File Metrics Analyzer")

# Input for directory path
directory_path = st.text_input("Enter the directory path to analyze:", value=".")

# Button to trigger analysis
if st.button("Analyze CSV Files"):
    if not os.path.isdir(directory_path):
        st.error("Please enter a valid directory path.")
    else:
        csv_metrics = []
        
        # Walk through directory
        for root, _, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.csv'):
                    file_path = Path(root) / file
                    try:
                        # Read CSV
                        df = pd.read_csv(file_path)
                        
                        # Calculate metrics
                        metrics = {
                            'File Name': file,
                            'Path': str(file_path),
                            'Number of Rows': len(df),
                            'Number of Columns': len(df.columns),
                            'File Size (KB)': round(file_path.stat().st_size / 1024, 2),
                            'Column Names': ', '.join(df.columns)
                        }
                        csv_metrics.append(metrics)
                    except Exception as e:
                        st.warning(f"Could not process {file}: {str(e)}")
        
        # Display results
        if csv_metrics:
            st.subheader("CSV Files Found and Their Metrics")
            # Convert to DataFrame for better display
            metrics_df = pd.DataFrame(csv_metrics)
            st.dataframe(metrics_df)
            
            # Summary statistics
            st.subheader("Summary")
            st.write(f"Total CSV Files Found: {len(csv_metrics)}")
            st.write(f"Total Rows Across All Files: {metrics_df['Number of Rows'].sum()}")
            st.write(f"Total Columns Across All Files: {metrics_df['Number of Columns'].sum()}")
            st.write(f"Total File Size (KB): {metrics_df['File Size (KB)'].sum():.2f}")
        else:
            st.info("No CSV files found in the specified directory.")

# Instructions for running the app
st.markdown("""
### How to Run This App
1. Save this code as `csv_metrics_app.py`
2. Install required packages: `pip install streamlit pandas`
3. Run the app: `streamlit run csv_metrics_app.py`
4. Open the provided URL in your browser
5. Enter a directory path and click 'Analyze CSV Files'
""")