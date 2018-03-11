#!/usr/bin/env python3

import numpy as np
import imageio
from scipy.misc import imresize
from scipy.cluster.vq import kmeans


class ColorClusters():

    _save_block_size = 30
    _transparency_threshold = 0.9
    _max_img_size = 300

    def __init__(self):
        pass

    def _normalizeImage(self, img):
        """
            Normalize an image.

            :param numpy.array img: Input image
            :rtype: numpy.array
            :return: Numpy array with values in [0, 1] and resized if input
                     size is too large
        """
        h, w, _ = img.shape
        if w > self._max_img_size or h > self._max_img_size:
            img = imresize(img,
                           (self._max_img_size, self._max_img_size),
                           interp='nearest')
        return img / 255.

    def loadImage(self, path):
        """
            Load an image from a path.

            :param str path: Image filepath
            :rtype: numpy.array
            :return: Numpy array representing the image
        """
        oimg = imageio.imread(path)
        img = self._normalizeImage(oimg)
        h, w, c = img.shape
        return img.reshape((h * w, c))

    def getClusters(self, path, centers):
        """
            Get the cluter centers given an image path.

            :param str path: Image filepath
            :param int centers: Number of clusters
            :rtype: numpy.array
            :return: List of cluster centers. All the centers are points of the
                     image
        """
        img = self.loadImage(path)
        # Ignore transparent pixels
        _, c = img.shape
        if c > 3:
            b = img[:, 3] > self._transparency_threshold
            img = img[b][:, 0:3]
        centers, distorsion = kmeans(img, centers, check_finite=False)
        # Get the colors which are closer to the centers
        points = np.zeros(centers.shape)
        for i, center in enumerate(centers):
            # Compute the difference between the data points and the center
            dist = np.linalg.norm(img - center, axis=1)
            # Get the point with the lowest difference
            points[i] = img[np.argmin(dist)]
        # De-normalize
        points = points * 255.
        return points.astype('B')

    def saveCentersToImage(self, centers, path):
        """
            Save a list of centers as an image.

            :param numpy.array centers: Center list
            :param str path: Savepath
        """
        width = self._save_block_size * len(centers)
        height = self._save_block_size
        img = np.ones((height, width, 3), dtype=np.uint8)
        for i, center in enumerate(centers):
            start = i * self._save_block_size
            end = start + self._save_block_size
            img[0:self._save_block_size, start:end, :] *= center
        # Save the image to file
        imageio.imwrite(path, img)


def create():
    return ColorClusters()
