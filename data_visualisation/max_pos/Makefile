all:
	make delete_log 
	make compile
	make run_folder_1
	make run_folder_2
	make run_folder_3
	make run_folder_4
	make delete_binary

delete_binary:
	trash in.csv in.temp.csv in.txt main main.dSYM

delete_log:
	trash ../0-9_doc_1-10_gradient/max_position.txt
	trash ../0-9_doc_1-100_gradient/max_position.txt
	trash ../0-99_doc_1-100_gradient/max_position.txt
	trash ../0-99_doc_90.0-100.0_gradient/max_position.txt

compile:
	g++-11 -std=c++20 -Wshadow -Wall -Wno-unused-result -fsanitize=undefined -fmax-errors=1 -g -D_GLIBCXX_DEBUG -o main main.cpp

parse_input:
	sed '1d' in.csv > in.temp.csv
	wc -l < in.temp.csv > in.txt
	sed 's/,/ /g' in.temp.csv >> in.txt

run_folder_1:
	cp ../0-9_doc_1-10_gradient/out.csv in.csv
	make parse_input 
	./main < in.txt > ../0-9_doc_1-10_gradient/max_position.txt

run_folder_2:
	cp ../0-9_doc_1-100_gradient/out.csv in.csv
	make parse_input
	./main < in.txt > ../0-9_doc_1-100_gradient/max_position.txt

run_folder_3:
	cp ../0-99_doc_1-100_gradient/out.csv in.csv
	make parse_input
	./main < in.txt > ../0-99_doc_1-100_gradient/max_position.txt

run_folder_4:
	cp ../0-99_doc_90.0-100.0_gradient/out.csv in.csv
	make parse_input
	./main < in.txt > ../0-99_doc_90.0-100.0_gradient/max_position.txt
