from model import *
from data import *
from annotate import *
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from PIL import Image
import cv2


def inference(image_dir, score_thresh=0.70, image_width=192, image_height=256, label_to_detect=Person_label,
              device='cuda'):
    # For RCNN model
    # img = COCOdata(image_dir)

    img = Image.open(image_dir)
    # load the model
    pretrained_model = yolomodel()
    # print(pretrained_model.names)
    pretrained_model.to(device)
    pretrained_model.eval()

    arr_img = np.array(img)
    # infer the predictions
    start = time.time()
    with torch.no_grad():
        prediction = pretrained_model(image_dir)
    end = time.time()
    print("Total inference time: ", end - start)
    # prediction.show()

    # Get the bounding boxes of required objects
    dataframe = prediction.pandas().xyxy[0]
    boxes = [(row['xmin'], row['ymin'], row['xmax'], row['ymax']) for _, row in dataframe.iterrows() if
             row['name'] == 'person']
    scores = [(row['confidence']) for _, row in dataframe.iterrows() if row['name'] == 'person']
    num_object_detected = len(scores)

    displayed_obj = 0
    colors = ["blue", "green", "red", "pink", "yellow"]
    for i in range(num_object_detected):
        if scores[i] > score_thresh:
            displayed_obj += 1
            box = boxes[i]

            # Plot original image
            fig = plt.figure(i, figsize=(12, 12))
            ax1 = fig.add_subplot(1, 2, 1)
            ax1.imshow(img)

            # draw bounding box
            color = colors[i % len(colors)]
            ax1.add_patch(Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], alpha=0.35, facecolor=color,
                                    edgecolor=color, hatch='x'))

            rescaled_img = img.resize((image_width, image_height), box=(box[0], box[1], box[2], box[3]))
            rescaled_img = np.array(rescaled_img)

            # Rescale Image
            ax2 = fig.add_subplot(1, 2, 2)
            #ax2.imshow(rescaled_img)
            cv2.imshow("Rescaled image", rescaled_img)

            cv2.waitKey(1000)
            cv2.destroyAllWindows()


    print("Detected", displayed_obj, "objects with score >", score_thresh)


if __name__ == "__main__":
    inference(image_dir='C:/Object-Detection/coco2017/val2017/000000002473.jpg')
