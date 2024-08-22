# Install necessary packages if not already installed
if (!requireNamespace("tidyverse", quietly = TRUE)) install.packages("tidyverse")

# Load required library
library(tidyverse)

# Function to analyze any format (CSV, Excel, JSON)
analyze_data <- function(file_path) {
  file_extension <- tools::file_ext(file_path)
  
  # Choose the appropriate function based on the file extension
  data <- switch(file_extension,
                 csv = read_csv("C:\Users\danis\Downloads\Book1.csv"),
                 xlsx = read_excel("C:\Users\danis\Downloads\Book1.xlsx"),
                 pdf = readpdf("C:\Users\danis\Downloads\Book1.pdf"),
                 stop("Unsupported file format")
  )
  
  # Perform common analysis
  summary(data)
}

# Example usage
csv_file <- "C:\Users\danis\Downloads\Book1.csv"
excel_file <- "C:\Users\danis\Downloads\Book1.xlsx"
json_file <- "C:\Users\danis\Downloads\Book1.pdf"

# Analyze CSV file
analyze_data(csv_file)

# Analyze Excel file
analyze_data(excel_file)

# Analyze JSON file
analyze_data(pdf_file)