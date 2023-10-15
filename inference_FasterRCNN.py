from PIL import Image
import torch
import time
from annotate import *
from model import *
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import utils_file

def inference_rcnn(img_path, label_to_detect=Person_label_rcnn, score_threshold=0.75, device='cuda',input_width=192, input_height=256):
    
    # put model into eval mode
    model = faster_rcnn_model()
    model = model.to(device)
    model.eval()
    
    # Open the Image
    img = Image.open(img_path)

    # Generate the input tensor and normalize
    img_tensor = torch.tensor(np.asarray(img)).permute(2,0,1).unsqueeze(0)
    img_tensor = img_tensor.float()/255.0 # Cast & Normalize
    img_tensor = img_tensor.to(device)
     
    # Do inference
    start = time.time()
    with torch.no_grad():
        predictions = model(img_tensor)
    end = time.time()
    inference_time = utils_file.calc_inferencetime(start=start, end=end)
    print("Inference time: ", inference_time)

    # Get the bounding boxes of the relevant objects
    object_indices = (predictions[0]['labels'] == label_to_detect).nonzero()
    boxes = predictions[0]['boxes'][object_indices].int().cpu().numpy()
    scores = predictions[0]['scores'][object_indices].cpu().numpy()
    num_objects_detected = boxes.shape[0]

    # For each object box, plot the bounding-box on the original image:
    displayed_objects = 0
    colors = ["blue", "green", "red", "pink","yellow"]
    for i in range(num_objects_detected):
        if scores[i][0] > score_threshold:
            displayed_objects += 1
          
            # Plot the original Image with the bounding box
            fig = plt.figure(i,figsize=(14, 6))
            ax1 = fig.add_subplot(1, 2, 1)
            ax1.imshow(img)   
            
            # draw bounding box
            x_start, y_start, x_end, y_end = boxes[i][0]
            color = colors[i % len(colors)]
            ax1.add_patch(Rectangle((x_start, y_start), x_end-x_start, y_end-y_start, alpha=0.35, facecolor=color, edgecolor=color, hatch='x'))

            # Rescale Input Image
            rescaled_img = img.resize((input_width,input_height), box=(x_start, y_start, x_end, y_end))
            rescaled_img = np.array(rescaled_img)

            # show rescaled Input Image
            ax2 = fig.add_subplot(1, 2, 2)
            ax2.imshow(rescaled_img)   
            
    print('---------------------------------------------')
    print("Detected", displayed_objects, "objects with score >", score_threshold)
    print('---------------------------------------------')

    plt.show()
    img.close()
    
    return inference_time


if __name__ == "__main__":
    inference_rcnn(img_path='C:/Object-Detection/coco2017/val2017/000000002473.jpg')