call chdir /d C:\Users\Admin\Desktop

call chdir /d C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection

call C:\Users\Admin\AppData\Local\Programs\Python\Python36\python.exe C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\xml_to_csv.py

call chdir /d C:\Users\Admin\Desktop

call C:\Users\Admin\AppData\Local\Programs\Python\Python36\python.exe C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\generate_tfrecord.py --csv_input=C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\images\train_labels.csv --image_dir=C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\images\train --output_path=C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\train.record

call C:\Users\Admin\AppData\Local\Programs\Python\Python36\python.exe C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\generate_tfrecord.py --csv_input=C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\images\test_labels.csv --image_dir=C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\images\test --output_path=C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\test.record


C:\Users\Admin\AppData\Local\Programs\Python\Python36\python.exe C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\model_main.py --logtostderr --model_dir=C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\training/ --pipeline_config_path=C:\Users\Admin\Desktop\KJSCE_Object_Detection\models\research\object_detection\training\faster_rcnn_inception_v2_pets.config