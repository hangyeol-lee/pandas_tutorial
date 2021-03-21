import pandas as pd
import matplotlib.pyplot as plt

excel_file = pd.ExcelFile('movies.xls')

movies_sheet1 = pd.read_excel(excel_file, sheet_name=0, index_col=0)
movies_sheet1.head()

movies_sheet2 = pd.read_excel(excel_file, sheet_name=1, index_col=0)
movies_sheet2.head()

movies_sheet3 = pd.read_excel(excel_file, sheet_name=2, index_col=0)
movies_sheet3.head()

movies = pd.concat([movies_sheet1, movies_sheet2, movies_sheet3])

ax = movies['IMDB Score'].plot(kind="hist")
ax.set_xlabel("Ratings")

plt.show()