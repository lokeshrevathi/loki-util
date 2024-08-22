import base64

# Original string
data = "Secret message"

# Convert string to bytes
data_bytes = data.encode('utf-8')

# Base64 encoding
encoded_data = base64.b64encode(data_bytes)
encoded_str = encoded_data.decode('utf-8')
print(f"Encoded string: {encoded_str}")

# Base64 decoding
decoded_bytes = base64.b64decode(encoded_str)
decoded_str = decoded_bytes.decode('utf-8')
print(f"Decoded string: {decoded_str}")