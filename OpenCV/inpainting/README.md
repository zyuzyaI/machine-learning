# [Perform image inpainting with OpenCV](https://www.pyimagesearch.com/2020/05/18/image-inpainting-with-opencv-and-python/)

Technology has advanced image painting significantly, allowing us to:

- Restore old, degraded photos
- Repair photos with missing areas due to damage and aging
- Mask out and remove particular objects from an image (and do so in an aesthetically pleasing way)

![](https://www.pyimagesearch.com/wp-content/uploads/2020/05/opencv_inpainting_example.jpg) 

[image sourse](https://heartbeat.fritz.ai/guide-to-image-inpainting-using-machine-learning-to-edit-and-correct-defects-in-photos-3c1b0e13bbd0?gi=9e620cf85884)

The OpenCV library ships with two inpainting algorithms:

1. cv2.INPAINT_TELEA: [An image inpainting technique based on the fast marching method](https://www.researchgate.net/publication/238183352_An_Image_Inpainting_Technique_Based_on_the_Fast_Marching_Method) (Telea, 2004)
2. cv2.INPAINT_NS: [Navier-stokes, Fluid dynamics, and image and video inpainting](https://www.math.ucla.edu/~bertozzi/papers/cvpr01.pdf) (Bertalmío et al., 2001)

When applying inpainting with OpenCV, we need to provide two images:

1. The input image we wish to inpaint and restore. Presumably, this image is “damaged” in some manner, and we need to apply inpainting algorithms to fix it
2. The mask image, which indicates where in the image the damage is. This image should have the same spatial dimensions (width and height) as the input image. Non-zero pixels correspond to areas that should be inpainted (i.e., fixed), while zero pixels are considered “normal” and do not need inpainting

![](https://www.pyimagesearch.com/wp-content/uploads/2020/05/opencv_inpainting_results02.png)

