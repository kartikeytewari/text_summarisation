run_test:
	python3 -u main.py ./input/multi_news_input/document ./input/multi_news_input/summary > data_visualisation/100doc_100gradient/raw_out.csv
	terminal-notifier -title "Text Summarisation" -message "Process completed" -sound "default" 

install:
	pip3 install requirements.txt

run:
	python3 main.py ./input/multi_news_input/document ./input/multi_news_input/summary > ./output/multi_news.csv

output_csv:
	perl -pe 's/((?<=,)|(?<=^)),/ ,/g;' output/multi_news.csv | column -t -s, | less  -F -S -X -K
