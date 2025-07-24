import pandas as pd
from fpdf import FPDF

#Read CSV data
data = pd.read_csv("/content/data.csv")

#Analyze Data
average_score = data['SCORE'].mean()
max_score = data['SCORE'].max()
min_score = data['SCORE'].min()
topper = data.loc[data['SCORE'].idxmax()]['NAME']
low_scorer = data.loc[data['SCORE'].idxmin()]['NAME']

#Generate PDF Report
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Automated Report", ln=True, align='C')
pdf.ln(10)

# Adding each row of the CSV
pdf.set_font("Arial", size=10)
pdf.cell(200, 10, txt="Student Scores:", ln=True)
for i, row in data.iterrows():
    pdf.cell(200, 10, txt=f"{row['NAME']} - {row['SCORE']}", ln=True)

#Summary
pdf.ln(5)
pdf.set_font("Arial", style='B', size=12)
pdf.cell(200, 10, txt="Summary:", ln=True)
pdf.set_font("Arial", size=10)
pdf.cell(200, 10, txt=f"Average Score: {average_score:.2f}", ln=True)
pdf.cell(200, 10, txt=f"Highest Score: {max_score} (Topper: {topper})", ln=True)
pdf.cell(200, 10, txt=f"Lowest Score: {min_score} (Lowest: {low_scorer})", ln=True)

#Save PDF
pdf.output("sample_report.pdf")

print("✅ Report Generated Successfully: sample_report.pdf")
