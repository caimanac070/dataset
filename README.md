#Dataset

This dataset was generated in Python (`dataset.py`) as part of the activity **SUPERVISED vs UNSUPERVISED LEARNING**.  
It contains 500 synthetic student records with demographic, academic, and financial information, plus the target variable **dropout (yes/no)**.



## How to generate the dataset

First, run the Python script to create the file `dropout_data.csv`:

bash
python dataset.py


This will create a CSV file named **dropout_data.csv** in the same folder.



## How to open the dataset

Once the CSV file has been generated, you can open it in Python with pandas:

python
import pandas as pd

df = pd.read_csv("dropout_data.csv")

print(df.shape)   # Show dataset dimensions (rows, columns)
print(df.head())  # Show the first 5 rows




## Variables

- **age** (int): Student age, usually between 16–30. Includes some outliers (e.g., 10, 45, 60).  
- **gender** (categorical): 'M' or 'F'. About 5% missing values.  
- **origin** (categorical): 'urban' or 'rural'. About 5% missing values.  
- **highschool_avg** (float): High school GPA (0–5). Includes some outliers (negative values, values >5).  
- **admission_score** (int): Admission test score (0–100). Includes some outliers (>100 and negative values).  
- **first_sem_avg** (float): First semester GPA (0–5). Includes missing values and some outliers.  
- **socioeconomic_level** (int): Socioeconomic level (1–6).  
- **scholarship** (categorical): 'yes' or 'no'. Some missing values.  
- **loan** (categorical): 'yes' or 'no'. Some missing values.  
- **financial_aid** (categorical): 'yes' or 'no'.  
- **dropout** (categorical): 'yes' or 'no'. Target variable generated with higher probability for students with low academic performance, no scholarship, and loans.



## Missing values and outliers

- Missing values were introduced in `gender`, `origin`, `highschool_avg`, `first_sem_avg`, `scholarship`, and `loan`.  
- Outliers were added in `age`, `highschool_avg`, and `admission_score` to simulate data issues.  



## Dataset size

- Records: 500  
- Columns: 11  
