# Paper

- **Title**: Deep High-Resolution Representation Learning for Human Pose Estimation
- **Authors**: Ke Sun, Bin Xiao, Dong Liu, Jingdong Wang
- **Paper**: https://arxiv.org/pdf/1902.09212.pdf
- **Code**: https://github.com/leoxiaobin/deep-high-resolution-net.pytorch
- **Tags**: Neural Network, Residual, Deep Architectures
- **Year**: 2019

# Summary

## Why
  - Most existing methods recover high-resolution representations from low-resolution representations produced by a high-to-low resolution network.  
    - Hourglass [40] recovers the high resolution through a symmetric low-to-high process. 
    - SimpleBaseline [72] adopts a few transposed convolution layers for generating high-resolution representations. 
    - In addition, dilated convolutions are also used to blow up the later layers of a high-to-low resolution network (e.g., VGGNet or ResNet)
  - Instead, our proposed network maintains high-resolution representations through the whole process.


## What
  - Start from 'high-resolution' subnetwork as the first stage;
  - Gradually add 'high-to-low' resolution subnetworks one by one to form more starges;
  - connect the multi-resolution subnetworks in parallel;
  - This paper is interested in single-person pose estimation


![Figure 1](images/Deep_High-Resolution_Representation_Learning_for_Human_Pose_Estimation/figure1.png?raw=true "Figure 1")

Figure 1. Illustrating the architecture of the proposed HRNet. It
consists of parallel high-to-low resolution subnetworks with repeated information exchange across multi-resolution subnetworks
(multi-scale fusion). The horizontal and vertical directions correspond to the depth of the network and the scale of the feature
maps, respectively.


## Results

### Improvement

  - **Pose_HRnet_w32 with less parameters (28.5M) give better result than ResNet_50 with more parameters (34.0M), which indicate it run faster with better accuracy than ResNet_50.**

### Results on MPII val 
| Arch               | Head | Shoulder | Elbow | Wrist |  Hip | Knee | Ankle | Mean | Mean@0.1 |
|--------------------|------|----------|-------|-------|------|------|-------|------|----------|
| pose_resnet_50     | 96.4 |     95.3 |  89.0 |  83.2 | 88.4 | 84.0 |  79.6 | 88.5 |     34.0 |
| pose_resnet_101    | 96.9 |     95.9 |  89.5 |  84.4 | 88.4 | 84.5 |  80.7 | 89.1 |     34.0 |
| pose_resnet_152    | 97.0 |     95.9 |  90.0 |  85.0 | 89.2 | 85.3 |  81.3 | 89.6 |     35.0 |
| **pose_hrnet_w32*- | 97.1 |     95.9 |  90.3 |  86.4 | 89.1 | 87.1 |  83.3 | 90.3 |     37.7 |

