def query_and_filtering(file_reader, query):
    try:
        filtered_data = file_reader.df.query(query)
        print("Query and filtering results:")
        print(filtered_data)
    except Exception as e:
        print(f"Error in query and filtering: {e}")
