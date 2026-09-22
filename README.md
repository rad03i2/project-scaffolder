# Project Scaffolder

A small, safe project generator for creating useful Python package and dependency-free static-web foundations from the command line. It is designed for developers who want repeatable structure without a heavyweight template engine.

## English

### Why it exists
Starting projects repeatedly means recreating packaging, source folders, tests, ignore rules, and basic web wiring. Project Scaffolder makes those first steps deterministic while keeping generated output understandable and editable.

### Features
- `python` template: `src/` package layout, `pyproject.toml`, runnable module, smoke test, README and `.gitignore`.
- `web` template: responsive HTML, CSS and JavaScript with accessible live status and no framework dependency.
- Safe project-name validation and destination containment.
- Refuses to replace scaffold-managed files unless `--force` is explicitly used.
- `--dry-run` preview and `--json` machine-readable output.
- Custom author metadata.
- Reusable Python API.
- No runtime dependencies, network calls, telemetry, generated credentials, or code execution.

### Requirements & installation
Python 3.10 or newer.

```bash
python -m pip install -e .
project-scaffolder --version
```

For development:

```bash
python -m pip install -e . pytest
```

### Usage
```bash
# Python package
project-scaffolder my-tool

# Static web project
project-scaffolder my-site --template web

# Choose destination and author
project-scaffolder sample -d ./work --author "Example Author"

# Preview only
project-scaffolder sample --dry-run

# Automation-friendly output
project-scaffolder sample --dry-run --json

# Available templates
project-scaffolder --list-templates
```

`--force` only replaces files managed by the selected template; unrelated files already in the project directory are left alone.

### Python API
```python
from project_scaffolder import scaffold

result = scaffold("my-tool", destination="./projects", template="python", dry_run=True)
print(result.root)
for path in result.created:
    print(path)
```

### Preview guidance
This is a CLI generator, so screenshots are not required. For a release page, a terminal recording showing `--dry-run`, generation, and the resulting tree is the most useful preview. Generated web projects can be previewed by opening their `index.html` directly in a browser.

### Configuration
Project Scaffolder intentionally has no config file or environment variables. Behavior is controlled through explicit CLI flags/API arguments. Supported templates are `python` and `web`.

### Project structure
```text
project-scaffolder/
├── src/project_scaffolder/
│   ├── __init__.py
│   ├── cli.py
│   └── core.py
├── tests/
│   ├── test_cli.py
│   └── test_core.py
├── .github/workflows/ci.yml
├── CONTRIBUTING.md
├── SECURITY.md
├── LICENSE
└── pyproject.toml
```

### Testing
```bash
python -m compileall -q src tests
python -m pytest -q
```
CI runs compilation, tests, and a CLI smoke check on Python 3.10, 3.12, and 3.13 across Ubuntu, Windows, and macOS.

### Security & privacy
The tool operates locally, performs no network requests, and does not execute generated code. Names are validated to prevent path traversal. Existing template-managed files are protected by default. Review generated projects before deploying them; scaffolding does not replace dependency, application, or deployment security review.

### Limitations
- Only Python and dependency-free static-web templates are included today.
- Templates are intentionally minimal foundations, not full application frameworks.
- `--force` can replace template-managed files, so preview with `--dry-run` first when working in an existing directory.
- Generated Python projects use Hatchling metadata but do not pin build-tool versions beyond a safe minimum.

### Optional roadmap
Additional templates may be added when they can remain small, tested, and genuinely runnable. Template discovery/plugins and interactive prompting are optional future work; the current CLI remains deliberately deterministic.

### Contributing & license
See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Licensed under the [MIT License](LICENSE).

### Author
**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **@rad03i2**

---

## العربية

### نظرة عامة
**Project Scaffolder** أداة سطر أوامر صغيرة وآمنة لإنشاء أساس عملي ومنظم لمشاريع Python أو مواقع الويب الثابتة دون الحاجة إلى محرك قوالب ثقيل. الهدف هو اختصار الأعمال المتكررة في بداية المشروع مع إبقاء كل ملف مولّد واضحًا وقابلًا للتعديل.

### لماذا توجد الأداة؟
عند بدء مشاريع متعددة نعيد عادة إنشاء بنية المصدر، إعدادات الحزمة، الاختبارات، ملف التجاهل، أو ملفات HTML وCSS وJavaScript الأساسية. تقوم الأداة بإنشاء هذه البداية بصورة ثابتة وقابلة للتكرار بدل نسخ الملفات يدويًا في كل مرة.

