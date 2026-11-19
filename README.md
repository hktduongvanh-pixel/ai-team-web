# 🤖 AI Team – Gia đình AI chuyên biệt

Hệ thống Multi-Agent AI hoạt động theo mô hình **Planner → Workers → Reviewer**.

## 📋 Tổng quan

Thay vì dùng một AI duy nhất, hệ thống này kết nối nhiều Agent chuyên môn:

| Agent | Vai trò |
|-------|--------|
| **Planner** | Tiếp nhận yêu cầu, phân tích, lên kế hoạch chi tiết |
| **Researcher** | Thu thập & phân tích thông tin, đề xuất công cụ |
| **Writer** | Soạn thảo nội dung chính |
| **Reviewer** | Kiểm tra lỗi, sửa chữa, tổng hợp thành **1 đáp án cuối cùng** |

## 🚀 Cách chạy (Giai đoạn 1 - Prototype)

### 1. Cài đặt

```bash
cd ai-team-web
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Cấu hình API Key

```bash
cp .env.example .env
# Sau đó mở file .env và điền API key của bạn
```

**Khuyến nghị hiện tại:**
- Dùng **DeepSeek** (free tier khá mạnh) hoặc **Gemini** / **gpt-4o-mini**

### 3. Chạy giao diện Streamlit

```bash
streamlit run frontend/streamlit_app.py
```

Mở trình duyệt tại `http://localhost:8501`

## 📁 Cấu trúc thư mục

```
ai-team-web/
├── backend/
│   ├── agents/
│   │   ├── planner.py
│   │   ├── writer.py
│   │   ├── researcher.py
│   │   └── reviewer.py
│   ├── crews/
│   │   └── main_crew.py
│   ├── knowledge/
│   │   └── free_ai_tools.md      # Danh sách AI miễn phí
│   └── tools/
├── frontend/
│   └── streamlit_app.py
├── .env.example
├── requirements.txt
└── README.md
```

## 🛣️ Lộ trình tiếp theo

- [x] **Giai đoạn 1**: Prototype với 4 Agent cốt lõi + Streamlit
- [ ] **Giai đoạn 2**: Thêm Coder, Image, Study, Media Agent
- [ ] **Giai đoạn 3**: Chuyển sang Next.js + FastAPI
- [ ] **Giai đoạn 4**: Real-time progress, memory, human-in-the-loop

## 💡 Ghi chú

- Hệ thống ưu tiên sử dụng các công cụ AI có gói miễn phí.
- Reviewer là Agent quan trọng nhất – đảm bảo chất lượng đầu ra.
- Có thể thay đổi model cho từng Agent thông qua biến môi trường.

---
**Phiên bản:** 0.1.0 (Prototype) | 2026
