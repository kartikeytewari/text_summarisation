# Text Summarisation
## Multi-Document Text Summarisation using Machine Learning and Natural Language Processing

Text summarisation of multi-document datasets using Natural Language Processing and statistical approaches.

## Research Paper
- Published research paper on the findings is [here](https://doi.org/10.1007/978-981-19-7867-8_52).
- To cite using bib use:
```
@InProceedings{10.1007/978-981-19-7867-8_52,
author="Tewari, Kartikey
and Yadav, Arun Kumar
and Kumar, Mohit
and Yadav, Divakar",
editor="Tistarelli, Massimo
and Dubey, Shiv Ram
and Singh, Satish Kumar
and Jiang, Xiaoyi",
title="Extractive Text Summarization Using Statistical Approach",
booktitle="Computer Vision and Machine Intelligence",
year="2023",
publisher="Springer Nature Singapore",
address="Singapore",
pages="655--667",
abstract="Nowadays, text summarization is an important research area because of its large requirements in society. The usage is increasing in different areas such as education, health care, and legal. In the past, researchers have carried a lot of work on different text summarization techniques. Also, they propose machine learning/deep learning-based approaches for text summarization. This study proposed a novel statistical approach for extractive multi-document text summarization. The proposed approach is based on weight assignment of keywords, in local files and global files. We evaluate the approach of the publicly available ``Multi-news'' dataset. Results show that the proposed approach outperforms 1.08{\%} in the ROUGE-L F1 score on the state-of-the-art method.",
isbn="978-981-19-7867-8"
}
```

# Running:
- Activate venv using: `source venv/bin/activate`
- Run the progrmmae: `./main.py <path to input file>`

# Project Dependencies:
- Python3 (Python 3.9.10)
- requirements.txt file (pip 22.0.3)
- bash/zsh shell (zsh 5.8.1)
- C++ (gcc version 11.2.0 (Homebrew GCC 11.2.0_3))

# Output files:
- local_file_weight 95.0
- local_file_weight 97.5
- local_file_weight 98.5
- local_file_weight 99.5
