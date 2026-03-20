# InfectAI – Setup and Run Guide

This document explains how to install dependencies and run the InfectAI application locally.

---

## 1. Create a virtual environment
### - For MacOS/Linux

```
python3 -m venv venv
source venv/bin/activate
```
### - For Windows

```
python -m venv venv
venv\Scripts\activate
```

## 2. Install Dependncies

```
pip install --upgrade pip
pip install -r requirements.txt
```

## 3. Run the application

```
streamlit run app.py
```