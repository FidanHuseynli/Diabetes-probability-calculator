import csv
import math
import tkinter as tk

from tkinter import messagebox

def loadAndPreprocess(fileName):
    rawData = []
    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        headers = next(reader)
        for row in reader:
            rawData.append([float(x) for x in row])

    inputCols = list(range(8))
    outputCols = 8

    colsMin = [min(row[i] for row in rawData) for i in inputCols]
    colsMax = [max(row[i] for row in rawData) for i in inputCols]

    preprocessedData = []
    for row in rawData:
        normalizedRow = []
        for i in inputCols:
            if colsMax[i] == colsMin[i]:
                normalizedRow.append(0.0)
            else:
                normalizedRow.append((row[i] - colsMin[i]) / (colsMax[i] - colsMin[i]))

        normalizedRow.append(row[outputCols])
        preprocessedData.append(normalizedRow)

    return rawData, preprocessedData, headers, colsMin, colsMax

rawData, preprocessedData, headers, colsMin, colsMax = loadAndPreprocess("diabetes.csv")

print(f"{len(rawData)} kayıt okundu.")
print("Min değerler:", colsMin)
print("Max değerler:", colsMax)
print("İlk ham kayıt:  ", rawData[0])
print("İlk norm kayıt:", preprocessedData[0])

def savePreprocessed(filename, preprocessedData, headers):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for row in preprocessedData:
            writer.writerow([round(x, 9) for x in row])

savePreprocessed("diabetes_preprocessed.csv", preprocessedData, headers)
print("Preprocessed dosyası kaydedildi.")

def euclideanDistance(row1, row2):
    distance = 0.0
    for i in range(8):
        distance += (row1[i] - row2[i]) ** 2
    return math.sqrt(distance)

def knn(preprocessedData, inputRow, k):
    distances = []
    for row in preprocessedData:
        dist = euclideanDistance(inputRow, row)
        distances.append((dist, row[8]))

    distances.sort(key=lambda x: x[0])
    kNearest = distances[:k]

    diabeticCount = sum(1 for _, outcome in kNearest if outcome == 1.0)
    probability = (diabeticCount / k) * 100

    return probability, kNearest

columnNames = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
                "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]

def validateAndCalculate():
    for i, entry in enumerate(entries):
        if entry.get().strip() == "":
            messagebox.showerror("Error", f"{columnNames[i]} field cannot be empty!")
            return

    try:
        userValues = [float(entry.get()) for entry in entries]
    except ValueError:
        messagebox.showerror("Error", "Please enter numeric values in all fields!")
        return

    for i in range(8):
        if userValues[i] < colsMin[i] or userValues[i] > colsMax[i]:
            messagebox.showerror("Error",
                                 f"{columnNames[i]} must be between {colsMin[i]} and {colsMax[i]}!\n"
                                 f"Entered value: {userValues[i]}")
            return

    try:
        k = int(kEntry.get())
    except ValueError:
        messagebox.showerror("Error", "K value must be an integer!")
        return

    if k < 1 or k > len(preprocessedData):
        messagebox.showerror("Error",
                             f"K value must be between 1 and {len(preprocessedData)}!")
        return

    normalizedInput = []
    for i in range(8):
        if colsMax[i] == colsMin[i]:
            normalizedInput.append(0.0)
        else:
            normalizedInput.append((userValues[i] - colsMin[i]) / (colsMax[i] - colsMin[i]))

    probability, kNearest = knn(preprocessedData, normalizedInput, k)

    resultText = f"Diabetes Probability: %{probability:.1f}\n\n"
    resultText += f"Closest {k} neighbors:\n"
    for dist, outcome in kNearest:
        resultText += f"  Distance: {dist:.4f} | {'Diabetic' if outcome == 1.0 else 'Healthy'}\n"

    resultLabel.config(text=resultText)

window = tk.Tk()
window.title("Diabetes Prediction Program")
window.geometry("400x600")
window.resizable(False, False)

entries = []
for i, name in enumerate(columnNames):
    tk.Label(window, text=f"{name} (min:{colsMin[i]:.1f} - max:{colsMax[i]:.1f}):").grid(
        row=i, column=0, padx=10, pady=5, sticky="w")
    entry = tk.Entry(window)
    entry.grid(row=i, column=1, padx=10, pady=5)
    entries.append(entry)

tk.Label(window, text=f"K (1 - {len(preprocessedData)}):").grid(
    row=8, column=0, padx=10, pady=5, sticky="w")
kEntry = tk.Entry(window)
kEntry.insert(0, "5")
kEntry.grid(row=8, column=1, padx=10, pady=5)
tk.Button(window, text="Calculate", command=validateAndCalculate, bg="blue", fg="white").grid(
    row=9, column=0, columnspan=2, pady=10)

resultLabel = tk.Label(window, text="", justify="left", font=("Courier", 10))
resultLabel.grid(row=10, column=0, columnspan=2, padx=10)

window.mainloop()



