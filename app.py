import qrcode #Import The Module

img = qrcode.make('Welcome to CodeWithNiranjan')

type(img)

img.save("img.png") #Save the file