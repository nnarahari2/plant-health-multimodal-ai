# Plant Health Multimodal AI

## Overview

This project implements a multimodal plant health monitoring system using computer vision and environmental sensor fusion.

The system combines:
- Plant image classification using deep learning
- Environmental sensor data collection
- Multimodal fusion for plant health prediction

## Features

- CNN-based image classification
- Sensor-based environmental monitoring
- Multimodal fusion model
- Real-time image inference
- Confusion matrix evaluation
- Accuracy comparison visualization

## Model Architecture

The image branch uses ResNet18 for feature extraction.

The sensor branch uses a multilayer perceptron (MLP) for processing:
- Temperature
- Humidity
- Soil moisture

The extracted features are fused together for final prediction.

## Hardware Components

- ESP32
- DHT22 temperature/humidity sensor
- Capacitive soil moisture sensor
- Breadboard
- Jumper wires

## Results

| Model | Accuracy |
|---|---|
| Image Model | 91.28% |
| Sensor Model | 30.80% |
| Fusion Model | 90.00% |

The project includes:
- Accuracy comparison plots
- Confusion matrices
- Fusion model evaluation

## Project Structure

```text
plant-health-multimodal-ai/
│
├── data/
├── models/
├── notebooks/
├── results/
├── scripts/
├── demo/
├── README.md
```

## Future Work

- Real-time sensor integration
- Live multimodal inference
- Edge deployment
- Flask dashboard

