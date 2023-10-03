import torch
import torchvision

def yolomodel():
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    return model

def ssdmodel():
    ssdModel = torch.hub.load("NVIDIA/DeepLearningExamples:torchhub",
                              "nvidia_ssd")
    utils = torch.hub.load("NVIDIA/DeepLearningExamples:torchhub",
                           "nvidia_ssd_processing_utils")
    return ssdModel, utils

def faster_rcnn_model():
   model = torchvision.models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
   return model

    