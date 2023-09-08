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

#  Export plates to excel in batches

def export_plates_to_excel(plates, filename):
    wb = Workbook()
    ws = wb.active
    ws.append(['Number Plate'])
    for plate in plates:
        ws.append([plate])
    wb.save(filename)

batch_size = 10000  # Adjust the batch size as needed
start_time = time.time()
total_valid_plates = 0
batch_number = 1

while True:
    batch_plates = generate_valid_plates()[:batch_size]
    if not batch_plates:
        break
    
    export_filename = f'valid_number_plates_batch{batch_number}.xlsx'
    export_plates_to_excel(batch_plates, export_filename)
    
    total_valid_plates += len(batch_plates)
    print(f"Exported {len(batch_plates)} plates to {export_filename}")
    
    batch_number += 1

end_time = time.time()

print(f"Total valid plates: {total_valid_plates}")
print(f"Total execution time (minutes): {(end_time - start_time) / 60:.2f} minutes")
