import re
import math
import spacy
nlp = spacy.load("en_core_web_sm")

d = 0.85  # Hệ số 

example_text = """Deep learning (also known as deep structured learning) is part of a 
broader family of machine learning methods based on artificial neural networks with 
representation learning. Learning can be supervised, semi-supervised or unsupervised. 
Deep-learning architectures such as deep neural networks, deep belief networks, deep reinforcement learning, 
recurrent neural networks and convolutional neural networks have been applied to
fields including computer vision, speech recognition, natural language processing, 
machine translation, bioinformatics, drug design, medical image analysis, material
inspection and board game programs, where they have produced results comparable to 
and in some cases surpassing human expert performance. Artificial neural networks
(ANNs) were inspired by information processing and distributed communication nodes
in biological systems. ANNs have various differences from biological brains. Specifically, 
neural networks tend to be static and symbolic, while the biological brain of most living organisms
is dynamic (plastic) and analogue. The adjective "deep" in deep learning refers to the use of multiple
layers in the network. Early work showed that a linear perceptron cannot be a universal classifier, 
but that a network with a nonpolynomial activation function with one hidden layer of unbounded width can.
Deep learning is a modern variation which is concerned with an unbounded number of layers of bounded size, 
which permits practical application and optimized implementation, while retaining theoretical universality 
under mild conditions. In deep learning the layers are also permitted to be heterogeneous and to deviate widely 
from biologically informed connectionist models, for the sake of efficiency, trainability and understandability, 
whence the structured part."""

# B1: tách văn bản thành các câu
raw_sentences = [s.strip() for s in example_text.split('.') if s.strip()]
# in kết quả
print("B1: Các câu trong văn bản đã tách:")
for i, s in enumerate(raw_sentences):
    print(f"Sentence {i+1}: {s}")

# B2: loại bỏ các từ trùng lặp trong mỗi câu, tạo object cho mỗi câu
sentences = []
for s in raw_sentences:
    doc = nlp(s)  # xử lý câu bằng spaCy để loại bỏ stopwords và chuẩn hóa
    filtered = [token.text for token in doc if token.pos_ in ["NOUN", "VERB"]]  # chỉ giữ lại danh từ và động từ

    sentences.append({
        'sentence': s,
        'words': filtered,
        'score': 1.0,
        'out_sum': 0.0
    })
# in kết quả
print("\nB2: Loại bỏ các từ trùng lặp trong mỗi câu:")
for i, obj in enumerate(sentences):
    print(f"Sentence {i+1}:  {set(obj['words'])})")

# B3: tạo ma trận tần suất từ chung cho mỗi câu
edges = []
for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        common_words = set(sentences[i]['words']) & set(sentences[j]['words'])
        denom = math.log(len(sentences[i]['words'])) + math.log(len(sentences[j]['words']))
        similarity = len(common_words) / denom if denom > 0 else 0
        edges.append({'i': i, 'j': j, 'similarity': similarity})
# In kết quả
print("\nB3: Ma trận tương đồng giữa các câu:")
for edge in edges:
    print(f"Sentence {edge['i']+1} - Sentence {edge['j']+1}: similarity = {edge['similarity']}")

# # B4: Xếp hạng lặp (giả lập đơn giản)
# B4.1: Tổng điểm của mỗi câu dựa trên các cạnh kết nối với nó
for i, obj in enumerate(sentences):
    out_sum = 0
    for edge in edges:
        if edge['i'] == i or edge['j'] == i:
            out_sum += (edge['similarity'])
    sentences[i]['out_sum'] = out_sum
# in kết quả
print("\nB4.1: Tổng điểm của mỗi câu:")
for i, obj in enumerate(sentences):
    print(f"Sentence {i+1} (out_sum={obj['out_sum']})")

# B4.2: Cập nhật điểm của mỗi câu dựa trên điểm của các câu kết nối với nó
for _ in range(30):  # lặp 30 lần
    new_scores = []
    for i, obj in enumerate(sentences):
        total = 0
        for edge in edges:
            if (edge['i'] == i or edge['j'] == i) and edge['similarity'] > 0:
                sentenceOther = sentences[edge['j'] if edge['i'] == i else edge['i']]
                if sentenceOther['out_sum'] != 0:
                    total += (edge['similarity'] * sentenceOther['score']) / sentenceOther['out_sum']
        new_scores.append((1 - d) + d * total)
    # Cập nhật điểm mới cho mỗi câu
    for i in range(len(sentences)):
        sentences[i]['score'] = new_scores[i]

# In kết quả
print("\nB4.2: Điểm của mỗi câu sau khi cập nhật:")
for i, obj in enumerate(sentences):
    print(f"Sentence {i+1} (score={obj['score']})")

# B5: sắp xếp các câu theo điểm và chọn ra 3 câu có điểm cao nhất
sentences.sort(key=lambda x: x['score'], reverse=True)
summary = sentences[:3]  # chọn 3 câu có điểm cao nhất
print("\nTóm tắt:")
for i, obj in enumerate(summary):
    print(f"Sentence {i+1}: {obj['sentence']} (score={obj['score']})")
