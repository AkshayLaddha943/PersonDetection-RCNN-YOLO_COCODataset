import matplotlib.pyplot as plt
import inference
import inference_FasterRCNN
import utils_file

inference_time_rcnn = inference_FasterRCNN.inference_rcnn(img_path='C:/Object-Detection/coco2017/val2017/000000002473.jpg')
inference_time_yolo = inference.inference(img_path='C:/Object-Detection/coco2017/val2017/000000002473.jpg')
utils_file.plot_results(inference_time_rcnn, inference_time_yolo)


# def plot_results(prediction_time0, prediction_time1):
    