# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Ngụy Quang Hưng  
> **Mã Sinh Viên / Mã Học viên:** SV202602998  
> **Chủ đề Lựa chọn:** 2.2 Trợ lý Hỗ trợ Kỹ thuật IT Helpdesk  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Tra cứu ticket trước, nếu chưa hoàn thành hoặc cần hỗ trợ thêm thì tạo ticket mới. |
| **2. Tool Interaction** | 5 / 5 | Chắc chắn cần kết nối với Hệ thống quản lý sự cố (ITSM) qua MCP Server để thao tác. |
| **3. Dynamic Decision** | 4 / 5 | Agent phải ra quyết định tạo ticket hay chỉ trả về kết quả dựa trên trạng thái tra cứu. |
| **4. Long Horizon Goal** | 3 / 5 | Tương tác tương đối ngắn gọn để giải quyết sự cố CNTT, không kéo dài quá nhiều lượt. |
| **TỔNG ĐIỂM AGENTIC FIT** | **16 / 20** | *Bài toán phù hợp triển khai Agentic System với sự hỗ trợ của MCP.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "query": "Mạng wifi tầng 3 bị chập chờn từ sáng nay, mã nhân viên của tôi là NV999, nhờ bạn tạo ticket hỗ trợ ưu tiên Cao nhé.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "create_ticket",
    "arguments": {
      "employee_id": "NV999",
      "priority": "Cao",
      "issue_description": "Mạng wifi tầng 3 bị chập chờn từ sáng nay"
    },
    "observation": {
      "status": "SUCCESS",
      "ticket_id": "TK-8935",
      "employee_id": "NV999",
      "priority": "Cao",
      "description": "Mạng wifi tầng 3 bị chập chờn từ sáng nay",
      "message": "Tạo ticket thành công với mã TK-8935 cho nhân viên NV999, độ ưu tiên Cao."
    },
    "latency_ms": 2490.79
  },
  {
    "step": 2,
    "query": "Mạng wifi tầng 3 bị chập chờn từ sáng nay, mã nhân viên của tôi là NV999, nhờ bạn tạo ticket hỗ trợ ưu tiên Cao nhé.",
    "action_type": "FINAL_ANSWER",
    "thought": "Tổng hợp kết quả từ MCP Server thành công.",
    "output": "Tạo ticket thành công với mã TK-8935 cho nhân viên NV999, độ ưu tiên Cao.",
    "latency_ms": 10.0
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [x] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
