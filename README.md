# 📘 Môn: Khoa học Dữ liệu

## 👥 Nhóm 2: Có nhiều like

### Thành viên:

* Nguyễn Thanh Thiệt
* Dương Lý Cử
* Hồng Phước Thịnh
* Kim Hoàng Trân

---

## 🎯 Bài toán

Xây dựng hệ thống **tóm tắt văn bản tự động** bằng thuật toán **TextRank**, giúp trích xuất các câu quan trọng nhất từ một đoạn văn bản đầu vào.

---

## 📂 Cấu trúc thư mục

* `textSummarization.py`
  ➝ Cài đặt TextRank **có sử dụng thư viện hỗ trợ**

* `textSummarizationNoLib.py`
  ➝ Cài đặt TextRank **thuần Python (không dùng thư viện ngoài)**

* `textSummarizationSpacy.py`
  ➝ Cài đặt TextRank sử dụng **SpaCy (POS tagging, preprocessing nâng cao)**

* `Nhóm Hai Có Nhiều Like.pdf`
  ➝ Slides thuyết trình **Thuật toán TextRank cho tóm tắt văn bản**

---

## ⚙️ Hướng dẫn sử dụng

### 1. Cài đặt môi trường

Cài đặt Python (khuyến nghị >= 3.8)

Cài đặt thư viện (nếu dùng bản có thư viện):

```bash
pip install spacy
python -m spacy download en_core_web_sm
```

---

### 2. Chạy chương trình

Chạy từng file tương ứng:

```bash
python textSummarization.py
```

hoặc:

```bash
python textSummarizationNoLib.py
```

hoặc:

```bash
python textSummarizationSpacy.py
```

---

## 🧠 Phương pháp sử dụng

* Tách câu từ văn bản
* Tiền xử lý (lowercase, loại bỏ stopwords, ký tự đặc biệt)
* Xây dựng **đồ thị câu (sentence graph)**
* Tính **độ tương đồng giữa các câu**
* Áp dụng thuật toán **TextRank (giống PageRank)**
* Trích xuất các câu có điểm cao nhất làm bản tóm tắt

---

## 📊 Ghi chú

* Phiên bản **không dùng thư viện** giúp hiểu rõ bản chất thuật toán
* Phiên bản **SpaCy** cải thiện chất lượng nhờ POS tagging
* Có thể mở rộng với:

  * TF-IDF
  * Word Embedding
  * BERT Summarization

---

## 📬 Liên hệ

Nếu có thắc mắc hoặc góp ý, vui lòng liên hệ các thành viên trong nhóm.

---

⭐ *Cảm ơn đã sử dụng project!*
