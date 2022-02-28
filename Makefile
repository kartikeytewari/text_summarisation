run_test:
	python3 -u test.py ./input/multi_news_input/document ./input/multi_news_input/summary > test.csv
	terminal-notifier -title "Text Summarisation" -message "Process completed" -sound "default"

run_train:
	python3 -u train.py ./input/multi_news_input/document ./input/multi_news_input/summary > data_visualisation/[0-99]doc_[90.0-100.0]gradient/raw_out.csv
	terminal-notifier -title "Text Summarisation" -message "Process completed" -sound "default" 

install:
	pip3 install requirements.txt

run:
	python3 main.py ./input/multi_news_input/document ./input/multi_news_input/summary > ./output/multi_news.csv

output_csv:
	perl -pe 's/((?<=,)|(?<=^)),/ ,/g;' output/multi_news.csv | column -t -s, | less  -F -S -X -K
