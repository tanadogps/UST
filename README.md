# Universal Style Transfer via Feature Transforms with TensorFlow & Keras

This is a TensorFlow/Keras implementation of [Universal Style Transfer via Feature Transforms](https://arxiv.org/pdf/1705.08086.pdf) by Li et al. The core architecture is an auto-encoder trained to reconstruct from intermediate layers of a pre-trained VGG19 image classification net. Stylization is accomplished by matching the statistics of content/style image features through the [Whiten-Color Transform (WCT)](https://www.projectrhea.org/rhea/index.php/ECE662_Whitening_and_Coloring_Transforms_S14_MH), which is implemented here in both TensorFlow and NumPy. No style images are used for training, and the WCT allows for 'universal' style transfer for arbitrary content/style image pairs.

As in the original paper, reconstruction decoders for layers `reluX_1 (X=1,2,3,4,5)` are trained separately and then hooked up in a multi-level stylization pipeline in a single graph. To reduce memory usage, a single VGG encoder is loaded up to the deepest relu layer and is shared by all decoders.

See [here](https://github.com/Yijunmaverick/UniversalStyleTransfer) for the official Torch implementation and [here](https://github.com/sunshineatnoon/PytorchWCT) for a PyTorch version.


## Requirements

* Python 3.x
* tensorflow 1.2.1+
* keras 2.0.x
* scikit-image

## Running a pre-trained model

1. Download VGG19 model: `https://www.dropbox.com/s/kh8izr3fkvhitfn/vgg_normalised.t7?dl=1` and place it on the 'models' folder

2. Download checkpoints for the five decoders: `https://www.dropbox.com/s/ssg39coiih5hjzz/models.zip?dl=1`, unzip the 5 decoders and place them at the 'models' folder

3. Obtain style images. Two good sources are the [Wikiart dataset](https://www.kaggle.com/c/painter-by-numbers) and [Describable Textures Dataset](https://www.robots.ox.ac.uk/~vgg/data/dtd/).

4. Run the Interface by opening UST.py

5. Import style and content images (both need to be in .png format)

6. Choose an output directory as well as the style parameter (default set to 60%)

7. Run the software and enjoy ! 