from PIL import Image
import random
import os
import sys

print()
print("Création de pele mele by OrCaD v0.12")
print()
print("Retrouvez la page du projet ici :")
print("https://forum.hfsplay.fr/decoration-de-borne-f87/deco-borne-generateur-de-pele-mele-t18042.html")
print()
print("Ctrl+C interrompt la génération et sauvegarde le résultat intermédiaire")
print()
try:
     with open('collage.png'):
            print("L'image collage.png existe deja :")
            print("1.Utiliser")
            print("2.Ecraser")
            print("3.Quitter")
            print()
            while True:
                reponse = input("Choisissez 1, 2 ou 3: ")
                if reponse in ['1', '2', '3']:
                    break
                else:
                    print ("Choix incorrect !")
            if reponse=='1' :
                base_image = Image.open('collage.png').convert("RGBA")
                width, height = base_image.size
            elif reponse=='2' :
                base_image = Image.open('collage.png').convert("RGBA")
                width, height = base_image.size
                base_image = Image.new("RGBA", (width, height), (255, 255, 255))
            elif reponse=='3' :
                print()
                print("Effacez collage.png pour generer un nouveau collage")
                print()
                os.system("pause")
                sys.exit()
except IOError:
         print("Taille du nouveau collage :")
         while True:
            try:
                width=int(input("Largeur de l'image : "))
                break
            except ValueError:
                print("Entrez un nombre.")
         while True:
            try:
                height=int(input("Hauteur de l'image : "))
                break
            except ValueError:
                print("Entrez un nombre.")         
         base_image = Image.new("RGBA", (width, height), (255, 255, 255))
print()
while True:
     try:
          Vratio = int(input("Ratio minimum (defaut 100) : "))
          break
     except ValueError:
          Vratio = 100
if Vratio>100 :
     print("valeur impossible, seule la réduction est possible.")
     Vratio = 100          
path = "./images/"
if os.path.isdir(path):
     i=1
     for root, directories, files in os.walk(path):
         num_files = len(files)
         if num_files != 0 :
             random.shuffle(files)
             try:
                  for file in files:
                      sticker = Image.open(path+file).convert("RGBA")
                      wsticker, hsticker = sticker.size
                      if Vratio !=100 :
                           RandomResize=random.randrange(Vratio, 100)/100
                           wsticker = int(wsticker*RandomResize)
                           hsticker = int(hsticker*RandomResize)
                           sticker = sticker.resize((wsticker, hsticker), Image.ANTIALIAS)
                      sticker = sticker.rotate(random.randrange(80)-40, expand = 1)
                      base_image.paste(sticker, (random.randrange(width)-random.randrange(wsticker),random.randrange(height)-random.randrange(wsticker)), sticker)
                      print(i,'/',num_files,' ',file)
                      i+=1
             except KeyboardInterrupt:
                  print()
                  print("Processus interrompu, je sauvegarde l'image. Patientez")
                  print()
                  break
         else :
             print()
             print("/!\ le dossier /images est vide")
             print()
else :
     print()
     print("/!\ le dossier /images n'existe pas")
     print()
base_image.save("collage.png") 
os.system("pause")
