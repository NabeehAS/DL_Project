# Country Classification Project

(![alt text](http://url/to/img.png))

This repository contains all the files and notebooks used in our project, "Country Classification." Each file is self-contained, and you can recreate a specific experiment by running the corresponding notebook.

## Final Report
The final project report is titled **Country Classification**. It details the methods, experiments, and results of this project.

---

## Project Files

### Code Files
- **AI_project_30-1000MobileNetV2Crop**  
  Uses MobileNetV2 with cropping applied during training. Implements the MobileNet experiment described in the report.

- **AI_project_30-1000NoCrop**  
  Uses ResNet-50 with the "Normal Transformation" method as described in the report.

- **AI_project_30-1000CropTrain**  
  Uses ResNet-50 with the "Cropping" technique, as explained in the report.

- **AI_project_30-1000CropTrainFreezeUnfreeze**  
  Uses ResNet-50 with the "Freeze Unfreeze" method detailed in the report.

- **AI_project_30-1000MulFix**  
  Uses ResNet-50 with the "Data Augmentation" technique. Ensures that no image and its mirrored counterpart are included in both the training and testing sets.

- **AI_project_30-1000Mul**  
  Uses ResNet-50 with the "Data Augmentation" technique, allowing mirrored images in training and testing, as described in the report.

### Utility Files
- **alpha2**  
  Contains a list of the alpha-2 codes for the countries used in this project. Used by `collector` and `coordinates` scripts.

- **coordinates**  
  Collects coordinates for countries listed in `alpha2` and saves them to appropriately named text files.

- **collector**  
  Collects images for each country and saves them in appropriately named folders. Requires a Google API key.

- **flipper**  
  Creates flipped copies of each image.

### Additional Experiments
- **CNN_benchmark**  
  Benchmarks CNNs with varying numbers of convolutional layers.

- **proof_of_concept**  
  Implements the "Proof of Concept" test described in the project report.

---

Feel free to reach out for further questions or suggestions!



