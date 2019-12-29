import openpyxl
store= []

with open ("C:/Users/angular_nija_avenger/Documents/notes/online money.txt", "r") as myfile:
    for line in myfile:
        if not len(line) == 1:
            store.append(line)

workbook = openpyxl.load_workbook("websites.xlsx")
wb = openpyxl.Workbook()
sheet = wb["Sheet"]

for i in range(0,len(store)):
    num = "A"+str(i)
    sheet[f"A{num}"] = store[i]
    
wb.save("websites.xlsx")


