#Pre-requites
# 1) All original image should be there in Img Files folder(4 image compulsory)
# 2) All .xml file from labelImg should be there in XML Files folder( 4 .xml compulsory)

import os
from random import choice
import shutil 
def main():
    # Function to rename multiple .jpg files
    #Img_Files = 'C:/Users/Admin/Desktop/OD_project_wit_code_extra_files/images'
    for count, filename in enumerate(os.listdir("C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files")): 
        dst ="annotation" + str(count) + ".jpg"
        os.rename(os.path.join('C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files',filename),
                  os.path.join('C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files',dst))

    # Function to rename multiple .xml files
    for count, filename in enumerate(os.listdir("C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files")):
        dst1 = "annotation" + str(count) + ".xml"  
        os.rename(os.path.join('C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files',filename),
                  os.path.join('C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files',dst1))

    # Function to copy multiple .jpg and . xml files   
    for i in range(100):
        shutil.copy2('C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files/annotation0.xml', 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files/annotation0{}.xml'.format(i))
        shutil.copy2('C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files/annotation0.jpg', 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files/annotation0{}.jpg'.format(i))
        shutil.copy2('C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files/annotation1.xml', 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files/annotation1{}.xml'.format(i))
        shutil.copy2('C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files/annotation1.jpg', 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files/annotation1{}.jpg'.format(i))
        shutil.copy2('C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files/annotation2.xml', 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files/annotation2{}.xml'.format(i))
        shutil.copy2('C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files/annotation2.jpg', 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files/annotation2{}.jpg'.format(i))
        shutil.copy2('C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files/annotation3.xml', 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files/annotation3{}.xml'.format(i))
        shutil.copy2('C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files/annotation3.jpg', 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files/annotation3{}.jpg'.format(i))


    # Function to move all files in same folder
    source = 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/Img Files'
    source1 = 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/XML Files'
    destination = 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/images/images1'
    # If folder contains previous files it will remove them all
    filelist = [ f for f in os.listdir(destination) if f.endswith(".jpg") ]
    for f in filelist:
        os.remove(os.path.join(destination, f))
    filelist1 = [ f for f in os.listdir(destination) if f.endswith(".xml") ]
    for f in filelist1:
        os.remove(os.path.join(destination, f))
    #Starting Moving 
    files = os.listdir(source)
    files1 = os.listdir(source1)
    for f in files:
        dest = shutil.move(source+'\\'+f, destination)
    for f in files1:
        dest = shutil.move(source1+'\\'+f, destination)


    # Function to delete all previous .jpg and .xml files in train folder
    destination_train = 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/images/train'
    filelist = [ f for f in os.listdir(destination_train) if f.endswith(".jpg") ]
    for f in filelist:
        os.remove(os.path.join(destination_train, f))
    filelist1 = [ f for f in os.listdir(destination_train) if f.endswith(".xml") ]
    for f in filelist1:
        os.remove(os.path.join(destination_train, f))


    # Function to delete all previous .jpg and .xml files in test folder
    destination_test = 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/images/test'
    filelist = [ f for f in os.listdir(destination_test) if f.endswith(".jpg") ]
    for f in filelist:
        os.remove(os.path.join(destination_test, f))
    filelist1 = [ f for f in os.listdir(destination_test) if f.endswith(".xml") ]
    for f in filelist1:
        os.remove(os.path.join(destination_test, f))

    #arrays to store file names
    imgs =[]
    xmls =[]

    #setup dir names
    trainPath = 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/images/train'
    testPath = 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/images/test'
    crsPath = 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/images/images1/' #dir where images and annotations stored

    #setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
    train_ratio = 0.80
    test_ratio = 0.20

    #total count of imgs
    totalImgCount = len(os.listdir(crsPath))

    #soring files to corresponding arrays
    for (dirname, dirs, files) in os.walk(crsPath):
        for filename in files:
            if filename.endswith('.xml'):
                xmls.append(filename)
            else:
                imgs.append(filename)


    #counting range for cycles
    countForTrain = int(len(imgs)*train_ratio)
    countForTest = int(len(imgs)*test_ratio)

    #cycle for train dir
    for x in range(countForTrain):

        fileJpg = choice(imgs) # get name of random image from origin dir
        fileXml = fileJpg[:-4] +'.xml' # get name of corresponding annotation file

        #move both files into train dir
        shutil.move(os.path.join(crsPath, fileJpg), os.path.join(trainPath, fileJpg))
        shutil.move(os.path.join(crsPath, fileXml), os.path.join(trainPath, fileXml))

        #remove files from arrays
        imgs.remove(fileJpg)
        xmls.remove(fileXml)



    #cycle for test dir   
    for x in range(countForTest):

        fileJpg = choice(imgs) # get name of random image from origin dir
        fileXml = fileJpg[:-4] +'.xml' # get name of corresponding annotation file

        #move both files into train dir
        shutil.move(os.path.join(crsPath, fileJpg), os.path.join(testPath, fileJpg))
        shutil.move(os.path.join(crsPath, fileXml), os.path.join(testPath, fileXml))

        #remove files from arrays
        imgs.remove(fileJpg)
        xmls.remove(fileXml)


    #summary information after splitting
    print('Total images: ', totalImgCount)
    print('Images in train dir:', len(os.listdir(trainPath)))
    print('Images in test dir:', len(os.listdir(testPath)))

    #Function to remove previous .csv file from the folder
    destination_remove_csv = 'C:/Users/Admin/Desktop/KJSCE_Object_Detection/models/research/object_detection/images'
    filelist = [ f for f in os.listdir(destination_remove_csv) if f.endswith(".csv") ]
    for f in filelist:
        os.remove(os.path.join(destination_remove_csv, f))

if __name__ == '__main__': 
      
    # Calling main() function 
    main()
