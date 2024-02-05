def export_results(file_reader, output_file_path):
    try:
        file_reader.df.to_csv(output_file_path, index=False)
        print(f"Results exported to {output_file_path}")
    except Exception as e:
        print(f"Error in exporting results: {e}")
