# Paper

* **Title**: MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications
* **Authors**: Andrew G. Howard, Menglong Zhu, Bo Chen, Dmitry Kalenichenko, Weijun Wang, Tobias Weyand, Marco Andreetto, Hartwig Adam
* **Link**: https://arxiv.org/pdf/1704.04861.
* **Code**: https://github.com/tensorflow/tfjs-models
* **Code for transfer learning**: https://github.com/pytorch/vision/blob/master/torchvision/models/mobilenet.py
* **Code for Android demo**: https://github.com/tensorflow/examples/tree/master/lite/examples/posenet/android
* **Tags**: Neural Network, Mobile, Depthwise Convolution
* **Year**: 2017

# Summary

* Why
  * To make the neural network fast enought to work on mobile.

* What
  * This paper proposes a depthwise separable convolution method to reduce the number of multiple-addition operations significantly.

  * What is depthwise convolution?  In a standard convolution, a layer takes in an input feature map F of size DF x DF x M and use a kernel K of size Dk x Dk x M X N.

    DF - width/height of feature map input

    M - channel size of feature map input

    Dk - kernel size

    N - number of channels in kernel

    Vanina computation cost = Dk * Dk * M * N * DF * DF.

    In Depthwise separable convolution, the input feature map pass depthwise convolution first followed by pointwise convolutions. For depthwise convolution, the kernel filter is applied to each input channel instead of all channels at a time. If input map was DF x DF x M originally, the depthwise output map is DF x DF x M still. The depthwise output map is then passed through a 1 x 1 x N pointwise convolution. It is used to create a linear combination of the output of the depthwise layers.

    Computation cost of depthwise = DF x DF x M x Dk x Dk 

    Computation cost of pointwise = M x N x 1 x 1
    
    Depthwise computation cost = (DF x DF x M x Dk x Dk) + (M x N x DF x DF)

    Reduction of computation = Depthwise computation cost) / (Vanina computation cost)
    = 1 / N + 1 / (Dk x Dk)

  * Full model summary:
  ![Table 1. MobileNet Body Architecture](images/MobileNets:_Efficient_Convolutional_Neural_Networks_for_Mobile_Vision_Applications/table1.png?raw=true "Table 1. MobileNet Body Architecture")
    
    The full model is only 4.2 million parameters.

* How

  * The authors propose 2 multiplier hyperparameters to adjust the complexity of the model and hence the runtime speed. 
  ![Formula1. hyperparameters to control the complexity](images/MobileNets:_Efficient_Convolutional_Neural_Networks_for_Mobile_Vision_Applications/formula1.png?raw=true "Formula1. hyperparameters to control the complexity")

  * Another way of hypertuning for runtime speed is the number of layers. To make it shallower, the authors propose removing the 5x layers of 14 x 14 x 512 filters.  However, removing layers (shallower) will lose 3% more accuracy than reducing width. 

* Results

  ![Result](images/MobileNets:_Efficient_Convolutional_Neural_Networks_for_Mobile_Vision_Applications/result1.png?raw=true "Result")