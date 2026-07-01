import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

# 필요한 데이터셋 다운로드
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

text = "Natural Language Toolkit is powerful."

# 1. 토큰화 (단어 분리)
tokens = word_tokenize(text)
print(tokens)  # 결과: ['Natural', 'Language', 'Toolkit', 'is', 'powerful', '.']

# 2. 품사 태깅
tagged = pos_tag(tokens)
print(tagged)
# 주요 품사 태그:
# NN  - 명사 (Noun)            예: Natural, Language, Toolkit
# VBZ - 동사 3인칭 단수 현재형     예: is
# JJ  - 형용사 (Adjective)      예: powerful
# .   - 구두점 (Punctuation)

