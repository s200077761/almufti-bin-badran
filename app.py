"""
Gradio App for Almufti Bin Badran
تطبيق Gradio للمفتي بن بدران
"""

import gradio as gr
import sys
from pathlib import Path

# إضافة المسار
sys.path.insert(0, str(Path(__file__).parent))

from almufti.core.chat_engine import ChatEngine
from almufti.core.language_processor import LanguageProcessor
from almufti.search.web_search import WebSearch
from almufti.homework.math_solver import MathSolver
from almufti.database.db_manager import DatabaseManager

# تهيئة المكونات
db = DatabaseManager()
chat_engine = ChatEngine(db, language="ar")
language_processor = LanguageProcessor()
web_search = WebSearch()
math_solver = MathSolver()

# بدء محادثة جديدة
chat_engine.start_conversation("Gradio Chat Session")


def chat_response(message, language):
    """
    توليد رد على رسالة المستخدم
    
    Args:
        message: رسالة المستخدم
        language: اللغة
        
    Returns:
        رد المساعد
    """
    try:
        if not message.strip():
            return "يرجى إدخال رسالة" if language == "ar" else "Please enter a message"
        
        response = chat_engine.generate_response(message)
        return response
    except Exception as e:
        return f"خطأ: {str(e)}" if language == "ar" else f"Error: {str(e)}"


def search_web(query, language):
    """
    البحث على الإنترنت
    
    Args:
        query: استعلام البحث
        language: اللغة
        
    Returns:
        نتائج البحث
    """
    try:
        if not query.strip():
            return "يرجى إدخال استعلام بحث" if language == "ar" else "Please enter a search query"
        
        result = web_search.search_and_summarize(query, language)
        
        output = result.get('summary', '')
        output += "\n\n" + ("النتائج الكاملة:" if language == "ar" else "Full Results:") + "\n"
        
        for i, res in enumerate(result.get('results', [])[:5], 1):
            output += f"\n{i}. {res['title']}\n"
            output += f"   {res['snippet'][:200]}...\n"
            output += f"   {res['url']}\n"
        
        return output
    except Exception as e:
        return f"خطأ في البحث: {str(e)}" if language == "ar" else f"Search error: {str(e)}"


def solve_math(problem, language):
    """
    حل مسألة رياضية
    
    Args:
        problem: المسألة الرياضية
        language: اللغة
        
    Returns:
        الحل والخطوات
    """
    try:
        if not problem.strip():
            return "يرجى إدخال مسألة رياضية" if language == "ar" else "Please enter a math problem"
        
        # محاولة حل معادلة خطية
        result = math_solver.solve_linear_equation(problem)
        
        if 'error' not in result:
            output = f"{'الحل:' if language == 'ar' else 'Solution:'} x = {result['solution']}\n\n"
            output += f"{'الخطوات:' if language == 'ar' else 'Steps:'}\n"
            for step in result['steps']:
                output += f"• {step}\n"
            output += f"\n{'التحقق:' if language == 'ar' else 'Verification:'} {result['verification']}"
            return output
        else:
            return result['error']
    except Exception as e:
        return f"خطأ: {str(e)}" if language == "ar" else f"Error: {str(e)}"


def analyze_text(text, language):
    """
    تحليل النص
    
    Args:
        text: النص المراد تحليله
        language: اللغة
        
    Returns:
        تحليل النص
    """
    try:
        if not text.strip():
            return "يرجى إدخال نص" if language == "ar" else "Please enter text"
        
        # كشف اللغة
        detected_lang = language_processor.detect_language(text)
        
        # استخراج الكلمات المفتاحية
        keywords = language_processor.extract_keywords(text, detected_lang, top_n=10)
        
        # إحصائيات النص
        stats = language_processor.get_text_statistics(text, detected_lang)
        
        output = f"{'اللغة المكتشفة:' if language == 'ar' else 'Detected Language:'} {detected_lang}\n\n"
        
        output += f"{'الكلمات المفتاحية:' if language == 'ar' else 'Keywords:'}\n"
        for keyword, score in keywords:
            output += f"• {keyword}: {score:.2f}\n"
        
        output += f"\n{'إحصائيات النص:' if language == 'ar' else 'Text Statistics:'}\n"
        output += f"{'عدد الأحرف:' if language == 'ar' else 'Characters:'} {stats['character_count']}\n"
        output += f"{'عدد الكلمات:' if language == 'ar' else 'Words:'} {stats['word_count']}\n"
        output += f"{'عدد الجمل:' if language == 'ar' else 'Sentences:'} {stats['sentence_count']}\n"
        output += f"{'متوسط طول الكلمة:' if language == 'ar' else 'Avg Word Length:'} {stats['avg_word_length']:.2f}\n"
        output += f"{'غنى المفردات:' if language == 'ar' else 'Vocabulary Richness:'} {stats['vocabulary_richness']:.2f}\n"
        
        return output
    except Exception as e:
        return f"خطأ: {str(e)}" if language == "ar" else f"Error: {str(e)}"


