def extract_metadata(file_reader):
    try:
        metadata = file_reader.df.info()
        print("Metadata:")
        print(metadata)
    except Exception as e:
        print(f"Error in extracting metadata: {e}")
