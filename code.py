from pil import Image, ImageFilter
from shutil import copyfile
import os
import random
textureFolders = ['block', 'colormap', 'effect', 'entity', 'environment',
                  'gui', 'item', 'map', 'misc', 'mob_effect', 'painting', 'particle', 'entity/armorstand', 'entity/banner', 'entity/bear', 'entity/bed', 'entity/bee', 'entity/bell', 'entity/boat', 'entity/cat', 'entity/creeper', 'entity/conduit', 'entity/end_crystal', 'entity/enderdragon', 'entity/enderman', 'entity/fish', 'entity/fox', 'entity/ghast', 'entity/horse', 'entity/illager', 'entity/iron_golem', 'entity/llama', 'entity/panda', 'entity/parrot', 'entity/pig', 'entity/projectiles', 'entity/rabbit', 'entity/sheep', 'entity/shield', 'entity/shulker', 'entity/signs', 'entity/skeleton', 'entity/slime', 'entity/spider', 'entity/turtle', 'entity/villager', 'entity/wither', 'entity/zombie', 'entity/zombie_villager']


# os.getcwd()
index = 0
for folder in textureFolders:
    for filename in os.listdir('Default 1.15 Resource Pack/assets/minecraft/textures/' + folder + '/'):
        if filename.endswith('.png'):
            print(str(index) + ' : ' + filename)
            # filename = 'hay_block_side.png'
            img = Image.open(
                'Default 1.15 Resource Pack/assets/minecraft/textures/' + folder + '/' + filename)
            px = img.load()
            red = green = blue = alpha = 0
            # if type(px) != type(123):
            cpx = 0
            for x in range(img.width):
                for y in range(img.height):
                    px[x, y] = px[random.randint(0, img.width-1), random.randint(0, img.height-1)]
            if not os.path.exists('textures/'):
                os.makedirs('textures/')

            if not os.path.exists('textures/' + folder):
                os.makedirs('textures/' + folder)
            img.save('textures/' + folder + '/' + filename)
           
            index += 1
        elif filename.endswith('.mcmeta'):
            copyfile('Default 1.15 Resource Pack/assets/minecraft/textures/' + folder + '/' + filename, 'textures/' + folder + '/' + filename)
