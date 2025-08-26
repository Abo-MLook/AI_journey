from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


img = Image.open('oboe-with-book.jpg')
_ = plt.imshow(img)
plt.show()


imggray = img.convert('LA')
_ = plt.imshow(imggray)
plt.show()



imgmat = np.array(list(imggray.getdata(band=0)), float)
imgmat.shape = (imggray.size[1], imggray.size[0])
imgmat = np.matrix(imgmat)
_ = plt.imshow(imgmat, cmap='gray')
plt.show()


U, sigma, V = np.linalg.svd(imgmat)
reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
_ = plt.imshow(reconstimg, cmap='gray')
plt.show()



for i in [2, 4, 8, 16, 32, 64]:
    reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
    plt.imshow(reconstimg, cmap='gray')
    title = "n = %s" % i
    plt.title(title)
    plt.show()

print(imgmat.shape)
full_representation = 4032*3024

svd64_rep = 64*4032 + 64 + 64*3024

print(svd64_rep/full_representation)

#Specifically, the image represented as 64 singular vectors is 3.7% of the size of the original!
#Alongside images, we can use singular vectors for dramatic, lossy compression of other types of media files.