### المزايا
- قالب `python` يتضمن بنية `src/`، و`pyproject.toml`، ووحدة قابلة للتشغيل، واختبارًا أوليًا، وREADME و`.gitignore`.
- قالب `web` يتضمن HTML متجاوبًا وCSS وJavaScript دون إطار عمل خارجي، مع عنصر حالة مناسب لتقنيات الوصول.
- التحقق من اسم المشروع ومنع الخروج من مجلد الوجهة.
- عدم استبدال ملفات القالب الموجودة إلا عند طلب `--force` صراحة.
- معاينة آمنة بواسطة `--dry-run` وإخراج JSON للأتمتة.
- تخصيص اسم المؤلف.
- Python API قابلة لإعادة الاستخدام.
- لا توجد اعتماديات تشغيلية أو اتصالات شبكة أو telemetry أو أسرار مولّدة أو تنفيذ تلقائي للكود.

### المتطلبات والتثبيت
تحتاج Python 3.10 أو أحدث.

```bash
python -m pip install -e .
project-scaffolder --version
```

للتطوير والاختبار:

```bash
python -m pip install -e . pytest
```

### الاستخدام
```bash
# إنشاء مشروع Python
project-scaffolder my-tool

# إنشاء موقع ثابت
project-scaffolder my-site --template web

# تحديد الوجهة والمؤلف
project-scaffolder sample -d ./work --author "Example Author"

# معاينة دون كتابة ملفات
project-scaffolder sample --dry-run

# إخراج JSON
project-scaffolder sample --dry-run --json

# عرض القوالب
project-scaffolder --list-templates
```

خيار `--force` يستبدل فقط الملفات التي يديرها القالب المختار، ولا يحذف الملفات الأخرى الموجودة في مجلد المشروع.

### Python API
```python
from project_scaffolder import scaffold

result = scaffold("my-tool", destination="./projects", template="python", dry_run=True)
print(result.root)
```

### المعاينة
لأن المشروع أداة CLI فلا يحتاج إلى لقطات شاشة ثابتة. أفضل عرض له هو تسجيل طرفية قصير يوضح `--dry-run` ثم إنشاء المشروع وشجرة الملفات. ويمكن معاينة قالب الويب مباشرة بفتح `index.html` في المتصفح.

### الإعداد
لا تستخدم الأداة ملف إعداد أو متغيرات بيئة. كل السلوك يحدد صراحة عبر خيارات CLI أو معاملات Python API. القوالب المتاحة حاليًا: `python` و`web`.

### بنية المشروع
الكود موجود في `src/project_scaffolder`، والاختبارات في `tests`، وCI في `.github/workflows/ci.yml`، مع ملفات مستقلة للمساهمة والأمان والترخيص.

### الاختبارات
```bash
python -m compileall -q src tests
python -m pytest -q
```
يختبر CI المشروع على Python 3.10 و3.12 و3.13 في Ubuntu وWindows وmacOS، مع فحص compilation وتجربة CLI.

### الأمان والخصوصية
كل العمل محلي ولا توجد طلبات شبكة ولا تنفيذ للكود المولّد. يتم التحقق من أسماء المشاريع لمنع path traversal، والملفات الموجودة محمية افتراضيًا. يجب مع ذلك مراجعة المشروع الناتج قبل نشره؛ إنشاء الهيكل لا يغني عن مراجعة أمان التطبيق واعتمادياته وإعدادات النشر.

### القيود
- القوالب الحالية هي Python والويب الثابت فقط.
- القوالب أساسات عملية صغيرة وليست أطر تطبيقات كاملة.
- `--force` يستطيع استبدال الملفات التي يديرها القالب؛ يفضل استخدام `--dry-run` أولًا داخل المجلدات الموجودة.
- مشروع Python المولّد يستخدم Hatchling ولا يثبت كل أدوات البناء على إصدار واحد محدد.

### التطوير المستقبلي الاختياري
يمكن إضافة قوالب أخرى عندما تكون صغيرة وقابلة للاختبار والتشغيل الحقيقي. دعم الإضافات أو الوضع التفاعلي أفكار اختيارية مستقبلية، بينما يبقى السلوك الحالي متوقعًا ومحددًا.

### المساهمة والترخيص
راجع [CONTRIBUTING.md](CONTRIBUTING.md) وإرشادات [SECURITY.md](SECURITY.md). المشروع مرخص تحت [MIT](LICENSE).

### المؤلف
**Radwan Abdulhadi Ahmed**  
**رضوان عبدالهادي أحمد**  
GitHub: **@rad03i2**
