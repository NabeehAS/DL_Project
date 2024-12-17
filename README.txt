each file stands on its own, to recreate an expirement simply run the desired notebook

code files:

AI_project_30-1000MobileNetV2Crop: Used MobileNetV2, implemented the only experiment for MobileNet with cropping for training transformation.

AI_project_30-1000NoCrop: Used ResNet-50, implemented the "Normal Transformation" method mentioned in the report.

AI_project_30-1000CropTrain: Used ResNet-50, implemented the "Cropping" technique, we have mentioned in the report.

AI_project_30-1000CropTrainFreezeUnfreeze: Used ResNet-50, implemented the "Freeze Unfreeze" method mentioned in the report.

AI_project_30-1000MulFix: Used ResNet-50, implemented the "Data augmentation" technique, before insuring that no pictures or their mirrored ones are both in the train and test set.

AI_project_30-1000Mul: Used ResNet-50, implemented the "Data augmentation" technique, after insuring that no pictures or their mirrored ones are both in the train and test set.

alpha2: contains a list of the alpha 2 codes of the countries we worked with, used in collector and cordinates

cordinates: used to collect coardinates from the countries listed in alpha2, puts them in a txt file with an apropiate name

collector: collects the images from each country and saves them under an appropiatly named folder, needs a google API key to work

flipper: copies each image and flips it.

CNN_benchmark: CNN with different conv layer count, implements test of same name.

proof_of_concept: implements the test of the same name.



