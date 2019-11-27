# Paper

* **Title**: SRFeat: Single Image Super-Resolution with Feature Discrimination
* **Authors**: Seong-Jin Park, Hyeongseok Son, Sunghyun Cho, Ki-Sang Hong, Seungyong Lee
* **Link**: http://openaccess.thecvf.com/content_ECCV_2018/papers/Seong-Jin_Park_SRFeat_Single_Image_ECCV_2018_paper.pdf
* **Tags**: super-resolution, adversarial network, high frequency features, perceptual quality
* **Year**: 2018

# Summary

* Why
  * Generative adversarial networks (GANs) have recently been adopted to single image super-resolution (SISR) and showed impressive results with realistically synthesized high-frequency textures. However, the results of such GAN-based approaches tend to include less meaningful high-frequency noise that is irrelevant to the input image. 
  
* What
  * In this paper, we propose a novel GAN-based SISR method that overcomes the limitation and produces more realistic results by attaching an additional discriminator that works in the feature domain.

* How
  ![architecture](images/SRFeat:_Single_Image_Super-Resolution_with_Feature_Discrimination/architecture.png?raw=true "architecture") 

* Results
  ![results](images/SRFeat:_Single_Image_Super-Resolution_with_Feature_Discrimination/results.png?raw=true "results") 