def column_statistics(file_reader):
    try:
        statistics = file_reader.df.describe()
        print("Column statistics:")
        print(statistics)
    except Exception as e:
        print(f"Error in column statistics: {e}")
