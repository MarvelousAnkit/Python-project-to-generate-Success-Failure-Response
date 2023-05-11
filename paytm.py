from PIL import Image, ImageDraw, ImageFont , ImageFilter

# Open the image file
image = Image.open("new.jpg")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Define the font to use

# Draw the text on the image
name = "Riya Kumari"
amount = str(976)
if len(name)<15:
    a=49
else:
    a=40
font = ImageFont.truetype("arialbd.ttf", size=a)
font1 = ImageFont.truetype("arial.ttf", size=77)
font2 = ImageFont.truetype("arial.ttf", size=40)
font3 = ImageFont.truetype("arialbd.ttf", size=33)
font4 = ImageFont.truetype("arial.ttf", size=29)

# Split the name into words
words = name.split()

# Get the first and last words
first_word, last_word = words[0], words[-1]

# Extract the first letter of each word and join as string
first_letters = ''.join([first_word[0], last_word[0]])

# Print the result
print(first_letters)
if len(amount)==4:
    x1=180
    y1=390
    x2=230
    y2=390
elif len(amount)==5:
    x1=150
    y1=390
    x2=190
    y2=390
elif len(amount)==3:
    x1=230
    y1=390
    x2=275
    y2=390
elif len(amount)==2:
    x1=270
    y1=390
    x2=315
    y2=390
else:
    x1=320
    y1=390
    x2=365
    y2=390

draw.text((210, 240), name, fill=(0,0,0), font=font)

draw.text((x1, y1), "₹", fill=(0,0,0), font=font1)
draw.text((x2, y2), amount , fill=(0,0,0), font=font1)
draw.text((110, 258), first_letters, fill=(255,255,255), font=font2)
draw.text((170, 530), "07 May, 11:50 AM", fill=(26, 178, 255), font=font3)
draw.text((17,28), "11:50", fill=(0,0,0), font=font4)


blur_radius = 1
blur_box = (5 - blur_radius, 26 - blur_radius, 100 + blur_radius, 85 + blur_radius)
blur_region = image.crop(blur_box)
blur_region = blur_region.filter(ImageFilter.GaussianBlur(blur_radius))
image.paste(blur_region, blur_box)


# Save the modified image
image.save("output.jpg")

