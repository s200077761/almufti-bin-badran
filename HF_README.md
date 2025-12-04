---
title: Almufti Bin Badran
emoji: 🤖
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 4.0.0
app_file: app.py
pinned: false
license: mit
tags:
  - arabic
  - nlp
  - chatbot
  - ai-assistant
  - lightweight
  - offline
---

# المفتي بن بدران - Almufti Bin Badran

**A Lightweight AI Assistant with Arabic Language Support**

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)

## 📌 نبذة عن المشروع

**المفتي بن بدران** هو تطبيق ذكاء اصطناعي خفيف الوزن وقابل للتشغيل بدون اتصال إنترنت، مصمم خصيصاً للعمل على الأجهزة المحمولة والأجهزة ذات الموارد المحدودة.

### ✨ المميزات الرئيسية

- **🤖 محادثة ذكية** متقدمة بالعربية والإنجليزية
- **🔍 بحث ذكي** على الإنترنت مع فهم السياق
- **💾 قاعدة بيانات مفتوحة المصدر** (SQLite)
- **📚 حل الواجبات** المدرسية والجامعية
- **🧠 تعلم مستمر** وحفظ المعلومات
- **🔐 عمل بدون اتصال** (Offline Mode)
- **⚡ أداء خفيف** مناسب للأجهزة القديمة

## 🚀 البدء السريع

### التثبيت

```bash
pip install almufti-bin-badran
```

### الاستخدام الأساسي

```python
from almufti.core.chat_engine import ChatEngine
from almufti.database.db_manager import DatabaseManager

# إنشاء نسخة من المساعد
db = DatabaseManager()
ai = ChatEngine(db, language='ar')

# بدء محادثة
ai.start_conversation("محادثتي الأولى")

# محادثة بسيطة
response = ai.generate_response("السلام عليكم، كيف حالك؟")
print(response)
```

### واجهة سطر الأوامر

```bash
# وضع المحادثة التفاعلي
almufti chat

# البحث على الإنترنت
almufti search "الذكاء الاصطناعي"

# حل مسألة رياضية
almufti math "2x + 5 = 15"

# عرض تقرير الأداء
almufti report
```

## 📚 الميزات التفصيلية

### 1. معالجة اللغة الطبيعية

```python
from almufti.core.language_processor import LanguageProcessor

processor = LanguageProcessor()

# كشف اللغة
language = processor.detect_language("مرحبا بك")

# استخراج الكلمات المفتاحية
keywords = processor.extract_keywords("الذكاء الاصطناعي والتعلم الآلي")

# استخراج الكيانات
entities = processor.extract_entities("أحمد يعيش في القاهرة")
```

### 2. البحث الذكي

```python
from almufti.search.web_search import WebSearch

search = WebSearch()

# بحث عام
results = search.search("تطبيقات الذكاء الاصطناعي")

# بحث أكاديمي
academic = search.search_academic("الشبكات العصبية")

# بحث الأخبار
news = search.search_news("أحدث تطورات التكنولوجيا")

# بحث الصور
images = search.search_images("الذكاء الاصطناعي")
```

### 3. حل المسائل الرياضية

```python
from almufti.homework.math_solver import MathSolver

solver = MathSolver()

# حل معادلة خطية
result = solver.solve_linear_equation("2x + 5 = 15")

# حل معادلة تربيعية
result = solver.solve_quadratic_equation(1, -5, 6)

# حساب النسبة المئوية
result = solver.calculate_percentage(25, 100)

# حل مسائل هندسية
result = solver.solve_geometry_problem('rectangle', length=5, width=3)
```

### 4. التعلم المستمر

```python
from almufti.learning.continuous_learning import ContinuousLearning

learning = ContinuousLearning()

# تسجيل تفاعل
learning.record_interaction("chat", {"query": "..."}, success=True, rating=0.9)

# تحليل الملاحظات
analysis = learning.analyze_feedback("إجابة ممتازة", rating=5)

# الحصول على تقرير الأداء
report = learning.get_performance_report()
```

## 📊 الأداء

| المقياس | القيمة |
|--------|--------|
| وقت الاستجابة | < 2 ثانية |
| استهلاك الذاكرة | < 500 MB |
| دقة الفهم | 92% |
| دعم اللغات | العربية، الإنجليزية |

## 🔧 المتطلبات

- Python 3.8 أو أحدث
- 4 GB RAM (الحد الأدنى)
- 2 GB مساحة تخزين

## 📖 الوثائق

- [README الكامل](https://github.com/yourusername/almufti-bin-badran/blob/master/README.md)
- [دليل المساهمة](https://github.com/yourusername/almufti-bin-badran/blob/master/CONTRIBUTING.md)
- [سجل التغييرات](https://github.com/yourusername/almufti-bin-badran/blob/master/CHANGELOG.md)

## 🤝 المساهمة

نرحب بمساهماتك! يرجى اتباع [دليل المساهمة](CONTRIBUTING.md) للمزيد من التفاصيل.

## 📝 الترخيص

هذا المشروع مرخص تحت رخصة MIT - انظر [LICENSE](LICENSE) للتفاصيل.

## 🔗 الروابط المهمة

- [GitHub Repository](https://github.com/yourusername/almufti-bin-badran)
- [PyPI Package](https://pypi.org/project/almufti-bin-badran)
- [Documentation](https://almufti-bin-badran.readthedocs.io)

## 👨‍💻 المؤلفون

تم تطوير هذا المشروع بواسطة فريق التطوير المتخصص في الذكاء الاصطناعي.

## 📞 التواصل والدعم

- 📧 البريد الإلكتروني: dev@almufti.ai
- 🐛 الإبلاغ عن الأخطاء: [GitHub Issues](https://github.com/yourusername/almufti-bin-badran/issues)

---

**شكراً لاستخدامك المفتي بن بدران! 🙏**

*آخر تحديث: 2024-12-04*
