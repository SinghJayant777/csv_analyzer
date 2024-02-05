import matplotlib.pyplot as plt

def data_visualization(file_reader, column_name):
    try:
        plt.figure(figsize=(10, 6))
        file_reader.df[column_name].plot(kind='hist')
        plt.title(f'Data Distribution for {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"Error in data visualization: {e}")
