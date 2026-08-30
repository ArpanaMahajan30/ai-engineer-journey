# AI Job Market Analysis (2030)

An exploratory data analysis project examining how AI is expected to impact global job roles, salaries, hiring demand, automation risk, and required skills through 2030.

---

## 🎯 Business Questions

- Which job roles and countries offer the highest average salaries?
- Which roles have the strongest projected demand and growth through 2030?
- How exposed are jobs in the dataset to AI-driven automation?
- What technical and soft skills are most frequently required?
- How do education level and years of experience relate to salary?
- How are remote work, hiring trends, automation level, upskilling needs, and AI tool usage represented across the workforce?

---

## 📊 Dataset

**Source:** [AI Impact in Future on Jobs Market in 2030](https://www.kaggle.com/datasets/muhammadwaqas023/ai-impact-in-future-on-jobs-market-in-2030) by muhammadwaqas023, via Kaggle.

The dataset models how Artificial Intelligence is expected to transform employment, skills, and careers by 2030.

- **Size:** 3,000 rows × 20 columns
- **Key columns:** `Job_Title`, `Industry`, `Country`, `Education_Level`, `Years_Experience`, `AI_Replacement_Risk`, `Future_Demand_Score`, `Remote_Work_Possibility`, `Average_Salary_USD`, `Required_Skills`, `Automation_Level`, `Job_Growth_2030`, `Company_Size`, `AI_Tool_Usage`, `Upskilling_Needed`, `Hiring_Trend_2026`

The raw CSV is not included in this repository. Download it from Kaggle and place it in the `data/` folder as:

`AI_Impact_on_Jobs_2030.csv`

> **Note:** This dataset appears to be synthetic/illustrative rather than survey-collected real-world data. Findings below describe patterns within this dataset, not validated labor-market forecasts.

---

## 🛠 Tools & Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook

---

## 🔍 What This Analysis Covers

1. Data loading, inspection, and quality checks
2. Job title frequency across the dataset
3. Salary distribution and potential outliers
4. Highest-paying job roles and countries
5. AI Replacement Risk distribution
6. Future demand by job title
7. Automation level distribution
8. Projected job growth by job title through 2030
9. Remote work and hiring trends
10. Upskilling needs
11. Most frequently required technical and soft skills
12. Education level vs. salary
13. Years of experience vs. salary and correlation analysis
14. AI tool usage across the workforce

---

## 📈 Key Findings

1. **Highest-paying role:** HR Specialist, with an average salary of approximately $131,882.

2. **Highest-demand role:** Software Developer has the highest average Future Demand Score.

3. **Highest-paying country:** The United Kingdom has the highest average salary among the countries represented in the dataset.

4. **AI Replacement Risk:** The average AI Replacement Risk is approximately 0.503, with risk levels distributed across the dataset rather than concentrated at one extreme.

5. **Work model:** Hybrid work is the most common arrangement, although Hybrid, Yes, and No categories are relatively close in frequency.

6. **Hiring outlook:** Growing and Stable hiring trends are almost equally common, while Declining roles occur slightly less frequently.

7. **Automation level:** Automation exposure is relatively balanced — Low (1,037), Medium (1,011), and High (952).

8. **Projected job growth:** Blockchain Developer has the highest average `Job_Growth_2030` value at approximately 18.94, followed by Software Developer (18.60) and Healthcare Analyst (18.54). Several technology-focused roles appear among the top-growth occupations.

9. **Upskilling need:** Upskilling needs are almost evenly divided, with 1,511 observations marked "No" and 1,489 marked "Yes."

10. **Education vs. salary:** Average salaries are relatively similar across education levels. Higher education levels do not consistently correspond to higher average salaries within this dataset.

11. **Skills in demand:** Cloud Computing is the most frequently listed skill. Technical skills such as Azure, Machine Learning, Deep Learning, and Kubernetes appear frequently, while Communication and Leadership also rank highly.

12. **Experience vs. salary:** The correlation between years of experience and salary is approximately `r = 0.013`, indicating little to no linear relationship between the two variables in this dataset.

13. **AI tool usage:** AI tool usage is relatively balanced across Low, Moderate, and High categories, with Low usage being slightly more common.

Full findings, visualizations, recommendations, and conclusions are documented inside the notebook.

---

## ▶️ How to Run

1. Download the dataset from the [Kaggle dataset page](https://www.kaggle.com/datasets/muhammadwaqas023/ai-impact-in-future-on-jobs-market-in-2030).
2. Create a `data` folder inside the project directory.
3. Place `AI_Impact_on_Jobs_2030.csv` inside the `data` folder.
4. Open `ai_impact_analysis.ipynb` in Jupyter Notebook or VS Code.
5. Restart the kernel and run all cells from top to bottom.

---

## 📁 Project Structure

```text
project_01__ai_impact_on_jobs/
│
├── data/
│   └── AI_Impact_on_Jobs_2030.csv
│
├── ai_impact_analysis.ipynb
│
└── README.md
```

---

## 👩‍💻 Author

**Arpana Mahajan**
[LinkedIn](https://www.linkedin.com/in/arpana-mahajan-93b1ab191/) · [GitHub](https://github.com/ArpanaMahajan30)
