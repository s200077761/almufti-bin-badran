#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
المفتي بن بدران - Almufti Bin Badran
Gradio Web Interface with Enhanced UI and Logo
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

# Custom CSS for beautiful UI
custom_css = """
/* Main container styling */
.gradio-container {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
}

/* Header styling */
.header-container {
    text-align: center;
    padding: 30px;
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e8ba3 100%);
    border-radius: 20px;
    margin-bottom: 30px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
}

.logo-image {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    border: 5px solid #ffd700;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    margin: 0 auto 20px;
    display: block;
}

.title-text {
    font-size: 3em;
    font-weight: bold;
    color: white;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    margin: 15px 0;
}

.subtitle-text {
    font-size: 1.3em;
    color: #ffd700;
    margin: 10px 0;
}

/* Button styling */
.primary-button {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%) !important;
    border: none !important;
    border-radius: 12px !important;
    color: white !important;
    font-weight: bold !important;
    padding: 14px 28px !important;
    font-size: 1.1em !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(30, 60, 114, 0.3) !important;
}

.primary-button:hover {
    transform: translateY(-3px) !important;
    box-shadow: 0 6px 20px rgba(30, 60, 114, 0.5) !important;
}

/* Tab styling */
.tab-nav {
    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%) !important;
    border-radius: 12px !important;
    padding: 8px !important;
}

/* Input styling */
.input-box {
    border: 2px solid #2a5298 !important;
    border-radius: 10px !important;
    padding: 12px !important;
}

/* Footer styling */
.footer-container {
    text-align: center;
    padding: 25px;
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    border-radius: 20px;
    margin-top: 30px;
    color: white;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
}

.footer-container a {
    color: #ffd700;
    text-decoration: none;
    font-weight: bold;
}

.footer-container a:hover {
    text-decoration: underline;
}
"""


def chat_response(message, language):
    """توليد رد على رسالة المستخدم"""
    try:
        if not message.strip():
            return "يرجى إدخال رسالة" if language == "ar" else "Please enter a message"
        
        response = chat_engine.generate_response(message)
        return response
    except Exception as e:
        return f"خطأ: {str(e)}" if language == "ar" else f"Error: {str(e)}"


def search_web(query, language):
    """البحث على الإنترنت"""
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
    """حل مسألة رياضية"""
    try:
        if not problem.strip():
            return "يرجى إدخال مسألة رياضية" if language == "ar" else "Please enter a math problem"
        
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
    """تحليل النص"""
    try:
        if not text.strip():
            return "يرجى إدخال نص" if language == "ar" else "Please enter text"
        
        detected_lang = language_processor.detect_language(text)
        keywords = language_processor.extract_keywords(text, detected_lang, top_n=10)
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


