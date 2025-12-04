"""
أمثلة الاستخدام الأساسية
Basic Usage Examples for Almufti Bin Badran
"""

import sys
from pathlib import Path

# إضافة المسار
sys.path.insert(0, str(Path(__file__).parent.parent))

from almufti.core.chat_engine import ChatEngine
from almufti.core.language_processor import LanguageProcessor
from almufti.search.web_search import WebSearch
from almufti.homework.math_solver import MathSolver
from almufti.database.db_manager import DatabaseManager
from almufti.learning.continuous_learning import ContinuousLearning


def example_language_processing():
    """مثال على معالجة اللغة"""
    print("\n" + "="*50)
    print("مثال 1: معالجة اللغة")
    print("="*50 + "\n")

    processor = LanguageProcessor()

    # كشف اللغة
    text = "السلام عليكم ورحمة الله وبركاته"
    language = processor.detect_language(text)
    print(f"النص: {text}")
    print(f"اللغة المكتشفة: {language}\n")

    # استخراج الكلمات المفتاحية
    text = "الذكاء الاصطناعي والتعلم الآلي والشبكات العصبية والبيانات الضخمة"
    keywords = processor.extract_keywords(text, 'ar', top_n=5)
    print(f"النص: {text}")
    print(f"الكلمات المفتاحية:")
    for keyword, score in keywords:
        print(f"  • {keyword}: {score:.2f}")

    # إحصائيات النص
    print("\nإحصائيات النص:")
    stats = processor.get_text_statistics(text, 'ar')
    for key, value in stats.items():
        print(f"  • {key}: {value}")


def example_chat_engine():
    """مثال على محرك المحادثة"""
    print("\n" + "="*50)
    print("مثال 2: محرك المحادثة")
    print("="*50 + "\n")

    db = DatabaseManager("data/example.db")
    chat = ChatEngine(db, language="ar")

    # بدء محادثة
    conv_id = chat.start_conversation("محادثة تجريبية")
    print(f"تم بدء محادثة جديدة: {conv_id}\n")

    # إضافة رسائل
    messages = [
        "السلام عليكم، كيف حالك؟",
        "ما هو الذكاء الاصطناعي؟",
        "كيف يمكنني تعلم البرمجة؟"
    ]

    for msg in messages:
        chat.add_user_message(msg)
        response = chat.generate_response(msg)
        print(f"المستخدم: {msg}")
        print(f"المساعد: {response}\n")

    # الحصول على السياق
    context = chat.get_context()
    print(f"عدد الرسائل في السياق: {len(context)}\n")

    db.close()


def example_web_search():
    """مثال على البحث على الإنترنت"""
    print("\n" + "="*50)
    print("مثال 3: البحث على الإنترنت")
    print("="*50 + "\n")

    search = WebSearch(max_results=5)

    # البحث البسيط
    query = "الذكاء الاصطناعي"
    print(f"البحث عن: {query}\n")

    results = search.search(query, language="ar")
    print(f"وجدنا {len(results)} نتائج:\n")

    for i, result in enumerate(results[:3], 1):
        print(f"{i}. {result['title']}")
        print(f"   {result['snippet'][:150]}...")
        print(f"   المصدر: {result['url']}\n")


def example_math_solver():
    """مثال على حل المسائل الرياضية"""
    print("\n" + "="*50)
    print("مثال 4: حل المسائل الرياضية")
    print("="*50 + "\n")

    solver = MathSolver()

    # حل معادلة خطية
    print("1. حل معادلة خطية:")
    equation = "2x + 5 = 15"
    result = solver.solve_linear_equation(equation)
    if 'error' not in result:
        print(f"المعادلة: {equation}")
        print(f"الحل: x = {result['solution']}\n")

    # حل معادلة تربيعية
    print("2. حل معادلة تربيعية:")
    result = solver.solve_quadratic_equation(1, -5, 6)
    print(f"المعادلة: x² - 5x + 6 = 0")
    print(f"الحلول: {result['solutions']}\n")

    # حساب النسبة المئوية
    print("3. حساب النسبة المئوية:")
    result = solver.calculate_percentage(25, 100)
    print(f"النسبة المئوية: {result['percentage']}%\n")

    # حل مسألة هندسية
    print("4. حل مسألة هندسية (مستطيل):")
    result = solver.solve_geometry_problem('rectangle', length=5, width=3)
    print(f"المساحة: {result['area']}")
    print(f"المحيط: {result['perimeter']}\n")


