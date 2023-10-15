import time
import matplotlib.pyplot as plt

def calc_inferencetime(start, end):
    total_time = end - start
    return total_time

def plot_results(prediction_time0, prediction_time1):
    labels = ['Faster RCNN', 'YOLO']
    times = [prediction_time0, prediction_time1]
    plt.bar(labels, times, color=['blue', 'green'])
    plt.title("Inference Comparison")
    plt.xlabel('Model')
    plt.ylabel('Inference Time (s)')
    plt.show()