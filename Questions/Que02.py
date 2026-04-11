# Write a program to convert bits to Megabytes, Gigabytes and Terabytes. 

bits = int(input("Enter number of bits: "))

byte = bits/8
kb = byte / 1024
mb = kb / 1024
gb = mb / 1024
tb = mb / 1024

print("\nConversion Result:")
print(f"{bits} bitts into Megabytes (MB):", mb)
print(f"{bits} bitts Gigabytes (GB):", gb)
print(f"{bits} bitts Terabytes (TB):", tb)