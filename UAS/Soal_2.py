import pandas as pd

data = [
    [ 'mahasiswa 1', 90,80],
    [ 'mahasiswa 2', 50, 60],
    [ 'mahasiswa 3', 65, 70]
]

df = pd.DataFrame(data, columns=['nama', 'algoritma dan struktur data 2', 'matematika numerik'])

df['rata-rata'] = df[['algoritma dan struktur data 2','matematika numerik']].mean(axis=1)

print('data mahasiswa dan nilai rata-rata:')
print(df)

print('nilai rata-rata untuk setiap mahasiswa:')
for index, row in df.iterrows():
    print(f'{row['nama']} {row['rata-rata']:.2f}')