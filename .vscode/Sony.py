import csv 
def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as csvfile:
            #create a csv reader object
            csv_reader = csv.reader(csvfile)
            
            header = next(csv_reader)
            print(f"CSV Header: {hearder}")
            
            for row in csv_reader:
                name, age, department = row
                
                print(f"Name: {name}, Age: {age}, Department: {department}")
    except FileNotFoundError:
                print(f"The file '{file_path}' does not exist.")
    except Exception as e:
                print(f"An error occurred: {e}")
                
file_path = '"C:\Users\danis\Downloads\DANISH NAWAZ Roll No. 11222757 B. Tech.  (Computer Science  Engineering)  MMDU UMS.xlsx"'
read_csv_file(file_path)