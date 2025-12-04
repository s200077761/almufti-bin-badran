# دليل التثبيت
# Installation Guide

## المتطلبات الأساسية
## System Requirements

### الحد الأدنى
- **نظام التشغيل:** Windows 10+, macOS 10.14+, Linux (Ubuntu 18.04+)
- **Python:** 3.8 أو أحدث
- **الذاكرة:** 4 GB RAM
- **المساحة:** 2 GB

### الموصى به
- **نظام التشغيل:** Windows 11, macOS 12+, Linux (Ubuntu 20.04+)
- **Python:** 3.10 أو أحدث
- **الذاكرة:** 8 GB RAM
- **المساحة:** 5 GB

---

## طرق التثبيت
## Installation Methods

### 1. التثبيت من PyPI (الطريقة الموصى بها)
### From PyPI (Recommended)

```bash
# تثبيت الحزمة
pip install almufti-bin-badran

# أو مع دعم الصوت
pip install almufti-bin-badran[audio]

# أو مع أدوات التطوير
pip install almufti-bin-badran[dev]
```

### 2. التثبيت من المصدر
### From Source

```bash
# استنساخ المستودع
git clone https://github.com/yourusername/almufti-bin-badran.git
cd almufti-bin-badran

# إنشاء بيئة افتراضية
python3 -m venv venv

# تفعيل البيئة الافتراضية
# على Linux/macOS:
source venv/bin/activate

# على Windows:
venv\Scripts\activate

# تثبيت المكتبات
pip install -r requirements.txt

# تثبيت الحزمة بشكل محلي
pip install -e .
```

### 3. التثبيت من Conda
### From Conda

```bash
# إنشاء بيئة جديدة
conda create -n almufti python=3.10

# تفعيل البيئة
conda activate almufti

# تثبيت الحزمة
pip install almufti-bin-badran
```

### 4. التثبيت في Docker
### Docker Installation

```bash
# بناء صورة Docker
docker build -t almufti-bin-badran .

# تشغيل الحاوية
docker run -it almufti-bin-badran

# أو مع مجلد مشترك
docker run -it -v $(pwd):/app almufti-bin-badran
```

---

## التحقق من التثبيت
## Verify Installation

```bash
# التحقق من الإصدار
almufti --version

# تشغيل الاختبارات
pytest tests/

# تشغيل المساعد
almufti chat
```

---

## التثبيت على أنظمة محددة
## Platform-Specific Installation

### على Windows

```bash
# تثبيت Python من python.org
# أو استخدام Windows Package Manager
winget install Python.Python.3.11

# إنشاء بيئة افتراضية
python -m venv venv
venv\Scripts\activate

# تثبيت المكتبات
pip install -r requirements.txt
```

### على macOS

```bash
# استخدام Homebrew
brew install python@3.11

# إنشاء بيئة افتراضية
python3 -m venv venv
source venv/bin/activate

# تثبيت المكتبات
pip install -r requirements.txt
```

### على Linux (Ubuntu/Debian)

```bash
# تحديث النظام
sudo apt update && sudo apt upgrade

# تثبيت Python
sudo apt install python3.11 python3.11-venv python3-pip

# إنشاء بيئة افتراضية
python3.11 -m venv venv
source venv/bin/activate

# تثبيت المكتبات
pip install -r requirements.txt
```

---

## التثبيت مع الميزات الإضافية
## Installation with Extra Features

### دعم الصوت
### Audio Support

```bash
# تثبيت مع دعم الصوت
pip install almufti-bin-badran[audio]

# أو يدويًا
pip install librosa soundfile
```

### أدوات التطوير
### Development Tools

```bash
# تثبيت مع أدوات التطوير
pip install almufti-bin-badran[dev]

# أو يدويًا
pip install pytest pytest-cov black flake8
```

### جميع الميزات
### All Features

```bash
pip install almufti-bin-badran[audio,dev]
```

---

## حل المشاكل الشائعة
## Troubleshooting

### مشكلة: "Python غير مثبت"
### Issue: "Python not found"

**الحل:**
- تأكد من تثبيت Python 3.8+
- تحقق من إضافة Python إلى PATH
- استخدم `python3` بدلاً من `python`

```bash
python3 --version
```

### مشكلة: "خطأ في تثبيت المكتبات"
### Issue: "Error installing dependencies"

**الحل:**
```bash
# تحديث pip
pip install --upgrade pip

# حذف الحزم المخزنة مؤقتًا
pip cache purge

# إعادة التثبيت
pip install -r requirements.txt --no-cache-dir
```

### مشكلة: "خطأ في استيراد المكتبات"
### Issue: "Import error"

**الحل:**
```bash
# تأكد من تفعيل البيئة الافتراضية
which python  # على Linux/macOS
where python  # على Windows

# أعد تثبيت المكتبات
pip install -r requirements.txt --force-reinstall
```

### مشكلة: "استهلاك عالي للذاكرة"
### Issue: "High memory usage"

**الحل:**
- تقليل حجم السياق في الإعدادات
- استخدام نماذج أخف
- تفعيل ضغط البيانات

```yaml
# في config/settings.yaml
performance:
  max_memory: 1024  # تقليل من 2048
  cache_size: 256   # تقليل من 512
```

---

## التحديث
## Updating

### تحديث من PyPI

```bash
pip install --upgrade almufti-bin-badran
```

### تحديث من المصدر

```bash
cd almufti-bin-badran
git pull origin master
pip install -e . --upgrade
```

---

## الإزالة
## Uninstallation

```bash
# إزالة الحزمة
pip uninstall almufti-bin-badran

# حذف المجلد (إذا تم التثبيت من المصدر)
rm -rf almufti-bin-badran
```

---

## الخطوات التالية
## Next Steps

بعد التثبيت الناجح:

1. **اقرأ الوثائق:** [README.md](README.md)
2. **جرب الأمثلة:** [examples/basic_usage.py](examples/basic_usage.py)
3. **ابدأ محادثة:** `almufti chat`
4. **ساهم في المشروع:** [CONTRIBUTING.md](CONTRIBUTING.md)

---

## الدعم
## Support

إذا واجهت مشاكل:

- 📖 اقرأ [README.md](README.md)
- 🐛 ابحث في [GitHub Issues](https://github.com/yourusername/almufti-bin-badran/issues)
- 💬 اسأل في [Discussions](https://github.com/yourusername/almufti-bin-badran/discussions)
- 📧 تواصل: dev@almufti.ai

---

**آخر تحديث:** 2024-12-04
