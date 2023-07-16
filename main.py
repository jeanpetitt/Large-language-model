import pandas as pd, requests, gzip, shutil

url =  ('https://github.com/jeanpetitt/Large-language-model/raw/main/movie_data.csv.gz')
filename = url.split('/')[-1]

with open(filename, "wb") as f:
  r = requests.get(url)
  f.write(r.content)
  print(f)

with gzip.open('movie_data.csv.gz', 'rb') as f_in:
  with open('movie_data.csv', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)

df = pd.read_csv('movie_data.csv', header=None)
print(df.head(2))