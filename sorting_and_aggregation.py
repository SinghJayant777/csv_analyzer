def sorting_and_aggregation(file_reader, column_name):
    try:
        sorted_data = file_reader.df.sort_values(by=column_name)
        aggregated_data = file_reader.df.groupby(column_name).size()
        
        print("Sorted data:")
        print(sorted_data)
        print("Aggregated data:")
        print(aggregated_data)
    except Exception as e:
        print(f"Error in sorting and aggregation: {e}")
