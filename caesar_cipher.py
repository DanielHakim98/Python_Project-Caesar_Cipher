def caesar(str_1, num):
  str_new = []
  str_bytes = str_1.encode()

  for byte in str_bytes:
    if byte >= 65 and byte <= 90:
      byte += num
      if byte < 65 or byte > 90:
        byte = check_wrap_capital(byte)
    elif byte >= 97 and byte <= 122:
      byte += num
      if byte < 97 or byte > 122:
        byte = check_wrap_lower(byte)
    str_new.append(byte)
  str_decode = bytearray(str_new).decode()
  return str_decode

def check_wrap_capital(byte):
  if byte > 90:
    while(byte > 90):
      byte = (byte - 90) + 65 - 1
  else:
    while(byte < 65):
      byte = 90 - (65 - byte) + 1
  return byte

def check_wrap_lower(byte):
  if byte > 122:
    while(byte > 122):
      byte = (byte - 122) + 97 - 1
  else:
    while(byte < 97):
      byte = 122 - (97 - byte) + 1
  return byte

print(caesar('A',1))
print(caesar('Aaa',1))
print(caesar('Hello, World!', 5))
print(caesar('Mjqqt, Btwqi!', -5))
print(caesar('Z',1))
print(caesar('Hello, World!', 75))
print(caesar("Hello, World!",-29))
