import cv2
import matplotlib.pyplot as plt

def plot_img_yolo(image_path:str,label_path:str, color = (255,0,0), thickness = 4)-> None:
  """
  Method to plot the bounding boxes on an image annotated in YOLO Darknet txt format
  NOTE: This method is meant for plotting only one class perfectly as of now!
  """
  # Read the image
  img = cv2.imread(image_path)
  # Convert it to RGB Color Space
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  # Get the image dimensions
  img_w, img_h, _ = img.shape
  # Read the annotations from the label file
  label_list = []
  with open(label_path, "r") as f:
    for line in f:
      label_list.append(line.split(" "))
  # Plotting all the bounding boxes
  for labels in  label_list:
    # Get the coordinates in YOLO format for each bounding box
    _, x_center, y_center, bbox_width, bbox_height = list(map(float, labels))
    # Coverting the coordindates w.r.t the image dimensions
    x_min = int((x_center - bbox_width/2) * img_w)
    y_min = int((y_center - bbox_height/2) * img_h)
    x_max = int((x_center + bbox_width/2) * img_w)
    y_max = int((y_center + bbox_height/2) * img_h)
    # Plot the bounding box
    img = cv2.rectangle(img, (x_min, y_min), (x_max, y_max), color , thickness) 
    plt.imshow(img)