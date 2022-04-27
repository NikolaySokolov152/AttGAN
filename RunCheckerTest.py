import os
import sys
import cv2

try:
    if not os.path.isdir("output"):
        print ("you need to create an 'output' folder")
        raise Exception('Error output')
        

    if not os.path.isdir("output/AttGAN_128"):
        print ("you need to download and unzip the model to the output folder")
        print ("\thttps://drive.google.com/file/d/1lcQ-ijNrGD4919eJ5Dv-7ja5rsx5p0Tp/view?usp=sharing")
        raise Exception('Error output/AttGAN_128')
        
    if not os.path.isfile("output/AttGAN_128/generator.pb") or not os.path.isfile("output/AttGAN_128/settings.yml"):
        print ("you need to download and unzip the model files to the output/AttGAN_128 folder")
        print ("\thttps://drive.google.com/file/d/1lcQ-ijNrGD4919eJ5Dv-7ja5rsx5p0Tp/view?usp=sharing")
        raise Exception('Error output/AttGAN_128 gen data')
        

    if not os.path.isdir("data"):
        print ("you need to create an 'data' folder")
        raise Exception('Error data')
        
    if not os.path.isdir("data/image"):
        print ("you need to create an 'image' folder in 'data'")
        raise Exception('Error data/image')
        

    if not os.path.isfile("data/atributs.txt"):
        print ("you need create labels of image atributs.txt")
        raise Exception('Error data/atributs.txt')
        
    if len(os.listdir("data/image")) == 0:
        print ("you need add image im data/image folder")
        raise Exception('Error no Image')
        

    print ("Попытка запуска основной программы")
    os.system('python3 test.py --experiment_name AttGAN_128')
    print ("Завершено")

    if not os.path.isdir("output/AttGAN_128/samples_testing_2"):
        print("Запуск прошёл неудачно")
        
    num_create = len(os.listdir("output/AttGAN_128/samples_testing_2"))
    if num_create != 0:
        print("Запуск прошёл удачно. В директории 'output/AttGAN_128/samples_testing_2' лежит", num_create, " сгенерированных изображения")
        
        dir_check = 'check_result'
        dir_result = 'output/AttGAN_128/samples_testing_2'
        
        for name in os.listdir(dir_result):
            img_check = cv2.imread(os.path.join(dir_check, name))
            img_result = cv2.imread(os.path.join(dir_result, name))
           
            img_check = img_check.astype(float)
            img_result = img_result.astype(float)
                    
            err = (abs(img_check[:,:,:] - img_result[:,:,:])).sum()
        
            print ("ошибка с", name, "составляет", err)
        
        
    else:
        print("Запуск прошёл неудачно")
        
    
    print ("TEST COMPLITE")
except Exception as e:
    print (e)
    print ("TEST FAILS!!!!!!!")
    