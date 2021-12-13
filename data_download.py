# Script to download datasets
import tensorflow_datasets as tfds

# tensorflow dataset multi_news
ds = tfds.load('multi_news', data_dir="./input/multi_news")
