[k-NN classifier for image classification](https://www.pyimagesearch.com/2016/08/08/k-nn-classifier-for-image-classification/)


In the remainder of this blog post, I’ll detail how the k-NN classifier works. We’ll then apply k-NN to the [Kaggle Dogs vs. Cats dataset](https://www.kaggle.com/c/dogs-vs-cats/data)

The goal of the Dogs vs. Cats dataset, as the name suggests, is to classify whether a given image contains a dog or a cat.

![](https://www.pyimagesearch.com/wp-content/uploads/2016/08/knn_animal_clusters-1024x936.jpg)

In order to apply the k-nearest Neighbor classification, we need to define a distance metric or similarity function. 

Common choices include the [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance):

| ![Euclidean distance](https://pyimagesearch.com/wp-content/uploads/2016/08/knn_classifier_euclidean.png) |
|:--:|
| *Euclidean distance* |

And the [Manhattan/city block distance](https://en.wikipedia.org/wiki/Taxicab_geometry):

| ![Manhattan/city block distance](https://pyimagesearch.com/wp-content/uploads/2016/08/knn_classifier_manhattan.png) |
|:--:|
| *Manhattan/city block distance* |

Other distance metrics/similarity functions can be used depending on your type of data (the chi-squared distance is often used for distributions [i.e., histograms]). In today’s blog post, for the sake of simplicity, we’ll be using the Euclidean distance to compare images for similarity.

For work you need:
- [scikit-learn library](http://scikit-learn.org/stable/)
- [imutils library](https://github.com/jrosebr1/imutils)
- [opencv-python library](https://pypi.org/project/opencv-python/)