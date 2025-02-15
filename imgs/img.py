from PIL import Image

mac = Image.open('example.jpg')
print(type(mac))
# mac.show()
print(mac.size ,  mac.filename, mac.format_description)