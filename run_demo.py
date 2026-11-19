"""
Script chạy thử nhanh AI Team từ terminal (không cần Streamlit).
Dùng để test logic trước khi mở giao diện web.
"""

import os
import sys
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.crews.main_crew import run_ai_team
from langchain_openai import ChatOpenAI


def main():
    print("=" * 60)
    print("🤖 AI TEAM – GIA ĐÌNH AI CHUYÊN BIỆT (Demo Terminal)")
    print("=" * 60)
    print()

    # Kiểm tra API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("⚠️  Chưa tìm thấy OPENAI_API_KEY trong file .env")
        print("   Hãy copy .env.example thành .env và điền key của bạn.")
        print()
        user_input = input("Hoặc dán API key vào đây để chạy thử ngay: ").strip()
        if user_input:
            os.environ["OPENAI_API_KEY"] = user_input
        else:
            print("Thoát.")
            return

    print("Nhập yêu cầu của bạn (Enter để dùng ví dụ mẫu):")
    request = input("> ").strip()

    if not request:
        request = "Viết một đoạn giới thiệu ngắn (khoảng 150 từ) về lợi ích của hệ thống Multi-Agent AI so với việc dùng một AI duy nhất."
        print(f"\n→ Dùng ví dụ mẫu: {request}")

    print("\n🚀 Team AI bắt đầu làm việc...\n")

    try:
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
        result = run_ai_team(request, llm=llm)

        print("\n" + "=" * 60)
        print("✅ ĐÁP ÁN CUỐI CÙNG TỪ REVIEWER")
        print("=" * 60)
        print(result)
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Lỗi: {e}")
        print("\nGợi ý:")
        print("- Kiểm tra API key có đúng không")
        print("- Đã cài đủ thư viện chưa: pip install -r requirements.txt")
        print("- Thử model khác nếu model hiện tại không khả dụng")


if __name__ == "__main__":
    main()