### Note:
- Flip test is used.
- Input size is 256x256
- pose_resnet_[50,101,152] is our previous work of [*Simple Baselines for Human Pose Estimation and Tracking*](http://openaccess.thecvf.com/content_ECCV_2018/html/Bin_Xiao_Simple_Baselines_for_ECCV_2018_paper.html)

### Results on COCO val2017 with detector having human AP of 56.4 on COCO val2017 dataset
| Arch               | Input size | #Params | GFLOPs |    AP | Ap .5 | AP .75 | AP (M) | AP (L) |    AR | AR .5 | AR .75 | AR (M) | AR (L) |
|--------------------|------------|---------|--------|-------|-------|--------|--------|--------|-------|-------|--------|--------|--------|
| pose_resnet_50     |    256x192 | 34.0M   |    8.9 | 0.704 | 0.886 |  0.783 |  0.671 |  0.772 | 0.763 | 0.929 |  0.834 |  0.721 |  0.824 |
| pose_resnet_50     |    384x288 | 34.0M   |   20.0 | 0.722 | 0.893 |  0.789 |  0.681 |  0.797 | 0.776 | 0.932 |  0.838 |  0.728 |  0.846 |
| pose_resnet_101    |    256x192 | 53.0M   |   12.4 | 0.714 | 0.893 |  0.793 |  0.681 |  0.781 | 0.771 | 0.934 |  0.840 |  0.730 |  0.832 |
| pose_resnet_101    |    384x288 | 53.0M   |   27.9 | 0.736 | 0.896 |  0.803 |  0.699 |  0.811 | 0.791 | 0.936 |  0.851 |  0.745 |  0.858 |
| pose_resnet_152    |    256x192 | 68.6M   |   15.7 | 0.720 | 0.893 |  0.798 |  0.687 |  0.789 | 0.778 | 0.934 |  0.846 |  0.736 |  0.839 |
| pose_resnet_152    |    384x288 | 68.6M   |   35.3 | 0.743 | 0.896 |  0.811 |  0.705 |  0.816 | 0.797 | 0.937 |  0.858 |  0.751 |  0.863 |
| **pose_hrnet_w32** |    256x192 | 28.5M   |    7.1 | 0.744 | 0.905 |  0.819 |  0.708 |  0.810 | 0.798 | 0.942 |  0.865 |  0.757 |  0.858 |
| **pose_hrnet_w32** |    384x288 | 28.5M   |   16.0 | 0.758 | 0.906 |  0.825 |  0.720 |  0.827 | 0.809 | 0.943 |  0.869 |  0.767 |  0.871 |
| **pose_hrnet_w48** |    256x192 | 63.6M   |   14.6 | 0.751 | 0.906 |  0.822 |  0.715 |  0.818 | 0.804 | 0.943 |  0.867 |  0.762 |  0.864 |
| **pose_hrnet_w48** |    384x288 | 63.6M   |   32.9 | 0.763 | 0.908 |  0.829 |  0.723 |  0.834 | 0.812 | 0.942 |  0.871 |  0.767 |  0.876 |

### Note:
- Flip test is used.
- Person detector has person AP of 56.4 on COCO val2017 dataset.
- pose_resnet_[50,101,152] is our previous work of [*Simple Baselines for Human Pose Estimation and Tracking*](http://openaccess.thecvf.com/content_ECCV_2018/html/Bin_Xiao_Simple_Baselines_for_ECCV_2018_paper.html).
- GFLOPs is for convolution and linear layers only.


### Results on COCO test-dev2017 with detector having human AP of 60.9 on COCO test-dev2017 dataset
| Arch               | Input size | #Params | GFLOPs |    AP | Ap .5 | AP .75 | AP (M) | AP (L) |    AR | AR .5 | AR .75 | AR (M) | AR (L) |
|--------------------|------------|---------|--------|-------|-------|--------|--------|--------|-------|-------|--------|--------|--------|
| pose_resnet_152    |    384x288 | 68.6M   |   35.3 | 0.737 | 0.919 |  0.828 |  0.713 |  0.800 | 0.790 | 0.952 |  0.856 |  0.748 |  0.849 |
| **pose_hrnet_w48** |    384x288 | 63.6M   |   32.9 | 0.755 | 0.925 |  0.833 |  0.719 |  0.815 | 0.805 | 0.957 |  0.874 |  0.763 |  0.863 |
| **pose_hrnet_w48\*** |    384x288 | 63.6M   |   32.9 | 0.770 | 0.927 |  0.845 |  0.734 |  0.831 | 0.820 | 0.960 |  0.886 |  0.778 |  0.877 |

### Note:
- Flip test is used.
- Person detector has person AP of 60.9 on COCO test-dev2017 dataset.
- pose_resnet_152 is our previous work of [*Simple Baselines for Human Pose Estimation and Tracking*](http://openaccess.thecvf.com/content_ECCV_2018/html/Bin_Xiao_Simple_Baselines_for_ECCV_2018_paper.html).
- GFLOPs is for convolution and linear layers only.
- pose_hrnet_w48\* means using additional data from [AI challenger](https://challenger.ai/dataset/keypoint) for training.

