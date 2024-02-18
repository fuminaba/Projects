# Projects :sparkles:
Welcome to projects directory! You'll find some project's I've completed here for fun or while exploring some topic of interest.   

## Environment
Environment management is done using Anaconda (conda version 23.7.4) 
Many of the projects use TensorFlow 2.10, the version last compatible with Windows Native. The full environment/packages are in the `imaging-informatics-tf.yaml` file.  
This can be replicated with the following commands: 
```
$ conda env create -f imaging-informatics-tf.yaml
$ conda activate imagin-tf
```
where `$` denotes the start of the terminal.

You can view individual projects below:  

| Project # | Project Name | Some Topics | Details | 
| --- | --- | --- | --- | 
| 0 | [ImagIn - Image Informatics Package](Projects/Imagin/) | TensorFlow, Image Processing, Image Analysis, Feature Extraction | Python package for image processing and analysis using deep learning frameworks such as TensorFlow and PyTorch which are used in the projects on this page. |
| 1 | [MedMNIST Image Classification with TensorFlow](Projects/MedMNIST-TF) | TensorFlow; Nested CV; Hyperparameter Optimization; | Using TensorFlow and the MedMNIST 2D Pathology image dataset, an image classifier is trained using a nested cross validation to find optimal hyperparameters and model selection. | 
