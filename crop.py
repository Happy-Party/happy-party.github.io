from PIL import Image

im = Image.open('image_1.png')
width, height = im.size
print(f"Width: {width}, Height: {height}")

# 3x3 grid
w = width // 3
h = height // 3

# Top right is row 0, col 2
left = 2 * w
upper = 0
right = left + w
lower = upper + h

im_cropped = im.crop((left, upper, right, lower))
im_cropped.save('dino_bag.png')
print("Cropped top right image to dino_bag.png")
