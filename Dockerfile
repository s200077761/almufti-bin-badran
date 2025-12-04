# استخدام صورة Python الرسمية
FROM python:3.11-slim

# تعيين مجلد العمل
WORKDIR /app

# تثبيت المكتبات النظام المطلوبة
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# نسخ ملفات المشروع
COPY . /app

# تثبيت المكتبات Python
RUN pip install --no-cache-dir -r requirements.txt

# إنشاء مجلدات البيانات
RUN mkdir -p data/{models,knowledge,conversations} logs

# تعيين متغيرات البيئة
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# فتح المنفذ (إذا كان يستخدم Gradio)
EXPOSE 7860

# أمر التشغيل الافتراضي
CMD ["almufti", "menu"]

# أو لتشغيل تطبيق Gradio:
# CMD ["python", "app.py"]
