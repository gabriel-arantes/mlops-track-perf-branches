import pandas as pd

url_train='https://drive.google.com/file/d/1_lR9J9bzi27mFd4YtG9v-uyYQrsLTQjn/view?usp=sharing'
file_id_train = url_train.split('/')[-2]
read_url_train ='https://drive.google.com/uc?id=' + file_id_train

# read the train
df_train = pd.read_csv(read_url_train)
df_train.to_csv("train.csv")

url_test='https://drive.google.com/file/d/1_lR9J9bzi27mFd4YtG9v-uyYQrsLTQjn/view?usp=sharing'
file_id_test = url_test.split('/')[-2]
read_url_test ='https://drive.google.com/uc?id=' + file_id_test

# read the test
df_test = pd.read_csv(read_url_test)
df_test.to_csv("test.csv")