# 🛡️ Online Safety & Child Protection Analysis

### AI, Platform Governance & Regulatory Transparency (EU DSA + Jigsaw Dataset)

---

## 📌 Overview

This project presents a **data-driven analysis of online safety, content moderation, and child protection mechanisms** across major digital platforms.

It combines:

* 🇪🇺 **Regulatory transparency data** from the **EU Digital Services Act (DSA)**
* 💬 **Content-level toxicity data** from the **Jigsaw Toxic Comment dataset**

The goal is to evaluate:

* Platform moderation behavior
* Automated vs human detection systems
* Child safety enforcement
* Toxic content distribution

---

## 🎯 Objectives

* Analyze **platform-level moderation decisions** using real regulatory data
* Evaluate **automation in content moderation systems**
* Identify **child safety-related moderation patterns**
* Compare **policy-level enforcement vs content-level toxicity**
* Build a **scalable, modular data analysis pipeline**

---

## 📊 Datasets Used

### 1. 🇪🇺 EU DSA Transparency Database

* **Source:** European Commission
* **Link:** https://transparency.dsa.ec.europa.eu/
* **Type:** Regulatory dataset (Statements of Reasons)
* **Format:** CSV (daily exports, large-scale)

#### 📌 Description:

Each record represents a **moderation decision** made by a platform under the Digital Services Act.

#### 📂 Key Fields:

* `platform_name` → Platform (Meta, TikTok, etc.)
* `decision_ground` → Legal or platform rule basis
* `category_specification` → Type of harmful content
* `automated_detection` → AI vs human detection
* `decision_visibility` → Action taken (removed, restricted)
* `created_at` → Timestamp

#### ⚠️ Data Handling:

* Dataset is **very large (GB-scale per day)**
* This project uses:

  * **1–3 days of data (sampling strategy)**
  * Random sampling for performance

---

### 2. 💬 Jigsaw Toxic Comment Dataset

* **Source:** Kaggle
* **Link:** https://www.kaggle.com/datasets/julian3833/jigsaw-toxic-comment-classification-challenge
* **Type:** Labeled NLP dataset

#### 📌 Description:

Contains user-generated comments labeled across multiple toxicity categories.

#### 📂 Key Fields:

* `comment_text`
* `toxic`
* `severe_toxic`
* `obscene`
* `threat`
* `insult`
* `identity_hate`

#### 🧠 Feature Engineering:

* `toxicity_score` → Sum of toxicity labels
* `is_toxic` → Binary classification

---

## 🏗️ Project Architecture

```bash
online-safety-project/
│
├── data/
│   ├── dsa/                  # EU DSA dataset (multiple CSV files)
│   └── jigsaw.csv           # Jigsaw dataset
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── analysis.py
│   ├── visualization.py
│   └── utils.py
│
├── outputs/                 # Generated charts and results
│
├── main.py                  # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate environment

```bash
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 📈 Outputs

All results are saved in:

```bash
outputs/
```

### Generated Files:

* 📊 `platform_distribution.png` → Platform moderation volume
* 📊 `toxicity.png` → Toxicity distribution
* 📊 Additional visual insights

---

## 🔍 Key Analysis Performed

### 🧩 1. Platform Moderation Analysis

* Volume of moderation decisions
* Platform-level comparison

### 🤖 2. Automation Analysis

* % of automated vs human moderation
* AI adoption across platforms

### 🛡️ 3. Child Safety Detection

* Filtering of child-related harmful content
* Platform enforcement patterns

### 💬 4. Toxic Content Analysis

* Distribution of toxicity levels
* Severity classification

---

## 🧠 Methodology

* **Data Integration:** Regulatory + NLP datasets
* **Sampling Strategy:** Large-scale data handling
* **Feature Engineering:** Toxicity scoring
* **Statistical Analysis:** Distribution & correlation
* **Visualization:** Matplotlib + Seaborn

---

## ⚠️ Limitations

* DSA dataset limited to **EU regulatory scope**
* Sampling used due to **large data size**
* Jigsaw dataset may not fully reflect real platform content

---

## 🚀 Future Improvements

* Add **multi-platform comparison (TikTok, YouTube)**
* Integrate **real-time API data**
* Apply **NLP techniques (keyword extraction, sentiment)**
* Build **interactive dashboard (Streamlit / Power BI)**

---

## 🏆 Key Takeaways

* Platforms rely heavily on **automated moderation systems**
* Child safety enforcement varies significantly
* Regulatory datasets provide **valuable transparency insights**
* Combining policy + data gives **stronger analysis**

---

## 👤 Author

**Your Name**

* Data Science | AI Policy | Governance Analysis

---

## 📜 License

This project uses publicly available datasets under:

* EU Open Data License
* Kaggle dataset license

---

## ⭐ If you found this useful

Give this repo a ⭐ and feel free to contribute!

---
