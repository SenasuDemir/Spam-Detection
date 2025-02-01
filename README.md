# 📌 YouTube Spam Detection Project

## Introduction
Spam detection is a critical challenge in online platforms, particularly in user-generated content such as YouTube comments. This project focuses on detecting spam comments in YouTube videos using machine learning techniques.

The **YouTube Spam Collection dataset** consists of 1,956 real messages extracted from five popular videos, with comments labeled as either spam (1) or ham (0). The dataset contains structured attributes such as `COMMENT_ID`, `AUTHOR`, `DATE`, `CONTENT`, and `CLASS`, which serve as the foundation for feature extraction and model training.

By leveraging **Natural Language Processing (NLP)** techniques and various **machine learning algorithms**, this project aims to enhance automated moderation systems, ensuring a cleaner and more meaningful user experience.

---

## 🧠 Objectives
- **Classify YouTube comments** as spam or non-spam based on textual content.
- Evaluate multiple machine learning models to find the best-performing one.
- Use **NLP** methods like tokenization, stopword removal, and vectorization to preprocess the data.
- Explore models such as **Logistic Regression**, **Gradient Boosting**, **Random Forest**, and more.

---

## 📊 Models and Results
The following machine learning models were evaluated for spam detection:

1. **Logistic Regression**
2. **Gradient Boosting**
3. **AdaBoost**
4. **Decision Tree**
5. **Random Forest**
6. **Naïve Bayes** (Bernoulli and Multinomial)

Based on accuracy scores, **Logistic Regression** and **Gradient Boosting** achieved the highest accuracy of **88.27%**, making them the best-performing models for this task.

### 🔍 Confusion Matrix Analysis (Logistic Regression)
- **True Positives (Spam correctly classified as Spam):** 177
- **True Negatives (Not Spam correctly classified as Not Spam):** 169
- **False Positives (Not Spam incorrectly classified as Spam):** 7
- **False Negatives (Spam incorrectly classified as Not Spam):** 39

The model performs well in detecting spam comments, but there is room for improvement, particularly in minimizing false negatives.

---

## 🚀 Final Thoughts
- **Logistic Regression** and **Gradient Boosting** were found to be the most effective for spam detection tasks.
- Future work can involve exploring word embeddings like **Word2Vec**, **TF-IDF**, or **BERT**, as well as **ensemble techniques** to further enhance classification performance.
- Automating spam detection contributes to a safer, cleaner online community by reducing unwanted spam messages effectively.

---

## 📥 Dataset
The dataset used for this project is the **YouTube Spam Collection**. You can download the dataset from Kaggle:

- [YouTube Spam Collection Dataset](https://www.kaggle.com/datasets/lakshmi25npathi/images/code)

---

## 🌐 Hugging Face Space
The project is hosted on Hugging Face Spaces. You can access and interact with the spam detection model here:

- [Spam Detection on Hugging Face](https://huggingface.co/spaces/Senasu/Spam_Detection)

---