def example_continuous_learning():
    """مثال على التعلم المستمر"""
    print("\n" + "="*50)
    print("مثال 5: التعلم المستمر")
    print("="*50 + "\n")

    db = DatabaseManager("data/example_learning.db")
    learning = ContinuousLearning(db)

    # تسجيل تفاعل
    interaction_data = {
        "query": "ما هو الذكاء الاصطناعي؟",
        "response": "الذكاء الاصطناعي هو محاكاة الذكاء البشري...",
        "user_rating": 5
    }

    learning.record_interaction("chat", interaction_data, success=True, rating=0.9)
    print("تم تسجيل التفاعل\n")

    # تحليل الملاحظات
    feedback = "إجابة ممتازة وشاملة جداً"
    analysis = learning.analyze_feedback(feedback, rating=5)
    print(f"تحليل الملاحظات:")
    print(f"  • المشاعر: {analysis['sentiment']}")
    print(f"  • مجالات التحسن: {analysis['improvement_areas']}\n")

    # الحصول على تقرير الأداء
    report = learning.get_performance_report()
    print(f"تقرير الأداء:")
    print(f"  • متوسط التقييم: {report.get('average_rating', 0):.2f}")
    print(f"  • اتجاه التحسن: {report.get('improvement_trend', 'غير معروف')}")
    print(f"  • نقاط القوة: {', '.join(report.get('strengths', []))}\n")

    db.close()


def example_database_operations():
    """مثال على عمليات قاعدة البيانات"""
    print("\n" + "="*50)
    print("مثال 6: عمليات قاعدة البيانات")
    print("="*50 + "\n")

    db = DatabaseManager("data/example_db.db")

    # حفظ محادثة
    conv_id = db.save_conversation("محادثة تجريبية", "ar")
    print(f"تم حفظ محادثة: {conv_id}\n")

    # إضافة رسائل
    msg_id1 = db.add_message(conv_id, "user", "السلام عليكم")
    msg_id2 = db.add_message(conv_id, "assistant", "وعليكم السلام ورحمة الله")
    print(f"تم إضافة رسائل: {msg_id1}, {msg_id2}\n")

    # إضافة معرفة
    knowledge_id = db.add_knowledge(
        "الرياضيات",
        "الرياضيات هي دراسة الأرقام والأشكال والعلاقات",
        "wikipedia",
        0.95,
        "ar"
    )
    print(f"تم إضافة معرفة: {knowledge_id}\n")

    # البحث في قاعدة المعرفة
    results = db.search_knowledge("الرياضيات")
    print(f"نتائج البحث: {len(results)} نتيجة")
    for result in results:
        print(f"  • {result['topic']}: {result['content'][:100]}...\n")

    # الحصول على محادثة كاملة
    conversation = db.get_conversation(conv_id)
    print(f"المحادثة الكاملة:")
    print(f"  • العنوان: {conversation['conversation']['title']}")
    print(f"  • عدد الرسائل: {len(conversation['messages'])}\n")

    db.close()


if __name__ == "__main__":
    print("\n" + "="*50)
    print("أمثلة الاستخدام - Almufti Bin Badran")
    print("="*50)

    try:
        example_language_processing()
        example_chat_engine()
        example_web_search()
        example_math_solver()
        example_continuous_learning()
        example_database_operations()

        print("\n" + "="*50)
        print("تم إكمال جميع الأمثلة بنجاح!")
        print("="*50 + "\n")

    except Exception as e:
        print(f"\nحدث خطأ: {e}")
        import traceback
        traceback.print_exc()