# إنشاء واجهة Gradio
with gr.Blocks(title="المفتي بن بدران - Almufti Bin Badran") as demo:
    gr.Markdown("""
    # 🤖 المفتي بن بدران
    # Almufti Bin Badran - AI Assistant with Arabic Support
    
    تطبيق ذكاء اصطناعي خفيف الوزن مع دعم اللغة العربية والإنجليزية
    
    A lightweight AI assistant with Arabic and English language support
    """)
    
    with gr.Tabs():
        # تبويب المحادثة
        with gr.Tab("💬 المحادثة / Chat"):
            with gr.Row():
                language_chat = gr.Radio(
                    choices=["العربية (Arabic)", "English"],
                    value="العربية (Arabic)",
                    label="اختر اللغة / Choose Language"
                )
            
            message_input = gr.Textbox(
                label="رسالتك / Your Message",
                placeholder="اكتب رسالتك هنا / Type your message here...",
                lines=3
            )
            
            chat_button = gr.Button("إرسال / Send", variant="primary")
            chat_output = gr.Textbox(
                label="رد المساعد / Assistant Response",
                lines=5,
                interactive=False
            )
            
            chat_button.click(
                fn=lambda msg, lang: chat_response(msg, "ar" if "Arabic" in lang else "en"),
                inputs=[message_input, language_chat],
                outputs=chat_output
            )
        
        # تبويب البحث
        with gr.Tab("🔍 البحث / Search"):
            with gr.Row():
                language_search = gr.Radio(
                    choices=["العربية (Arabic)", "English"],
                    value="العربية (Arabic)",
                    label="اختر اللغة / Choose Language"
                )
            
            search_input = gr.Textbox(
                label="استعلام البحث / Search Query",
                placeholder="ابحث عن موضوع / Search for a topic...",
                lines=2
            )
            
            search_button = gr.Button("بحث / Search", variant="primary")
            search_output = gr.Textbox(
                label="نتائج البحث / Search Results",
                lines=8,
                interactive=False
            )
            
            search_button.click(
                fn=lambda query, lang: search_web(query, "ar" if "Arabic" in lang else "en"),
                inputs=[search_input, language_search],
                outputs=search_output
            )
        
        # تبويب حل المسائل الرياضية
        with gr.Tab("🧮 الرياضيات / Math"):
            with gr.Row():
                language_math = gr.Radio(
                    choices=["العربية (Arabic)", "English"],
                    value="العربية (Arabic)",
                    label="اختر اللغة / Choose Language"
                )
            
            math_input = gr.Textbox(
                label="المسألة الرياضية / Math Problem",
                placeholder="مثال: 2x + 5 = 15 / Example: 2x + 5 = 15",
                lines=2
            )
            
            math_button = gr.Button("حل / Solve", variant="primary")
            math_output = gr.Textbox(
                label="الحل / Solution",
                lines=8,
                interactive=False
            )
            
            math_button.click(
                fn=lambda problem, lang: solve_math(problem, "ar" if "Arabic" in lang else "en"),
                inputs=[math_input, language_math],
                outputs=math_output
            )
        
        # تبويب تحليل النص
        with gr.Tab("📝 تحليل النص / Text Analysis"):
            with gr.Row():
                language_analysis = gr.Radio(
                    choices=["العربية (Arabic)", "English"],
                    value="العربية (Arabic)",
                    label="اختر اللغة / Choose Language"
                )
            
            text_input = gr.Textbox(
                label="النص / Text",
                placeholder="أدخل النص المراد تحليله / Enter text to analyze...",
                lines=5
            )
            
            analyze_button = gr.Button("تحليل / Analyze", variant="primary")
            analysis_output = gr.Textbox(
                label="التحليل / Analysis",
                lines=10,
                interactive=False
            )
            
            analyze_button.click(
                fn=lambda text, lang: analyze_text(text, "ar" if "Arabic" in lang else "en"),
                inputs=[text_input, language_analysis],
                outputs=analysis_output
            )
    
    gr.Markdown("""
    ---
    
    ### 📚 معلومات إضافية / Additional Information
    
    **المميزات / Features:**
    - 💬 محادثة ذكية / Smart Chat
    - 🔍 بحث على الإنترنت / Web Search
    - 🧮 حل مسائل رياضية / Math Solver
    - 📝 تحليل النصوص / Text Analysis
    - 🌍 دعم اللغة العربية والإنجليزية / Arabic & English Support
    
    **الروابط المهمة / Important Links:**
    - [GitHub Repository](https://github.com/yourusername/almufti-bin-badran)
    - [Documentation](https://github.com/yourusername/almufti-bin-badran/blob/master/README.md)
    - [License](https://github.com/yourusername/almufti-bin-badran/blob/master/LICENSE)
    
    ---
    
    **شكراً لاستخدامك المفتي بن بدران! 🙏**
    """)


if __name__ == "__main__":
    demo.launch()
