import argparse
import pandas as pd
from data_validation_and_cleaning import data_validation_and_cleaning
from column_statistics import column_statistics
from query_and_filtering import query_and_filtering
from sorting_and_aggregation import sorting_and_aggregation
from data_visualization import data_visualization
from exporting_results import export_results
from data_transformation import data_transformation
from error_handling import error_handling
from extract_metadata import extract_metadata


class CSVFileReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def read_and_parse_csv(self):
        try:
            self.df = pd.read_csv(self.file_path)
            print("CSV file read and parsed successfully.")
        except Exception as e:
            print(f"Error reading CSV file: {e}")

    def export_results(self, output_file_path):
        try:
            self.df.to_csv(output_file_path, index=False)
            print(f"Results exported to {output_file_path}")
        except Exception as e:
            print(f"Error in exporting results: {e}")

    def data_transformation(self):
        # Implement data transformation logic here
        pass

    def error_handling(self):
        # Implement error handling logic here
        pass

    def extract_metadata(self):
        try:
            metadata = self.df.info()
            print("Metadata:")
            print(metadata)
        except Exception as e:
            print(f"Error in extracting metadata: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='CSV File Reader')
    parser.add_argument('file_path', type=str, nargs='?',
                        help='Path to the CSV file')
    args = parser.parse_args()

    if args.file_path is None:
        args.file_path = input("Enter the path to the CSV file: ")

    file_reader = CSVFileReader(args.file_path)
    file_reader.read_and_parse_csv()

    while True:
        print("\nChoose an option:")
        print("1. Data Validation and Cleaning")
        print("2. Column Statistics")
        print("3. Query and Filtering")
        print("4. Sorting and Aggregation")
        print("5. Data Visualization")
        print("6. Export Results")
        print("7. Data Transformation")
        print("8. Error Handling")
        print("9. Extract Metadata")
        print("0. Exit")

        option = input("Enter the option number: ")

        if option == '1':
            data_validation_and_cleaning(file_reader)
        elif option == '2':
            column_statistics(file_reader)
        elif option == '3':
            query = input("Enter query: ")
            query_and_filtering(file_reader, query)
        elif option == '4':
            column_name = input(
                "Enter column name for sorting and aggregation: ")
            sorting_and_aggregation(file_reader, column_name)
        elif option == '5':
            column_name = input("Enter column name for visualization: ")
            data_visualization(file_reader, column_name)
        elif option == '6':
            output_file_path = input(
                "Enter output file path for exporting results: ")
            export_results(file_reader, output_file_path)
        elif option == '7':
            data_transformation(file_reader)
        elif option == '8':
            error_handling(file_reader)
        elif option == '9':
            extract_metadata(file_reader)
        elif option == '0':
            print("Exiting the CSV File Reader.")
            break
        else:
            print("Invalid option. Please choose a valid option.")
