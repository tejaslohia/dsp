# Read Binary file containing Big Endian short data and convert to csv file

import csv
import struct

file_path="./FFT.bin"
csv_file_path="./FFT.csv"
with open(file_path, 'rb') as binary_file:
    binary_data = binary_file.read()

print(len(binary_data))

dataLen=(int)(len(binary_data)/2)
fft_data=struct.unpack(f">{dataLen}h",binary_data)

with open(csv_file_path, 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    for (item) in fft_data:
        csv_writer.writerow([item])
      
print("over")
