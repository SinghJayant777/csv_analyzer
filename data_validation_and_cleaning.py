import pandas as pd


def data_validation_and_cleaning(file_reader):
    try:
        # Handling missing values by dropping rows
        file_reader.df.dropna(inplace=True)
        print("\033[92m1. Missing values handled.\033[0m")

        # Removing redundant whitespaces
        file_reader.df = file_reader.df.apply(
            lambda x: x.str.strip() if x.dtype == 'O' else x)
        print("\033[92m2. Redundant whitespaces removed.\033[0m")

        # Removing special characters
        file_reader.df = file_reader.df.replace(
            '[^A-Za-z0-9 ]+', '', regex=True)
        print("\033[92m3. Special characters removed.\033[0m")

        # Standardizing text casing
        file_reader.df = file_reader.df.apply(
            lambda x: x.str.lower() if x.dtype == 'O' else x)
        print("\033[92m4. Casing standardized.\033[0m")

        # Standardizing date formats
        file_reader.df['registration_date'] = pd.to_datetime(
            file_reader.df['registration_date'])
        file_reader.df['last_login'] = pd.to_datetime(
            file_reader.df['last_login'])
        file_reader.df['subscription_expiry'] = pd.to_datetime(
            file_reader.df['subscription_expiry'])
        print("\033[92m5. Date formats standardized.\033[0m")

        print("\033[93mData validation and cleaning completed.\033[0m")
    except Exception as e:
        print(f"Error in data validation and cleaning: {e}")
