import pandas as pd

# Read CSV File
data = pd.read_csv("sales.csv")

# Display Data
print("Sales Data")
print(data)

# Calculations
total_sales = data["Sales"].sum()
average_sales = data["Sales"].mean()
highest_sale = data["Sales"].max()

# Display Results
print("\n----- SALES REPORT -----")
print("Total Sales:", total_sales)
print("Average Sales:", average_sales)
print("Highest Sale:", highest_sale)

# Save Report
with open("report.txt", "w") as file:
    file.write("SALES REPORT\n")
    file.write("-----------------\n")
    file.write(f"Total Sales: {total_sales}\n")
    file.write(f"Average Sales: {average_sales}\n")
    file.write(f"Highest Sale: {highest_sale}\n")

print("\nReport Generated Successfully!")