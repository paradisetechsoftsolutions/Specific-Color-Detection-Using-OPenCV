# Specific-Color-Detection-Using-OPenCV

Colour detection is necessary for recognizing objects and its coomonly used as a tool in various image editing and drawing apps. Colour detection is the process of detecting colour as well as name of color. A color detection algorithm identifies pixels in an image that match a specified color or color range. Detected colour pixels can then be changed to distinguish them from the rest of the image

# Prerequisites
OpenCV and numpy are the Python packages that are necessary for this project in Python. Moreover, other requirements can be check from requirement.txt file given in the repository.

# Some important functions used in the code
* **cv2.imread** - Loads an image from a file
* **cv2.inRange** - Checks if array elements lie between the elements of two other arrays. Threshold the HSV image for a range of red color in this repositoty code.
* **cv2.bitwise_and** - Bitwise operations are used in image manipulation and used for extracting essential parts in the image.
* **cv2.matchTemplate** - Template Matching is a method for searching and finding the location of a template image in a larger image.

# Steps for Building
* Reading image
* Converting RGB image to HSV
* Colour detection
* Displaying

# What is HSV ?
HSV stands for Hue Saturation Value. Commonly used color space conversion methods are: BGR ↔ Gray and BGR ↔ HSV. For HSV, hue range is [0,179], saturation range is [0,255], and value range is [0,255]. Different software use different scales. So if you are comparing OpenCV values with them, you need to normalize these ranges. After converting BGR image to HSV, we can extract a colored object. We threshold the HSV image for a range of our desired color. Now after extracting, we can do whatever we want to do on that image.

# Running code and expected output of the input image

The image that we are going to use in this repository is shown below as well as attached in repository also.

![image](https://user-images.githubusercontent.com/39157936/87852154-2ded9180-c91d-11ea-8d58-0c0b67dcc50b.jpg)

# Masked image showing only detect red color [right side] only:
![object found_screenshot_15 07 2020](https://user-images.githubusercontent.com/39157936/87851622-16f87080-c918-11ea-811b-709a63478db0.png)

# Bounding box over detected patch of image

![Bounding Box over template image_screenshot_18 07 2020](https://user-images.githubusercontent.com/39157936/87851634-31cae500-c918-11ea-9925-26c31373c687.png)  

# Running the code  

To run the code , I would recommend to create virtual environment and then install requirements file.To create the virtual environment please do follow below command  

```
sudo apt-get install virtualenv  
```  
Now it is time to create virtual env using the below command   

```
virtualenv --python python3.5 *name_of_env*  
```    
Activate the virtualenv using the below command  

```
source name_of_env/bin/activate  
```  

Now install the requirement using the below command  

```
pip3 install -r requirements.txt  
```    

Done. Now it is the time to run the main code  

```
python3 specific_color_using_opencv.py --image image.jpg  
```
