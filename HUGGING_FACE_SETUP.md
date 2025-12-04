# إعداد Hugging Face Space
# Hugging Face Space Setup Guide

## الخطوات اليدوية لإنشاء المساحة

### 1. إنشاء Space جديد على Hugging Face

1. اذهب إلى https://huggingface.co/spaces
2. انقر على "Create new Space"
3. املأ البيانات:
   - **Space name:** almufti-bin-badran
   - **License:** MIT
   - **Space SDK:** Gradio
   - **Visibility:** Public

### 2. رفع الملفات

بعد إنشاء المساحة، استنسخ المستودع:

```bash
git clone https://huggingface.co/spaces/s200077761/almufti-bin-badran
cd almufti-bin-badran
```

ثم انسخ الملفات من المشروع الرئيسي:

```bash
cp -r /path/to/almufti-bin-badran/almufti .
cp /path/to/almufti-bin-badran/app.py .
cp /path/to/almufti-bin-badran/requirements.txt .
cp /path/to/almufti-bin-badran/README.md .
```

### 3. رفع التغييرات

```bash
git add .
git commit -m "Add Almufti Bin Badran AI Assistant"
git push
```

## الرابط النهائي

بعد الانتهاء، ستكون المساحة متاحة على:
https://huggingface.co/spaces/s200077761/almufti-bin-badran

## ملفات المساحة المطلوبة

- **app.py** - تطبيق Gradio الرئيسي
- **requirements.txt** - المكتبات المطلوبة
- **almufti/** - مجلد المكتبة الرئيسية
- **README.md** - التوثيق

## متطلبات التشغيل

- Python 3.8+
- Gradio 4.0+
- المكتبات المذكورة في requirements.txt

## ملاحظات

- المساحة ستعمل تلقائياً عند الرفع
- قد تستغرق عملية البناء بضع دقائق
- يمكنك مراقبة التقدم من خلب تبويب "Logs"

