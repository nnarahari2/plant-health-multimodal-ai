# Multimodal Plant Health Intelligence System 🌱

A deep learning project exploring multimodal learning for plant health prediction using plant imagery and environmental data.

## Goal

This project investigates whether combining visual plant information with environmental features can improve prediction performance.

Models compared:

- Image-only model
- Sensor-only model
- Image + sensor fusion model

The goal is to determine whether multimodal learning improves plant health classification compared to single-input approaches.

## Tech Stack

- Python
- PyTorch
- OpenCV
- NumPy
- Pandas
- Scikit-Learn

## Planned Architecture

### Image Branch

Plant Image → CNN → Feature Extraction

### Sensor Branch

Temperature  
Humidity  
Soil Moisture  
Light Level  

→ MLP → Feature Extraction

### Fusion

Image Features + Sensor Features  
↓  
Fusion Layer  
↓  
Plant Health Prediction

## Project Status

🚧 Currently in development

Planned phases:

- Dataset collection
- Environmental data generation
- Image-only baseline
- Sensor-only baseline
- Multimodal fusion model
- Experiments and evaluation

## Motivation

Inspired by prior work involving agricultural sensing systems and an interest in artificial intelligence, computer vision, and intelligent systems.

## Future Work

- Add real sensor hardware integration
- Expand to additional plant datasets
- Investigate uncertainty and robustness methods

