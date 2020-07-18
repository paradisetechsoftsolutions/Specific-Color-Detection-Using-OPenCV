# importing Modules
import cv2
import argparse
import numpy as np

class ColorDetection:

	def read_image_argparse(self):
		"""
		Using Argument Parser one can pass the image through the \
        terminal as argument flag
		"""
		self.ap = argparse.ArgumentParser()
		self.ap.add_argument("-i", "--image", required = True, help = "Path to the image")
		self.args = vars(self.ap.parse_args())
		self.image = cv2.imread(self.args["image"])
		return self.image

	def red_lower_upper(self, hsv_image, image_read):
		"""
		This code will create the red mask and show only \
		red portion from the image
		"""
		self.lower_red = np.array([160,20,70])
		self.upper_red = np.array([190,255,255])
		self.red = cv2.inRange(hsv_image, self.lower_red, self.upper_red)
		self.output_only_red = cv2.bitwise_and(image_read, image_read, mask = self.red)
		return self.output_only_red, self.red

	def draw_boundary_box(self, template_image, image_read):
		self.gray_image=cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
		self.result=cv2.matchTemplate(self.gray_image,template_image, cv2.TM_CCOEFF)
		self.sin_val, self.max_val, self.min_loc, self.max_loc=cv2.minMaxLoc(self.result)
		self.top_left = self.max_loc
		# increasing the size of bounding rectangle by 140 pixels
		self.bottom_right=(self.top_left[0]+140,self.top_left[1]+140)
		cv2.rectangle(image_read, self.top_left, self.bottom_right, (0,255,0),5)
		cv2.imshow('Bounding Box over template image',image_read)
		cv2.waitKey(0)

# creating the object of the class
color_detect = ColorDetection()
# Showing image read in the above step
image_read = color_detect.read_image_argparse()
# converting img from BGR (Blue-Green-Red) to HSV (hue-saturation-value)
hsv = cv2.cvtColor(image_read, cv2.COLOR_BGR2HSV)
# print("HSV is ......... \n", hsv)
red_detected_image = color_detect.red_lower_upper(hsv, image_read)[0]
cv2.imshow("input image vs only red portion", np.hstack([image_read, red_detected_image]))
cv2.waitKey(0)
template_image = cv2.imread('image1.jpg', 0)
color_detect.draw_boundary_box(template_image, image_read)
