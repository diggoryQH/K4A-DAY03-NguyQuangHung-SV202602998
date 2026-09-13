"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    {
        "name": "lookup_ticket",
        "description": "Tra cứu tình trạng và thông tin của ticket hỗ trợ kỹ thuật (IT Helpdesk).",
        "parameters": {
            "type": "object",
            "properties": {
                "ticket_id": {
                    "type": "string",
                    "description": "Mã ticket cần tra cứu (ví dụ: 'TK-101')"
                }
            },
            "required": ["ticket_id"]
        }
    },
    {
        "name": "create_ticket",
        "description": "Tạo một yêu cầu hỗ trợ kỹ thuật (IT Helpdesk ticket) mới.",
        "parameters": {
            "type": "object",
            "properties": {
                "employee_id": {
                    "type": "string",
                    "description": "Mã nhân viên yêu cầu hỗ trợ (ví dụ: 'NV999')"
                },
                "issue_description": {
                    "type": "string",
                    "description": "Mô tả chi tiết về sự cố hoặc yêu cầu hỗ trợ"
                },
                "priority": {
                    "type": "string",
                    "description": "Mức độ ưu tiên của yêu cầu (ví dụ: 'Thấp', 'Trung bình', 'Cao')"
                }
            },
            "required": ["employee_id", "issue_description", "priority"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "TK-101": {
        "status": "Đang xử lý",
        "priority": "Cao",
        "employee_id": "NV102",
        "description": "Không kết nối được VPN từ xa."
    },
    "TK-102": {
        "status": "Hoàn thành",
        "priority": "Trung bình",
        "employee_id": "NV999",
        "description": "Cần cài đặt phần mềm Adobe Illustrator."
    }
}


def execute_lookup_ticket(ticket_id: str) -> str:
    """Thực thi tra cứu ticket theo mã"""
    ticket = MOCK_DATABASE.get(ticket_id.strip().upper())
    if ticket:
        return json.dumps({
            "status": "SUCCESS",
            "ticket_id": ticket_id,
            "data": ticket
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu ticket có mã '{ticket_id}'"
        }, ensure_ascii=False)


def execute_create_ticket(employee_id: str, issue_description: str, priority: str = "Trung bình") -> str:
    """Thực thi tạo ticket hỗ trợ kỹ thuật"""
    import random
    new_ticket_id = f"TK-{random.randint(1000, 9999)}"
    return json.dumps({
        "status": "SUCCESS",
        "ticket_id": new_ticket_id,
        "employee_id": employee_id,
        "priority": priority,
        "description": issue_description,
        "message": f"Tạo ticket thành công với mã {new_ticket_id} cho nhân viên {employee_id}, độ ưu tiên {priority}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "lookup_ticket": execute_lookup_ticket,
    "create_ticket": execute_create_ticket
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
