from PIL import Image

WIDTH = 100
HEIGHT = 200

number = ['2','3','4','5','6','7','8','9','10','ace','jack','queen','king']
suit = ['clubs','diamonds','hearts','spades']


for i in range(len(number)):
    for j in range(4):
        print('images/'+number[i]+'_of_'+suit[j]+'.png')
        image = Image.open('images/'+number[i]+'_of_'+suit[j]+'.png')
        image = image.resize((WIDTH,HEIGHT))
        image.save(fp='images/'+number[i]+'_of_'+suit[j]+'_small.png')


image = Image.open('images/play_button.png')
image = image.resize((100,100))
image.save(fp='images/play_button_small.png')



