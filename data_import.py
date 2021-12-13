import os
import sys
import tensorflow as tf
import tensorflow_datasets as tfds

# set environment variables
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# load dataset
ds = tfds.load('multi_news', data_dir="./input/multi_news", split="train")

# write data to expected file format
old_output=sys.stdout
count=0
for i in ds:
    if (count<10):
        file_name_document="file://./input/multi_news_input/document/" + str(count)
        # sys.stdout=file_name_document
        tf.print(i["document"], output_stream=file_name_document)
        sys.stdout.flush()

        file_name_summary="file://./input/multi_news_input/summary/" + str(count)
        # sys.stdout=file_name_summary
        tf.print(i["summary"], output_stream=file_name_summary)
        sys.stdout.flush()
        count+=1
