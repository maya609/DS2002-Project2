import pandas as pd

def etl_netflix_data(input_path='netflix_titles.csv', output_path='cleaned_netflix.csv'):
    try:
        # Extract
        df = pd.read_csv(input_path)

        # Transform
        df = df.dropna(subset=['title', 'type', 'release_year'])  # essential info
        df = df.drop(columns=['show_id', 'description'], errors='ignore')  # optional
        df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
        df = df[df['date_added'].notna()]

        # Load
        df.to_csv(output_path, index=False)
        print(f"ETL completed. Cleaned data saved to: {output_path}")
    except Exception as e:
        print(f"ETL failed: {e}")

# Example usage
if __name__ == '__main__':
    etl_netflix_data()
