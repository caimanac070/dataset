import numpy as np
import pandas as pd


np.random.seed(42)

N = 500  


age = np.random.normal(19, 3, size=N).astype(int)
age = np.clip(age, 16, 30)

gender = np.random.choice(['M', 'F'], size=N, p=[0.52, 0.48])
origin = np.random.choice(['urban', 'rural'], size=N, p=[0.7, 0.3])

highschool_avg = np.round(np.random.normal(3.5, 0.7, size=N), 2)
admission_score = np.random.randint(0, 101, size=N)
first_sem_avg = np.round(np.random.normal(3.0, 0.8, size=N), 2)


socioeconomic_level = np.random.choice([1,2,3,4,5,6], size=N, p=[0.10,0.15,0.30,0.25,0.15,0.05])
scholarship = np.random.choice(['yes','no'], size=N, p=[0.3,0.7])
loan = np.random.choice(['yes','no'], size=N, p=[0.4,0.6])
financial_aid = np.random.choice(['yes','no'], size=N, p=[0.25,0.75])


dropout_prob = (
    (first_sem_avg < 3).astype(int) * 0.5 +
    (scholarship == 'no').astype(int) * 0.2 +
    (loan == 'yes').astype(int) * 0.3
)
dropout = np.where(np.random.rand(N) < dropout_prob, 'yes', 'no')


df = pd.DataFrame({
    'age': age,
    'gender': gender,
    'origin': origin,
    'highschool_avg': highschool_avg,
    'admission_score': admission_score,
    'first_sem_avg': first_sem_avg,
    'socioeconomic_level': socioeconomic_level,
    'scholarship': scholarship,
    'loan': loan,
    'financial_aid': financial_aid,
    'dropout': dropout
})


for col in ['gender','origin','highschool_avg','first_sem_avg']:
    df.loc[df.sample(frac=0.05).index, col] = np.nan


df.loc[np.random.choice(df.index, 5), 'age'] = [45, 50, 60, 70, 10]   # edades raras
df.loc[np.random.choice(df.index, 5), 'highschool_avg'] = [6, 7, -1, 8, -2]  # notas fuera de rango
df.loc[np.random.choice(df.index, 3), 'admission_score'] = [120, -5, 140]   # puntajes inválidos


df.to_csv("dropout_data.csv", index=False)

print("Dataset generado: dropout_data.csv con", df.shape[0], "registros")
