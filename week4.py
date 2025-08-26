# Read & Write with Error Handling
try:
    # Get filename from user
    filename = input("Enter filename to read: ")
    
    # Try to read the file
    with open(filename, 'r') as file:
        content = file.read()
    
    # Modify content (convert to uppercase)
    modified = content.upper()
    
    # Get output filename
    output_name = input("Enter output filename: ")
    
    # Write modified content
    with open(output_name, 'w') as file:
        file.write(modified)
    
    print(f"Success! Modified content written to {output_name}")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"Error: {e}")