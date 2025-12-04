# نشر المفتي بن بدران
# Almufti Bin Badran Deployment Guide

## 📦 حزم التوزيع
## Distribution Packages

تم بناء حزمتي توزيع جاهزتين للنشر:

### 1. Source Distribution (tar.gz)
```
dist/almufti-bin-badran-1.0.0.tar.gz (26 KB)
```

### 2. Wheel Distribution
```
dist/almufti_bin_badran-1.0.0-py3-none-any.whl (28 KB)
```

---

## 🚀 نشر على PyPI
## Publishing to PyPI

### الخطوة 1: إنشاء حساب PyPI

1. اذهب إلى https://pypi.org/account/register/
2. أنشئ حساباً جديداً
3. تحقق من بريدك الإلكتروني

### الخطوة 2: إنشاء Token

1. اذهب إلى https://pypi.org/manage/account/tokens/
2. أنشئ token جديد
3. احفظ الـ token في مكان آمن

### الخطوة 3: إعداد .pypirc

أنشئ ملف `~/.pypirc`:

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi_YOUR_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi_YOUR_TOKEN_HERE
```

### الخطوة 4: التحقق من الحزمة

```bash
twine check dist/*
```

### الخطوة 5: رفع إلى TestPyPI (اختياري)

```bash
twine upload --repository testpypi dist/*
```

### الخطوة 6: رفع إلى PyPI

```bash
twine upload dist/*
```

---

## 🌐 نشر على Hugging Face Spaces
## Publishing to Hugging Face Spaces

### الخطوة 1: إنشاء Space

1. اذهب إلى https://huggingface.co/spaces
2. انقر على "Create new Space"
3. ملأ البيانات:
   - **Name:** almufti-bin-badran
   - **License:** MIT
   - **SDK:** Gradio
   - **Visibility:** Public

### الخطوة 2: استنساخ المساحة

```bash
git clone https://huggingface.co/spaces/s200077761/almufti-bin-badran
cd almufti-bin-badran
```

### الخطوة 3: نسخ الملفات

```bash
cp -r /path/to/almufti-bin-badran/almufti .
cp /path/to/almufti-bin-badran/app.py .
cp /path/to/almufti-bin-badran/requirements.txt .
cp /path/to/almufti-bin-badran/README.md .
```

### الخطوة 4: رفع التغييرات

```bash
git add .
git commit -m "Initial commit: Almufti Bin Badran"
git push
```

---

## 🐳 نشر باستخدام Docker
## Publishing with Docker

### بناء صورة Docker

```bash
docker build -t almufti-bin-badran:latest .
```

### تشغيل الحاوية

```bash
docker run -p 7860:7860 almufti-bin-badran:latest
```

### نشر على Docker Hub

```bash
docker tag almufti-bin-badran:latest s200077761/almufti-bin-badran:latest
docker push s200077761/almufti-bin-badran:latest
```

---

## 📋 قائمة التحقق من النشر
## Deployment Checklist

- [ ] تم بناء الحزم (dist/)
- [ ] تم التحقق من الحزم (twine check)
- [ ] تم إنشاء حساب PyPI
- [ ] تم إنشاء PyPI token
- [ ] تم إعداد .pypirc
- [ ] تم الرفع إلى TestPyPI (اختياري)
- [ ] تم الرفع إلى PyPI
- [ ] تم إنشاء Hugging Face Space
- [ ] تم رفع الملفات إلى HF Space
- [ ] تم بناء صورة Docker
- [ ] تم نشر على Docker Hub (اختياري)

---

## 🔗 الروابط النهائية
## Final Links

### PyPI
```
https://pypi.org/project/almufti-bin-badran/
pip install almufti-bin-badran
```

### Hugging Face Spaces
```
https://huggingface.co/spaces/s200077761/almufti-bin-badran
```

### GitHub Repository
```
https://github.com/s200077761/almufti-bin-badran
```

### Docker Hub
```
docker pull s200077761/almufti-bin-badran:latest
```

---

## 📞 الدعم
## Support

- **البريد الإلكتروني:** dev@almufti.ai
- **GitHub Issues:** https://github.com/s200077761/almufti-bin-badran/issues
- **Discussions:** https://github.com/s200077761/almufti-bin-badran/discussions

---

## 📝 ملاحظات مهمة
## Important Notes

1. **الأمان:** لا تشارك PyPI token مع أحد
2. **الإصدارات:** استخدم semantic versioning (major.minor.patch)
3. **التوثيق:** حدّث README.md قبل كل إصدار جديد
4. **الاختبارات:** شغل الاختبارات قبل النشر

---

**آخر تحديث:** 2024-12-04
**الحالة:** جاهز للنشر ✅
