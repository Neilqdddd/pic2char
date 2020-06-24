from PIL import Image #a python image package

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# a list of character

image_path = "jiang.jpg" #location of the image

def tran_char(r,g,b,alpha=256):
    #transfer image to char
    if alpha==0:
        return ' '
    l = len(ascii_char) #to get the char
    g = int(0.2126*r+0.7152*g+0.0722*b) #for the gray level
    unit = (256.0+1)/l
    return ascii_char[int(g/unit)]


if __name__ =='__main__':
    im= Image.open(image_path)
    w = int(im.size[0]*0.75)
    h = int(im.size[1]*0.5)
    im = im.resize((w,h), Image.NEAREST)
    txt = ''
    for i in range(h):
        for j in range(w):
            txt += tran_char(*im.getpixel((j,i)))
        txt +='\n'
    print(txt)

    with open('output.txt','w') as f:
        f.write(txt)

    f.close()

