import time
from openpyxl import Workbook

def generate_valid_plates():
    valid_plates = []

    for letter1 in range(ord('K'), ord('L')):
        for letter2 in range(ord('A'), ord('Z') + 1):
            for letter3 in range(ord('A'), ord('Z') + 1):
                for number1 in range(10):
                    for number2 in range(10):
                        for number3 in range(10):
                            for letter4 in range(ord('A'), ord('Z') + 1):
                                plate = f"{chr(letter1)}{chr(letter2)}{chr(letter3)} {number1}{number2}{number3}{chr(letter4)}"
                                if "000" not in plate and not plate.startswith("KDF"):
                                    valid_plates.append(plate)

    return valid_plates

start_time = time.time()
valid_plates = generate_valid_plates()
end_time = time.time()

total_valid_plates = len(valid_plates)

# Export valid plates to an Excel file
wb = Workbook()
ws = wb.active
ws.append(['Number Plate'])
for plate in valid_plates:
    ws.append([plate])

wb.save('valid_number_plates.xlsx')

for plate in valid_plates:
    print(plate)

execution_time_minutes = (end_time - start_time) / 60
print(f"Total valid plates: {total_valid_plates}")
print(f"Total execution time (minutes): {execution_time_minutes:.2f} minutes")
print("Number plates exported to 'valid_number_plates.xlsx'")