# إنشاء واجهة Gradio المحسّنة
with gr.Blocks(title="المفتي بن بدران - Almufti Bin Badran") as demo:
    
    # Add custom CSS
    gr.HTML(f"<style>{custom_css}</style>")
    
    # Header with Logo
    gr.HTML("""
        <div class="header-container">
            <img src="file/assets/logo.png" class="logo-image" alt="Almufti Logo">
            <h1 class="title-text">🤖 المفتي بن بدران</h1>
            <h2 class="title-text">Almufti Bin Badran AI Assistant</h2>
            <p class="subtitle-text">مساعد ذكاء اصطناعي خفيف الوزن مع دعم كامل للغة العربية</p>
            <p class="subtitle-text">A Lightweight AI Assistant with Full Arabic Language Support</p>
        </div>
    """)
    
    with gr.Tabs():
        # تبويب المحادثة
        with gr.Tab("💬 المحادثة / Chat"):
            gr.Markdown("""
            ### 🎯 كيفية الاستخدام | How to Use
            اكتب رسالتك واضغط إرسال، وسيرد عليك المفتي بن بدران بذكاء!
            
            Type your message and press Send, Almufti will respond intelligently!
            """)
            
            with gr.Row():
                language_chat = gr.Radio(
                    choices=["العربية (Arabic)", "English"],
                    value="العربية (Arabic)",
                    label="🌐 اختر اللغة / Choose Language"
                )
            
            message_input = gr.Textbox(
                label="✉️ رسالتك / Your Message",
                placeholder="اكتب رسالتك هنا... مثال: ما هو الذكاء الاصطناعي؟",
                lines=3
            )
            
            chat_button = gr.Button("📤 إرسال / Send", variant="primary", size="lg")
            
            chat_output = gr.Textbox(
                label="💬 رد المساعد / Assistant Response",
                lines=6,
                interactive=False
            )
            
            gr.Examples(
                examples=[
                    ["السلام عليكم، كيف حالك؟"],
                    ["ما هو الذكاء الاصطناعي؟"],
                    ["أخبرني عن أحدث أخبار التكنولوجيا"],
                    ["Hello, how are you?"],
                    ["What is machine learning?"],
                ],
                inputs=message_input,
                label="📝 أمثلة / Examples"
            )
            
            chat_button.click(
                fn=lambda msg, lang: chat_response(msg, "ar" if "Arabic" in lang else "en"),
                inputs=[message_input, language_chat],
                outputs=chat_output
            )
        
        # تبويب البحث
        with gr.Tab("🔍 البحث / Search"):
            gr.Markdown("""
            ### 🔍 البحث الذكي | Intelligent Search
            ابحث عن أي موضوع وسيقوم المفتي بتلخيص النتائج لك!
            
            Search for any topic and Almufti will summarize the results!
            """)
            
            with gr.Row():
                language_search = gr.Radio(
                    choices=["العربية (Arabic)", "English"],
                    value="العربية (Arabic)",
                    label="🌐 اختر اللغة / Choose Language"
                )
            
            search_input = gr.Textbox(
                label="🔎 استعلام البحث / Search Query",
                placeholder="ابحث عن... مثال: أحدث أخبار الذكاء الاصطناعي",
                lines=2
            )
            
            search_button = gr.Button("🔍 بحث / Search", variant="primary", size="lg")
            
            search_output = gr.Textbox(
                label="📊 نتائج البحث / Search Results",
                lines=10,
                interactive=False
            )
            
            gr.Examples(
                examples=[
                    ["أحدث أخبار الذكاء الاصطناعي"],
                    ["كيفية تعلم البرمجة"],
                    ["Latest AI developments"],
                ],
                inputs=search_input,
                label="📝 أمثلة / Examples"
            )
            
            search_button.click(
                fn=lambda query, lang: search_web(query, "ar" if "Arabic" in lang else "en"),
                inputs=[search_input, language_search],
                outputs=search_output
            )
        
        # تبويب حل المسائل الرياضية
        with gr.Tab("🧮 الرياضيات / Math"):
            gr.Markdown("""
            ### 🧮 حل المسائل الرياضية | Math Problem Solver
            أدخل المعادلة وسيقوم المفتي بحلها وشرح الخطوات!
            
            Enter the equation and Almufti will solve it with steps!
            """)
            
            with gr.Row():
                language_math = gr.Radio(
                    choices=["العربية (Arabic)", "English"],
                    value="العربية (Arabic)",
                    label="🌐 اختر اللغة / Choose Language"
                )
            
            math_input = gr.Textbox(
                label="➗ المسألة الرياضية / Math Problem",
                placeholder="مثال: 2x + 5 = 15",
                lines=2
            )
            
            math_button = gr.Button("✅ حل / Solve", variant="primary", size="lg")
            
            math_output = gr.Textbox(
                label="📐 الحل / Solution",
                lines=10,
                interactive=False
            )
            
            gr.Examples(
                examples=[
                    ["2x + 5 = 15"],
                    ["3x - 7 = 20"],
                    ["5x + 10 = 35"],
                ],
                inputs=math_input,
                label="📝 أمثلة / Examples"
            )
            
            math_button.click(
                fn=lambda problem, lang: solve_math(problem, "ar" if "Arabic" in lang else "en"),
                inputs=[math_input, language_math],
                outputs=math_output
            )
        
        # تبويب تحليل النص
        with gr.Tab("📝 تحليل النص / Text Analysis"):
            gr.Markdown("""
            ### 📝 تحليل النصوص | Text Analysis
            قم بتحليل أي نص واستخراج الكلمات المفتاحية والإحصائيات!
            
            Analyze any text and extract keywords and statistics!
            """)
            
            with gr.Row():
                language_analysis = gr.Radio(
                    choices=["العربية (Arabic)", "English"],
                    value="العربية (Arabic)",
                    label="🌐 اختر اللغة / Choose Language"
                )
            
            text_input = gr.Textbox(
                label="📄 النص / Text",
                placeholder="أدخل النص المراد تحليله...",
                lines=6
            )
            
            analyze_button = gr.Button("🔬 تحليل / Analyze", variant="primary", size="lg")
            
            analysis_output = gr.Textbox(
                label="📊 التحليل / Analysis",
                lines=12,
                interactive=False
            )
            
            analyze_button.click(
                fn=lambda text, lang: analyze_text(text, "ar" if "Arabic" in lang else "en"),
                inputs=[text_input, language_analysis],
                outputs=analysis_output
            )
        
        # تبويب معلومات
        with gr.Tab("ℹ️ عن المشروع / About"):
            gr.Markdown("""
            # 🤖 المفتي بن بدران - Almufti Bin Badran
            
            ## ✨ المميزات | Features
            
            - 💬 **محادثة ذكية** - Smart conversation with context understanding
            - 🔍 **بحث ذكي** - Intelligent web search with summarization
            - 🧮 **حل المسائل** - Mathematical problem solver with steps
            - 📝 **تحليل النصوص** - Text analysis and NLP processing
            - 🧠 **التعلم المستمر** - Continuous learning from interactions
            - 💾 **قاعدة بيانات مفتوحة** - Open-source SQLite database
            - ⚡ **خفيف الوزن** - Lightweight and fast performance
            - 🌐 **دعم متعدد اللغات** - Arabic and English support
            
            ## 📚 الوثائق | Documentation
            
            - **GitHub:** [github.com/s200077761/almufti-bin-badran](https://github.com/s200077761/almufti-bin-badran)
            - **PyPI:** [pypi.org/project/almufti-bin-badran](https://pypi.org/project/almufti-bin-badran)
            - **Hugging Face:** [huggingface.co/spaces/s200077761/almufti-bin-badran](https://huggingface.co/spaces/s200077761/almufti-bin-badran)
            - **البريد | Email:** dev@almufti.ai
            
            ## 📄 الترخيص | License
            
            MIT License - مفتوح المصدر | Open Source
            
            ## 🎯 الاستخدام | Usage
            
            ```bash
            # التثبيت | Installation
            pip install almufti-bin-badran
            
            # الاستخدام | Usage
            from almufti import ChatEngine
            chat = ChatEngine()
            response = chat.chat("السلام عليكم")
            ```
            
            ---
            
            **الإصدار | Version:** 1.0.0  
            **التاريخ | Date:** 2024-12-04  
            **الحالة | Status:** ✅ Production Ready
            """)
    
    # Footer
    gr.HTML("""
        <div class="footer-container">
            <p style="font-size: 1.3em; margin-bottom: 15px;">
                <strong>Made with ❤️ for the Arabic AI Community</strong>
            </p>
            <p style="font-size: 1.1em; margin: 10px 0;">
                © 2024 Almufti Bin Badran - All Rights Reserved
            </p>
            <p style="font-size: 1.1em; margin-top: 15px;">
                <a href="https://github.com/s200077761/almufti-bin-badran" target="_blank">🐙 GitHub</a> | 
                <a href="https://pypi.org/project/almufti-bin-badran/" target="_blank">📦 PyPI</a> | 
                <a href="https://huggingface.co/spaces/s200077761/almufti-bin-badran" target="_blank">🤗 Hugging Face</a> | 
                <a href="mailto:dev@almufti.ai">✉️ Contact</a>
            </p>
            <p style="margin-top: 15px; font-size: 1.2em;">
                <strong>شكراً لاستخدامك المفتي بن بدران! 🙏</strong>
            </p>
        </div>
    """)


if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        show_error=True
    )
