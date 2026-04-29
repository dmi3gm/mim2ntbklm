

# SOURCE_FILE: 0.OPS/0.1.Knowledge-Logic/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# 0.1. Knowledge Logic

Онтология и модель организации знаний в хранилище.

## Содержимое

| № | Документ | Описание |
|---|----------|----------|
| 01 | [01-kernels-model.md](01-kernels-model.md) | Модель ядер: что такое ядро, как создавать новые |
| 02 | [02-document-families.md](02-document-families.md) | 9 семейств документов внутри каждого ядра |
| 03 | [03-our-systems-map.md](03-our-systems-map.md) | Карта "наших систем" и их позиция в цепочке |
| 04 | [04-ontology.md](04-ontology.md) | Общая онтология для всех ядер |
| 05 | [05-glossary.md](05-glossary.md) | Глоссарий терминов |
| 06 | [06-taxonomy.md](06-taxonomy.md) | Система классификации документов |
| 07 | [07-naming.md](07-naming.md) | Соглашения об именовании |
| 08 | [08-anti-patterns.md](08-anti-patterns.md) | Анти-паттерны (типичные ошибки) |
| 09 | [09-examples-library.md](09-examples-library.md) | Библиотека примеров для AI |

## Принцип

Знания организованы иерархически:

```
Хранилище
└── Ядро (Kernel)
    └── Система (Suprasystem / SoI / Constructor)
        └── Роль (Meaning / Architecture / Operations)
            └── Документ
```


# SOURCE_FILE: 0.OPS/0.2.Kernels-Bridge/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# 0.2. Kernels Bridge

Связи и отношения между ядрами хранилища.

## Содержимое

| Документ | Описание |
|----------|----------|
| [01-value-chain.md](01-value-chain.md) | Цепочка создания ценности |
| [02-kernels-relations.md](02-kernels-relations.md) | Матрица связей между ядрами |
| [03-systems-relations.md](03-systems-relations.md) | Структура связанности систем |

## Назначение

Этот раздел отвечает на вопросы:
- Как ядра связаны друг с другом?
- Какая цепочка создания ценности?
- Какая структура связанности систем?


# SOURCE_FILE: 0.OPS/0.4.FPF-Integration/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# 0.6. FPF Integration

Интеграция с First Principles Framework (FPF) — эпистемологическим фундаментом S2R.

## Что такое FPF?

**First Principles Framework (FPF)** — это "операционная система для мышления", архитектура трансдисциплинарного рассуждения. FPF не методология, а **эпистема метода** — структурированная спецификация того, как думать.

**Источник:** [github.com/ailev/FPF](https://github.com/ailev/FPF)

## Содержимое

| Документ | Описание |
|----------|----------|
| [fpf-integration.md](fpf-integration.md) | Как S2R использует FPF |
| [fpf-patterns-map.md](fpf-patterns-map.md) | Карта паттернов FPF в S2R |
| [fpf/](fpf/) | Копия FPF-спецификации |

## Файлы FPF

```
fpf/
├── INDEX.md          # Локальные принципы проекта (~250 строк)
├── FPF-Spec.md       # Полная спецификация FPF (~43K строк)
└── FPF-Readme.md     # Обзор фреймворка
```

## Версия FPF

| Параметр | Значение |
|----------|----------|
| **Версия** | Актуальная на момент создания репозитория |
| **Источник** | https://github.com/ailev/FPF |
| **Обновление** | По необходимости вручную |

### Как обновить FPF

```bash
curl -sL "https://raw.githubusercontent.com/ailev/FPF/main/FPF-Spec.md" \
  -o 0.OPS/0.4.FPF-Integration/fpf/FPF-Spec.md
```

## Связь S2R и FPF

S2R **строится на основе FPF**, заимствуя:

| Концепция S2R | FPF-паттерн | Описание |
|---------------|-------------|----------|
| Ядро как холон | A.1 | Каждое ядро — целое и часть одновременно |
| Локальная онтология | A.1.1 | Bounded Context — термины локальны |
| Три системы | A.3 | System Triad: Suprasystem, SoI, Constructor |
| Строгое различение | A.7 | Роль ≠ Человек, Документ ≠ Система |
| Доверие | B.3 | F-G-R кортеж оценки информации |
| I/D/S дисциплина | E.10.D2 | Intension, Description, Specification |

## Стратегия работы с FPF

### Для обычных задач

Используй `fpf/INDEX.md` — локальные принципы проекта.

### Для глубокого анализа

Запрашивай конкретные части `FPF-Spec.md`:

| Часть | Строки | Тема |
|-------|--------|------|
| Preface | 1-500 | Введение, OS-метафора |
| Part A | 500-8000 | Kernel: Holon, Role, Transformer |
| Part B | 8000-15000 | Trans-disciplinary: Trust, Evolution |
| Part C | 15000-25000 | Calculi: Sys, KD, NQD |
| Part D | 25000-28000 | Ethics & Conflict |
| Part E | 28000-33000 | Constitution & Authoring |
| Part F | 33000-38000 | Unification: Bridges |
| Part G | 38000-43000 | SoTA Kit |

## См. также

- [fpf-integration.md](fpf-integration.md) — детали интеграции
- [../0.1.Knowledge-Logic/04-ontology.md](../0.1.Knowledge-Logic/04-ontology.md) — общая онтология


# SOURCE_FILE: 0.OPS/0.5.AI-Reports/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# 0.5. AI Reports

Автоматические AI-проверки и отчёты по состоянию хранилища.

## Содержимое

| Папка | Описание |
|-------|----------|
| [Validation-Specs/](Validation-Specs/) | Технические задания на автоматические проверки |
| [Validation-Results/](Validation-Results/) | Результаты выполненных проверок |

## Расписание проверок

| Проверка | Расписание | Режим |
|----------|------------|-------|
| Формальная проверка | Воскресенье, 9:00 | Авто / Ручной |
| Содержательная проверка | Воскресенье, 9:00 | Авто / Ручной |
| Анализ развития | Воскресенье, 9:00 | Авто / Ручной |

## Как запустить проверку вручную

```
/validate formal     # Формальная проверка
/validate content    # Содержательная проверка
/validate develop    # Анализ предложений по развитию
/validate all        # Все проверки
```

## Структура результатов

Результаты проверок сохраняются в `Validation-Results/` с именем:

```
{YYYY-MM-DD}-{тип-проверки}.md
```

Например:
- `2026-01-14-formal.md`
- `2026-01-14-content.md`
- `2026-01-14-develop.md`

## Формат отчёта

```markdown
# [Тип отчёта]

**Дата:** YYYY-MM-DD
**Сгенерировано:** Claude Code

## Резюме

[Краткие выводы]

## Детали

[Подробный анализ]

## Рекомендации

- [ ] Рекомендация 1
- [ ] Рекомендация 2
```

## Спецификации проверок

- [Validation-Specs/01-formal-checks.md](Validation-Specs/01-formal-checks.md) — формальные проверки
- [Validation-Specs/02-content-checks.md](Validation-Specs/02-content-checks.md) — содержательные проверки
- [Validation-Specs/03-development-analysis.md](Validation-Specs/03-development-analysis.md) — анализ развития


# SOURCE_FILE: 0.OPS/0.5.AI-Reports/Validation-Results/README.md
---
---
type: index
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Validation Results

Результаты автоматических AI-проверок хранилища.

## Формат имён файлов

```
{YYYY-MM-DD}-{тип-проверки}.md
```

## Типы проверок

| Тип | Описание |
|-----|----------|
| `formal` | Результаты формальных проверок |
| `content` | Результаты содержательных проверок |
| `develop` | Анализ развития и рекомендации |
| `all` | Полный отчёт всех проверок |

## Примеры

- `2026-01-14-formal.md` — формальная проверка от 14 января
- `2026-01-14-all.md` — полный отчёт от 14 января

## Последние результаты

*Пока нет результатов проверок.*


# SOURCE_FILE: 0.OPS/0.5.AI-Reports/Validation-Specs/README.md
---
---
type: index
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Validation Specs

Технические задания на автоматические AI-проверки хранилища.

## Спецификации

| Документ | Описание | Команда |
|----------|----------|---------|
| [01-formal-checks.md](01-formal-checks.md) | Формальные проверки структуры и ссылок | `/validate formal` |
| [02-content-checks.md](02-content-checks.md) | Содержательные проверки методологии | `/validate content` |
| [03-development-analysis.md](03-development-analysis.md) | Анализ полноты и предложения по развитию | `/validate develop` |

## Расписание

Все проверки запускаются автоматически:
- **Время:** Воскресенье, 9:00
- **Режим:** Автоматический или ручной

## Уровни важности

| Уровень | Значение | Действие |
|---------|----------|----------|
| Error | Критическая ошибка | Требует немедленного исправления |
| Warning | Предупреждение | Рекомендуется исправить |
| Info | Информация | На усмотрение |

## Запуск всех проверок

```
/validate all
```


# SOURCE_FILE: 0.OPS/0.6.Repository-Processes/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# 0.6. Repository Processes

Процессы и стандарты работы с хранилищем.

## Содержимое

| Документ | Описание |
|----------|----------|
| [01-project-description-template.md](01-project-description-template.md) | ⭐ Шаблон описания проекта (первый шаг) |
| [02-standards.md](02-standards.md) | Стандарты оформления документов |
| [03-structure.md](03-structure.md) | Структура папок репозитория |
| [04-document-creation.md](04-document-creation.md) | Процесс создания документов |
| [05-frontmatter-spec.md](05-frontmatter-spec.md) | Спецификация метаданных |
| [06-workflows.md](06-workflows.md) | Рабочие процессы |
| [07-roles.md](07-roles.md) | Роли и ответственность |
| [08-deployment-guide.md](08-deployment-guide.md) | ⭐ **Руководство по развёртыванию** |

## Быстрый старт для развёртывания

> **Новым пользователям:** Следуйте этим шагам для развёртывания S2R под ваш проект.

1. ⭐ Прочитай [08-deployment-guide.md](08-deployment-guide.md) — **полное руководство по развёртыванию**
2. Заполни [01-project-description-template.md](01-project-description-template.md) — опиши проект
3. Переименуй папки ядер с реальными именами систем
4. Заполни `0.1.Knowledge-Logic/03-our-systems-map.md` — карта систем
5. Заполни `0.2.Kernels-Bridge/01-value-chain.md` — цепочка ценности

## Быстрый старт для работы с документами

1. Прочитай [02-standards.md](02-standards.md) — как оформлять
2. Используй [04-document-creation.md](04-document-creation.md) — как создавать
3. Следуй [05-frontmatter-spec.md](05-frontmatter-spec.md) — метаданные


# SOURCE_FILE: 0.OPS/0.7.Plans-and-Meetings/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# 0.4. Plans and Meetings

Планирование и координация работы с хранилищем.

## Принцип: Совещания по материалам хранилища

> **Ключевое правило:** Все совещания в компании проходят **исключительно по материалам этого хранилища**.

Это означает:
1. **Подготовка к встрече** — участники готовят и размещают материалы в хранилище заранее
2. **На встрече** — обсуждение происходит по документам из хранилища
3. **После встречи** — договорённости фиксируются, изменения вносятся в хранилище

### Типы обсуждаемых вопросов

| Тип | Описание | Результат |
|-----|----------|-----------|
| **Онтологические** | Термины, структура, модель | Изменения в `0.1.Knowledge-Logic/` |
| **Операционные** | Процессы, задачи, исполнение | Изменения в соответствующих семействах |
| **Стратегические** | Направления, приоритеты | Изменения в `X.1.Meaning/` |

## Процесс работы с предложениями

### 1. Внесение предложений

Любое подразделение может внести предложение:
1. Создать документ с предложением
2. Положить в папку `0.9.Inbox/`
3. Указать автора и дату

### 2. Рассмотрение на встрече

На регулярной встрече:
1. Рассматриваются материалы из `0.9.Inbox/`
2. Обсуждаются онтологические и операционные вопросы
3. Принимаются решения

### 3. Фиксация договорённостей

По итогам встречи:
1. Создаётся протокол в этой папке
2. Фиксируются договорённости с ответственными
3. При необходимости вносятся изменения в хранилище
4. Обработанные предложения удаляются из `0.9.Inbox/` или архивируются

## Содержимое папки

Здесь размещаются:
- Протоколы встреч по структуре знаний
- Планы развития хранилища
- Roadmap документации
- Договорённости и решения

## Шаблон протокола встречи

```markdown
# Встреча: [Тема]

**Дата:** YYYY-MM-DD
**Участники:** @user1, @user2
**Тип вопросов:** Онтологические / Операционные / Смешанные

## Рассмотренные материалы

- [Документ 1](путь/к/документу.md)
- [Предложение из Inbox](../0.9.Inbox/предложение.md)

## Повестка

1. ...
2. ...

## Решения и договорённости

| Решение | Ответственный | Срок | Статус |
|---------|---------------|------|--------|
| Внести изменения в X | @user | дата | ⏳ |
| Обновить онтологию | @user | дата | ⏳ |

## Изменения в хранилище

По итогам встречи внесены изменения:
- [ ] `путь/к/файлу.md` — описание изменения
- [ ] `путь/к/файлу2.md` — описание изменения

## Следующие шаги

...
```

## Регулярность встреч

| Тип встречи | Периодичность | Фокус |
|-------------|---------------|-------|
| Операционная | Еженедельно | Текущие задачи, Inbox |
| Онтологическая | Ежемесячно | Структура, термины |
| Стратегическая | Ежеквартально | Направления развития |

## См. также

- [../0.9.Inbox/README.md](../0.9.Inbox/README.md) — входящие предложения
- [../0.6.Repository-Processes/workflows.md](../0.6.Repository-Processes/workflows.md) — рабочие процессы


# SOURCE_FILE: 0.OPS/0.9.Inbox/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# 0.9. Inbox

Входящие идеи и черновики, ожидающие классификации.

## Назначение

Сюда помещаются:
- Новые идеи, не классифицированные по семействам
- Черновики документов
- Заметки для последующей обработки

## Процесс обработки

1. Добавь файл в Inbox
2. Еженедельно: ревью содержимого
3. Определи семейство (ядро + F1-F9)
4. Перенеси в правильную папку
5. Удали из Inbox

## Формат входящего

```markdown
# [Заголовок идеи]

**Дата:** YYYY-MM-DD
**Автор:** @username

## Суть

[Описание идеи]

## Возможное размещение

- Ядро: A / B / ?
- Семейство: FX?
- Или: не знаю
```


# SOURCE_FILE: 0.OPS/0.99.Archive/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# 0.99. Archive

Архив устаревших документов.

## Назначение

Сюда перемещаются:
- Документы со статусом `archived`
- Устаревшие версии
- Исторические записи

## Правила архивации

1. Измени статус на `archived` перед переносом
2. Сохрани оригинальный путь в frontmatter
3. Добавь причину архивации
4. Обнови связи в других документах

## Структура архива

```
0.99.Archive/
├── YYYY-MM/                 # По месяцам
│   ├── old-document.md
│   └── another-old.md
└── README.md
```

## Поиск в архиве

Используй grep для поиска:
```bash
grep -r "ключевое слово" 0.99.Archive/
```


# SOURCE_FILE: 0.OPS/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# 0.OPS (F0)

**F0: Метаэпистема хранилища** — управление знаниями о знаниях в S2R/SRR.

> **Почему OPS?** OPS — коротко, стандартно, прямо означает "операционная логика и порядок работы". Туда естественно ложатся и inbox/archive как операционные корзины.

## Назначение

F0 выполняет три ключевые функции:

1. **Управление хранилищем** — логика организации знаний, стандарты, процессы
2. **Общая онтология** — термины и концепции, применимые ко всем ядрам
3. **Мосты между ядрами** — описание связей между "нашими системами"

## Структура

```
0.OPS/
├── 0.1.Knowledge-Logic/        # Онтология и модель знаний
├── 0.2.Kernels-Bridge/         # Связи между ядрами
├── 0.3.Roles-Matrix-3x3/       # Матрица ролей 3×3
├── 0.4.FPF-Integration/        # Интеграция с FPF
├── 0.5.AI-Reports/             # Автоматические отчёты
├── 0.6.Repository-Processes/   # Процессы и стандарты
├── 0.7.Plans-and-Meetings/     # Планирование
├── 0.9.Inbox/                  # Входящие идеи
└── 0.99.Archive/               # Архив
```

> **Примечание:** `CLAUDE.md` (инструкции для AI) перенесён в корень репозитория.

## Отличие от других семейств

F0 **не делится по ролям** (Предприниматель/Инженер/Менеджер), а организован по функциональным областям. Это единственное семейство, управляющее всеми остальными.

## Ключевые документы

| Документ | Расположение | Описание |
|----------|--------------|----------|
| [01-kernels-model.md](0.1.Knowledge-Logic/01-kernels-model.md) | 0.1 | Модель ядер и правила их создания |
| [02-document-families.md](0.1.Knowledge-Logic/02-document-families.md) | 0.1 | Модель 9 семейств внутри каждого ядра |
| [03-our-systems-map.md](0.1.Knowledge-Logic/03-our-systems-map.md) | 0.1 | Карта "наших систем" |
| [04-ontology.md](0.1.Knowledge-Logic/04-ontology.md) | 0.1 | Общая онтология |
| [05-glossary.md](0.1.Knowledge-Logic/05-glossary.md) | 0.1 | Глоссарий терминов |
| [07-naming.md](0.1.Knowledge-Logic/07-naming.md) | 0.1 | Соглашения об именовании |
| [08-anti-patterns.md](0.1.Knowledge-Logic/08-anti-patterns.md) | 0.1 | Анти-паттерны (типичные ошибки) |
| [09-examples-library.md](0.1.Knowledge-Logic/09-examples-library.md) | 0.1 | Библиотека примеров для AI |
| [01-value-chain.md](0.2.Kernels-Bridge/01-value-chain.md) | 0.2 | Цепочка создания ценности |
| [roles-matrix.md](0.3.Roles-Matrix-3x3/roles-matrix.md) | 0.3 | Матрица ролей 3×3 (полная) |
| [roles-matrix-brief.md](0.3.Roles-Matrix-3x3/roles-matrix-brief.md) | 0.3 | Матрица ролей 3×3 (краткая) |
| [fpf-integration.md](0.4.FPF-Integration/fpf-integration.md) | 0.4 | Интеграция с FPF |
| [01-project-description-template.md](0.6.Repository-Processes/01-project-description-template.md) | 0.6 | Шаблон описания проекта |

## Связи

- Управляет всеми ядрами (A, B, C...)
- Интегрируется с [FPF](0.4.FPF-Integration/fpf/INDEX.md)


# SOURCE_FILE: A.SOI-Name/A0.SOI-Name-Management/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA0
---

# A0. Kernel Management

Управление ядром A (опционально).

## Содержимое

| Документ | Описание |
|----------|----------|
| [local-ontology.md](local-ontology.md) | Локальная онтология ядра |

## Когда нужен этот раздел

- Есть специфичная терминология ядра A
- Нужны локальные определения, отличающиеся от общих
- Есть отдельная команда со своими процессами

## Ответственные за семейства

> **TODO:** Заполните при необходимости.

| Семейство | Ответственный |
|-----------|---------------|
| FA1-FA3 | *[@username]* |
| FA4-FA6 | *[@username]* |
| FA7-FA9 | *[@username]* |


# SOURCE_FILE: A.SOI-Name/A1.Suprasystem-Name/A1.1.Meaning/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA1
system: Suprasystem
role: Meaning
---

# FA1: Suprasystem × Предприниматель

## Фокус семейства

**Вопрос:** Зачем целевая система существует в своём окружении?

Документы этого семейства описывают:
- Рынок и тренды
- Стратегический контекст
- Позиционирование
- Конкурентный ландшафт
- Смысл существования в надсистеме

## Типичные документы

- Анализ рынка
- Исследование трендов
- Позиционирование
- Конкурентный анализ
- Стратегический контекст

## Шаблон документа

```yaml
---
type: doc
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
kernel: A
family: FA1
system: Suprasystem
role: Meaning
---
```

## Содержимое

> **TODO:** Добавьте документы семейства FA1.


# SOURCE_FILE: A.SOI-Name/A1.Suprasystem-Name/A1.2.Architecture/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA2
system: Suprasystem
role: Architecture
---

# FA2: Suprasystem × Инженер

## Фокус семейства

**Вопрос:** Как устроено окружение целевой системы?

Документы этого семейства описывают:
- Внешние системы и API
- Интерфейсы с окружением
- Технологический ландшафт
- Зависимости от внешних систем
- Интеграции

## Типичные документы

- Карта внешних систем
- Описание API-интеграций
- Технологический ландшафт
- Зависимости

## Шаблон документа

```yaml
---
type: doc
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
kernel: A
family: FA2
system: Suprasystem
role: Architecture
---
```

## Содержимое

> **TODO:** Добавьте документы семейства FA2.


# SOURCE_FILE: A.SOI-Name/A1.Suprasystem-Name/A1.3.Operations/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA3
system: Suprasystem
role: Operations
---

# FA3: Suprasystem × Менеджер

## Фокус семейства

**Вопрос:** Как целевая система взаимодействует с окружением?

Документы этого семейства описывают:
- Партнёрства и контракты
- Внешние стейкхолдеры
- Коммуникации с рынком
- Операционные связи с окружением

## Типичные документы

- Реестр партнёров
- Карта стейкхолдеров
- Коммуникационная стратегия
- Контракты и SLA

## Шаблон документа

```yaml
---
type: doc
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
kernel: A
family: FA3
system: Suprasystem
role: Operations
---
```

## Содержимое

> **TODO:** Добавьте документы семейства FA3.


# SOURCE_FILE: A.SOI-Name/A2.SOI-Name/A2.1.Meaning/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA4
system: System-of-Interest
role: Meaning
---

# FA4: System-of-Interest × Предприниматель

## Фокус семейства

**Вопрос:** Зачем нужна целевая система? Какую ценность создаёт?

Документы этого семейства описывают:
- Требования и спецификации
- JTBD и сценарии использования
- Value proposition
- Критерии успеха
- Потребности пользователей

## Типичные документы

- Требования (BRD, PRD)
- User Stories / JTBD
- Value Proposition Canvas
- Критерии приёмки
- Пользовательские сценарии

## Шаблон документа

```yaml
---
type: spec
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
kernel: A
family: FA4
system: System-of-Interest
role: Meaning
---
```

## Содержимое

> **TODO:** Добавьте документы семейства FA4.


# SOURCE_FILE: A.SOI-Name/A2.SOI-Name/A2.2.Architecture/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA5
system: System-of-Interest
role: Architecture
---

# FA5: System-of-Interest × Инженер

## Фокус семейства

**Вопрос:** Как устроена целевая система?

Документы этого семейства описывают:
- Архитектурные решения (ADR)
- Компонентная модель
- Технический дизайн
- Схемы и диаграммы
- Структура системы

## Типичные документы

- Architecture Decision Records (ADR)
- Компонентная диаграмма
- Схема данных
- API-спецификации
- Технический дизайн

## Шаблон документа

```yaml
---
type: spec
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
kernel: A
family: FA5
system: System-of-Interest
role: Architecture
---
```

## Содержимое

> **TODO:** Добавьте документы семейства FA5.


# SOURCE_FILE: A.SOI-Name/A2.SOI-Name/A2.3.Operations/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA6
system: System-of-Interest
role: Operations
---

# FA6: System-of-Interest × Менеджер

## Фокус семейства

**Вопрос:** Как работает целевая система?

Документы этого семейства описывают:
- Процессы реализации
- Операционные процедуры
- Метрики и мониторинг
- Инструкции по эксплуатации
- Workflow использования

## Типичные документы

- Операционные процедуры
- Runbooks
- Метрики и KPI
- Инструкции пользователя
- Процессы поддержки

## Шаблон документа

```yaml
---
type: process
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
kernel: A
family: FA6
system: System-of-Interest
role: Operations
---
```

## Содержимое

> **TODO:** Добавьте документы семейства FA6.


# SOURCE_FILE: A.SOI-Name/A3.Constructor-Name/A3.1.Meaning/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA7
system: Constructor
role: Meaning
---

# FA7: Constructor × Предприниматель

## Фокус семейства

**Вопрос:** Зачем существует система создания? Какие принципы?

Документы этого семейства описывают:
- Видение и миссия создателя
- Экономика создания
- Принципы работы
- Стратегия развития
- Бизнес-модель создателя

## Типичные документы

- Видение и миссия
- Бизнес-модель
- Принципы команды
- Экономика проекта
- Стратегия развития

## Шаблон документа

```yaml
---
type: doc
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
kernel: A
family: FA7
system: Constructor
role: Meaning
---
```

## Содержимое

> **TODO:** Добавьте документы семейства FA7.


# SOURCE_FILE: A.SOI-Name/A3.Constructor-Name/A3.2.Architecture/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA8
system: Constructor
role: Architecture
---

# FA8: Constructor × Инженер

## Фокус семейства

**Вопрос:** Как устроена система создания?

Документы этого семейства описывают:
- Инструменты разработки
- CI/CD и инфраструктура
- Технологический стек
- Среды разработки
- Платформа создания

## Типичные документы

- Технологический стек
- CI/CD pipeline
- Инфраструктура
- Среды (dev, staging, prod)
- Инструменты команды

## Шаблон документа

```yaml
---
type: doc
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
kernel: A
family: FA8
system: Constructor
role: Architecture
---
```

## Содержимое

> **TODO:** Добавьте документы семейства FA8.


# SOURCE_FILE: A.SOI-Name/A3.Constructor-Name/A3.3.Operations/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA9
system: Constructor
role: Operations
---

# FA9: Constructor × Менеджер

## Фокус семейства

**Вопрос:** Как работает система создания?

Документы этого семейства описывают:
- Структура команды
- Роли и ответственность
- Методология (Scrum, Kanban...)
- Ритуалы и практики
- Процессы разработки

## Типичные документы

- Структура команды
- Роли и обязанности
- Методология разработки
- Ритуалы (стендапы, ретро)
- Onboarding

## Шаблон документа

```yaml
---
type: process
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
kernel: A
family: FA9
system: Constructor
role: Operations
---
```

## Содержимое

> **TODO:** Добавьте документы семейства FA9.


# SOURCE_FILE: A.SOI-Name/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA0
---

# Ядро A: [SOI-Name] (Целевая система)

> **Для AI-агентов:** Это шаблон ядра A. При развёртывании проекта:
> 1. Переименуйте папку `A.SOI-Name` → `A.{Имя-Целевой-Системы}`
> 2. Переименуйте подпапки с реальными именами систем
> 3. Заполните этот README информацией о конкретной системе

## Описание

Ядро A всегда строится относительно **главной целевой системы** проекта — той системы, ради которой существует весь проект и которая создаёт конечную ценность.

## Целевая система ядра

| Аспект | Описание |
|--------|----------|
| **Название** | *[Укажите название целевой системы]* |
| **Суть** | *[Что это за система?]* |
| **Конечная ценность** | *[Какую ценность создаёт?]* |
| **Для кого** | *[Кто получает ценность?]* |

## Структура ядра (шаблон)

> **Важно:** Замените плейсхолдеры реальными именами систем!

```
A.{SOI-Name}/                       # ← Имя целевой системы
├── A0.{SOI-Name}-Management/       # FA0: Управление ядром
├── A1.{Suprasystem-Name}/          # ← Имя надсистемы
│   ├── A1.1.Meaning/               # FA1: Контекст, рынок
│   ├── A1.2.Architecture/          # FA2: Окружение, интерфейсы
│   └── A1.3.Operations/            # FA3: Партнёрства
├── A2.{SOI-Name}/                  # ← Имя целевой системы (SoI)
│   ├── A2.1.Meaning/               # FA4: Требования, ценность
│   ├── A2.2.Architecture/          # FA5: Архитектура
│   └── A2.3.Operations/            # FA6: Реализация
└── A3.{Constructor-Name}/          # ← Имя конструктора
    ├── A3.1.Meaning/               # FA7: Принципы
    ├── A3.2.Architecture/          # FA8: Платформа
    └── A3.3.Operations/            # FA9: Команда
```

### Пример именования (Автомобиль)

```
A.Automobile/                       # Целевая система: автомобиль
├── A0.Automobile-Management/
├── A1.Taxi/                        # Надсистема: такси (водитель + автомобиль)
│   ├── A1.1.Meaning/
│   ├── A1.2.Architecture/
│   └── A1.3.Operations/
├── A2.Automobile/                  # SoI: автомобиль
│   ├── A2.1.Meaning/
│   ├── A2.2.Architecture/
│   └── A2.3.Operations/
└── A3.Assembly-Line/               # Конструктор: конвейер (система производства)
    ├── A3.1.Meaning/
    ├── A3.2.Architecture/
    └── A3.3.Operations/
```

### Пример именования (Мобильное приложение)

```
A.Mobile-App/                       # Целевая система: мобильное приложение
├── A0.Mobile-App-Management/
├── A1.User-Smartphone/             # Надсистема: смартфон пользователя
│   ├── A1.1.Meaning/
│   ├── A1.2.Architecture/
│   └── A1.3.Operations/
├── A2.Mobile-App/                  # SoI: само приложение
│   ├── A2.1.Meaning/
│   ├── A2.2.Architecture/
│   └── A2.3.Operations/
└── A3.Dev-Team/                    # Конструктор: команда разработки
    ├── A3.1.Meaning/
    ├── A3.2.Architecture/
    └── A3.3.Operations/
```

## Три системы

### A1. Suprasystem (Надсистема)

**Вопрос:** В какую систему физически входит целевая система?

> **Важно:** Надсистема — это **физическая система**, а не контекст, процесс или область знания.
> - ✅ Правильно: Смартфон (для приложения), Такси (для автомобиля)
> - ❌ Неправильно: "Повседневная жизнь", "Рынок", "Отрасль"

*[Опишите физическую систему, в которую входит SoI]*

### A2. System-of-Interest (Целевая система)

**Вопрос:** Что мы создаём/изменяем?

*[Опишите саму целевую систему]*

### A3. Constructor (Система создания)

**Вопрос:** Кто/что создаёт целевую систему?

*[Опишите создателя — команду, процесс, платформу]*

## Позиция в цепочке ценности

```
[Конечная ценность]
       ↑
       │
A. {SOI-Name} ◄── вы здесь
       ↑
       │ создаётся
       │
B. {Our-System} (ядро B)
```

## Связи с другими ядрами

| Ядро | Тип связи | Описание |
|------|-----------|----------|
| B | создаёт / входит в состав / в окружении | *[Укажите тип связи ядра B с целевой системой]* |

## Владелец ядра

**Владелец:** *[@username]*

## Как использовать этот шаблон (для AI)

1. Получите от пользователя описание целевой системы
2. Определите имя целевой системы (для A2)
3. Определите имя надсистемы (для A1) — в чём существует целевая система?
4. Определите имя конструктора (для A3) — кто создаёт целевую систему?
5. Переименуйте папки с реальными именами
6. Заполните этот README конкретной информацией
7. Обновите карту систем: `0.OPS/0.1.Knowledge-Logic/03-our-systems-map.md`

## См. также

- [../0.OPS/0.1.Knowledge-Logic/01-kernels-model.md](../0.OPS/0.1.Knowledge-Logic/01-kernels-model.md) — модель ядер
- [../0.OPS/0.2.Kernels-Bridge/01-value-chain.md](../0.OPS/0.2.Kernels-Bridge/01-value-chain.md) — цепочка ценности


# SOURCE_FILE: B.Our-System-Name/B0.Our-System-Name-Management/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB0
---

# B0. Kernel Management

Управление ядром B (опционально).

## Содержимое

| Документ | Описание |
|----------|----------|
| [local-ontology.md](local-ontology.md) | Локальная онтология ядра |

## Когда нужен этот раздел

- Есть специфичная терминология ядра B
- Нужны локальные определения
- Есть отдельная команда со своими процессами

## Ответственные за семейства

> **TODO:** Заполните при необходимости.

| Семейство | Ответственный |
|-----------|---------------|
| FB1-FB3 | *[@username]* |
| FB4-FB6 | *[@username]* |
| FB7-FB9 | *[@username]* |


# SOURCE_FILE: B.Our-System-Name/B1.Suprasystem-Name/B1.1.Meaning/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB1
system: Suprasystem
role: Meaning
---

# FB1: Suprasystem × Предприниматель

## Фокус семейства

**Вопрос:** Зачем наша система существует в своём контексте?

Документы описывают контекст и смысл существования нашей системы.

## Содержимое

> **TODO:** Добавьте документы семейства FB1.


# SOURCE_FILE: B.Our-System-Name/B1.Suprasystem-Name/B1.2.Architecture/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB2
system: Suprasystem
role: Architecture
---

# FB2: Suprasystem × Инженер

## Фокус семейства

**Вопрос:** Как устроено окружение нашей системы?

Документы описывают внешние системы и интерфейсы.

## Содержимое

> **TODO:** Добавьте документы семейства FB2.


# SOURCE_FILE: B.Our-System-Name/B1.Suprasystem-Name/B1.3.Operations/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB3
system: Suprasystem
role: Operations
---

# FB3: Suprasystem × Менеджер

## Фокус семейства

**Вопрос:** Как наша система взаимодействует с окружением?

Документы описывают партнёрства и взаимодействия.

## Содержимое

> **TODO:** Добавьте документы семейства FB3.


# SOURCE_FILE: B.Our-System-Name/B2.Our-System-Name/B2.1.Meaning/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB4
system: System-of-Interest
role: Meaning
---

# FB4: System-of-Interest × Предприниматель

## Фокус семейства

**Вопрос:** Зачем нужна наша система? Какую ценность создаёт?

Документы описывают требования и ценность нашей системы.

## Содержимое

> **TODO:** Добавьте документы семейства FB4.


# SOURCE_FILE: B.Our-System-Name/B2.Our-System-Name/B2.2.Architecture/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB5
system: System-of-Interest
role: Architecture
---

# FB5: System-of-Interest × Инженер

## Фокус семейства

**Вопрос:** Как устроена наша система?

Документы описывают архитектуру нашей системы.

## Содержимое

> **TODO:** Добавьте документы семейства FB5.


# SOURCE_FILE: B.Our-System-Name/B2.Our-System-Name/B2.3.Operations/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB6
system: System-of-Interest
role: Operations
---

# FB6: System-of-Interest × Менеджер

## Фокус семейства

**Вопрос:** Как работает наша система?

Документы описывают операции и процессы.

## Содержимое

> **TODO:** Добавьте документы семейства FB6.


# SOURCE_FILE: B.Our-System-Name/B3.Constructor-Name/B3.1.Meaning/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB7
system: Constructor
role: Meaning
---

# FB7: Constructor × Предприниматель

## Фокус семейства

**Вопрос:** Зачем существует создатель нашей системы?

Документы описывают принципы и видение создателя.

## Содержимое

> **TODO:** Добавьте документы семейства FB7.


# SOURCE_FILE: B.Our-System-Name/B3.Constructor-Name/B3.2.Architecture/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB8
system: Constructor
role: Architecture
---

# FB8: Constructor × Инженер

## Фокус семейства

**Вопрос:** Как устроена система создания?

Документы описывают инструменты и платформу.

## Содержимое

> **TODO:** Добавьте документы семейства FB8.


# SOURCE_FILE: B.Our-System-Name/B3.Constructor-Name/B3.3.Operations/README.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB9
system: Constructor
role: Operations
---

# FB9: Constructor × Менеджер

## Фокус семейства

**Вопрос:** Как работает система создания?

Документы описывают команду и методологию.

## Содержимое

> **TODO:** Добавьте документы семейства FB9.


# SOURCE_FILE: B.Our-System-Name/README.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB0
---

# Ядро B: [Our-System-Name] (Наша система-1)

> **Для AI-агентов:** Это шаблон ядра B. При развёртывании проекта:
> 1. Скопируйте эту папку для каждой "нашей системы"
> 2. Переименуйте папку `B.Our-System-Name` → `B.{Имя-Системы}`
> 3. Переименуйте подпапки с реальными именами систем
> 4. Заполните этот README информацией о конкретной системе

## Описание

Ядро B — это шаблон для описания **"нашей системы-1"**: системы, за которую мы отвечаем и которая участвует в создании или является частью целевой системы (Ядро A).

## Целевая система ядра

| Аспект | Описание |
|--------|----------|
| **Название** | *[Укажите название вашей системы-1]* |
| **Тип** | *[Подсистема целевой / Часть цепочки создания]* |
| **Суть** | *[Что это за система?]* |
| **Роль в проекте** | *[Как связана с целевой системой A?]* |

## Структура ядра

```
B.Our-System-Name/                       # Наша система-1 (шаблон)
├── README.md                            # Этот файл
├── B0.Our-System-Name-Management/       # FB0: Управление ядром
│   ├── README.md
│   └── local-ontology.md
├── B1.Suprasystem-Name/                 # Надсистема для нашей системы-1
│   ├── B1.1.Meaning/                    # FB1
│   │   └── README.md
│   ├── B1.2.Architecture/               # FB2
│   │   └── README.md
│   └── B1.3.Operations/                 # FB3
│       └── README.md
├── B2.Our-System-Name/                  # Наша система-1 (SoI)
│   ├── B2.1.Meaning/                    # FB4
│   │   └── README.md
│   ├── B2.2.Architecture/               # FB5
│   │   └── README.md
│   └── B2.3.Operations/                 # FB6
│       └── README.md
└── B3.Constructor-Name/                 # Система создания нашей системы-1
    ├── B3.1.Meaning/                    # FB7
    │   └── README.md
    ├── B3.2.Architecture/               # FB8
    │   └── README.md
    └── B3.3.Operations/                 # FB9
        └── README.md
```

### Пример именования (после заполнения)

```
B.Mobile-App/                            # Наша система-1: мобильное приложение
├── B0.Mobile-App-Management/
├── B1.Organizer-Context/                # Надсистема для нашей системы-1
│   ├── B1.1.Meaning/
│   ├── B1.2.Architecture/
│   └── B1.3.Operations/
├── B2.Mobile-App/                       # Наша система-1 (SoI)
│   ├── B2.1.Meaning/
│   ├── B2.2.Architecture/
│   └── B2.3.Operations/
└── B3.Dev-Team/                         # Конструктор: команда разработки
    ├── B3.1.Meaning/
    ├── B3.2.Architecture/
    └── B3.3.Operations/
```

## Три системы ядра B

### B1. Suprasystem (Надсистема для нашей системы-1)

**Вопрос:** В чём существует наша система-1?

*[Опишите контекст, в котором работает ваша система. Это может быть целевая система A или другой контекст.]*

### B2. System-of-Interest (Наша система-1)

**Вопрос:** Что представляет собой наша система-1?

*[Опишите вашу систему — её суть, границы, ключевые характеристики.]*

### B3. Constructor (Система создания нашей системы-1)

**Вопрос:** Кто создаёт нашу систему-1?

*[Опишите команду или процесс, создающий эту систему.]*

## Позиция в цепочке ценности

```
A. {Target-System}
       ↑
       │ создаёт / входит в состав / в окружении
       │
B. {Our-System-1} ◄── вы здесь
       ↑
       │ создаётся
       │
[команда/процесс]
```

## Связи с другими ядрами

| Ядро | Тип связи | Описание |
|------|-----------|----------|
| A | создаёт / входит в состав / в окружении | *[Укажите тип связи B с A]* |
| C | создаёт / входит в состав / в окружении | *[Если есть другие ядра]* |

## Владелец ядра

**Владелец:** *[@username]*

## Как использовать этот шаблон (для AI)

1. Определите "нашу систему-1" — за что отвечает команда?
2. Определите имя системы (для B2)
3. Определите надсистему (для B1) — в чём существует эта система?
4. Определите конструктора (для B3) — кто создаёт эту систему?
5. Переименуйте папки с реальными именами
6. Заполните этот README конкретной информацией
7. Для дополнительных систем (C, D...) — копируйте эту структуру

### Создание ядер C, D и далее

При копировании:
1. Замените "B" на новую букву (C, D...)
2. Замените "Our-System-Name" на имя конкретной системы
3. Замените "Наша система-1" на "Наша система-2", "Наша система-3" и т.д.

### Когда создавать новое ядро?

Создавай новое ядро, если:
- [ ] Есть отдельная команда, отвечающая за систему
- [ ] Система имеет свой жизненный цикл
- [ ] Нужна отдельная документация по 9 семействам
- [ ] Система достаточно сложна для детального описания

### Когда НЕ создавать ядро?

Не создавай ядро, если:
- Это просто модуль/компонент внутри существующей системы
- Достаточно описания в FX5 (Architecture) родительского ядра
- Нет отдельной команды или ответственного

## См. также

- [../0.OPS/0.1.Knowledge-Logic/01-kernels-model.md](../0.OPS/0.1.Knowledge-Logic/01-kernels-model.md) — модель ядер
- [../0.OPS/0.2.Kernels-Bridge/01-value-chain.md](../0.OPS/0.2.Kernels-Bridge/01-value-chain.md) — цепочка ценности
- [../0.OPS/0.1.Knowledge-Logic/03-our-systems-map.md](../0.OPS/0.1.Knowledge-Logic/03-our-systems-map.md) — карта систем
- [../A.SOI-Name/README.md](../A.SOI-Name/README.md) — ядро A


# SOURCE_FILE: README.md
---
# S2R Template

> **Тип репозитория:** `Format`

> **Для AI-агентов:** Этот репозиторий — **промпт-шаблон** для создания проектных хранилищ. Используйте документы из `0.OPS/` как инструкции для развёртывания структуры под конкретный проект пользователя.

SRR (Systems–Roles Repository): a multi-kernel systems×roles (3×3) project repository template aligned with FPF

**S2R** — имя метода.
**SRR** — его формальная расшифровка: Systems–Roles Repository (Хранилище систем и ролей).
Этот репозиторий — **шаблон (Template)** структуры SRR с поддержкой **множества ядер**.

> **S2R Template** — шаблон репозитория для **SRR**: хранилища проекта по матрице *Системы × Роли* (3×3) с опорой на FPF и поддержкой графа создателей.

---

## Позиционирование в экосистеме

S2R — это **Format** (протокол оформления), а не Pack или Framework.

### Upstream (зависимости)

| Репозиторий | Тип | Что берём |
|-------------|-----|-----------|
| [FPF](https://github.com/ailev/FPF) | Framework | Мета-онтология, базовые различения |
| [SPF](https://github.com/TserenTserenov/SPF) | Framework | Принципы организации знаний |

### Downstream (кто использует S2R)

| Репозиторий | Тип | Как использует |
|-------------|-----|----------------|
| [ecosystem-development](https://github.com/aisystant/ecosystem-development) | Downstream/governance | Инстанс S2R для экосистемы Aisystant |

### Роль S2R

```
FPF (Level 1)  →  мета-онтология
       ↓
SPF (Level 2)  →  форма + процесс для Pack
       ↓
S2R (Format)   →  структура downstream-репозиториев  ← ВЫ ЗДЕСЬ
       ↓
ecosystem-development  →  конкретный инстанс S2R
```

| S2R — это | S2R — это НЕ |
|-----------|--------------|
| Протокол структуры репозиториев | Pack (source-of-truth области) |
| Матрица 3×3 (системы × роли) | Содержание предметной области |
| Шаблон для governance-репозиториев | Процесс создания знаний |

---

## Назначение для AI

Этот репозиторий предназначен для использования **AI-агентами** (Claude Code, GPT и др.) как **инструкция для создания** проектных хранилищ:

1. **Изучите документы** в `0.OPS/0.1.Knowledge-Logic/` — это модель знаний
2. **Получите от пользователя** описание его проекта
3. **Создайте структуру** на основе шаблонов, заменяя плейсхолдеры реальными именами систем
4. **Заполните документы** согласно правилам именования

### Ключевые документы для AI

| Документ | Назначение |
|----------|------------|
| [01-kernels-model.md](0.OPS/0.1.Knowledge-Logic/01-kernels-model.md) | Как создавать ядра, правила именования |
| [02-document-families.md](0.OPS/0.1.Knowledge-Logic/02-document-families.md) | 9 семейств документов F1-F9 |
| [03-our-systems-map.md](0.OPS/0.1.Knowledge-Logic/03-our-systems-map.md) | Карта систем проекта |
| [04-ontology.md](0.OPS/0.1.Knowledge-Logic/04-ontology.md) | Общая онтология и запреты |
| [05-glossary.md](0.OPS/0.1.Knowledge-Logic/05-glossary.md) | Глоссарий терминов |
| [08-anti-patterns.md](0.OPS/0.1.Knowledge-Logic/08-anti-patterns.md) | Анти-паттерны (типичные ошибки) |
| [09-examples-library.md](0.OPS/0.1.Knowledge-Logic/09-examples-library.md) | Библиотека примеров для AI |
| [01-value-chain.md](0.OPS/0.2.Kernels-Bridge/01-value-chain.md) | Цепочка создания ценности |
| [roles-matrix.md](0.OPS/0.3.Roles-Matrix-3x3/roles-matrix.md) | Матрица ролей 3×3 |
| [fpf-integration.md](0.OPS/0.4.FPF-Integration/fpf-integration.md) | Интеграция с FPF |

---

## Ключевые концепции

### Ядра (Kernels)

**Ядро** — это полная системная перспектива относительно одной целевой системы (или "нашей системы"). Каждое ядро разворачивает свои 9 семейств документов (F1-F9).

- **Ядро A** — всегда относительно **главной целевой системы** проекта
- **Ядра B, C, D...** — относительно **"наших систем"**

> **Важно:** Папки ядер именуются по **имени целевой иили нашей системы**, а не абстрактно. Например: `A.Automobile/`, а не `A.Target-System/`.

### "Наши системы" (Our Systems)

"Наши системы" могут быть:
- **Подсистемами целевой системы** — компоненты, входящие в целевую систему
- **Частями цепочки создания** — системы, которые создают целевую систему (включая поддержку, ремонт, модернизацию) и которые образуют граф создателей.

### Граф создателей

Системы связаны через **цепочку создания ценности**. Каждая команда работает со своим ядром, и ядра связаны между собой.

**Пример: Автомобильное производство**

```
                           [Такси]
                    (Водитель + Автомобиль)
                    Надсистема целевой системы
                                  ↑
                                  │ входит
                                  │
┌─────────────────────────────────────────────────────────────────────┐
│                       A. Автомобиль/                                │
│                   Целевая система проекта                          │
└─────────────────────────────────────────────────────────────────────┘
            ↑ создаёт                        ↑ входит как часть
            │                                │
┌───────────────────────────┐   ┌───────────────────────────┐
│      C. Конвейер/         │   │      B. Мотор/            │
│  "Наша система" команды-2 │   │  "Наша система" команды-1 │
└───────────────────────────┘   └───────────────────────────┘
            ↑
    ┌───────┴───────┐
    ↓               ↓
┌───────────────┐   ┌───────────────────────┐
│ D. Станок-    │   │    E. Команда-2/      │
│    ЧПУ/       │   │ "Наша система" ком.-4 │
│ "Наша сист."  │   │                       │
│  команды-3    │   │                       │
└───────────────┘   └───────────────────────┘
```

**Ключевые особенности:**

| Команда | Ядро | "Наша система" | Пояснение |
|---------|------|----------------|-----------|
| Команда-1 | B | Мотор | подсистема целевой системы |
| Команда-2 | C | Конвейер | система создания целевой системы |
| Команда-3 | D | Станок ЧПУ | подсистема системы создания ЦС |
| Команда-4 | E | Команда-2 | система создания системы создания ЦС |

> **Важно:** Разные команды работают с разными ядрами. Для успешной работы необходимо:
> - **Техническая интеграция** — согласование интерфейсов между системами
> - **Согласование онтологий** — одинаковые термины могут означать разное в разных ядрах
> - **Коммуникация** — регулярная синхронизация между командами
>
> Подробнее: [01-kernels-model.md](0.OPS/0.1.Knowledge-Logic/01-kernels-model.md) → раздел "Развёрнутый пример"

### Правило именования папок

```
Хорошо (на примере автомобиля):
A.Автомобиль/                   # Имя целевой системы
├── A1.Такси/                   # Имя надсистемы (Водитель+Автомобиль)
├── A2.Автомобиль/              # Имя SoI
└── A3.Конвейер/                # Имя системы создания

B.Мотор/                        # Ядро для подсистемы
├── B1.Автомобиль/              # Надсистема мотора
├── B2.Мотор/                   # SoI
└── B3.Моторный-цех/            # Система создания мотора

Плохо:
A.Target-System/                # Абстрактно, нет названия системы
├── A1.Suprasystem/             # Это роль, не имя
├── A2.System-of-Interest/      # Это роль, не имя
└── A3.Constructor/             # Это роль, не имя
```

## Матрица 3×3 внутри каждого ядра

Каждое ядро (A, B, C...) содержит 9 семейств документов:

### Краткая матрица: ключевые слова

| Уровень \ Роль | Предприниматель (X.1) | Инженер (X.2) | Менеджер (X.3) |
|----------------|----------------------|---------------|----------------|
| **1.X. Надсистема** | **Спрос / Оффер** | **Сценарии / Прототип** | **Доверие / Репутация** |
| **2.X. Целевая система** | **Смысл / Границы** | **Архитектура / Интерфейсы** | **SLO / Incidents** |
| **3.X. Система создания** | **Стратегия / Инвестиции** | **CI/CD / Quality** | **Ресурсы / Регламенты** |

### Матрица ролей

| Уровень \ Роль | Предприниматель (X.1) | Инженер (X.2) | Менеджер (X.3) |
|----------------|----------------------|---------------|----------------|
| **1.X. Надсистема** | FX1: Продвиженец | FX2: Владелец продукта | FX3: PR/GR |
| **2.X. Целевая система** | FX4: Визионер ЦС | FX5: Инженер ЦС | FX6: Оператор ЦС |
| **3.X. Система создания** | FX7: Бизнесмен | FX8: Организатор разработки | FX9: Администратор |

> **Полное описание ролей с методами и метриками:** [roles-matrix.md](0.OPS/0.3.Roles-Matrix-3x3/roles-matrix.md)
>
> **Краткая версия:** [roles-matrix-brief.md](0.OPS/0.3.Roles-Matrix-3x3/roles-matrix-brief.md)

## F0 (0.OPS): Метаэпистема хранилища

**F0** — метаэпистема, управляющая знаниями о знаниях в хранилище.

> **Почему OPS?** OPS — коротко, стандартно, прямо означает "операционная логика и порядок работы". Туда естественно ложатся inbox/archive как операционные корзины.

F0 отвечает за:
- Общую онтологию для всех ядер
- Связи и мосты между ядрами
- Стандарты и процессы
- Интеграцию с FPF

Каждое ядро может иметь своё **FX0** (Kernel Management) с локальной онтологией.

---

## Структура репозитория

```
s2r/
├── 0.OPS/         # F0: Метаэпистема хранилища
│   ├── 0.1.Knowledge-Logic/         # Онтология, модель ядер
│   │   ├── README.md
│   │   ├── 01-kernels-model.md      # ⭐ Модель ядер
│   │   ├── 02-document-families.md  # ⭐ Семейства F1-F9
│   │   ├── 03-our-systems-map.md    # ⭐ Карта систем
│   │   ├── 04-ontology.md
│   │   ├── 05-glossary.md
│   │   ├── 06-taxonomy.md
│   │   ├── 07-naming.md             # ⭐ Правила именования
│   │   ├── 08-anti-patterns.md      # ⭐ Анти-паттерны (типичные ошибки)
│   │   └── 09-examples-library.md   # ⭐ Библиотека примеров для AI
│   ├── 0.2.Kernels-Bridge/          # Связи между ядрами
│   │   ├── README.md
│   │   ├── 01-value-chain.md        # ⭐ Цепочка ценности
│   │   ├── 02-kernels-relations.md  # Матрица связей
│   │   └── 03-systems-relations.md  # Структура связанности систем
│   ├── 0.3.Roles-Matrix-3x3/        # ⭐ Матрица ролей 3×3
│   │   ├── roles-matrix.md          # Полная версия
│   │   └── roles-matrix-brief.md    # Краткая версия
│   ├── 0.4.FPF-Integration/         # ⭐ Интеграция с FPF
│   │   ├── fpf/                     # Копия FPF-Spec
│   │   ├── fpf-integration.md
│   │   └── fpf-patterns-map.md
│   ├── 0.5.AI-Reports/              # AI-проверки и отчёты
│   │   ├── Validation-Specs/        # ТЗ на проверки
│   │   └── Validation-Results/      # Результаты проверок
│   ├── 0.6.Repository-Processes/    # Стандарты, процессы
│   │   ├── README.md
│   │   ├── 01-project-description-template.md  # ⭐ Шаблон описания проекта
│   │   ├── 02-standards.md          # Стандарты оформления
│   │   ├── 03-structure.md          # Структура репозитория
│   │   ├── 04-document-creation.md  # Создание документов
│   │   ├── 05-frontmatter-spec.md   # Спецификация метаданных
│   │   ├── 06-workflows.md          # Рабочие процессы
│   │   ├── 07-roles.md              # Роли и ответственность
│   │   └── 08-deployment-guide.md   # ⭐ Руководство по развёртыванию
│   ├── 0.7.Plans-and-Meetings/      # Планирование
│   ├── 0.9.Inbox/                   # Входящие идеи
│   └── 0.99.Archive/                # Архив
│
├── A.SOI-Name/                      # Ядро A: ШАБЛОН (переименовать!)
│   ├── A0.SOI-Name-Management/      # FA0: Управление ядром
│   ├── A1.Suprasystem-Name/         # Надсистема (переименовать!)
│   │   ├── A1.1.Meaning/            # FA1
│   │   ├── A1.2.Architecture/       # FA2
│   │   └── A1.3.Operations/         # FA3
│   ├── A2.SOI-Name/                 # Целевая система (переименовать!)
│   │   ├── A2.1.Meaning/            # FA4
│   │   ├── A2.2.Architecture/       # FA5
│   │   └── A2.3.Operations/         # FA6
│   └── A3.Constructor-Name/         # Система создания (переименовать!)
│       ├── A3.1.Meaning/            # FA7
│       ├── A3.2.Architecture/       # FA8
│       └── A3.3.Operations/         # FA9
│
├── B.Our-System-Name/               # Ядро B: ШАБЛОН (переименовать!)
│   └── ... (аналогичная структура)
│
├── CLAUDE.md                        # ⭐ Инструкции для AI
├── README.md                        # Этот файл
└── CONTRIBUTING.md                  # Правила участия
```

---

## Быстрый старт (для людей)

> ⭐ **Полное руководство по развёртыванию:** [08-deployment-guide.md](0.OPS/0.6.Repository-Processes/08-deployment-guide.md)

### Шаг 0: Подключите Claude Code

Для эффективной работы с хранилищем рекомендуется использовать **Claude Code**:

```bash
# Клонируйте репозиторий
git clone https://github.com/TserenTserenov/s2r.git my-project
cd my-project
rm -rf .git && git init

# Запустите Claude Code
claude
```

Claude Code автоматически прочитает `CLAUDE.md` и поможет с развёртыванием.

### Шаг 1: Опишите проект

Заполните [01-project-description-template.md](0.OPS/0.6.Repository-Processes/01-project-description-template.md) — это поможет определить системы.

### Шаг 2: Переименуйте папки ядер

> **Важно:** X1 (надсистема) — это **физическая система**, не контекст или процесс!

```bash
# Пример для автомобиля
mv A.SOI-Name A.Automobile
mv A.Automobile/A1.Suprasystem-Name A.Automobile/A1.Taxi
mv A.Automobile/A2.SOI-Name A.Automobile/A2.Automobile
mv A.Automobile/A3.Constructor-Name A.Automobile/A3.Assembly-Line
```

### Шаг 3: Обновите связи

- Заполните `0.1.Knowledge-Logic/03-our-systems-map.md`
- Заполните `0.2.Kernels-Bridge/01-value-chain.md`

### Что оставить без изменений

| Папка/Файл | Действие |
|------------|----------|
| `0.3.Roles-Matrix-3x3/` | ✅ Оставить (методология) |
| `0.4.FPF-Integration/` | ✅ Оставить (методология) |
| `CLAUDE.md` | ✅ Оставить (инструкции для AI) |
| `0.1.Knowledge-Logic/01-09` | ✅ Оставить (методология) |

### Что заполнить

| Файл | Действие |
|------|----------|
| `0.1/03-our-systems-map.md` | 📝 Заполнить картой систем |
| `0.2/01-value-chain.md` | 📝 Заполнить цепочкой ценности |
| `0.6/01-project-description-template.md` | 📝 Заполнить описанием проекта |

### Что переименовать

| Папка | Действие |
|-------|----------|
| `A.SOI-Name/` | ✏️ Переименовать в `A.{Ваша-Система}/` |
| `B.Our-System-Name/` | ✏️ Переименовать или удалить |
| Подпапки `A1`, `A2`, `A3` | ✏️ Переименовать с именами систем |

---

## Быстрый старт (для AI)

При развёртывании репозитория для пользователя:

1. **Запросите описание проекта** — что создаёт пользователь?
2. **Определите целевую систему** — что является "A"?
3. **Определите "наши системы"** — что является "B", "C"?
4. **Постройте цепочку ценности** — кто кого создаёт?
5. **Переименуйте папки** — используя имена систем
6. **Заполните шаблоны** — README, карта систем, value-chain

Смотрите инструкции в [CLAUDE.md](CLAUDE.md).

---

## Для кого этот шаблон

- **Проектные команды** — организация знаний о сложных системах
- **Стартапы** — структурирование знаний о продукте
- **Корпорации** — управление знаниями с множеством подсистем и команд
- **Разработчики** — документация архитектуры и процессов
- **AI-агенты** — промпт для создания проектных хранилищ

## Чем S2R НЕ является

- Это **не процесс разработки** и не "жизненный цикл проекта"
- Это **схема организации знаний** + операционная дисциплина
- Это **не замена архитектурным фреймворкам**, а способ организовать их результаты

---

## S2R в архитектуре знаний

S2R — это методология **организации репозиториев** (измерение "Форма"), а не уровень знаний.

### Три ортогональных измерения

| Измерение | Что определяет | Кто определяет |
|-----------|----------------|----------------|
| Содержание | Терминология, понятия | FPF → SPF |
| **Форма** | Структура репозитория | **S2R** |
| Процесс | Как производить знания | SPF |

### S2R определяет

- Структуру ядер (A/B/C/D...)
- Матрицу 3×3 (система × роль)
- Семейства документов (F1-F9)
- Правила именования и навигации

### S2R НЕ определяет

- Что является знанием (это FPF/SPF)
- Как производить знания (это SPF)
- Какие термины использовать (это FPF)

### S2R и Pack: различение формы и содержания

S2R организует **проектные документы**. Pack хранит **доменное знание** (source-of-truth).

Документ в ячейке S2R (например, FA5 — архитектура целевой системы) — это **проектный артефакт**, который:
- **описывает** конкретную систему этого проекта
- **ссылается на** один или несколько Pack'ов как источники доменного знания
- **использует** универсальные компетенции (инженерия, менеджмент) из образования

S2R-документ — downstream по отношению к Pack. Pack — source-of-truth.

**Один объект — много предметных областей.** Один и тот же объект (автомобиль, ИТ-система, человек) может появляться в разных ячейках S2R и в разных Pack'ах под разными именами — потому что в разных bounded context'ах он описан с разным словарём и разными различениями. Это не дублирование, а разные модели одной реальности.

| Пример | В одном Pack | В другом Pack | Почему разные |
|--------|-------------|--------------|---------------|
| Автомобиль | «Транспортное средство» (логистика) | «Предмет роскоши» (luxury) | Разные характеристики важны |
| Человек | «Созидатель» (личное развитие) | «Пользователь» (ИТ-платформа) | Разные объекты внимания |
| ИТ-система | «Платформа» (архитектура) | «Среда мастерской» (методика) | Разные bounded context'ы |

### Место S2R в иерархии

```
FPF (Level 1)  →  мета-онтология, различения
 ├──▶ SPF (Level 2)  →  форма + процесс → Pack (source-of-truth знания)
 │                                            │
 └──▶ S2R (Format)   →  структура проектных   │
       документов                              │
       │                                       │
       └── S2R-документы ССЫЛАЮТСЯ на ─────────┘
```

SPF и S2R — **параллельные downstream от FPF**, работающие в разных измерениях. SPF про знание (содержание), S2R про организацию документов (форма). Они встречаются, когда проектный документ (S2R) ссылается на доменное знание (Pack).

---

## Терминология

| Термин | Описание |
|--------|----------|
| **S2R** | Имя метода (бренд) |
| **SRR** | Systems–Roles Repository (формальная расшифровка) |
| **Kernel (Ядро)** | Системная перспектива с 9 семействами |
| **Our System** | Наша система — за которую мы отвечаем |
| **F0-F9** | Семейства документов |
| **FPF** | First Principles Framework — эпистемологический фундамент |

---

## Ссылки

- **Введение в системное мышление:** [docs.system-school.ru](https://docs.system-school.ru/ru/personal/systems-thinking-introduction/preface)
- **FPF:** [github.com/ailev/FPF](https://github.com/ailev/FPF)
- [CLAUDE.md](CLAUDE.md) — инструкции для работы с Claude Code
- [CONTRIBUTING.md](CONTRIBUTING.md) — правила участия

---

## Лицензия

MIT License — используйте свободно для своих проектов.


# SOURCE_FILE: 0.OPS/0.1.Knowledge-Logic/01-kernels-model.md
---
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
fpf_patterns:
  - A.1
  - A.1.1
  - A.3
---

# Модель ядер (Kernels Model)

> **Для AI-агентов:** Этот документ — спецификация для создания структуры ядер в конкретном проекте. Используйте его как руководство при развёртывании репозитория.

## Что такое ядро?

**Ядро (Kernel)** — это полная системная перспектива относительно одной целевой системы. Каждое ядро разворачивает свои 9 семейств документов (FX1-FX9) относительно своей целевой системы.

### Холоническая природа ядра (FPF A.1)

Ядро — это **холон**:
- **Как целое:** содержит 9 семейств + управление
- **Как часть:** входит в репозиторий наряду с другими ядрами

```
Репозиторий (холон)
├── Ядро A (холон)
│   ├── Семейство FA1 (холон)
│   │   └── Документы (холоны)
│   └── ...
├── Ядро B (холон)
└── ...
```

## Типы ядер

### Ядро A — Главная целевая система

**Ядро A всегда строится относительно главной целевой системы проекта.**

Это система, ради которой существует весь проект. Она определяет конечную ценность для пользователей/клиентов. Все остальные ядра (B, C, D...) существуют для поддержки ядра A.

**Именование:** `A.{SOI-Name}/`

### Ядра B, C, D... — "Наши системы"

**Последующие ядра строятся относительно "наших систем".**

"Наши системы" — это системы, за которые отвечает команда проекта и которые:
- Являются подсистемами целевой системы (Ядро A)
- Являются частями цепочки создания

**Именование:** `{Letter}.{System-Name}/`

## Позиции "наших систем"

### Подсистема целевой системы

Система, которая является **частью** целевой системы (Ядро A).

```
A.Customer-Success/          # Целевая система
├── A2.SOI = Успешный клиент
│   └── Подсистемы:
│       ├── B.Mobile-App/    # Ядро B — приложение клиента
│       └── C.Web-Portal/    # Ядро C — веб-портал
```

### Часть цепочки создания

Система, которая **создаёт или поддерживает** целевую систему.

```
A.Customer-Success/          # Целевая система
└── A3.Constructor = Продуктовая команда
    └── Части цепочки:
        ├── D.Backend-API/   # Ядро D — бэкенд
        ├── E.DevOps/        # Ядро E — DevOps-платформа
        └── F.Support/       # Ядро F — служба поддержки
```

## Развёрнутый пример: Автомобильное производство

Рассмотрим пример, демонстрирующий как разные команды работают с разными ядрами в одном проекте.

### Исходная ситуация

**Целевая система проекта** — автомобиль (готовый к продаже).

Четыре команды работают над проектом, и у каждой **своя "наша система"**:

| Команда | "Наша система" | Позиция в проекте |
|---------|----------------|-------------------|
| Команда-1 | Мотор | Подсистема целевой системы (часть автомобиля) |
| Команда-2 | Конвейер | Часть цепочки создания (создаёт автомобиль) |
| Команда-3 | Станок ЧПУ | Часть цепочки создания (часть конвейера) |
| Команда-4 | Команда-2 | Мета-уровень (развивает команду конвейера) |

### Структура ядер

```
                    [Довольный владелец автомобиля]
                                  ↑
                                  │
┌─────────────────────────────────────────────────────────────────────┐
│                        A. Automobile/                               │
│  A1: Owner-Life-Context    — жизнь владельца                       │
│  A2: Automobile            — автомобиль (целевая система)           │
│  A3: Manufacturing-System  — система производства                   │
│                                                                     │
│  🎯 Команда-1 работает здесь: мотор как подсистема A2              │
└─────────────────────────────────────────────────────────────────────┘
                                  ↑
            ┌─────────────────────┴─────────────────────┐
            ↓                                           ↓
┌───────────────────────────┐           ┌───────────────────────────┐
│      B. Engine/           │           │     C. Assembly-Line/     │
│  "Наша система" команды-1 │           │  "Наша система" команды-2 │
│                           │           │                           │
│  B1: Automobile-Context   │           │  C1: Factory-Context      │
│  B2: Engine               │           │  C2: Assembly-Line        │
│  B3: Engine-Dev-Team      │           │  C3: Line-Engineering     │
└───────────────────────────┘           └───────────────────────────┘
                                                      ↑
                                        ┌─────────────┴─────────────┐
                                        ↓                           ↓
                            ┌───────────────────────┐   ┌───────────────────────┐
                            │    D. CNC-Machine/    │   │    E. Team-2/         │
                            │ "Наша система" ком.-3 │   │ "Наша система" ком.-4 │
                            │                       │   │                       │
                            │ D1: Line-Context      │   │ E1: Org-Context       │
                            │ D2: CNC-Machine       │   │ E2: Team-2            │
                            │ D3: CNC-Dev-Team      │   │ E3: HR-and-L&D        │
                            └───────────────────────┘   └───────────────────────┘
```

### Ключевые особенности

#### 1. Каждая команда — своё ядро

Каждая команда видит проект **со своей перспективы**:

| Команда | Ядро | Что является целевой системой (X2) |
|---------|------|-------------------------------------|
| Команда-1 | B | Мотор — подсистема автомобиля (целевая система) |
| Команда-2 | C | Конвейер — то, что они развивают |
| Команда-3 | D | Станок ЧПУ — то, за что они отвечают |
| Команда-4 | E | Команда-2 — их фокус |

#### 2. Разная глубина вложенности

- **Ядро A** — уровень 1 (целевая система проекта)
- **Ядра B, C** — уровень 2 (непосредственно создают/входят в A)
- **Ядра D, E** — уровень 3 (создают/поддерживают уровень 2)

#### 3. Необходимость связей между ядрами

Поскольку команды работают над связанными системами, необходимо:

**Техническая интеграция:**
- Интерфейс мотора (B) должен соответствовать требованиям автомобиля (A)
- Конвейер (C) должен уметь устанавливать мотор (B)
- Станок ЧПУ (D) должен производить детали для конвейера (C)

**Организационная координация:**
- Команда-4 (E) развивает команду-2 (C3), влияя на конвейер (C2)
- Изменения в моторе (B) требуют согласования с конвейером (C)

#### 4. Согласование онтологий (FPF A.1.1)

> **Критически важно:** Разные команды могут использовать разные термины для одних концепций.

| Термин | Команда-1 (B) | Команда-2 (C) | Общая онтология |
|--------|---------------|---------------|-----------------|
| "Узел" | Сборка мотора | Секция конвейера | ⚠️ Разные значения! |
| "Цикл" | Цикл работы двигателя | Цикл сборки | ⚠️ Разные значения! |

**Решение:**
1. Каждое ядро имеет `X0.Management/local-ontology.md` со своими терминами
2. Общая онтология в `0.OPS/0.1.Knowledge-Logic/04-ontology.md`
3. При коммуникации между ядрами — явно указывать контекст

#### 5. Коммуникация между командами

Для успешной работы проекта команды должны:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    КОММУНИКАЦИОННАЯ МАТРИЦА                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Команда-1 (B) ←→ Команда-2 (C)                                    │
│  • Согласование интерфейса установки мотора                        │
│  • Требования к точности позиционирования                          │
│                                                                     │
│  Команда-2 (C) ←→ Команда-3 (D)                                    │
│  • Спецификации деталей для станка                                 │
│  • График производства и мощности                                  │
│                                                                     │
│  Команда-2 (C) ←→ Команда-4 (E)                                    │
│  • Планы развития компетенций                                      │
│  • Обратная связь по узким местам                                  │
│                                                                     │
│  Все команды → 0.OPS/                                              │
│  • Согласование общей терминологии                                 │
│  • Обновление карты систем                                         │
│  • Синхронизация цепочки ценности                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Вывод из примера

1. **Ядро = перспектива команды** — каждая команда работает со своим ядром
2. **Связи обязательны** — ядра не изолированы, их связи описаны в `0.2.Kernels-Bridge/`
3. **Онтология требует согласования** — команды должны договориться о терминах
4. **Глубина может быть любой** — проект может иметь 2, 3, 4+ уровней ядер

---

## Система vs Эпистема: критическое различение

> **ВАЖНО:** Это различение определяет, когда создавать ядро, а когда — раздел документа.

### Определения

| Концепт | Определение | Признаки |
|---------|-------------|----------|
| **Система** | Сущность с границей, входами/выходами, ролями/владельцем, жизненным циклом изменений | Можно указать: кто отвечает, что на входе/выходе, что НЕ делает |
| **Эпистема** | Область описания/знания | Нельзя указать владельца, входы/выходы, границу |

### Примеры

| Концепт | Это... | Может быть ядром? | Куда помещать? |
|---------|--------|-------------------|----------------|
| Мобильное приложение | Система | ✅ Да | Отдельное ядро `B.Mobile-App/` |
| Конвейер | Система | ✅ Да | Отдельное ядро `C.Assembly-Line/` |
| Команда разработки | Система | ✅ Да | Отдельное ядро или X3 |
| Экономика проекта | Эпистема | ❌ Нет | Раздел в F1, F4, F7 |
| Маркетинг | Эпистема | ❌ Нет | Раздел в F1, F3 |
| Метрики | Эпистема | ❌ Нет | Раздел в F6, F9 |
| Обучение пользователей | Эпистема | ❌ Нет | Раздел в F1, F3, F6 |
| Монетизация | Эпистема | ❌ Нет | Раздел в F1, F4 |

### Запрещённые названия ядер (эпистемы)

```
❌ E.Экономика/
❌ G.Продвижение/
❌ H.Монетизация/
❌ I.Обучение/
❌ J.Аналитика/        # Если это не система аналитики с командой
❌ K.Документация/     # Если это не система документирования
```

### Чеклист: это система или эпистема?

Перед созданием ядра ответь на вопросы:

| Вопрос | Если "да" → система | Если "нет" → эпистема |
|--------|---------------------|----------------------|
| Есть владелец/роль, отвечающая за это? | ✅ | ❌ |
| Есть вход (что принимает)? | ✅ | ❌ |
| Есть выход (что производит)? | ✅ | ❌ |
| Есть граница (что НЕ делает)? | ✅ | ❌ |
| Есть собственный цикл изменений (релизы, версии)? | ✅ | ❌ |

**Правило:** Если хотя бы на 2 вопроса ответ "нет" — это эпистема, а не система.

---

## Фиксированная структура X1/X2/X3

### Строгие определения

```
X1 = Надсистема — система, в которую ФИЗИЧЕСКИ входит X2
X2 = Наша система (SoI) — то, за что отвечает команда
X3 = Система создания X2 — кто/что создаёт и развивает X2
```

### X1: Надсистема

**Это:** Физическая вложенность, а НЕ эпистемическая.

| Правильно | Неправильно |
|-----------|-------------|
| Мотор → входит в Автомобиль | Мотор → входит в "Транспортную отрасль" |
| Приложение → работает на Смартфоне | Приложение → часть "IT-рынка" |
| Команда → часть Организации | Команда → часть "HR-практик" |

### X2: Наша система (SoI)

**Это:** Центр ядра. То, за что отвечает команда.

| Что описывается в X2 | Где описывать |
|----------------------|---------------|
| Требования к системе | FX4 (Meaning) |
| Архитектура системы | FX5 (Architecture) |
| Реализация системы | FX6 (Operations) |
| **Подсистемы и их роли** | FX5 (Architecture) |
| **Интерфейсы с другими системами** | FX3 + FX5 |

### X3: Система создания (Constructor)

**Это:** Система, которая создаёт и развивает X2.

| Правильно для X3 | Неправильно для X3 |
|------------------|-------------------|
| Команда разработки | ❌ "Каталог подсистем" |
| Продуктовая команда | ❌ "Структура системы" |
| Платформа CI/CD | ❌ "Состав" |
| Методология разработки | ❌ "Обзор" |
| Партнёр-интегратор | ❌ "Документация" |

**ЗАПРЕТ:** X3 — это НЕ место для описания структуры X2. Структура X2 описывается в самом X2 (в FX5).

### Частая ошибка: куда описывать подсистемы?

```
Неправильно:
B.Ecosystem/
├── B2.Ecosystem/           # Наша система
└── B3.Subsystems-Catalog/  # ❌ Это НЕ создатель!

Правильно:
B.Ecosystem/
├── B2.Ecosystem/
│   └── B2.2.Architecture/
│       └── subsystems.md   # ✅ Подсистемы описаны ЗДЕСЬ
└── B3.Dev-Team/            # ✅ Это создатель
```

---

## Описание частей и стыков

### Принцип: "Где что описывать"

| Что описываем | Где | Почему |
|---------------|-----|--------|
| **Роль подсистем в целом** | В X2 родительской системы (FX5) | Архитектура целого |
| **Устройство подсистемы** | В X2 подсистемы (отдельное ядро) | Своя перспектива |
| **Стыки между ядрами** | 0.OPS/0.2.Kernels-Bridge/ + FX3 | Интеграция |

### Пример: Экосистема с подсистемами

```
B.Ecosystem/
├── B2.Ecosystem/
│   └── B2.2.Architecture/
│       ├── overview.md           # Общее описание
│       ├── subsystems.md         # Роли C2 и D2 в экосистеме
│       └── interfaces.md         # Стыки между подсистемами
└── B3.Ecosystem-Team/

C.Subsystem-1/                    # Отдельное ядро для подсистемы
├── C2.Subsystem-1/
│   └── C2.2.Architecture/
│       └── internal-arch.md      # Внутреннее устройство C
└── C3.Subsystem-1-Team/

D.Subsystem-2/                    # Ещё одна подсистема
└── ...
```

### Реестр стыков

Стыки между ядрами фиксируются в:
- `0.OPS/0.2.Kernels-Bridge/02-kernels-relations.md` — матрица связей
- `{X}1.3.Operations/` (FX3) — взаимодействие с надсистемой

---

## Структура ядра

Каждое ядро имеет **идентичную внутреннюю структуру**:

```
{Letter}.{System-Name}/
│
├── {Letter}0.{System-Name}-Management/     # Управление ядром
│   ├── README.md
│   └── local-ontology.md                   # Локальные термины
│
├── {Letter}1.{Suprasystem-Name}/           # Надсистема
│   ├── {Letter}1.1.Meaning/                # F{L}1
│   │   └── README.md
│   ├── {Letter}1.2.Architecture/           # F{L}2
│   │   └── README.md
│   └── {Letter}1.3.Operations/             # F{L}3
│       └── README.md
│
├── {Letter}2.{SOI-Name}/                   # Целевая система ядра
│   ├── {Letter}2.1.Meaning/                # F{L}4
│   ├── {Letter}2.2.Architecture/           # F{L}5
│   └── {Letter}2.3.Operations/             # F{L}6
│
└── {Letter}3.{Constructor-Name}/           # Система создания
    ├── {Letter}3.1.Meaning/                # F{L}7
    ├── {Letter}3.2.Architecture/           # F{L}8
    └── {Letter}3.3.Operations/             # F{L}9
```

**Важно:** Все папки именуются по названиям конкретных систем, а не абстрактно.

## Правила именования

### Правило 1: Имя отражает суть системы

```
Хорошо:
├── A.Automobile/                # Целевая: автомобиль
├── B.Mobile-App/                # Наша система: мобильное приложение
├── C.Recommendation-Engine/     # Наша система: движок рекомендаций
└── D.Analytics-Platform/        # Наша система: аналитическая платформа

Плохо:
├── A.Target/                    # Абстрактно, ничего не говорит
├── B.System2/                   # Бессмысленный номер
├── C.Module/                    # Размыто
└── D.Other/                     # Полностью неинформативно
```

### Правило 2: Подпапки также именуются осмысленно

> **ВАЖНО:** X1 (надсистема) — это **физическая система**, а не контекст, процесс или область знания.

```
Хорошо:
A.Automobile/
├── A1.Taxi/                     # Надсистема: такси (физическая система)
├── A2.Automobile/               # SOI: автомобиль
└── A3.Assembly-Line/            # Создатель: конвейер (система производства)

B.Mobile-App/
├── B1.User-Smartphone/          # Надсистема: смартфон пользователя
├── B2.Mobile-App/               # SOI: мобильное приложение
└── B3.Dev-Team/                 # Создатель: команда разработки

Плохо:
A.Target/
├── A1.Suprasystem/              # Абстрактно
├── A2.System-of-Interest/       # Шаблонно
└── A3.Constructor/              # Неинформативно

A.Product/
├── A1.Daily-Life/               # ❌ "Повседневная жизнь" — НЕ система
├── A2.Product/
└── A3.Experience/               # ❌ "Опыт" — НЕ система
```

### Правило 3: Согласованность внутри ядра

Имя SOI ядра должно соответствовать имени папки ядра:

```
B.Mobile-App/                    # Ядро названо по SOI
├── B0.Mobile-App-Management/    # Управление согласовано
├── B1.User-Smartphone/          # Надсистема: физическая система
├── B2.Mobile-App/               # SOI = имя ядра
└── B3.Dev-Team/                 # Создатель: команда разработки
```

## Алгоритм создания ядра

### Шаг 1: Определи позицию системы

| Вопрос | Если "да" |
|--------|-----------|
| Это главная цель проекта? | Ядро A |
| Это часть целевой системы? | Ядро B, C... (подсистема) |
| Это часть цепочки создания? | Ядро B, C... (создатель) |

### Шаг 2: Назови систему

1. Определи суть системы в 1-3 словах
2. Используй kebab-case для имени папки
3. Сделай имя понятным без контекста

### Шаг 3: Определи три системы ядра

| Система | Вопрос | Пример |
|---------|--------|--------|
| Suprasystem | В чём существует? | Контекст пользователя |
| SOI | Что это? | Мобильное приложение |
| Constructor | Кто создаёт? | Команда разработки |

### Шаг 4: Создай структуру папок

```bash
# Пример для ядра C
mkdir -p C.Recommendation-Engine/C0.Recommendation-Engine-Management
mkdir -p C.Recommendation-Engine/C1.App-Context/C1.{1,2,3}.{Meaning,Architecture,Operations}
mkdir -p C.Recommendation-Engine/C2.Recommendation-Engine/C2.{1,2,3}.{Meaning,Architecture,Operations}
mkdir -p C.Recommendation-Engine/C3.ML-Team/C3.{1,2,3}.{Meaning,Architecture,Operations}
```

### Шаг 5: Заполни README.md ядра

Используй шаблон из [A.SOI-Name/README.md](../../A.SOI-Name/README.md).

### Шаг 6: Обнови связи

1. Обнови [03-our-systems-map.md](03-our-systems-map.md)
2. Обнови [../0.2.Kernels-Bridge/01-value-chain.md](../0.2.Kernels-Bridge/01-value-chain.md)
3. Обнови [../0.2.Kernels-Bridge/02-kernels-relations.md](../0.2.Kernels-Bridge/02-kernels-relations.md)

## Когда создавать новое ядро?

### Создавай ядро, если:

- [ ] Есть отдельная команда, отвечающая за систему
- [ ] Система имеет свой жизненный цикл разработки
- [ ] Нужна детальная документация по всем 9 семействам
- [ ] Система достаточно сложна и автономна

### НЕ создавай ядро, если:

- [ ] Это просто модуль/компонент внутри системы
- [ ] Достаточно описания в F{X}5 (Architecture) родительского ядра
- [ ] Нет отдельной команды или ответственного
- [ ] Система тривиальна

## Управление ядром (X0)

Папка `X0.{Name}-Management/` нужна, если:
- У ядра есть своя команда с отдельными процессами
- Есть специфичная терминология, отличающаяся от общей
- Требуется локальная онтология

**Содержимое:**
- `README.md` — описание управления ядром
- `local-ontology.md` — локальные термины

## Связи между ядрами

Связи описываются в `0.2.Kernels-Bridge/`:
- `01-value-chain.md` — цепочка создания ценности
- `02-kernels-relations.md` — матрица связей
- `03-systems-relations.md` — структура связанности систем

## Связь с FPF

| Концепция | FPF-паттерн |
|-----------|-------------|
| Ядро как холон | A.1 Holonic Foundation |
| Локальная онтология | A.1.1 Bounded Context |
| Три системы | A.3 System Triad |
| Роли | U.RoleAssignment |

## См. также

- [02-document-families.md](02-document-families.md) — 9 семейств внутри ядра
- [03-our-systems-map.md](03-our-systems-map.md) — карта наших систем
- [../0.2.Kernels-Bridge/01-value-chain.md](../0.2.Kernels-Bridge/01-value-chain.md) — цепочка ценности


# SOURCE_FILE: 0.OPS/0.1.Knowledge-Logic/02-document-families.md
---
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
fpf_patterns:
  - A.1      # Holonic Foundation
  - A.7      # Strict Distinction
  - E.10.D2  # I/D/S Discipline
---

# Модель семейств документов (Document Families)

## Концепция

Каждое ядро разворачивает **9 семейств документов** (F1-F9), организованных как матрица (таблица) 3×3:
- **3 системы** (строки): Suprasystem, System-of-Interest, Constructor
- **3 роли** (столбцы): Предприниматель, Инженер, Менеджер

Дополнительно существует **F0** — метаэпистема хранилища (на уровне всего хранилища) и **FX0** — управление конкретным ядром.

## Матрица (таблица) 3×3

> **Синонимы:** "матрица 3×3" и "таблица 3×3" используются взаимозаменяемо.

```
                     Предприниматель    Инженер           Менеджер
                     (Meaning)          (Architecture)    (Operations)
                     Зачем?             Как устроено?     Как работает?
┌────────────────────────────────────────────────────────────────────────┐
│ X1. Suprasystem    FX1                FX2               FX3            │
│     (Надсистема)   Контекст           Окружение         Взаимодействие │
│                    Смысл              Интерфейсы        Партнёрства    │
├────────────────────────────────────────────────────────────────────────┤
│ X2. System-of-Int. FX4                FX5               FX6            │
│     (Целевая сист) Требования         Архитектура       Реализация     │
│                    Ценность           Структура         Процессы       │
├────────────────────────────────────────────────────────────────────────┤
│ X3. Constructor    FX7                FX8               FX9            │
│     (Создатель)    Принципы           Платформа         Команда        │
│                    Экономика          Инструменты       Методология    │
└────────────────────────────────────────────────────────────────────────┘

где X = буква ядра (A, B, C...)
```

## Описание систем

### Suprasystem (Надсистема) — X1

**Вопрос:** В чём существует наша целевая система?

Надсистема — это окружение, в котором функционирует целевая система. Она определяет контекст, ограничения и возможности.

| Роль | Семейство | Фокус |
|------|-----------|-------|
| Предприниматель | FX1 | Рынок, тренды, смысл существования |
| Инженер | FX2 | Внешние системы, интерфейсы, API |
| Менеджер | FX3 | Партнёры, стейкхолдеры, взаимодействия |

### System-of-Interest (Целевая система) — X2

**Вопрос:** Что мы создаём/изменяем?

Целевая система — это то, что мы проектируем, создаём или трансформируем. Центр всего ядра.

| Роль | Семейство | Фокус |
|------|-----------|-------|
| Предприниматель | FX4 | Требования, ценность, JTBD |
| Инженер | FX5 | Архитектура, компоненты, структура |
| Менеджер | FX6 | Реализация, процессы, операции |

### Constructor (Система создания) — X3

**Вопрос:** Кто/что создаёт целевую систему?

Конструктор — это система, которая создаёт, развивает и поддерживает целевую систему.

| Роль | Семейство | Фокус |
|------|-----------|-------|
| Предприниматель | FX7 | Принципы, видение, экономика команды |
| Инженер | FX8 | Платформа, инструменты, технологии |
| Менеджер | FX9 | Команда, роли, методология работы |

## Описание ролей

### Предприниматель (Meaning) — X.1

**Вопрос:** Зачем? Какой смысл?

Роль предпринимателя фокусируется на:
- Целях и ценности
- Потребностях и JTBD
- Экономике и жизнеспособности
- Стратегических решениях

### Инженер (Architecture) — X.2

**Вопрос:** Как устроено? Из чего состоит?

Роль инженера фокусируется на:
- Структуре и компонентах
- Интерфейсах и связях
- Технических решениях
- Принципах построения

### Менеджер (Operations) — X.3

**Вопрос:** Как работает? Как функционирует?

Роль менеджера фокусируется на:
- Процессах и workflows
- Операционной деятельности
- Координации и взаимодействии
- Исполнении и контроле

## Детальное описание семейств

### FX1: Suprasystem × Предприниматель

**Путь:** `X1.Suprasystem/X1.1.Meaning/`

Документы о смысле существования в контексте:
- Анализ рынка и трендов
- Позиционирование
- Конкурентный ландшафт
- Стратегический контекст

### FX2: Suprasystem × Инженер

**Путь:** `X1.Suprasystem/X1.2.Architecture/`

Документы об окружении как системе:
- Внешние API и интеграции
- Технологический ландшафт
- Зависимости от внешних систем
- Интерфейсы с окружением

### FX3: Suprasystem × Менеджер

**Путь:** `X1.Suprasystem/X1.3.Operations/`

Документы о взаимодействии с окружением:
- Партнёрства и контракты
- Внешние стейкхолдеры
- Коммуникации с рынком
- Операционные связи

### FX4: System-of-Interest × Предприниматель

**Путь:** `X2.System-of-Interest/X2.1.Meaning/`

Документы о ценности целевой системы:
- Требования и спецификации
- JTBD и сценарии использования
- Value proposition
- Критерии успеха

### FX5: System-of-Interest × Инженер

**Путь:** `X2.System-of-Interest/X2.2.Architecture/`

Документы об архитектуре:
- Архитектурные решения (ADR)
- Компонентная модель
- Технический дизайн
- Схемы и диаграммы

### FX6: System-of-Interest × Менеджер

**Путь:** `X2.System-of-Interest/X2.3.Operations/`

Документы о реализации и эксплуатации:
- Процессы разработки
- Операционные процедуры
- Метрики и мониторинг
- Инструкции по эксплуатации

### FX7: Constructor × Предприниматель

**Путь:** `X3.Constructor/X3.1.Meaning/`

Документы о принципах создателя:
- Видение и миссия команды
- Экономика создания
- Принципы работы
- Стратегия развития

### FX8: Constructor × Инженер

**Путь:** `X3.Constructor/X3.2.Architecture/`

Документы о платформе создания:
- Инструменты разработки
- CI/CD и инфраструктура
- Технологический стек
- Среды разработки

### FX9: Constructor × Менеджер

**Путь:** `X3.Constructor/X3.3.Operations/`

Документы о команде и процессах:
- Структура команды
- Роли и ответственность
- Методология (Scrum, Kanban...)
- Ритуалы и практики

## F0 и FX0

### F0: Repository Management (Метаэпистема хранилища)

**Путь:** `0.OPS/`

Метаэпистема — знания о знаниях хранилища:
- Общая онтология
- Связи между ядрами
- Стандарты и процессы
- Управление знаниями

### FX0: Kernel Management

**Путь:** `X.{System-Name}/X0.{System-Name}-Management/`

Управление конкретным ядром (опционально):
- Локальная онтология ядра
- Ответственные за семейства
- Специфичные процессы ядра

**Примеры правильного именования:**
```
A.Automobile/A0.Automobile-Management/
B.Mobile-App/B0.Mobile-App-Management/
C.Backend-Service/C0.Backend-Service-Management/
```

## Алгоритм определения семейства

```
1. Определи ЯДРО (A, B, C...)
   └── О какой "нашей системе" идёт речь?

2. Определи СИСТЕМУ (1, 2, 3)
   ├── Это о контексте/окружении? → X1.Suprasystem
   ├── Это о самой системе? → X2.System-of-Interest
   └── Это о создателе? → X3.Constructor

3. Определи РОЛЬ (.1, .2, .3)
   ├── Это о смысле/ценности? → X.1.Meaning
   ├── Это о структуре/устройстве? → X.2.Architecture
   └── Это о процессах/работе? → X.3.Operations
```

## Примеры размещения

> **Для AI-агентов:** При создании документов используйте имена конкретных систем проекта вместо абстрактных плейсхолдеров.

| Документ | Ядро | Семейство | Путь |
|----------|------|-----------|------|
| Анализ рынка | A | FA1 | `A.Automobile/A1.Taxi/A1.1.Meaning/` |
| API-спецификация | B | FB5 | `B.Mobile-App/B2.Mobile-App/B2.2.Architecture/` |
| Структура команды | B | FB9 | `B.Mobile-App/B3.Dev-Team/B3.3.Operations/` |
| Требования к продукту | A | FA4 | `A.Automobile/A2.Automobile/A2.1.Meaning/` |

### Правило именования папок

> **ВАЖНО:** X1 — это **физическая система**, не контекст, процесс или область.

```
Хорошо (Автомобиль):
A.Automobile/                   # Имя целевой системы
├── A1.Taxi/                    # Надсистема: физическая система
├── A2.Automobile/              # Имя SoI (совпадает с ядром)
└── A3.Assembly-Line/           # Имя конструктора

Хорошо (Приложение):
B.Mobile-App/
├── B1.User-Smartphone/         # Надсистема: физическая система
├── B2.Mobile-App/
└── B3.Dev-Team/

Плохо:
A.Target/                       # Абстрактно
├── A1.Daily-Life/              # ❌ "Повседневная жизнь" — НЕ система
├── A2.System-of-Interest/      # Это роль, не имя системы
└── A3.Constructor/             # Это роль, не имя системы
```

## I/D/S дисциплина (FPF E.10.D2)

При создании документа различай:

| Аспект | Вопрос | Пример |
|--------|--------|--------|
| **I** (Intension) | Что это по сути? | "Авторизация — механизм проверки прав" |
| **D** (Description) | Что мы наблюдаем? | "Используем JWT с TTL 24h" |
| **S** (Specification) | Что требуется? | "Время ответа < 100ms" |

## См. также

- [01-kernels-model.md](01-kernels-model.md) — что такое ядро
- [04-ontology.md](04-ontology.md) — общая онтология
- [../0.6.Repository-Processes/02-standards.md](../0.6.Repository-Processes/02-standards.md) — стандарты оформления


# SOURCE_FILE: 0.OPS/0.1.Knowledge-Logic/03-our-systems-map.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Карта наших систем (Our Systems Map)

> **Для AI-агентов:** Используйте этот документ как шаблон для создания карты систем конкретного проекта. Заполните плейсхолдеры на основе описания проекта от пользователя.

## Назначение

Этот документ описывает все "наши системы" в проекте и их позицию относительно:
1. Главной целевой системы (Ядро A)
2. Друг друга
3. Цепочки создания ценности

## Граф создателей (шаблон)

> **Инструкция:** Замените плейсхолдеры на реальные имена систем проекта.

```
                    ┌─────────────────────────┐
                    │   A. [SOI-Name]         │
                    │  (Целевая система)      │
                    └──────────┬──────────────┘
                               │
                               │ создаётся
                               ▼
              ┌────────────────┴────────────────┐
              │                                 │
    ┌─────────▼─────────┐           ┌──────────▼──────────┐
    │  B. [System-Name] │           │   C. [System-Name]  │
    │  (Наша система 1) │           │   (Наша система 2)  │
    └─────────┬─────────┘           └──────────┬──────────┘
              │                                 │
              │ создаётся                       │ создаётся
              ▼                                 ▼
    ┌─────────────────┐               ┌─────────────────┐
    │  D. [Sys-Name]  │               │  E. [Sys-Name]  │
    └─────────────────┘               └─────────────────┘
```

### Пример заполненного графа

```
                    ┌─────────────────────────┐
                    │   A. Automobile         │
                    │  (Целевая система)      │
                    └──────────┬──────────────┘
                               │
                               │ создаётся
                               ▼
              ┌────────────────┴────────────────┐
              │                                 │
    ┌─────────▼─────────┐           ┌──────────▼──────────┐
    │  B. Assembly-Line │           │   C. Quality-       │
    │  (Конвейер)       │           │      Control        │
    └─────────┬─────────┘           │   (Контроль кач-ва) │
              │                     └──────────┬──────────┘
              │ создаётся                       │ создаётся
              ▼                                 ▼
    ┌─────────────────┐               ┌─────────────────┐
    │  D. CNC-Machine │               │  E. Test-Stand  │
    │  (Станок ЧПУ)   │               │  (Испытат.стенд)│
    └─────────────────┘               └─────────────────┘
```

## Реестр наших систем

> **Инструкция:** Заполните таблицу при добавлении новых ядер.

| Ядро | Название | Тип | Позиция | Создатель |
|------|----------|-----|---------|-----------|
| A | *[Целевая система]* | Target | — | Ядро B, C... |
| B | *[Наша система 1]* | Our System | Подсистема A / Цепочка | Ядро D... |
| C | *[Наша система 2]* | Our System | Подсистема A / Цепочка | Ядро E... |

### Типы связей с целевой системой

- **Входит в состав** — система является частью другой системы
- **Создаёт** — система производит/поддерживает/ремонтирует другую систему
- **В окружении** — системы взаимодействуют через интерфейсы

## Текущая карта проекта

> **Для AI-агентов:** Заполните этот раздел при инициализации проекта на основе описания от пользователя.

```
TODO: Нарисуйте карту систем вашего проекта

Используйте шаблон выше, заменяя плейсхолдеры на реальные имена систем.
```

## Примеры карт для разных типов проектов

### Пример 1: Автомобильное производство (многоуровневый)

Этот пример демонстрирует ситуацию, когда **разные команды отвечают за разные системы** на разных уровнях иерархии.

```
                    ┌─────────────────────────────────────────────────┐
                    │              A. Automobile                       │
                    │         (Целевая система проекта)               │
                    │                                                  │
                    │  🎯 Команда-1 работает с мотором (B)            │
                    │     как подсистемой автомобиля                   │
                    └──────────────────────┬──────────────────────────┘
                           ↑ создаёт       │ ↑ часть
                           │               │ │
             ┌─────────────┴───────┐   ┌───┴─┴───────────────┐
             │                     │   │                     │
    ┌────────▼────────┐   ┌────────▼───▼────┐
    │ C. Assembly-    │   │   B. Engine     │
    │    Line         │   │    (Мотор)      │
    │  (Конвейер)     │   │                 │
    │                 │   │ Команда-1       │
    │ Команда-2       │   └─────────────────┘
    └────────┬────────┘
             │
    ┌────────┴────────┐
    │                 │
┌───▼─────────────┐  ┌▼──────────────────────┐
│ D. CNC-Machine  │  │ E. Team-2             │
│   (Станок)      │  │   (Команда-2)         │
│                 │  │                       │
│ Команда-3       │  │ Команда-4             │
└─────────────────┘  └───────────────────────┘
```

**Особенность:** Команда-4 (E) развивает команду-2, которая является частью конструктора (C3) системы C. Это **мета-уровень** — создание создателя.

| Ядро | Система | Команда | Позиция | Особенность |
|------|---------|---------|---------|-------------|
| A | Автомобиль | — | Целевая | Конечная ценность |
| B | Мотор | Команда-1 | Подсистема A (целевая система) | Физическая часть |
| C | Конвейер | Команда-2 | Создаёт A | Производство |
| D | Станок ЧПУ | Команда-3 | Часть C | Оборудование |
| E | Команда-2 | Команда-4 | Создаёт C3 | Мета-уровень |

> **Важно:** Команды должны согласовывать онтологию — один термин может означать разное в разных ядрах. См. [01-kernels-model.md](01-kernels-model.md) → "Согласование онтологий".

---

### Пример 2: Система умного дома

```
┌─────────────────────────────────────────────────────────────┐
│                    A. Smart-Home                            │
│             (Система умного дома)                           │
└─────────────────────────┬───────────────────────────────────┘
                          │ создаётся
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    B. IoT-Hub                               │
│              (Центральный контроллер)                       │
└─────────────────────────┬───────────────────────────────────┘
                          │ создаётся
            ┌─────────────┼─────────────┐
            ▼             ▼             ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ C. Sensors    │ │ D. Cloud-     │ │ E. Mobile-    │
│               │ │    Platform   │ │    App        │
└───────────────┘ └───────────────┘ └───────────────┘
```

### Пример 3: E-commerce платформа

```
┌─────────────────────────────────────────────────────────────┐
│                   A. Marketplace                            │
│               (Торговая площадка)                           │
└─────────────────────────┬───────────────────────────────────┘
                          │ создаётся
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   B. Web-Platform                           │
│               (Веб-платформа)                               │
└─────────────────────────┬───────────────────────────────────┘
                          │ создаётся
            ┌─────────────┼─────────────┐
            ▼             ▼             ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ C. Catalog-   │ │ D. Payment-   │ │ E. Delivery-  │
│    Service    │ │    Gateway    │ │    Tracker    │
└───────────────┘ └───────────────┘ └───────────────┘
```

## Правила добавления новой системы

### 1. Когда создавать новое ядро?

Создавай новое ядро, если:
- [ ] Есть отдельная команда, отвечающая за систему
- [ ] Система имеет свой жизненный цикл
- [ ] Нужна отдельная документация по 9 семействам
- [ ] Система достаточно сложна для детального описания

### 2. Когда НЕ создавать ядро?

Не создавай ядро, если:
- Это просто модуль/компонент внутри существующей системы
- Достаточно описания в FX5 (Architecture) родительского ядра
- Нет отдельной команды или ответственного

### 3. Процесс добавления

1. Определи позицию в карте (см. выше)
2. Выбери букву (B, C, D...)
3. Создай структуру папок (см. [01-kernels-model.md](01-kernels-model.md))
4. Обнови эту карту
5. Обнови [01-value-chain.md](../0.2.Kernels-Bridge/01-value-chain.md)

## Шаблон описания системы

> **Для AI-агентов:** Используйте этот шаблон для документирования каждой системы проекта.

```markdown
## [Буква]. [System-Name]

**Тип:** Подсистема / Цепочка создания / Гибрид

**Позиция в графе:**
- Создаётся: [кем/чем]
- Создаёт: [кого/что]

**Команда:** [название или ссылка]

**Ключевая ценность:** [одно предложение]

**Связи:**
- Зависит от: [ядра]
- Влияет на: [ядра]
```

### Пример заполненного описания

```markdown
## B. Mobile-App

**Тип:** Цепочка создания

**Позиция в графе:**
- Создаётся: D. Backend-API, E. Design-System
- Создаёт: A. Mobile-App (через UX)

**Команда:** Mobile Team (см. B3.Dev-Team/B3.3.Operations/)

**Ключевая ценность:** Предоставляет удобный интерфейс для взаимодействия клиента с сервисом

**Связи:**
- Зависит от: D (API), E (дизайн)
- Влияет на: A (клиентский опыт)
```

## См. также

- [01-kernels-model.md](01-kernels-model.md) — как создавать ядра
- [../0.2.Kernels-Bridge/01-value-chain.md](../0.2.Kernels-Bridge/01-value-chain.md) — цепочка ценности
- [../0.2.Kernels-Bridge/02-kernels-relations.md](../0.2.Kernels-Bridge/02-kernels-relations.md) — матрица связей


# SOURCE_FILE: 0.OPS/0.1.Knowledge-Logic/04-ontology.md
---
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
fpf_patterns:
  - A.1      # Holonic Foundation
  - A.1.1    # Bounded Context
  - A.7      # Strict Distinction
---

# Общая онтология (Ontology)

## Назначение

Этот документ определяет **общие термины и концепции**, применимые ко всем ядрам хранилища. Локальные термины конкретных ядер определяются в `X0.{System-Name}-Management/local-ontology.md`.

## Иерархия онтологий

```
┌────────────────────────────────────────┐
│     FPF (First Principles Framework)   │  ← Эпистемологический фундамент
└────────────────────┬───────────────────┘
                     │
┌────────────────────▼───────────────────┐
│   Общая онтология (этот документ)      │  ← Термины для всех ядер
└────────────────────┬───────────────────┘
                     │
      ┌──────────────┼──────────────┐
      │              │              │
┌─────▼─────┐  ┌─────▼─────┐  ┌─────▼─────┐
│ A0.local  │  │ B0.local  │  │ C0.local  │  ← Локальные онтологии ядер
└───────────┘  └───────────┘  └───────────┘
```

## Базовые концепции

### Система (System)

**Определение:** Совокупность взаимосвязанных элементов, выделенная из окружения и обладающая эмерджентными свойствами.

**FPF-связь:** A.1 Holonic Foundation — система есть холон (целое и часть).

### Целевая система (System-of-Interest, SoI)

**Определение:** Система, которую мы проектируем, создаём, изменяем или изучаем. Центр внимания проекта.

**Синонимы:** Target System (англ.)

### Надсистема (Suprasystem)

**Определение:** Система более высокого уровня, частью которой является целевая система. Определяет контекст и ограничения.

**Синонимы:** Supersystem (англ.)

### Система создания (Constructor)

**Определение:** Система, которая создаёт, развивает и поддерживает целевую систему.

**Примеры:** Команда разработки, производственная линия, организация.

## Организационные концепции

### Ядро (Kernel)

**Определение:** Полная системная перспектива относительно одной целевой системы. Содержит 9 семейств документов (F1-F9).

**Типы:**
- **Ядро A** — всегда относительно главной целевой системы
- **Ядра B, C, D...** — относительно "наших систем"

### Наша система (Our System)

**Определение:** Система, за которую мы отвечаем и которая участвует в создании или является частью целевой системы.

**Может быть:**
- Подсистемой целевой системы
- Частью цепочки создания

### Семейство документов (Document Family)

**Определение:** Группа документов, объединённых позицией в матрице 3×3 (Система × Роль).

**Обозначение:** FXN, где X — буква ядра, N — номер 1-9.

## Ролевые концепции

### Роль (Role)

**Определение:** Функциональная позиция, определяющая угол зрения на систему. Не путать с человеком или должностью.

**FPF-связь:** A.7 Strict Distinction — Роль ≠ Человек ≠ Должность.

### Три роли S2R

| Роль | Вопрос | Фокус |
|------|--------|-------|
| **Предприниматель** (Meaning) | Зачем? | Ценность, смысл, экономика |
| **Инженер** (Architecture) | Как устроено? | Структура, компоненты |
| **Менеджер** (Operations) | Как работает? | Процессы, операции |

## Документные концепции

### Документ (Document)

**Определение:** Единица знания, имеющая идентификатор, метаданные и содержимое.

### Frontmatter

**Определение:** YAML-блок в начале документа с метаданными.

### Статусы документа

| Статус | Описание |
|--------|----------|
| `stub` | Заглушка, только заголовок |
| `draft` | Черновик, в работе |
| `active` | Актуальный, используется |
| `archived` | Архивный, исторический |

## Типы документов

| Тип | Описание | Пример |
|-----|----------|--------|
| `doc` | Описательный документ | Обзор архитектуры |
| `spec` | Спецификация, требования | API-спецификация |
| `process` | Описание процесса | Workflow деплоя |
| `report` | Отчёт, результат анализа | Аудит безопасности |
| `template` | Шаблон для создания | Шаблон ADR |

## Связи и зависимости

### Цепочка создания (Creation Chain)

**Определение:** Последовательность систем, где каждая создаёт следующую.

```
Constructor → System-of-Interest → [использование в Suprasystem]
```

### Граф создателей (Creators Graph)

**Определение:** Направленный граф, показывающий какие системы создают какие.

## Качество и доверие

### F-G-R (FPF B.3)

Оценка доверия к информации:

| Компонент | Диапазон | Описание |
|-----------|----------|----------|
| **F** (Formality) | 0-9 | Формальность описания |
| **G** (Scope) | local/project/ecosystem | Область применимости |
| **R** (Reliability) | 0.0-1.0 | Надёжность, проверенность |

### I/D/S дисциплина (FPF E.10.D2)

| Аспект | Вопрос | Описание |
|--------|--------|----------|
| **I** (Intension) | Что это? | Сущностное определение |
| **D** (Description) | Что наблюдаем? | Описание характеристик |
| **S** (Specification) | Что требуется? | Спецификация, критерии |

## Запрещённые термины и конструкции

> **Для AI-агентов:** Эти термины запрещены в S2R, чтобы избежать типичных ошибок.

### Лексические запреты

| Запрещено | Почему | Использовать вместо |
|-----------|--------|---------------------|
| **"Контур"** | Размывает понятие системы, создаёт иллюзию границы без свойств системы | "Система", "Подсистема", "Область" |
| **"Правила" как система** | Правила — это описание, не система | "Стандарт", "Процесс" (в документах F6/F9) |
| **"Процесс" как ядро** | Процесс — это работа системы, не система сама | Описывать в FX6/FX9 соответствующей системы |

### Запрещённые названия ядер

Эти концепции являются **эпистемами** (областями знания), а не системами:

```
❌ E.Экономика/          → описывать в F1, F4, F7
❌ G.Продвижение/        → описывать в F1, F3
❌ H.Монетизация/        → описывать в F1, F4
❌ I.Обучение/           → описывать в F1, F3, F6
❌ J.Метрики/            → описывать в F6, F9
❌ K.Документация/       → (если нет отдельной системы документирования)
```

**Исключение:** Если у концепции есть команда-владелец, входы/выходы, граница и цикл изменений — это система, и можно создать ядро.

### Запрещённые значения для X3

X3 — это **система создания X2**, а не описание структуры X2.

| Запрещено для X3 | Почему | Где описывать |
|------------------|--------|---------------|
| "Каталог подсистем" | Это описание X2, не создатель | FX5 (Architecture) |
| "Структура" | Это архитектура X2 | FX5 (Architecture) |
| "Состав" | Это содержимое X2 | FX5 (Architecture) |
| "Обзор" | Это документ о X2 | FX4 или FX5 |
| "Документация" | Это описание X2 | F-документы X2 |

### Различение: Система vs Эпистема

| Концепт | Система? | Признаки |
|---------|----------|----------|
| **Система** | ✅ Да | Есть владелец, входы/выходы, граница, жизненный цикл |
| **Эпистема** | ❌ Нет | Область знания без владельца и границ |

Подробнее: [01-kernels-model.md](01-kernels-model.md) → раздел "Система vs Эпистема".

---

## Принципы

### SSOT (Single Source of Truth)

**Принцип:** Каждое знание живёт в одном месте. Ссылаемся, не копируем.

### Ограниченный контекст (Bounded Context)

**Принцип:** Термин имеет значение только в своём контексте. При пересечении границ — явно указываем мост.

**FPF-связь:** A.1.1 Bounded Context.

### Строгое различение (Strict Distinction)

**Принцип:** Не путаем сущности разных типов.

| Путаница | Различение |
|----------|------------|
| Документ "делает" | Система делает, документ описывает |
| Роль = Человек | Роль — функция, человек — исполнитель |
| План = Реальность | План — намерение, реальность — факт |

**FPF-связь:** A.7 Strict Distinction.

## Связь с FPF

| Концепция S2R | FPF-паттерн |
|---------------|-------------|
| Ядро как холон | A.1 Holonic Foundation |
| Локальная онтология | A.1.1 Bounded Context |
| Три системы | A.3 System Triad |
| Роли | U.RoleAssignment |
| Различение | A.7 Strict Distinction |
| Доверие | B.3 Trust Calculus |
| I/D/S | E.10.D2 Discipline |

## См. также

- [05-glossary.md](05-glossary.md) — глоссарий терминов
- [01-kernels-model.md](01-kernels-model.md) — модель ядер
- [02-document-families.md](02-document-families.md) — семейства документов
- [../0.4.FPF-Integration/fpf/INDEX.md](../0.4.FPF-Integration/fpf/INDEX.md) — локальные принципы FPF


# SOURCE_FILE: 0.OPS/0.1.Knowledge-Logic/05-glossary.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Глоссарий (Glossary)

Краткий справочник терминов. Подробные определения — в [04-ontology.md](04-ontology.md).

## Системные термины

| Термин | Определение |
|--------|-------------|
| **System-of-Interest (SoI)** | Целевая система, которую создаём/изменяем |
| **Suprasystem** | Надсистема, окружение целевой системы |
| **Constructor** | Система создания, создаёт целевую систему |
| **Our System** | Наша система — за которую мы отвечаем |
| **Kernel** | Ядро — системная перспектива с 9 семействами |

## Организационные термины

| Термин | Определение |
|--------|-------------|
| **S2R** | Имя метода (бренд) |
| **SRR** | Systems–Roles Repository (формальная расшифровка) |
| **F0-F9** | Семейства документов (F0 — управление, F1-F9 — матрица 3×3) |
| **FPF** | First Principles Framework — эпистемологический фундамент |

## Ролевые термины

| Термин | Определение |
|--------|-------------|
| **Meaning** | Роль Предпринимателя — "Зачем?" |
| **Architecture** | Роль Инженера — "Как устроено?" |
| **Operations** | Роль Менеджера — "Как работает?" |

## Документные термины

| Термин | Определение |
|--------|-------------|
| **Frontmatter** | YAML-метаданные в начале документа |
| **SSOT** | Single Source of Truth — один источник истины |
| **Status** | Статус документа: stub/draft/active/archived |

## FPF-термины

| Термин | Определение |
|--------|-------------|
| **Холон (Holon)** | Целое, являющееся частью большего целого |
| **Bounded Context** | Ограниченный контекст, область значения термина |
| **F-G-R** | Кортеж доверия: Formality-Scope-Reliability |
| **I/D/S** | Intension-Description-Specification |
| **ADI** | Цикл рассуждения: Abduction-Deduction-Induction |

## Аббревиатуры

| Аббревиатура | Расшифровка |
|--------------|-------------|
| SoI | System-of-Interest |
| FPF | First Principles Framework |
| ADR | Architecture Decision Record |
| JTBD | Jobs To Be Done |
| API | Application Programming Interface |

---

## Термины предметной области (Domain Terms)

> **Назначение:** Этот раздел содержит термины **конкретной предметной области** проекта, которые используются **во всех ядрах**.

### Общие термины проекта

*Заполните этот раздел терминами вашей предметной области.*

| Термин | Определение | Используется в ядрах |
|--------|-------------|---------------------|
| *Пример: Клиент* | *Физическое или юридическое лицо, использующее продукт* | *A, B* |
| *Пример: Заказ* | *Запрос клиента на получение товара или услуги* | *A, B, C* |

### Локальные термины ядер

Каждое ядро может иметь **собственные термины**, специфичные для его контекста. Они описываются в файле `X0.{Kernel-Name}-Management/local-ontology.md`.

**Правила для локальных терминов:**

1. **Связь с общими терминами** — при определении локального термина желательно указать, как он связан с терминами из этого глоссария
2. **Явное указание контекста** — если термин имеет разное значение в разных ядрах, это должно быть явно указано
3. **Избегание конфликтов** — если один и тот же термин используется в разных ядрах с разным значением, рекомендуется:
   - Переименовать локальный термин для ясности
   - Или явно указать: "В ядре X термин Y означает Z"

**Пример локального термина:**

```markdown
# В файле B0.Engine-Management/local-ontology.md

## Локальные термины ядра B

| Термин | Определение | Связь с общим глоссарием |
|--------|-------------|--------------------------|
| Блок цилиндров | Основной корпус двигателя | Компонент системы "Мотор" (см. глоссарий: SoI) |
| Степень сжатия | Отношение объёмов камеры сгорания | Характеристика для F5 (Architecture) |
```

### Синхронизация терминов между ядрами

При работе нескольких команд над разными ядрами:

1. **Общие термины** — добавляются в этот документ (05-glossary.md)
2. **Локальные термины** — остаются в `local-ontology.md` соответствующего ядра
3. **При конфликте** — термин выносится в общий глоссарий с уточнением контекста

## См. также

- [04-ontology.md](04-ontology.md) — полная онтология
- [../0.4.FPF-Integration/fpf/INDEX.md](../0.4.FPF-Integration/fpf/INDEX.md) — принципы FPF


# SOURCE_FILE: 0.OPS/0.1.Knowledge-Logic/06-taxonomy.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Таксономия (Taxonomy)

Система классификации документов в хранилище.

## Измерения классификации

### 1. По ядру (Kernel)

| Значение | Описание |
|----------|----------|
| A | Ядро целевой системы |
| B, C, D... | Ядра наших систем |

### 2. По системе (System)

| Значение | Описание |
|----------|----------|
| X1.Suprasystem | Документы о надсистеме |
| X2.System-of-Interest | Документы о целевой системе |
| X3.Constructor | Документы о создателе |

### 3. По роли (Role)

| Значение | Вопрос | Описание |
|----------|--------|----------|
| Meaning (.1) | Зачем? | Ценность, смысл |
| Architecture (.2) | Как устроено? | Структура |
| Operations (.3) | Как работает? | Процессы |

### 4. По типу документа (Type)

| Значение | Описание | Пример |
|----------|----------|--------|
| `doc` | Описательный | Обзор системы |
| `spec` | Спецификация | Требования, API |
| `process` | Процесс | Workflow |
| `report` | Отчёт | Результат анализа |
| `template` | Шаблон | Шаблон документа |

### 5. По статусу (Status)

| Значение | Описание |
|----------|----------|
| `stub` | Заглушка |
| `draft` | Черновик |
| `active` | Актуальный |
| `archived` | Архивный |

### 6. По масштабу (Scope)

| Значение | Описание |
|----------|----------|
| `local-edge` | Локальный, на границе |
| `project` | Уровень проекта |
| `ecosystem` | Уровень экосистемы |
| `universal` | Универсальный |

### 7. По слою (Layer)

| Значение | Описание |
|----------|----------|
| `methodology` | Методология, подходы |
| `architecture` | Архитектура, структура |
| `operations` | Операции, процессы |
| `data` | Данные, факты |

## Комбинированный адрес

Полный адрес документа:

```
{Kernel}.{System}.{Role}/{filename}.md

Примеры:
A.A2.System-of-Interest/A2.1.Meaning/requirements.md
B.B3.Constructor/B3.3.Operations/team-structure.md
```

## Правила классификации

1. **Один документ — одно место** (SSOT)
2. **Определи ядро первым** — о какой системе речь?
3. **Затем систему** — надсистема/SoI/создатель?
4. **Затем роль** — смысл/структура/процесс?

## См. также

- [02-document-families.md](02-document-families.md) — модель семейств
- [07-naming.md](07-naming.md) — соглашения об именовании


# SOURCE_FILE: 0.OPS/0.1.Knowledge-Logic/07-naming.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Соглашения об именовании (Naming Conventions)

## Общие правила

1. **Папки** — только на английском
2. **Файлы** — могут быть на русском или английском
3. **Используй kebab-case** для файлов: `my-document.md`
4. **Используй PascalCase или числовую нумерацию** для папок

## Именование папок

### Корневой уровень

```
0.OPS/     # Числовой префикс + PascalCase
A.Automobile/                # Буква ядра + имя целевой системы
B.Mobile-App/                # Буква ядра + имя нашей системы
```

### Уровень системы

> **Важно:** X1 — это **физическая система**, не контекст, процесс или область.

```
Хорошо (на примере автомобиля):
A1.Taxi/                     # Надсистема: физическая система (такси)
A2.Automobile/               # Имя целевой системы (SoI)
A3.Assembly-Line/            # Имя конструктора (конвейер)

Хорошо (на примере приложения):
B1.User-Smartphone/          # Надсистема: физическая система (смартфон)
B2.Mobile-App/               # SoI
B3.Dev-Team/                 # Конструктор

Плохо:
A1.Daily-Life/               # ❌ "Повседневная жизнь" — НЕ система
A1.Market/                   # ❌ "Рынок" — НЕ физическая система
A1.Industry/                 # ❌ "Отрасль" — НЕ физическая система
A3.Experience/               # ❌ "Опыт" — НЕ система
A1.Suprasystem/              # ❌ Это роль, не имя системы
A2.System-of-Interest/       # ❌ Абстрактно
A3.Constructor/              # ❌ Не описывает, ЧТО создаёт
```

### Уровень роли

```
X1.1.Meaning/                # X = ядро, 1 = система, .1/.2/.3 = роль
X1.2.Architecture/
X1.3.Operations/
```

> Роли остаются фиксированными: Meaning, Architecture, Operations

### Уровень F0

```
0.1.Knowledge-Logic/         # Онтология и модель знаний
0.2.Kernels-Bridge/          # Связи между ядрами
0.3.Roles-Matrix-3x3/        # Матрица ролей 3×3
0.4.FPF-Integration/         # Интеграция с FPF
0.5.AI-Reports/              # Автоматические отчёты
0.6.Repository-Processes/    # Процессы и стандарты
0.7.Plans-and-Meetings/      # Планирование
0.9.Inbox/
0.99.Archive/
```

## Именование файлов

### Документы

```
requirements.md              # Простое имя
api-specification.md         # kebab-case для составных
team-structure.md
value-chain.md
```

### README файлы

```
README.md                    # Всегда UPPERCASE
```

### Специальные файлы

```
local-ontology.md            # В X0.{System-Name}-Management/
_index.md                    # Если нужен индекс (редко)
```

## Паттерны именования ядер

### Хорошо

```
A.Automobile/                # Конкретная техническая система
B.Mobile-App/                # Описывает систему
C.Backend-Service/           # Технически точно
D.Analytics-Platform/        # Функционально
```

### Плохо

```
A.Target/                    # Слишком абстрактно
B.System2/                   # Неинформативно
C.Module/                    # Размыто
D.Other/                     # Бессмысленно
A.Impressed-Customer/        # ❌ "Клиент" — роль, не система
A.Experience/                # ❌ "Опыт" — процесс, не система
```

## Примеры полных путей

### Хорошо (с именами систем)

```
0.OPS/0.1.Knowledge-Logic/01-kernels-model.md
A.Automobile/A1.Taxi/A1.1.Meaning/market-analysis.md
A.Automobile/A2.Automobile/A2.1.Meaning/requirements.md
B.Mobile-App/B1.User-Smartphone/B1.2.Architecture/device-integration.md
B.Mobile-App/B3.Dev-Team/B3.3.Operations/team-structure.md
C.Backend-Service/C2.Backend-Service/C2.2.Architecture/api-schema.md
```

### Плохо (абстрактные названия)

```
A.Target-System/A2.System-of-Interest/A2.1.Meaning/requirements.md
A.Product/A1.Daily-Life/A1.1.Meaning/context.md           # ❌ Daily-Life — не система
B.Our-System/B3.Constructor/B3.3.Operations/team-structure.md
```

## См. также

- [06-taxonomy.md](06-taxonomy.md) — классификация документов
- [../0.6.Repository-Processes/02-standards.md](../0.6.Repository-Processes/02-standards.md) — стандарты


# SOURCE_FILE: 0.OPS/0.1.Knowledge-Logic/08-anti-patterns.md
---
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
fpf_patterns:
  - A.1.1    # Bounded Context
  - A.7      # Strict Distinction
---

# Анти-паттерны S2R (Anti-patterns)

> **Для AI-агентов:** Этот документ содержит типичные ошибки при работе с multi-kernel S2R. Перед созданием ядер или структуры — проверьте, что не повторяете эти ошибки.

## Анти-паттерн 1: Ядро по эпистеме

### Описание ошибки

Создание ядра для области знания (эпистемы) вместо системы.

### Пример ошибки

```
❌ Неправильно:
Project/
├── A.Product/
├── B.App/
├── C.Backend/
├── E.Экономика/          # ❌ Это эпистема!
├── G.Продвижение/        # ❌ Это эпистема!
├── H.Монетизация/        # ❌ Это эпистема!
└── I.Обучение/           # ❌ Это эпистема!
```

### Почему это ошибка

- "Экономика", "Продвижение", "Монетизация" — это не системы
- У них нет владельца, входов/выходов, границы, жизненного цикла
- Это **области знания**, которые описываются внутри документов F1-F9

### Правильный подход

```
✅ Правильно:
Project/
├── A.Product/
│   ├── A2.Product/
│   │   ├── A2.1.Meaning/
│   │   │   ├── value-proposition.md      # Здесь про экономику
│   │   │   └── business-model.md         # Здесь про монетизацию
│   │   └── A2.3.Operations/
│   │       └── marketing-channels.md     # Здесь про продвижение
├── B.App/
└── C.Backend/
```

### Чеклист проверки

Перед созданием ядра спроси:
- [ ] Есть владелец/команда?
- [ ] Есть вход (что принимает)?
- [ ] Есть выход (что производит)?
- [ ] Есть граница (что НЕ делает)?
- [ ] Есть цикл изменений (релизы)?

Если хотя бы 2 ответа "нет" — это эпистема, не ядро.

---

## Анти-паттерн 2: X3 как каталог

### Описание ошибки

Использование X3 для описания структуры X2 вместо системы создания.

### Пример ошибки

```
❌ Неправильно:
B.Ecosystem/
├── B1.Market/
├── B2.Ecosystem/
└── B3.Subsystems-Catalog/    # ❌ Это НЕ создатель!
    ├── B3.1.Meaning/
    │   └── subsystems-overview.md
    ├── B3.2.Architecture/
    │   └── subsystems-list.md
    └── B3.3.Operations/
        └── subsystems-status.md
```

### Почему это ошибка

- X3 = **система создания X2**, а не описание структуры X2
- "Каталог подсистем" — это документ о X2, не отдельная система
- Нарушает фиксированную структуру X1/X2/X3

### Правильный подход

```
✅ Правильно:
B.Ecosystem/
├── B1.Market/
├── B2.Ecosystem/
│   └── B2.2.Architecture/
│       ├── overview.md
│       └── subsystems.md         # ✅ Подсистемы описаны ЗДЕСЬ
└── B3.Ecosystem-Team/            # ✅ Это создатель
    ├── B3.1.Meaning/
    │   └── team-mission.md
    ├── B3.2.Architecture/
    │   └── team-structure.md
    └── B3.3.Operations/
        └── development-process.md
```

---

## Анти-паттерн 3: Эпистемическая надсистема

### Описание ошибки

Указание в X1 абстрактной области вместо физической надсистемы.

### Пример ошибки

```
❌ Неправильно:
B.Engine/
├── B1.Automotive-Industry/       # ❌ Это эпистема, не надсистема!
├── B2.Engine/
└── B3.Engine-Team/
```

### Почему это ошибка

- X1 = надсистема, в которую **физически** входит X2
- "Автомобильная отрасль" — это абстрактная область, не система
- Мотор физически входит в Автомобиль, не в "отрасль"

### Правильный подход

```
✅ Правильно:
B.Engine/
├── B1.Automobile/                # ✅ Физическая надсистема
│   └── B1.1.Meaning/
│       └── engine-role-in-car.md
├── B2.Engine/
└── B3.Engine-Team/
```

---

## Анти-паттерн 4: Использование "контура"

### Описание ошибки

Использование слова "контур" для обозначения части системы.

### Пример ошибки

```
❌ Неправильно:
B.Platform/
├── B2.Platform/
│   └── B2.2.Architecture/
│       ├── payment-contour.md        # ❌ "Контур" — запрещено
│       ├── analytics-contour.md      # ❌
│       └── notification-contour.md   # ❌
```

### Почему это ошибка

- "Контур" создаёт иллюзию границы без свойств системы
- Неясно: это подсистема? процесс? область ответственности?
- Размывает чёткое системное мышление

### Правильный подход

```
✅ Правильно:
B.Platform/
├── B2.Platform/
│   └── B2.2.Architecture/
│       ├── payment-subsystem.md      # ✅ Подсистема
│       ├── analytics-service.md      # ✅ Сервис
│       └── notification-module.md    # ✅ Модуль

# Или отдельные ядра, если это полноценные системы:
C.Payment-System/
D.Analytics-Service/
E.Notification-Service/
```

---

## Анти-паттерн 5: Процесс как ядро

### Описание ошибки

Создание ядра для процесса вместо системы.

### Пример ошибки

```
❌ Неправильно:
Project/
├── A.Product/
├── B.Onboarding-Process/     # ❌ Процесс — не система!
├── C.Deployment-Pipeline/    # ❌ Пайплайн — не система!
└── D.Review-Workflow/        # ❌ Workflow — не система!
```

### Почему это ошибка

- Процесс — это **работа системы**, не система сама
- У процесса нет владельца (владелец — у системы, которая выполняет процесс)
- Процессы описываются в F6/F9 соответствующей системы

### Правильный подход

```
✅ Правильно:
Project/
├── A.Product/
│   └── A2.Product/
│       └── A2.3.Operations/
│           └── onboarding-process.md   # ✅ Процесс в Operations
├── B.Platform/
│   └── B3.Dev-Team/
│       └── B3.3.Operations/
│           └── deployment-pipeline.md  # ✅ Процесс в Operations
```

---

## Анти-паттерн 6: Размножение ядер "на всякий случай"

### Описание ошибки

Создание ядер для всех возможных подсистем без реальной необходимости.

### Пример ошибки

```
❌ Неправильно (избыточно):
Project/
├── A.Product/
├── B.Frontend/
├── C.Backend/
├── D.Database/           # ❌ Возможно, достаточно описания в C
├── E.Cache/              # ❌ Возможно, достаточно описания в C
├── F.Queue/              # ❌ Возможно, достаточно описания в C
├── G.Logger/             # ❌ Точно достаточно описания
├── H.Config/             # ❌ Точно достаточно описания
└── I.Monitoring/         # ❓ Зависит от наличия отдельной команды
```

### Почему это ошибка

- Ядро нужно только если система достаточно сложна и автономна
- Ядро нужно только если есть отдельная команда или ответственный
- Избыточные ядра создают накладные расходы на поддержку

### Правильный подход

```
✅ Правильно (минималистично):
Project/
├── A.Product/
├── B.Frontend/
├── C.Backend/
│   └── C2.Backend/
│       └── C2.2.Architecture/
│           ├── database.md       # ✅ Описание в архитектуре
│           ├── cache.md          # ✅ Описание в архитектуре
│           └── queue.md          # ✅ Описание в архитектуре
└── D.Monitoring/                 # ✅ Если есть отдельная команда
```

### Критерий: когда создавать ядро?

| Критерий | Да → ядро | Нет → документ |
|----------|-----------|----------------|
| Отдельная команда | ✅ | ❌ |
| Свой жизненный цикл | ✅ | ❌ |
| Нужна полная документация F1-F9 | ✅ | ❌ |
| Достаточно описания в FX5 | ❌ | ✅ |

---

## Анти-паттерн 7: Абстрактные имена папок

### Описание ошибки

Использование абстрактных имён вместо конкретных названий систем.

### Пример ошибки

```
❌ Неправильно:
A.Target-System/
├── A1.Suprasystem/
├── A2.System-of-Interest/
└── A3.Constructor/
```

### Почему это ошибка

- Имена не несут информации о сути системы
- Невозможно понять проект по структуре папок
- Нарушает принцип осмысленного именования

### Правильный подход

```
✅ Правильно (Автомобиль):
A.Automobile/
├── A1.Taxi/                     # Физическая надсистема
├── A2.Automobile/
└── A3.Assembly-Line/            # Система-создатель

✅ Правильно (Приложение):
B.Mobile-App/
├── B1.User-Smartphone/          # Физическая надсистема
├── B2.Mobile-App/
└── B3.Dev-Team/                 # Система-создатель
```

---

## Сводная таблица анти-паттернов

| # | Анти-паттерн | Ключевая ошибка | Решение |
|---|--------------|-----------------|---------|
| 1 | Ядро по эпистеме | Экономика/Маркетинг как ядра | Описывать в F1-F9 |
| 2 | X3 как каталог | Структура X2 в X3 | Описывать в FX5 |
| 3 | Эпистемическая надсистема | "Отрасль" в X1 | Физическая надсистема |
| 4 | Использование "контура" | Размытие понятия системы | Подсистема/Сервис/Модуль |
| 5 | Процесс как ядро | Процесс вместо системы | Описывать в F6/F9 |
| 6 | Избыточные ядра | Ядро без команды | Описывать в FX5 |
| 7 | Абстрактные имена | Target-System вместо имени | Конкретные имена |

---

## См. также

- [01-kernels-model.md](01-kernels-model.md) → "Система vs Эпистема", "Фиксированная структура X1/X2/X3"
- [04-ontology.md](04-ontology.md) → "Запрещённые термины и конструкции"
- [CLAUDE.md](../../CLAUDE.md) → "КРИТИЧЕСКИЕ ПРАВИЛА multi-kernel S2R"


# SOURCE_FILE: 0.OPS/0.1.Knowledge-Logic/09-examples-library.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-15
family: F0
scope: repository
---

# Библиотека примеров для AI (Examples Library)

> **Для AI-агентов:** Этот документ содержит типовые примеры правильных и неправильных решений. Используйте как референс при работе с запросами пользователей.

## Раздел 1: Размещение документов

### Пример 1.1: Документ про требования к продукту

**Запрос:** "Где описать требования к нашему продукту?"

| Шаг | Вопрос | Ответ |
|-----|--------|-------|
| 1 | О какой системе? | Продукт = целевая система → Ядро A |
| 2 | Какой уровень? | Требования к самой системе → X2 (SoI) |
| 3 | Какая роль? | "Зачем? Что должно быть?" → Meaning (.1) |
| 4 | Семейство? | FA4 |

**Результат:** `A.{Product}/A2.{Product}/A2.1.Meaning/requirements.md`

---

### Пример 1.2: Документ про архитектуру бэкенда

**Запрос:** "Где описать архитектуру бэкенда?"

| Шаг | Вопрос | Ответ |
|-----|--------|-------|
| 1 | О какой системе? | Бэкенд = наша система → Ядро B/C (зависит от проекта) |
| 2 | Какой уровень? | Архитектура самой системы → X2 (SoI) |
| 3 | Какая роль? | "Как устроено?" → Architecture (.2) |
| 4 | Семейство? | FX5 |

**Результат:** `C.Backend/C2.Backend/C2.2.Architecture/architecture.md`

---

### Пример 1.3: Документ про процесс деплоя

**Запрос:** "Где описать процесс деплоя?"

| Шаг | Вопрос | Ответ |
|-----|--------|-------|
| 1 | О какой системе? | Деплой — процесс команды разработки → Ядро системы, которую деплоим |
| 2 | Какой уровень? | Процесс создания/поддержки → X3 (Constructor) |
| 3 | Какая роль? | "Как работает?" → Operations (.3) |
| 4 | Семейство? | FX9 |

**Результат:** `B.App/B3.Dev-Team/B3.3.Operations/deployment.md`

---

### Пример 1.4: Документ про рынок и конкурентов

**Запрос:** "Где описать анализ рынка?"

| Шаг | Вопрос | Ответ |
|-----|--------|-------|
| 1 | О какой системе? | Рынок = надсистема целевой системы → Ядро A |
| 2 | Какой уровень? | Контекст, в котором существует продукт → X1 (Suprasystem) |
| 3 | Какая роль? | "Зачем? Какой спрос?" → Meaning (.1) |
| 4 | Семейство? | FA1 |

**Результат:** `A.{Product}/A1.{Market}/A1.1.Meaning/market-analysis.md`

---

## Раздел 2: Создание ядер

### Пример 2.1: Правильное ядро — Мобильное приложение

**Запрос:** "Создай ядро для мобильного приложения"

**Проверка по критериям:**

| Критерий | Проверка | Результат |
|----------|----------|-----------|
| Владелец | Есть команда mobile | ✅ |
| Вход | Данные от API, действия пользователя | ✅ |
| Выход | UI, запросы к серверу | ✅ |
| Граница | Только мобильный клиент | ✅ |
| Цикл изменений | Версии в App Store | ✅ |

**Решение:** Создать ядро

```
B.Mobile-App/
├── B1.User-Device/          # Надсистема: смартфон пользователя
│   ├── B1.1.Meaning/
│   ├── B1.2.Architecture/
│   └── B1.3.Operations/
├── B2.Mobile-App/           # SoI: само приложение
│   ├── B2.1.Meaning/
│   ├── B2.2.Architecture/
│   └── B2.3.Operations/
└── B3.Mobile-Team/          # Constructor: команда разработки
    ├── B3.1.Meaning/
    ├── B3.2.Architecture/
    └── B3.3.Operations/
```

---

### Пример 2.2: Неправильное ядро — Маркетинг

**Запрос:** "Создай ядро для маркетинга"

**Проверка по критериям:**

| Критерий | Проверка | Результат |
|----------|----------|-----------|
| Владелец | Маркетолог? Но это роль, не владелец системы | ⚠️ |
| Вход | Что "принимает" маркетинг? Неясно | ❌ |
| Выход | Что "производит"? Неясно | ❌ |
| Граница | Что маркетинг НЕ делает? Размыто | ❌ |
| Цикл изменений | Нет версий/релизов | ❌ |

**Решение:** НЕ создавать ядро. Маркетинг — эпистема.

**Куда поместить:**
- Маркетинговая стратегия → `A1.../A1.1.Meaning/marketing-strategy.md` (FA1)
- Каналы продвижения → `A1.../A1.3.Operations/promotion-channels.md` (FA3)

**Исключение:** Если есть отдел маркетинга как команда с чёткими входами/выходами → можно создать ядро `D.Marketing-Team/` (но это ядро про команду, не про "маркетинг").

---

### Пример 2.3: Неправильное ядро — Аналитика

**Запрос:** "Создай ядро для аналитики"

**Проверка по критериям:**

| Критерий | Проверка | Результат |
|----------|----------|-----------|
| Владелец | Аналитик? | ⚠️ |
| Вход | Данные? Но откуда — неясно | ⚠️ |
| Выход | Отчёты? Инсайты? Размыто | ⚠️ |
| Граница | Что НЕ аналитика? | ❌ |
| Цикл изменений | Нет релизов | ❌ |

**Решение:** НЕ создавать ядро. "Аналитика" — эпистема.

**Куда поместить:**
- Метрики продукта → `A2.../A2.3.Operations/metrics.md` (FA6)
- Бизнес-аналитика → `A1.../A1.1.Meaning/business-analytics.md` (FA1)

**Исключение:** Если есть **Analytics Platform** (Amplitude, Mixpanel, собственная) как отдельная система с API → можно создать ядро `D.Analytics-Platform/`.

---

## Раздел 3: Типичные ошибки (анти-примеры)

### Анти-пример 3.1: X3 как каталог

**Неправильно:**

```
B.Ecosystem/
├── B1.Market/
├── B2.Ecosystem/
└── B3.Subsystems-Catalog/    ❌ X3 должен быть создателем!
    └── subsystems-list.md
```

**Правильно:**

```
B.Ecosystem/
├── B1.Market/
├── B2.Ecosystem/
│   └── B2.2.Architecture/
│       └── subsystems.md     ✅ Подсистемы в Architecture
└── B3.Ecosystem-Team/        ✅ X3 — создатель
```

---

### Анти-пример 3.2: Эпистемическая надсистема

**Неправильно:**

```
B.Engine/
├── B1.Automotive-Industry/   ❌ "Отрасль" — не физическая надсистема
├── B2.Engine/
└── B3.Engine-Team/
```

**Правильно:**

```
B.Engine/
├── B1.Automobile/            ✅ Мотор физически входит в автомобиль
├── B2.Engine/
└── B3.Engine-Team/
```

---

### Анти-пример 3.3: Абстрактные имена

**Неправильно:**

```
A.Target-System/              ❌ Неинформативно
├── A1.Suprasystem/           ❌ Это роль, не имя
├── A2.System-of-Interest/    ❌ Это роль, не имя
└── A3.Constructor/           ❌ Это роль, не имя
```

**Правильно (Автомобиль):**

```
A.Automobile/                 ✅ Конкретное имя
├── A1.Taxi/                  ✅ Физическая надсистема
├── A2.Automobile/            ✅ Конкретное имя SoI
└── A3.Assembly-Line/         ✅ Система-создатель
```

**Правильно (Приложение):**

```
B.Mobile-App/                 ✅ Конкретное имя
├── B1.User-Smartphone/       ✅ Физическая надсистема
├── B2.Mobile-App/            ✅ Конкретное имя SoI
└── B3.Dev-Team/              ✅ Система-создатель
```

---

### Анти-пример 3.4: Использование "контура"

**Неправильно:**

```
B2.Platform/
└── B2.2.Architecture/
    ├── payment-contour.md    ❌ "Контур" запрещён
    └── analytics-contour.md  ❌
```

**Правильно:**

```
B2.Platform/
└── B2.2.Architecture/
    ├── payment-subsystem.md  ✅ "Подсистема"
    └── analytics-service.md  ✅ "Сервис"
```

---

## Раздел 4: Примеры frontmatter

### Пример 4.1: Документ в ядре A, семейство FA4

```yaml
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA4
system: System-of-Interest
role: Meaning
related:
  - A2.1.Meaning/vision.md
  - A2.2.Architecture/overview.md
---
```

### Пример 4.2: Документ в ядре B, семейство FB5

```yaml
---
type: doc
status: draft
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB5
system: System-of-Interest
role: Architecture
related:
  - B2.1.Meaning/requirements.md
  - ../C.Backend/C2.2.Architecture/api-spec.md
---
```

### Пример 4.3: Документ F0 (метаэпистема)

```yaml
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---
```

---

## Раздел 5: Примеры связей между ядрами

### Пример 5.1: Подсистема как отдельное ядро

```
Ситуация: Мобильное приложение (B) использует Backend API (C)

Описание связи:
- В B2.2.Architecture/ → ссылка на C2.2.Architecture/api-spec.md
- В 0.2.Kernels-Bridge/02-kernels-relations.md → B↔C: API integration
- В C1.3.Operations/ → описание SLA для B
```

### Пример 5.2: Цепочка создания

```
Ситуация: Команда-4 развивает Команду-2, которая создаёт Конвейер

A.Automobile/         → целевая система
C.Assembly-Line/      → создаёт A, управляется командой-2
E.Team-2/             → команда-2 как система, создаётся командой-4

Связи:
- A ← C (C создаёт A)
- C ← E (E развивает C3)
```

---

## Раздел 6: Примеры Context Pack

> **Для AI-агентов:** Context Pack — это структурированный пакет контекста из репозитория, который собирается ПЕРЕД формированием финального ответа. Используй эти примеры как эталон оформления.

### Пример 6.1: Куда положить описание требований к авторизации?

**Запрос:** "Где описать требования к авторизации?"

#### Гипотезы (шаг 1.0)

```
Гипотеза 1: Требования к авторизации как функции целевой системы → F4 (уверенность: высокая)
Гипотеза 2: Процесс авторизации в системе создания → F9 (уверенность: низкая)
Гипотеза 3: Интерфейс авторизации с внешними системами → F2/F3 (уверенность: средняя)
```

#### Context Pack

```
## Context Pack для "Где описать требования к авторизации?"

### Использованные источники:
1. `0.1.Knowledge-Logic/02-document-families.md:151-160` — FX4: требования и спецификации
2. `0.3.Roles-Matrix-3x3/roles-matrix.md:145-177` — FX4: Визионер целевой системы
3. `0.1.Knowledge-Logic/02-document-families.md:131-140` — FX2: внешние API и интеграции

### Ключевые выдержки:
> FX4: System-of-Interest × Предприниматель — "Документы о ценности целевой системы: Требования и спецификации, JTBD и сценарии использования" (02-document-families.md:155-158)
> FX2: Suprasystem × Инженер — "Документы об окружении как системе: Внешние API и интеграции" (02-document-families.md:135-139)

### Не использовано (и почему):
- roles-matrix.md:FX9 — описывает роли команды, не функциональные требования системы
- 04-ontology.md — содержит общие термины, не специфику размещения
```

#### Результат

**Ответ:** Требования к авторизации относятся к **FX4** (Целевая система × Предприниматель / Meaning), т.к. это функциональное требование к системе. Путь: `A2.{System}/A2.1.Meaning/auth-requirements.md`.

Если авторизация — это интеграция с внешним сервисом (OAuth, LDAP), часть описания может идти в **FX2** (интерфейсы с внешними системами).

---

### Пример 6.2: Что такое семейство F7?

**Запрос:** "Объясни, что такое семейство F7"

#### Гипотезы (шаг 1.0)

```
Гипотеза 1: Вопрос о содержании семейства F7 по модели документов (уверенность: высокая)
Гипотеза 2: Вопрос о роли FX7 в матрице 3×3 (уверенность: высокая)
```

#### Context Pack

```
## Context Pack для "Что такое семейство F7?"

### Использованные источники:
1. `0.1.Knowledge-Logic/02-document-families.md:181-190` — FX7: Constructor × Предприниматель
2. `0.3.Roles-Matrix-3x3/roles-matrix.md:255-286` — FX7: Бизнесмен/Инвестор

### Ключевые выдержки:
> FX7: Constructor × Предприниматель — "Документы о принципах создателя: Видение и миссия команды, Экономика создания, Принципы работы, Стратегия развития" (02-document-families.md:183-189)

> FX7: Бизнесмен/Инвестор — "Что видит: Где ценность растёт, какие проекты перспективны, как распределять ресурсы. Что делает: Определяет стратегию, поддерживает рост, инвестирует в направления. Результаты: Финансовые средства, инвестиционные решения, портфель проектов, финансовые модели" (roles-matrix.md:255-280)

### Не использовано (и почему):
- 01-kernels-model.md — описывает общую модель, не конкретное семейство
- fpf-integration.md — не содержит описания семейств
```

#### Результат

**Ответ:** Семейство **FX7** (Constructor × Предприниматель / Meaning) отвечает на вопрос "Зачем нам система создания?" и фокусируется на:

- **Экономика создания** — бизнес-модель команды/компании
- **Инвестиции и стратегия** — распределение ресурсов
- **Видение и миссия** — принципы работы системы создания

Роль: **Бизнесмен/Инвестор**. Путь: `X3.{Constructor}/X3.1.Meaning/`.

---

### Пример 6.3: Связь между ядрами (сложный запрос)

**Запрос:** "Как описать, что Backend используется Mobile App?"

#### Гипотезы (шаг 1.0)

```
Гипотеза 1: Вопрос о связях между ядрами в Kernels-Bridge (уверенность: высокая)
Гипотеза 2: Вопрос об интерфейсах в F2/F5 (уверенность: средняя)
Гипотеза 3: Вопрос о структуре связанности систем (уверенность: средняя)
```

#### Context Pack

```
## Context Pack для "Как описать, что Backend используется Mobile App?"

### Использованные источники:
1. `0.2.Kernels-Bridge/02-kernels-relations.md` — матрица связей между ядрами
2. `0.2.Kernels-Bridge/03-systems-relations.md` — структура связанности систем
3. `0.1.Knowledge-Logic/02-document-families.md:131-140` — FX2: интерфейсы с окружением
4. `0.1.Knowledge-Logic/02-document-families.md:161-170` — FX5: архитектура

### Ключевые выдержки:
> Типы связей: "Создаёт (→)" — одна система создаёт другую; "Входит в состав (⊂)" — подсистема; "В окружении (↔)" — взаимодействие без вложенности (03-systems-relations.md)

> FX2: "Внешние API и интеграции, Зависимости от внешних систем, Интерфейсы с окружением" (02-document-families.md:137-139)

### Не использовано:
- 01-value-chain.md — описывает цепочку создания, а не использования
```

#### Результат

**Ответ:** Связь "Backend используется Mobile App" описывается в нескольких местах:

1. **Матрица связей** (`0.2.Kernels-Bridge/02-kernels-relations.md`): B↔C — API integration
2. **В ядре Mobile App** (`B1.../B1.2.Architecture/`): описание зависимости от Backend API (FX2)
3. **В ядре Backend** (`C2.../C2.2.Architecture/`): спецификация API для клиентов (FX5)

Тип связи: **"В окружении" (↔)** — системы взаимодействуют, но не вложены друг в друга.

---

### Пример 6.4: Минимальный Context Pack (простой запрос)

**Запрос:** "В какой папке хранить README ядра?"

#### Гипотезы

```
Гипотеза 1: Вопрос о структуре папок ядра (уверенность: высокая)
```

#### Context Pack (сокращённый)

```
## Context Pack для "В какой папке хранить README ядра?"

### Источник:
1. `0.1.Knowledge-Logic/01-kernels-model.md` — структура ядра

### Выдержка:
> Структура ядра: "X.Kernel-Name/README.md" — в корне папки ядра
```

#### Результат

**Ответ:** README ядра размещается в корне папки ядра: `X.Kernel-Name/README.md`

---

## См. также

- [CLAUDE.md](../../CLAUDE.md) → Часть 3.5: Режим Repository-First
- [CLAUDE.md](../../CLAUDE.md) → Часть 5: Примеры рассуждений
- [08-anti-patterns.md](08-anti-patterns.md) → Полный список анти-паттернов
- [01-kernels-model.md](01-kernels-model.md) → Модель ядер
- [02-document-families.md](02-document-families.md) → Семейства документов


# SOURCE_FILE: 0.OPS/0.2.Kernels-Bridge/01-value-chain.md
---
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
fpf_patterns:
  - A.1
  - A.3
---

# Цепочка создания ценности (Value Chain)

> **Для AI-агентов:** Используйте этот документ для построения графа систем конкретного проекта. Заполните шаблоны на основе описания проекта от пользователя.

## Концепция

**Цепочка создания ценности** показывает, как системы в проекте связаны через создание и использование друг друга.

```
[Конечная ценность для пользователя]
                ↑
                │ создаёт
                │
    [Целевая система — Ядро A]
                ↑
                │ создаёт / входит в состав
                │
     [Наши системы — Ядра B, C...]
                ↑
                │ создаёт
                │
      [Команды, инструменты...]
```

## Граф создателей (FPF A.3)

Согласно FPF, для каждой целевой системы существует **граф создателей** — совокупность систем, которые её создают. Этот граф может быть:
- **Линейным:** A ← B ← C
- **Разветвлённым:** A ← (B, C, D)
- **Сетевым:** сложные взаимосвязи

### Типы связей между системами

| Тип связи | Обозначение | Описание | Примеры |
|-----------|-------------|----------|---------|
| **Создаёт** | → | Система X производит, поддерживает, ремонтирует, модернизирует или ликвидирует систему Y | Конвейер → Автомобиль; Команда обслуживания → Сервер |
| **Входит в состав** | ⊂ | Система X является частью системы Y | Мотор ⊂ Автомобиль; Модуль авторизации ⊂ Backend |
| **В окружении** | ↔ | Системы X и Y находятся в окружении друг друга, взаимодействуют через интерфейсы (используют друг друга, обмениваются данными) | Frontend ↔ Backend; Приложение ↔ API; Дашборд ↔ Аналитика |

### Важные пояснения к связям

**"Создаёт" включает весь жизненный цикл:**
- Производство (изготовление)
- Поддержка (обеспечение работы)
- Ремонт (восстановление)
- Модернизация (улучшение)
- Ликвидация (утилизация)

Все эти действия выполняются **системой-создателем** (Constructor) относительно целевой системы.

**"В окружении" означает взаимодействие:**
- Системы обмениваются данными, ресурсами или сигналами
- Обе системы существуют самостоятельно
- Связь через определённые интерфейсы
- Включает: "использует", "получает от", "передаёт в"

## Структура цепочки

### Уровень 0: Конечная ценность

То, что получает пользователь/клиент в результате работы всех систем.

### Уровень 1: Целевая система (Ядро A)

Главная система проекта, непосредственно создающая ценность.

### Уровень 2: Наши системы (Ядра B, C...)

Системы, создающие целевую систему или входящие в её состав.

### Уровень 3+: Глубина цепочки

Системы, создающие системы уровня 2, и так далее.

## Шаблон цепочки

> **Инструкция для AI:** При развёртывании репозитория заполните этот шаблон на основе описания проекта.

```
┌─────────────────────────────────────────────────────────────────────┐
│                     [КОНЕЧНАЯ ЦЕННОСТЬ]                             │
│                 (что получает пользователь)                         │
└────────────────────────────┬────────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    A. [SOI-Name]                                    │
│                                                                     │
│  A1: [Suprasystem-Name] — надсистема (физическая система)           │
│  A2: [SOI-Name] — целевая система                                   │
│  A3: [Constructor-Name] — создатель                                 │
└────────────────────────────┬────────────────────────────────────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
┌───────────────────┐ ┌───────────────┐ ┌───────────────┐
│ B. [System-Name]  │ │ C. [System]   │ │ D. [System]   │
│                   │ │               │ │               │
│ B1: [Supra]       │ │ C1: [Supra]   │ │ D1: [Supra]   │
│ B2: [SOI]         │ │ C2: [SOI]     │ │ D2: [SOI]     │
│ B3: [Constr]      │ │ C3: [Constr]  │ │ D3: [Constr]  │
└───────────────────┘ └───────────────┘ └───────────────┘
```

## Правила построения цепочки

### Правило 1: Сверху — ценность, снизу — создатели

Читается сверху вниз: от ценности к создателям.
Читается снизу вверх: от создателей к ценности.

### Правило 2: Стрелка показывает направление создания

```
A ← B означает: B создаёт A
```

### Правило 3: Один уровень — одна глубина создания

Системы на одном горизонтальном уровне имеют одинаковую "дистанцию" до конечной ценности.

### Правило 4: Граф, а не дерево

Система может создавать несколько других систем. Несколько систем могут создавать одну систему.

## Реестр ядер

> **Заполняется при развёртывании репозитория.**

| Ядро | Название системы | Тип связи с A | Позиция | Создатели |
|------|------------------|---------------|---------|-----------|
| A | *[SOI-Name]* | Target | Уровень 1 | C... |
| B | *[System-Name]* | Входит в состав A | Уровень 2 | D... |
| C | *[System-Name]* | Создаёт A | Уровень 2 | E... |

## Примеры цепочек

### Пример 1: Автомобильное производство (развёрнутый)

Этот пример демонстрирует многоуровневую цепочку с разными командами и необходимостью координации.

**Ситуация:** Четыре команды работают над проектом автомобиля:
- Команда-1: отвечает за мотор (подсистема автомобиля)
- Команда-2: отвечает за конвейер (создаёт автомобиль)
- Команда-3: отвечает за станок ЧПУ (часть конвейера)
- Команда-4: отвечает за команду-2 (развивает её)

```
                    [Довольный владелец автомобиля]
                                  ↑
┌─────────────────────────────────────────────────────────────────────┐
│                        A. Automobile/                               │
│                   Целевая система проекта                          │
│                                                                     │
│  A1: Taxi — надсистема (такси = водитель + автомобиль)             │
│  A2: Automobile — автомобиль                                        │
│  A3: Assembly-Line — система производства                          │
└─────────────────────────────────────────────────────────────────────┘
            ↑ создаёт                        ↑ входит в состав
            │                                │
┌───────────────────────────┐   ┌───────────────────────────┐
│      C. Assembly-Line/    │   │      B. Engine/           │
│  "Наша система" команды-2 │   │  "Наша система" команды-1 │
│                           │   │                           │
│  Конвейер создаёт         │   │  Мотор — подсистема       │
│  автомобиль               │   │  автомобиля               │
└───────────────────────────┘   └───────────────────────────┘
            ↑
    ┌───────┴───────┐
    ↓               ↓
┌───────────────┐   ┌───────────────────────┐
│ D. CNC-       │   │    E. Team-2/         │
│   Machine/    │   │ "Наша система" ком.-4 │
│ "Наша сист."  │   │                       │
│  команды-3    │   │ Команда-2             │
│               │   │ (мета-уровень)        │
│ Станок —      │   │                       │
│ входит в      │   │ E3 создаёт C3         │
│ состав конв.  │   │                       │
└───────────────┘   └───────────────────────┘
```

**Ключевые связи:**

| Связь | Тип | Что требует согласования |
|-------|-----|--------------------------|
| C → A | Создаёт | Спецификации сборки автомобиля |
| B ⊂ A | Входит в состав | Интерфейс установки мотора |
| D ⊂ C | Входит в состав | Спецификации деталей для станка |
| E → C3 | Создаёт | План развития команды конвейера |
| B ↔ C | В окружении | Интеграция мотора в процесс сборки |

**Необходимая коммуникация между командами:**

1. **Команда-1 ↔ Команда-2:** Согласование интерфейса установки мотора
2. **Команда-2 ↔ Команда-3:** Спецификации деталей и график производства
3. **Команда-2 ↔ Команда-4:** Планы развития и обратная связь
4. **Все команды → 0.OPS/:** Согласование общей терминологии

> **Важно (FPF A.1.1):** Разные команды могут использовать одинаковые термины в разных значениях (например, "узел", "цикл"). Необходимо согласование онтологий через `0.OPS/0.1.Knowledge-Logic/04-ontology.md` и локальные онтологии каждого ядра.

---

### Пример 2: SaaS-платформа

```
[Рост бизнеса клиента]
         ↑
A. Client-Business/
├── A1.Market-Environment/         # Рыночное окружение клиента
├── A2.Client-Business/            # Бизнес клиента
└── A3.SaaS-Platform/              # Наша платформа создаёт успех клиента
         ↑
    ┌────┴────┐
    ↓         ↓
B. SaaS-     C. Support-
   Platform/    Service/
    ↑            ↑
    │            │
D. Dev-      E. Support-
   Team/        Team/
```

**Связи:**
- A3 → A2: SaaS-платформа создаёт успех бизнеса клиента
- D → B: Dev-Team создаёт SaaS-Platform
- E → C: Support-Team создаёт Support-Service
- B ↔ C: Платформа и поддержка в окружении друг друга (интеграция)

### Пример 3: Мобильное приложение

```
[Удовлетворённый пользователь]
            ↑
   A. Mobile-App/
   ├── A1.User-Smartphone/         # Смартфон пользователя
   ├── A2.Mobile-App/              # Наше приложение
   └── A3.Dev-Team/                # Команда разработки
            ↑
      ┌─────┼─────┐
      ↓     ↓     ↓
 B. Auth-  C. Backend- D. Analytics-
    Module/   API/        Service/
```

**Связи:**
- B ⊂ A: Auth-Module входит в состав Mobile-App
- A ↔ C: Mobile-App в окружении Backend-API (обмен данными)
- A ↔ D: Mobile-App в окружении Analytics-Service (получает данные)

### Пример 4: Система умного дома

```
[Комфорт жильца]
           ↑
  A. Smart-Home/
  ├── A1.House/                    # Физическая надсистема (дом)
  ├── A2.Smart-Home/               # Система умного дома
  └── A3.Installation-Team/        # Команда установки
           ↑
   B. IoT-Hub/
   ├── B1.Smart-Home/              # Hub входит в состав Smart-Home
   ├── B2.IoT-Hub/
   └── B3.Hardware-Team/
           ↑
     ┌─────┼─────┐
     ↓     ↓     ↓
C. Sensors/ D. Cloud/ E. Mobile-App/
```

**Связи:**
- B ⊂ A: IoT-Hub входит в состав Smart-Home
- C ⊂ B: Sensors входят в состав IoT-Hub
- B ↔ D: IoT-Hub в окружении Cloud (обмен данными)
- B ↔ E: IoT-Hub в окружении Mobile-App (управление)

## Как использовать цепочку

### При создании репозитория (для AI)

1. Запросите у пользователя описание проекта
2. Определите конечную ценность
3. Определите целевую систему (Ядро A)
4. Определите "наши системы" (Ядра B, C...)
5. Определите тип связи каждой системы с A:
   - **Входит в состав** — подсистема
   - **Создаёт** — система-создатель
   - **В окружении** — система взаимодействует через интерфейсы
6. Постройте граф связей
7. Заполните шаблон выше

### При добавлении нового ядра

1. Определите тип связи с существующими системами
2. Нарисуйте связи с существующими ядрами
3. Обновите диаграмму
4. Обновите реестр ядер

### При анализе проекта

1. Прочитайте цепочку сверху вниз (от ценности)
2. Проверьте, что все связи обоснованы и указан их тип
3. Найдите "разрывы" — системы без создателей
4. Найдите "сироты" — системы без влияния на ценность

## Связь с другими документами

| Документ | Связь |
|----------|-------|
| [02-kernels-relations.md](02-kernels-relations.md) | Детали связей между ядрами |
| [03-systems-relations.md](03-systems-relations.md) | Структура связанности систем |
| [../0.1.Knowledge-Logic/03-our-systems-map.md](../0.1.Knowledge-Logic/03-our-systems-map.md) | Карта всех систем |

## См. также

- [../0.1.Knowledge-Logic/01-kernels-model.md](../0.1.Knowledge-Logic/01-kernels-model.md) — модель ядер
- [02-kernels-relations.md](02-kernels-relations.md) — матрица связей


# SOURCE_FILE: 0.OPS/0.2.Kernels-Bridge/02-kernels-relations.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Матрица связей между ядрами (Kernels Relations)

## Типы связей

| Тип связи | Обозначение | Описание |
|-----------|-------------|----------|
| **Создаёт** | → | Система X производит, поддерживает, ремонтирует, модернизирует или ликвидирует систему Y |
| **Входит в состав** | ⊂ | Система X является частью системы Y |
| **В окружении** | ↔ | Системы X и Y взаимодействуют через интерфейсы (используют друг друга, обмениваются данными) |

## Матрица связей

> **TODO:** Заполните при добавлении ядер.

|     | A | B | C | D |
|-----|---|---|---|---|
| **A** | — | ⊃ | ← | ↔ |
| **B** | ⊂ | — | ↔ | — |
| **C** | → | ↔ | — | ← |
| **D** | ↔ | — | → | — |

**Легенда:**
- `→` — строка создаёт столбец
- `←` — столбец создаёт строку
- `⊂` — строка входит в состав столбца
- `⊃` — столбец входит в состав строки
- `↔` — системы в окружении друг друга
- `—` — нет прямой связи

## Описание связей

### A ⊃ B (B входит в состав A)

> **TODO:** Опишите связь

**Тип:** Входит в состав

**Описание:** ...

**Интерфейс:** ...

### C → A (C создаёт A)

> **TODO:** Опишите связь

**Тип:** Создаёт

**Описание:** ...

### B ↔ C (В окружении)

> **TODO:** Опишите связь

**Тип:** В окружении

**Описание:** ...

**Интерфейс:** ...

## Шаблон описания связи

```markdown
### [Ядро X] → [Ядро Y]

**Тип:** Создаёт | Входит в состав | В окружении

**Описание:** [Как X связан с Y]

**Артефакты связи:**
- [документ в X, описывающий связь]
- [документ в Y, описывающий связь]

**Интерфейс:**
- [API, контракт, протокол, физический интерфейс]
```

## Примеры заполненных связей

### Пример: Автомобильное производство

|     | A.Automobile | B.Engine | C.Assembly-Line |
|-----|--------------|----------|-----------------|
| **A.Automobile** | — | ⊃ | ← |
| **B.Engine** | ⊂ | — | ↔ |
| **C.Assembly-Line** | → | ↔ | — |

**Описание связей:**

- **B ⊂ A:** Мотор входит в состав автомобиля
- **C → A:** Конвейер создаёт автомобиль
- **B ↔ C:** Мотор и конвейер в окружении друг друга (интеграция при сборке)

## См. также

- [01-value-chain.md](01-value-chain.md) — цепочка ценности
- [03-systems-relations.md](03-systems-relations.md) — структура связанности систем


# SOURCE_FILE: 0.OPS/0.2.Kernels-Bridge/03-systems-relations.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Структура связанности систем (Systems Relations Structure)

## Концепция

Структура связанности показывает, как системы соотносятся друг с другом:
- Какие системы входят в состав других
- Какие системы создают другие
- Какие системы взаимодействуют в окружении

> **Важно:** Это не иерархия с "уровнями важности". Это структура отношений между системами.

## Типы связей

| Тип связи | Обозначение | Описание |
|-----------|-------------|----------|
| **Создаёт** | → | Система X производит/поддерживает/ремонтирует систему Y |
| **Входит в состав** | ⊂ | Система X является частью системы Y |
| **В окружении** | ↔ | Системы взаимодействуют через интерфейсы |

## Текущая карта

> **TODO:** Заполните при инициализации проекта.

```
Шаблон:

[Надсистема A1 — физическая система]
│
├── A. Целевая система (A2)
│   ├── [подсистема] ⊂ A → может быть ядром B
│   └── [подсистема] ⊂ A → может быть ядром C
│
├── [Создатель A3] → создаёт A
│   ├── [часть создателя] ⊂ A3 → может быть ядром D
│   └── ...
│
└── [Внешняя система] ↔ в окружении A
```

## Позиции систем

### Надсистема (A1)

Физическая система, в которую входит целевая система.

**Пример:** Такси (водитель + автомобиль) — надсистема для автомобиля.

### Целевая система (A2)

Главная система, ради которой существует проект.

**Пример:** Автомобиль — целевая система проекта.

### Наши системы (B, C, D...)

Системы, с которыми работают команды проекта:

| Позиция | Тип связи | Пример |
|---------|-----------|--------|
| Подсистема | B ⊂ A | Мотор входит в состав автомобиля |
| Создатель | C → A | Конвейер создаёт автомобиль |
| В окружении | D ↔ A | Дилерская сеть взаимодействует с автомобилем |

### Создатель целевой системы (A3)

Система, которая создаёт целевую систему.

**Пример:** Конвейер — создатель автомобиля.

## Правила определения позиции

| Вопрос | Позиция | Тип связи |
|--------|---------|-----------|
| Целевая система входит в эту систему? | Надсистема (A1) | A2 ⊂ A1 |
| Это главная цель проекта? | Целевая система (A2) | — |
| Это часть целевой системы? | Наша система (B...) | B ⊂ A |
| Это создаёт целевую систему? | Наша система (C...) | C → A |
| Это взаимодействует с целевой? | Наша система (D...) | D ↔ A |

## Когда выделять в отдельное ядро?

**Да, выделяй:**
- Есть отдельная команда
- Свой жизненный цикл
- Нужна детальная документация

**Нет, опиши в FX5:**
- Простой компонент
- Нет отдельной команды
- Достаточно краткого описания

## Пример: Автомобильное производство

```
[Такси — надсистема (A1)]
│
├── A. Автомобиль (A2) — целевая система
│   ├── B. Мотор ⊂ A (входит в состав)
│   ├── Колёса (описаны в A2.2.Architecture)
│   └── Кузов (описан в A2.2.Architecture)
│
├── C. Конвейер → A (создаёт)
│   ├── D. Станок ЧПУ ⊂ C (входит в состав)
│   └── E. Команда-2 → C (создаёт)
│
└── F. Дилерская сеть ↔ A (в окружении)
```

## См. также

- [01-value-chain.md](01-value-chain.md) — цепочка ценности
- [02-kernels-relations.md](02-kernels-relations.md) — матрица связей
- [../0.1.Knowledge-Logic/01-kernels-model.md](../0.1.Knowledge-Logic/01-kernels-model.md) — модель ядер


# SOURCE_FILE: 0.OPS/0.3.Roles-Matrix-3x3/roles-matrix-brief.md
---
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Краткая матрица ролей 3×3

> **Для AI-агентов:** Используй эту краткую таблицу для быстрого понимания зон ответственности. Полное описание: [roles-matrix.md](roles-matrix.md)

## Матрица: ключевые слова

| Уровень \ Роль | Предприниматель (X.1) | Инженер (X.2) | Менеджер (X.3) |
|----------------|----------------------|---------------|----------------|
| **1.X. Надсистема** | **Спрос / Оффер** | **Сценарии / Прототип** | **Доверие / Репутация** |
| **2.X. Целевая система** | **Смысл / Границы** | **Архитектура / Интерфейсы** | **SLO / Incidents** |
| **3.X. Система создания** | **Стратегия / Инвестиции** | **CI/CD / Quality** | **Ресурсы / Регламенты** |

## Матрица: роли

| Уровень \ Роль | Предприниматель (X.1) | Инженер (X.2) | Менеджер (X.3) |
|----------------|----------------------|---------------|----------------|
| **1.X. Надсистема** | FX1: Продвиженец | FX2: Владелец продукта | FX3: PR/GR |
| **2.X. Целевая система** | FX4: Визионер ЦС | FX5: Инженер ЦС | FX6: Оператор ЦС |
| **3.X. Система создания** | FX7: Бизнесмен | FX8: Организатор разработки | FX9: Администратор |

## Матрица: что видит и удерживает

| Уровень \ Роль | Предприниматель (X.1) | Инженер (X.2) | Менеджер (X.3) |
|----------------|----------------------|---------------|----------------|
| **1.X. Надсистема** | Люди, проблемы, мотивы | Работа пользователя, сценарии | Партнёры, регуляторы, медиа |
| **2.X. Целевая система** | Функция, границы, ценность | Конструкция, интерфейсы | Эксплуатация, сбои, нагрузка |
| **3.X. Система создания** | Рост, риски, инвестиции | Процессы, инструменты, качество | Люди, роли, бюджеты |

## Матрица: ключевые результаты

| Уровень \ Роль | Предприниматель (X.1) | Инженер (X.2) | Менеджер (X.3) |
|----------------|----------------------|---------------|----------------|
| **1.X. Надсистема** | Гипотезы ценности, офферы | Сценарии использования | Каналы, репутация |
| **2.X. Целевая система** | Образ и границы ЦС | Архитектура, прототип | SLO/SLA, инциденты |
| **3.X. Система создания** | Стратегия, портфель | CI/CD, стандарты | Регламенты, бюджеты |

---

## См. также

- [roles-matrix.md](roles-matrix.md) — полное описание ролей с методами и метриками
- [../0.1.Knowledge-Logic/02-document-families.md](../0.1.Knowledge-Logic/02-document-families.md) — семейства документов F1-F9


# SOURCE_FILE: 0.OPS/0.3.Roles-Matrix-3x3/roles-matrix.md
---
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
fpf_patterns:
  - A.3      # System Triad
  - U.RoleAssignment
---

# Матрица ролей 3×3 (Roles Matrix)

> **Для AI-агентов:** Этот документ определяет 9 проектных ролей и их области ответственности. Используйте для понимания, какие документы создавать и какие методы применять.
>
> **Краткая версия:** [roles-matrix-brief.md](roles-matrix-brief.md)

## Обзор матрицы

```
                     Предприниматель    Инженер              Менеджер
                     (Meaning)          (Architecture)       (Operations)
┌──────────────────────────────────────────────────────────────────────────┐
│ X1. Надсистема     FX1                FX2                  FX3           │
│                    Продвиженец        Владелец продукта    PR/GR         │
├──────────────────────────────────────────────────────────────────────────┤
│ X2. Целевая        FX4                FX5                  FX6           │
│     система        Визионер ЦС        Инженер ЦС           Оператор ЦС   │
├──────────────────────────────────────────────────────────────────────────┤
│ X3. Система        FX7                FX8                  FX9           │
│     создания       Бизнесмен          Организатор          Администратор │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## 1.Х. Область интересов надсистемы

### 1.1. Продвиженец (FX1)
*надсистема × предприниматель*

**Что видит и удерживает:**
Людей и группы в надсистеме, их жизненные и рабочие проблемы, ограничения, мотивы, способы принятия решений.

**Что делает:**
Переводит реальные проблемы людей в формулировку задач для будущей системы. Проверяет гипотезы ценности, ищет форматы, которые решают проблему лучше, чем текущие альтернативы.

**Методы (SoTA):**
- Jobs-to-Be-Done (modern versions: Intercom, Rewired Group)
- Problem discovery interviews
- Market Ethnography
- JTBD-Demand Curve Mapping
- Narrative Mapping
- Early Signal Testing (message testing, micro-funnels)
- Problem–Solution Fit validation

**Результаты:**
- Сегменты надсистемы в состоянии «осознанная задача и готовность к покупке»
- Гипотезы ценности, оформленные как сценарии изменения поведения
- Результаты тестов сообщений и офферов
- Карты «задача → решение → ограничение»

**Метрики:**
- Степень соответствия задачи реальному поведению людей
- Доля гипотез ценности, подтверждённых реальными людьми
- Ясность формулировок задач для внутренних ролей
- Сила связи «задача → решение»

---

### 1.2. Владелец продукта (FX2)
*надсистема × инженер*

**Что видит и удерживает:**
Какую работу люди хотят выполнить с помощью системы, какие сценарии должны быть поддержаны и как система будет использоваться в реальных условиях.

**Что делает:**
Формулирует сценарии использования и продуктовые решения. Переводит задачи в «что именно система должна уметь делать», но не через требования, а через поведенческие шаблоны и работу пользователя.

**Методы (SoTA):**
- Product Discovery (Teresa Torres)
- Opportunity-Solution Tree
- Modern Product Specification (Ben Horowitz school)
- User Story Mapping (упрощённые, поведенческие варианты)
- Outcome-Driven Innovation (Ulwick)
- Service Blueprinting
- Contextual Inquiry
- Behavioral Prototyping
- Job-Map decomposition (современная версия JTBD)

**Результаты:**
- Сценарии использования будущей целевой системы
- Карты возможностей (opportunities) и решений
- Продуктовые гипотезы и их подтверждения
- Карты работы пользователя до/во время/после взаимодействия с системой
- Дорожная карта развития (отдельно от описаний сценариев)

**Метрики:**
- Понимание сценариев всеми проектными ролями
- Подтверждаемость сценариев реальными пользователями
- Согласованность сценариев внутри команды разработки
- Количество сценариев, прошедших проверку «полезно — понятно — возможно реализовать»

---

### 1.3. PR/GR (FX3)
*надсистема × менеджер*

**Что видит и удерживает:**
Окружение системы: партнёров, государственные структуры, сообщества, медиа, и их ожидания, нормы и требования.

**Что делает:**
Выстраивает отношения, создает и поддерживает публичный образ, обеспечивает соблюдение правил и устойчивое взаимодействие.

**Методы (SoTA):**
- Reputation Management frameworks
- Public Narrative (Ganz)
- Community-Based Strategy
- Public Diplomacy techniques
- Issue-Mapping & Conflict-Mapping
- Regulatory Foresight
- Long-Horizon Media Planning
- Crisis Communication Protocols

**Результаты:**
- Основные внешние проектные роли в согласии, выстроенные каналы коммуникации
- Документы по регуляторному соответствию
- Карты ролей в надсистеме и их ожиданий
- План коммуникаций, медиа-стратегия
- Материалы для партнёров, регуляторов, медиа
- Публичный образ и его описание
- Реестр обязательств перед внешними ролями

**Метрики:**
- Уровень доверия внешних ролей к организации
- Наличие или отсутствие конфликтов между организацией и внешними ролями
- Соответствие действий организации нормам и обязательствам внешней среды
- Понятность публичных сообщений для внешних групп

---

## 2.Х. Область интересов целевой системы

### 2.1. Визионер целевой системы (FX4)
*целевая система × предприниматель*

**Что видит и удерживает:**
Функцию будущей системы и её востребованность, её границы, роль в мире, место среди альтернатив и желаемый эффект от её существования.

**Что делает:**
Формирует образ целевой системы — что она делает, какую пользу приносит, какие принципы и ограничения определяют её конструкцию, а также насколько выгодно её создавать.

**Методы (SoTA):**
- Systems Mapping
- System Framing & Boundary Setting
- Concept Architecture
- Value-Network Analysis
- Purpose-Driven Design
- Morphological Analysis
- Design Space Exploration

**Результаты:**
- Согласованный образ и границы ЦС
- Описание функций целевой системы и её название
- Картина «зачем эта система нужна миру» и что можно за неё получить
- Оценка стоимости ЦС на рынке
- Эскизные архитектуры (концептуальные уровни)
- Модель границ системы и её окружения
- Ключевые принципы и ограничения

**Метрики:**
- Ясность функции целевой системы для команды
- Правильность границ системы относительно окружающих систем
- Согласованность концепции с реальными задачами людей
- Согласованность образа системы между ролями

---

### 2.2. Инженер целевой системы (FX5)
*целевая система × инженер*

**Что видит и удерживает:**
Конструкцию системы, внутренние и внешние интерфейсы, предсказуемость поведения, последствия выбора тех или иных решений.

**Что делает:**
Проектирует архитектуру, схемы, модели поведения, проверяет конструкции, формирует основу для разработки и тестирования.

**Методы (SoTA):**
- Domain-Driven Design (DDD)
- Event Storming
- Architecture Decision Records (ADR)
- Quality Attribute Scenarios
- Systems Modeling Language (SysML v2)
- Model-Based Systems Engineering
- Design Reviews & Trade-off Analysis
- Simulation-based verification
- Architecture Fitness Functions

**Результаты:**
- Воплощение целевой системы (инкремент/MVP/прототип)
- Стабильные интерфейсы, проверенные поведенческие модели
- Архитектурные схемы и спецификации целевой системы
- Модели поведения (диаграммы, симуляции)
- Описание интерфейсов и контрактов
- Прототипы и экспериментальные стенды
- Набор решений и их обоснований

**Метрики:**
- Предсказуемость поведения системы при нагрузках
- Проверяемость решений
- Устойчивость конструкции
- Понятность интерфейсов для команд разработки

---

### 2.3. Операционный менеджер целевой системы (FX6)
*целевая система × менеджер*

**Что видит и удерживает:**
Выпуск ЦС и/или партий ЦС, её работоспособность, эксплуатация, ремонт, стабильность, обслуживание, сбои, обновления, нагрузка, реагирование на изменения.

**Что делает:**
Обеспечивает плановый выпуск ЦС, организует эксплуатацию, поддержку, развитие системы; следит за реальной работой и качеством её функционирования.

**Методы (SoTA):**
- Site Reliability Engineering (SRE)
- Change Management Frameworks
- Incident Management (modern protocols)
- Monitoring & Observability
- Chaos Engineering
- Postmortem Practices
- Capacity Planning
- Reliability Modeling

**Результаты:**
- Эксплуатируемая ЦС (или партия) с заданными SLO/SLA
- Регламенты и инструкции по эксплуатации целевой системы
- Графики работ, планы обновлений
- Отчёты о сбоях, постмортемы
- Метрики нагрузки и доступности
- Процессы реагирования на инциденты

**Метрики:**
- Количество партии
- Доступность системы для конечных пользователей
- Скорость восстановления после сбоя
- Стабильность изменений
- Предсказуемость поведения системы под ростом нагрузки

---

## 3.Х. Область интересов системы создания

### 3.1. Бизнесмен / Инвестор (FX7)
*система создания × предприниматель*

**Что видит и удерживает:**
Где ценность растёт, какие проекты перспективны, как распределять ресурсы, какие риски и горизонты.

**Что делает:**
Определяет стратегию, поддерживает рост, инвестирует в новые направления, создаёт условия для развития всей системы создания.

**Методы (SoTA):**
- Venture Decision Frameworks
- Portfolio Theory (modern adaptations)
- Expected Value Modeling
- Scenario Planning
- Long-term Strategic Finance
- Evidence-Based Allocation
- Growth loops & Flywheels

**Результаты:**
- Финансовые средства
- Оценка стоимости компании
- Инвестиционные решения для системы создания
- Портфель проектов
- Стратегия распределения ресурсов
- Финансовые модели и прогнозы

**Метрики:**
- Рентабельность проектов для всей системы создания
- Сбалансированность ресурсного портфеля
- Устойчивость системы в долгом горизонте
- Темп роста ключевых направлений

---

### 3.2. Организатор разработки (FX8)
*система создания × инженер*

**Что видит и удерживает:**
Как именно создаётся система: этапы, процессы, инструменты, качество, передача результатов, автоматизация.

**Что делает:**
Проектирует и совершенствует конвейер разработки, поддерживает инженерные практики, делает разработку воспроизводимой и надёжной.

**Методы (SoTA):**
- DevOps & Platform Engineering
- Continuous Integration / Continuous Delivery
- Trunk-based development
- Test Automation
- GitOps
- Flow Efficiency modeling
- Value Stream Mapping (modern version)
- Software Production Line design

**Результаты:**
- Воспроизводимый конвейер (платформа) создания (CI/CD, автотесты, качество)
- Описания процессов, пайплайны/шаблоны/проверки для системы создания
- Стандарты качества
- Оптимизированная структура этапов и ролей

**Метрики:**
- Скорость поставки изменений в целевую систему
- Надёжность релизов
- Качество автоматизации процесса создания
- Пропускная способность разработки

---

### 3.3. Администратор / Операционный руководитель (FX9)
*система создания × менеджер*

**Что видит и удерживает:**
Людей, роли, бюджеты, ресурсы, внутренние сервисы, безопасность, документооборот, бытовую инфраструктуру.

**Что делает:**
Обеспечивает бесперебойную работу команды и процессов: найм, оборудование, финансовые потоки, доступы, безопасность, внутренние правила.

**Методы (SoTA):**
- Organizational Design
- People-Ops frameworks
- Role-based Access Control
- Financial Planning & Analysis
- Internal Service Management
- Policy-Based Management
- OKR-Ops / Goal-Ops

**Результаты:**
- Конвейер (платформа) создания в рабочем состоянии и обеспечены ресурсами
- Регламенты, бюджеты и процессы системы создания
- Матрицы ролей
- Политики доступа, безопасности
- Планы найма и адаптации агентов (людей и ИИ)
- Финансовые модели и отчёты

**Метрики:**
- Скорость обработки внутренних запросов от проектных ролей
- Эффективность использования ресурсов
- Своевременность исполнения внутренних обязательств
- Устойчивость внутренних сервисов

---

## Сводная таблица

| Код | Роль | Система | Измерение | Ключевой фокус |
|-----|------|---------|-----------|----------------|
| FX1 | Продвиженец | Надсистема | Meaning | Проблемы и потребности людей |
| FX2 | Владелец продукта | Надсистема | Architecture | Сценарии использования |
| FX3 | PR/GR | Надсистема | Operations | Внешние роли и коммуникации |
| FX4 | Визионер ЦС | Целевая система | Meaning | Образ и функция системы |
| FX5 | Инженер ЦС | Целевая система | Architecture | Архитектура и конструкция |
| FX6 | Оператор ЦС | Целевая система | Operations | Эксплуатация и SRE |
| FX7 | Бизнесмен | Система создания | Meaning | Инвестиции и стратегия |
| FX8 | Организатор разработки | Система создания | Architecture | DevOps и CI/CD |
| FX9 | Администратор | Система создания | Operations | Люди, роли, бюджеты |

---

## См. также

- [roles-matrix-brief.md](roles-matrix-brief.md) — краткая версия матрицы
- [02-document-families.md](../0.1.Knowledge-Logic/02-document-families.md) — семейства документов F1-F9
- [01-kernels-model.md](../0.1.Knowledge-Logic/01-kernels-model.md) — модель ядер
- [CLAUDE.md](../../CLAUDE.md) — инструкции для Claude Code


# SOURCE_FILE: 0.OPS/0.4.FPF-Integration/fpf-integration.md
---
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
fpf_patterns:
  - A.1
  - A.1.1
  - A.7
  - B.3
---

# Интеграция S2R и FPF

## Принцип интеграции

S2R использует FPF как **эпистемологический фундамент**. Это означает:

1. **Терминология** — ключевые термины S2R берутся из FPF
2. **Паттерны мышления** — структура рассуждений следует FPF
3. **Онтология** — иерархия понятий опирается на FPF

## Ключевые паттерны FPF в S2R

### A.1 — Holonic Foundation (Холонический фундамент)

**Принцип:** Всё — холон: одновременно целое и часть большего целого.

**Применение в S2R:**
- Каждое ядро — холон (целое для своих семейств, часть репозитория)
- Каждый документ — холон (целое для своего содержимого, часть семейства)
- Репозиторий — холон (целое для проекта, часть экосистемы знаний)

### A.1.1 — Bounded Context (Ограниченный контекст)

**Принцип:** Значение термина локально — определено границами контекста.

**Применение в S2R:**
- Каждое ядро — отдельный контекст
- Локальная онтология ядра в `X0.{Name}-Management/local-ontology.md`
- При переносе терминов между ядрами — явное указание мостов

### A.3 — System Triad (Триада систем)

**Принцип:** Для каждой целевой системы определяется надсистема и создатель.

**Применение в S2R:**
- Структура ядра: X1.Suprasystem, X2.SOI, X3.Constructor
- Обязательность определения всех трёх систем
- Матрица 3×3 как развёртка триады по ролям

### A.7 — Strict Distinction (Строгое различение)

**Принцип:** Не путаем сущности разных типов.

**Применение в S2R:**

| Путаница | Правильно |
|----------|-----------|
| Документ "делает" | Система делает, документ описывает |
| Роль = Человек | Роль — функция, человек — исполнитель |
| План = Реальность | План — намерение, реальность — факт |
| Название = Сущность | Название указывает, сущность существует |

### B.3 — Trust Calculus (Расчёт доверия)

**Принцип:** Доверие к информации оценивается кортежем F-G-R.

**Применение в S2R:**

| Компонент | Диапазон | Описание |
|-----------|----------|----------|
| **F** (Formality) | 0-9 | Формальность описания |
| **G** (Scope) | local/project/ecosystem | Область применимости |
| **R** (Reliability) | 0.0-1.0 | Надёжность, проверенность |

### E.10.D2 — I/D/S Discipline

**Принцип:** Различай три аспекта описания.

**Применение в S2R:**

| Аспект | Вопрос | Пример |
|--------|--------|--------|
| **I** (Intension) | Что это по сути? | "Авторизация — проверка прав" |
| **D** (Description) | Что наблюдаем? | "Используем JWT токены" |
| **S** (Specification) | Что требуется? | "Время ответа < 100ms" |

## Как использовать FPF при работе с S2R

### При создании документа

1. Определи, какие паттерны FPF применимы
2. Укажи их в `fpf_patterns` в frontmatter
3. Следуй принципам паттернов в содержимом

### При анализе структуры

1. Проверь холоническую целостность (A.1)
2. Проверь границы контекстов (A.1.1)
3. Проверь строгость различений (A.7)

### При разрешении неясностей

1. Обратись к FPF-Spec.md за определением
2. Используй паттерны как критерии решения
3. Документируй решение со ссылкой на паттерн

## Навигация по FPF-Spec.md

Полная спецификация FPF (~43K строк) структурирована по частям:

```
Part A: Kernel Architecture
├── A.1  Holonic Foundation
├── A.1.1 Bounded Context
├── A.3  System Triad
├── A.7  Strict Distinction
└── ...

Part B: Trans-disciplinary Reasoning
├── B.3  Trust Calculus
├── B.5  ADI Cycle
└── ...

Part C: Domain Calculi
├── Sys-CAL (системный калькулюс)
├── KD-CAL (калькулюс знаний)
└── ...

Part E: Constitution
├── E.10.D2 I/D/S Discipline
└── ...
```

## Ограничения контекста

FPF-Spec.md (~200K токенов) не вмещается целиком в контекст LLM. Стратегия:

1. **INDEX.md** — для обычных задач (~250 строк)
2. **Конкретные части** — для глубокого анализа (запрос по строкам)
3. **Ссылки на паттерны** — для документирования решений

## См. также

- [fpf/INDEX.md](fpf/INDEX.md) — локальные принципы
- [fpf/FPF-Spec.md](fpf/FPF-Spec.md) — полная спецификация
- [fpf-patterns-map.md](fpf-patterns-map.md) — карта паттернов


# SOURCE_FILE: 0.OPS/0.4.FPF-Integration/fpf-patterns-map.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Карта паттернов FPF в S2R

## Основные паттерны

| Паттерн | Название | Где используется в S2R |
|---------|----------|------------------------|
| A.1 | Holonic Foundation | Структура ядер, документов |
| A.1.1 | Bounded Context | Локальные онтологии ядер |
| A.3 | System Triad | X1.Suprasystem, X2.SOI, X3.Constructor |
| A.7 | Strict Distinction | Различение документ/система, роль/человек |
| B.3 | Trust Calculus | Оценка достоверности информации |
| B.5 | ADI Cycle | Процесс рассуждения при анализе |
| E.10.D2 | I/D/S Discipline | Структура описаний |
| F.0.1 | Context Passport | Метаданные в frontmatter |

## Паттерны по областям S2R

### Структура репозитория

| Элемент S2R | Паттерн | Применение |
|-------------|---------|------------|
| Репозиторий | A.1 | Холон верхнего уровня |
| Ядро (Kernel) | A.1 | Холон системы |
| Семейство (Family) | A.1 | Холон документов |
| Документ | A.1 | Холон контента |

### Онтология

| Элемент S2R | Паттерн | Применение |
|-------------|---------|------------|
| Общая онтология | A.1.1 | Границы всего репозитория |
| Локальная онтология | A.1.1 | Границы конкретного ядра |
| Глоссарий | A.7 | Строгие определения |

### Три системы

| Система | Паттерн | Применение |
|---------|---------|------------|
| Suprasystem | A.3 | Надсистема — контекст |
| System-of-Interest | A.3 | Целевая система |
| Constructor | A.3 | Создатель |

### Метаданные

| Поле frontmatter | Паттерн | Применение |
|------------------|---------|------------|
| kernel | A.1.1 | Контекст документа |
| family | A.1 | Позиция в иерархии |
| fpf_patterns | — | Связь с FPF |
| status | B.3 | Надёжность (R) |
| scope | B.3 | Область (G) |

## Паттерны для AI-агентов

При работе AI с репозиторием:

| Задача | Релевантные паттерны |
|--------|---------------------|
| Определение места документа | A.1, A.1.1, A.3 |
| Создание документа | A.7, E.10.D2, F.0.1 |
| Анализ связей | A.1, B.3 |
| Проверка качества | A.7, B.3 |
| Разрешение конфликтов | A.1.1, A.7 |

## Как указывать паттерны

В frontmatter документа:

```yaml
fpf_patterns:
  - A.1       # Holonic Foundation
  - A.7       # Strict Distinction
  - B.3       # Trust Calculus
```

В тексте документа:

```markdown
Согласно паттерну A.7 (Strict Distinction), различаем...
```

## См. также

- [fpf-integration.md](fpf-integration.md) — детали интеграции
- [fpf/FPF-Spec.md](fpf/FPF-Spec.md) — полная спецификация


# SOURCE_FILE: 0.OPS/0.5.AI-Reports/Validation-Specs/01-formal-checks.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# ТЗ: Формальные проверки (Formal Checks)

> **Цель:** Автоматическая проверка формальной корректности хранилища.

## Расписание

- **Автоматически:** Воскресенье, 9:00
- **Вручную:** `/validate formal`

---

## 1. Проверка структуры папок

### 1.1. Корректность именования ядер

**Что проверяем:**
- Папки ядер имеют формат `{Буква}.{Имя-Системы}/`
- Буквы идут последовательно: A, B, C, D...
- Имена систем конкретные (не "Target-System", "Our-System")

**Критерии ошибки:**
```
❌ A.Target-System/          # Абстрактное имя
❌ A.SOI-Name/                # Шаблонное имя
❌ C.System/                  # Пропущена буква B
✅ A.Automobile/              # Конкретное имя
✅ B.Mobile-App/              # Конкретное имя
```

**Уровень:** Error

### 1.2. Корректность именования подсистем

**Что проверяем:**
- X1 — физическая система (надсистема)
- X2 — целевая система (SoI)
- X3 — конструктор

**Критерии ошибки:**
```
❌ A1.Daily-Life/             # НЕ физическая система
❌ A1.Market/                 # НЕ физическая система
❌ A1.Industry/               # НЕ физическая система
❌ A1.Suprasystem/            # Роль, не имя системы
✅ A1.Taxi/                   # Физическая система
✅ A1.User-Smartphone/        # Физическая система
```

**Уровень:** Error

### 1.3. Наличие обязательных папок

**Что проверяем:**
- Каждое ядро содержит X1, X2, X3
- Каждая система содержит .1.Meaning, .2.Architecture, .3.Operations

**Уровень:** Warning

---

## 2. Проверка frontmatter

### 2.1. Наличие обязательных полей

**Что проверяем:**
```yaml
---
type: [doc|index|archive]
status: [draft|active|deprecated]
created: YYYY-MM-DD
updated: YYYY-MM-DD
family: [F0|FA1-FA9|FB1-FB9|...]
scope: [repository|kernel|system]
---
```

**Уровень:** Error (для type, status), Warning (для остальных)

### 2.2. Корректность значений family

**Что проверяем:**
- F0 — только в папке 0.OPS/
- FA1-FA9 — только в ядре A
- FB1-FB9 — только в ядре B
- Номер family соответствует позиции (Meaning=1,4,7; Architecture=2,5,8; Operations=3,6,9)

**Пример соответствия:**
```
A1.Taxi/A1.1.Meaning/        → FA1
A1.Taxi/A1.2.Architecture/   → FA2
A1.Taxi/A1.3.Operations/     → FA3
A2.Automobile/A2.1.Meaning/  → FA4
A2.Automobile/A2.2.Architecture/ → FA5
```

**Уровень:** Warning

### 2.3. Актуальность дат

**Что проверяем:**
- `updated` >= `created`
- `updated` не в будущем
- Документы с `status: active` обновлялись в последние 180 дней

**Уровень:** Info

---

## 3. Проверка ссылок

### 3.1. Битые внутренние ссылки

**Что проверяем:**
- Все ссылки вида `[текст](путь.md)` ведут на существующие файлы
- Относительные пути корректны

**Уровень:** Error

### 3.2. Ссылки related

**Что проверяем:**
- Все файлы в `related:` существуют
- Обратные ссылки присутствуют (если A ссылается на B, то B должен ссылаться на A)

**Уровень:** Warning

### 3.3. Ссылки "См. также"

**Что проверяем:**
- Все ссылки в секции "## См. также" работают
- Нет дублирующихся ссылок

**Уровень:** Warning

---

## 4. Проверка дублирования

### 4.1. Дублирование имён файлов

**Что проверяем:**
- В одной папке нет файлов с одинаковыми именами (разный регистр)
- Нет файлов с одинаковыми базовыми именами в разных форматах

**Уровень:** Error

### 4.2. Дублирование заголовков

**Что проверяем:**
- В пределах одного ядра нет документов с идентичными H1 заголовками

**Уровень:** Warning

### 4.3. Дублирование терминов в глоссарии

**Что проверяем:**
- В `05-glossary.md` нет дублирующихся терминов
- Термины отсортированы

**Уровень:** Info

---

## 5. Проверка форматирования

### 5.1. Единообразие markdown

**Что проверяем:**
- Заголовки начинаются с `#` (не подчёркивание)
- Списки используют `-` или `*` (единообразно в файле)
- Таблицы правильно отформатированы

**Уровень:** Info

### 5.2. Наличие README.md

**Что проверяем:**
- Каждая папка содержит README.md
- README содержит описание содержимого папки

**Уровень:** Warning

---

## Формат вывода

```markdown
# Формальная проверка

**Дата:** 2026-01-14
**Сгенерировано:** Claude Code

## Резюме

- Ошибок (Error): 3
- Предупреждений (Warning): 7
- Информация (Info): 12

## Ошибки (требуют исправления)

### 1. Битая ссылка в A2.Automobile/A2.1.Meaning/requirements.md
- **Строка 45:** `[архитектура](../architecture.md)` → файл не найден
- **Исправление:** Заменить на `[архитектура](../A2.2.Architecture/README.md)`

### 2. Некорректное именование: B1.Market/
- **Проблема:** "Market" — не физическая система
- **Исправление:** Переименовать в физическую систему, например B1.User-Device/

## Предупреждения

### 1. Отсутствует README.md в A3.Assembly-Line/A3.2.Architecture/
...

## Информация

### 1. Документ не обновлялся 200 дней: A1.Taxi/A1.1.Meaning/market-analysis.md
...

## Статистика

| Категория | Всего | С ошибками |
|-----------|-------|------------|
| Папки | 45 | 2 |
| Файлы | 78 | 3 |
| Ссылки | 156 | 1 |
| Frontmatter | 78 | 5 |
```

---

## См. также

- [02-content-checks.md](02-content-checks.md) — содержательные проверки
- [03-development-analysis.md](03-development-analysis.md) — анализ развития
- [../../0.6.Repository-Processes/05-frontmatter-spec.md](../../0.6.Repository-Processes/05-frontmatter-spec.md) — спецификация frontmatter


# SOURCE_FILE: 0.OPS/0.5.AI-Reports/Validation-Specs/02-content-checks.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# ТЗ: Содержательные проверки (Content Checks)

> **Цель:** Автоматическая проверка соответствия содержимого документов методологии S2R.

## Расписание

- **Автоматически:** Воскресенье, 9:00
- **Вручную:** `/validate content`

---

## 1. Проверка соответствия методологии

### 1.1. Соответствие матрице ролей 3×3

**Источник методологии:** `0.3.Roles-Matrix-3x3/roles-matrix.md`

**Что проверяем:**

| Папка | Ожидаемое содержимое |
|-------|---------------------|
| X1.1.Meaning/ | Контекст, рынок, тренды, требования стейкхолдеров надсистемы |
| X1.2.Architecture/ | Архитектура окружения, интерфейсы с внешними системами |
| X1.3.Operations/ | Партнёрства, экосистема |
| X2.1.Meaning/ | Требования к SoI, ценностное предложение, JTBD |
| X2.2.Architecture/ | Архитектура системы, компоненты, технические решения |
| X2.3.Operations/ | Реализация, внедрение, эксплуатация |
| X3.1.Meaning/ | Принципы команды/организации, культура |
| X3.2.Architecture/ | Платформа создания, инструменты, методы |
| X3.3.Operations/ | Команда, процессы, методология разработки |

**Критерии несоответствия:**
```
❌ Документ о команде в A2.2.Architecture/  # Должен быть в A3.3.Operations/
❌ Требования к системе в A1.1.Meaning/     # Должен быть в A2.1.Meaning/
❌ Анализ рынка в A2.1.Meaning/             # Должен быть в A1.1.Meaning/
```

**Уровень:** Warning

### 1.2. Соответствие FPF-паттернам

**Источник методологии:** `0.4.FPF-Integration/fpf-patterns-map.md`

**Что проверяем:**
- Документы используют корректные FPF-паттерны для своего семейства
- Не смешиваются паттерны разных семейств

**Уровень:** Info

---

## 2. Проверка терминологии

### 2.1. Использование терминов из онтологии

**Источник:** `0.1.Knowledge-Logic/04-ontology.md`

**Что проверяем:**
- Термины используются согласно определениям в онтологии
- Нет "синонимов" для устоявшихся терминов

**Примеры несоответствия:**
```
❌ "целевая система" вместо "SoI" (если в глоссарии принят SoI)
❌ "надсистема" для обозначения контекста (надсистема — физическая система)
❌ "конструктор" для обозначения процесса (конструктор — это система)
```

**Уровень:** Info

### 2.2. Использование терминов из глоссария

**Источник:** `0.1.Knowledge-Logic/05-glossary.md`

**Что проверяем:**
- Термины проекта используются единообразно
- Новые термины добавлены в глоссарий

**Уровень:** Info

### 2.3. Проверка анти-паттернов

**Источник:** `0.1.Knowledge-Logic/08-anti-patterns.md`

**Что проверяем:**
- Документы не содержат известных анти-паттернов
- Системы названы корректно (не процессы, не роли, не контексты)

**Критерии:**
```
❌ Надсистема названа "Рынок", "Отрасль", "Повседневная жизнь"
❌ SoI назван "Опыт клиента", "Впечатление"
❌ Конструктор назван абстрактно без указания ЧТО создаёт
```

**Уровень:** Error

---

## 3. Проверка связности ядер

### 3.1. Согласованность между ядрами

**Источник:** `0.2.Kernels-Bridge/02-kernels-relations.md`

**Что проверяем:**
- Если система B входит в систему A, это отражено в обоих ядрах
- Связи между ядрами симметричны и непротиворечивы

**Пример:**
```
Ядро A: A.Automobile
Ядро B: B.Engine

Проверяем:
✅ В A указано, что Engine — подсистема Automobile
✅ В B указано, что Automobile — надсистема Engine
```

**Уровень:** Warning

### 3.2. Согласованность цепочки ценности

**Источник:** `0.2.Kernels-Bridge/01-value-chain.md`

**Что проверяем:**
- Все ядра упомянуты в цепочке ценности
- Порядок в цепочке соответствует реальным зависимостям

**Уровень:** Warning

### 3.3. Согласованность структуры связанности систем

**Источник:** `0.2.Kernels-Bridge/03-systems-relations.md`

**Что проверяем:**
- Структура связанности не содержит циклов
- Все системы из ядер присутствуют в структуре связанности

**Уровень:** Warning

---

## 4. Проверка противоречий

### 4.1. Противоречия в требованиях

**Что проверяем:**
- Требования в X2.1.Meaning/ не противоречат друг другу
- Требования разных ядер не конфликтуют

**Пример противоречия:**
```
❌ A2.1: "Система должна работать offline"
   B2.1: "Система требует постоянного подключения к серверу A"
```

**Уровень:** Error

### 4.2. Противоречия в архитектуре

**Что проверяем:**
- Архитектурные решения согласованы между ядрами
- Интерфейсы совместимы

**Уровень:** Warning

### 4.3. Противоречия в датах и версиях

**Что проверяем:**
- Версии компонентов согласованы
- Даты релизов не конфликтуют

**Уровень:** Info

---

## 5. Проверка полноты описания

### 5.1. Описание интерфейсов

**Что проверяем:**
- Для каждой системы описаны входные и выходные интерфейсы
- Интерфейсы между связанными системами совпадают

**Уровень:** Warning

### 5.2. Описание стейкхолдеров

**Что проверяем:**
- Для каждой системы определены стейкхолдеры
- Требования стейкхолдеров документированы

**Уровень:** Info

---

## Формат вывода

```markdown
# Содержательная проверка

**Дата:** 2026-01-14
**Сгенерировано:** Claude Code

## Резюме

- Ошибок (Error): 1
- Предупреждений (Warning): 4
- Информация (Info): 8

## Ошибки методологии

### 1. Анти-паттерн: B1 названа "Market"
- **Файл:** B.Mobile-App/B1.Market/README.md
- **Проблема:** "Market" — не физическая система, а контекст
- **Исправление:** Переименовать в физическую надсистему, например "B1.User-Smartphone"
- **Источник правила:** 0.1.Knowledge-Logic/08-anti-patterns.md

## Предупреждения

### 1. Документ в неправильном семействе
- **Файл:** A2.Automobile/A2.2.Architecture/team-structure.md
- **Проблема:** Документ о структуре команды находится в Architecture
- **Исправление:** Переместить в A3.Assembly-Line/A3.3.Operations/
- **Источник правила:** 0.3.Roles-Matrix-3x3/roles-matrix.md

### 2. Несогласованность между ядрами
- **Проблема:** В ядре A указано, что B — подсистема, но в ядре B это не отражено
- **Файлы:**
  - A.Automobile/README.md (строка 15)
  - B.Engine/README.md (отсутствует упоминание)
- **Исправление:** Добавить в B.Engine/README.md информацию о надсистеме

## Информация

### 1. Термин не в глоссарии
- **Термин:** "микросервис"
- **Встречается в:** B.Engine/B2.Engine/B2.2.Architecture/api-design.md
- **Рекомендация:** Добавить определение в 0.1.Knowledge-Logic/05-glossary.md

## Матрица соответствия

| Семейство | Ожидаемый контент | Соответствует |
|-----------|-------------------|---------------|
| A1.1.Meaning | Контекст рынка | ✅ |
| A1.2.Architecture | Окружение | ⚠️ Частично |
| A2.1.Meaning | Требования SoI | ✅ |
| A2.2.Architecture | Архитектура | ❌ Содержит team-structure |
```

---

## См. также

- [01-formal-checks.md](01-formal-checks.md) — формальные проверки
- [03-development-analysis.md](03-development-analysis.md) — анализ развития
- [../../0.3.Roles-Matrix-3x3/roles-matrix.md](../../0.3.Roles-Matrix-3x3/roles-matrix.md) — матрица ролей
- [../../0.1.Knowledge-Logic/08-anti-patterns.md](../../0.1.Knowledge-Logic/08-anti-patterns.md) — анти-паттерны


# SOURCE_FILE: 0.OPS/0.5.AI-Reports/Validation-Specs/03-development-analysis.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# ТЗ: Анализ развития (Development Analysis)

> **Цель:** Автоматический анализ полноты хранилища и генерация предложений по развитию.

## Расписание

- **Автоматически:** Воскресенье, 9:00
- **Вручную:** `/validate develop`

---

## 1. Анализ полноты семейств

### 1.1. Матрица заполненности

**Что анализируем:**
- Для каждого ядра строим матрицу 3×3
- Отмечаем заполненность каждого семейства

**Критерии заполненности:**
| Статус | Критерий |
|--------|----------|
| 🟢 Заполнено | ≥3 документа или README с содержательным описанием |
| 🟡 Частично | 1-2 документа или только шаблонный README |
| 🔴 Пусто | Нет документов или только пустой README |

**Пример вывода:**
```
Ядро A: Automobile

|           | Meaning | Architecture | Operations |
|-----------|---------|--------------|------------|
| Suprasystem (A1.Taxi) | 🟢 | 🟡 | 🔴 |
| SoI (A2.Automobile) | 🟢 | 🟢 | 🟡 |
| Constructor (A3.Assembly-Line) | 🔴 | 🔴 | 🟡 |
```

### 1.2. Приоритизация заполнения

**Логика приоритизации:**

1. **Критический приоритет:** A2.1.Meaning (требования к SoI) — без этого нельзя строить архитектуру
2. **Высокий приоритет:** A2.2.Architecture, A1.1.Meaning — основа проекта
3. **Средний приоритет:** A1.2, A2.3, A3.3 — операционная часть
4. **Низкий приоритет:** A1.3, A3.1, A3.2 — вспомогательные

**Формула приоритета:**
```
Priority = BaseWeight × (1 + DependencyCount × 0.2) × AgeMultiplier
```

---

## 2. Анализ связей между документами

### 2.1. Граф связей

**Что анализируем:**
- Строим граф связей между документами (по `related:` и ссылкам)
- Выявляем изолированные документы
- Выявляем документы-хабы (много входящих/исходящих ссылок)

**Метрики:**
| Метрика | Описание |
|---------|----------|
| Изолированные | Документы без связей |
| Слабосвязанные | <2 связей |
| Хабы | >5 связей |
| Средняя связность | Среднее число связей на документ |

### 2.2. Рекомендации по связям

**Что предлагаем:**
- Документы, которые должны быть связаны (по контексту)
- Избыточные связи (можно удалить)
- Недостающие обратные ссылки

---

## 3. Анализ актуальности

### 3.1. Устаревшие документы

**Критерии:**
| Категория | Порог | Рекомендация |
|-----------|-------|--------------|
| Актуальный | <90 дней | — |
| Требует проверки | 90-180 дней | Проверить актуальность |
| Устаревший | >180 дней | Обновить или архивировать |

### 3.2. Активность по семействам

**Что анализируем:**
- Частота обновлений по семействам
- Выявление "заброшенных" областей

---

## 4. Предложения по развитию

### 4.1. Рекомендации по документам

**Типы рекомендаций:**

| Тип | Триггер | Пример рекомендации |
|-----|---------|---------------------|
| Создать | Пустое семейство | "Создать requirements.md в A2.1.Meaning" |
| Разделить | Документ >500 строк | "Разделить api-spec.md на отдельные файлы" |
| Объединить | Много мелких файлов | "Объединить notes-*.md в один документ" |
| Обновить | Устаревший | "Обновить market-analysis.md (185 дней)" |
| Архивировать | deprecated + старый | "Архивировать old-requirements.md" |

### 4.2. Рекомендации по структуре

**Типы:**
- Создание недостающих ядер
- Реорганизация папок
- Добавление индексных файлов

### 4.3. Рекомендации по методологии

**На основе:**
- Сравнения с эталонной структурой
- Анализа успешных паттернов в других ядрах
- Best practices из FPF

---

## 5. Метрики здоровья хранилища

### 5.1. Общие метрики

| Метрика | Формула | Целевое значение |
|---------|---------|------------------|
| Полнота | Заполненных семейств / Всего семейств | >70% |
| Связность | Документов со связями / Всего документов | >80% |
| Актуальность | Актуальных / Всего | >60% |
| Соответствие | Без ошибок методологии / Всего | >90% |

### 5.2. Индекс здоровья

```
HealthIndex = (Полнота × 0.3) + (Связность × 0.2) +
              (Актуальность × 0.2) + (Соответствие × 0.3)
```

**Интерпретация:**
| Индекс | Статус |
|--------|--------|
| 0.8-1.0 | 🟢 Отлично |
| 0.6-0.8 | 🟡 Хорошо |
| 0.4-0.6 | 🟠 Требует внимания |
| 0.0-0.4 | 🔴 Критично |

---

## Формат вывода

```markdown
# Анализ развития

**Дата:** 2026-01-14
**Сгенерировано:** Claude Code

## Индекс здоровья: 0.72 🟡

| Компонент | Значение | Вес | Вклад |
|-----------|----------|-----|-------|
| Полнота | 65% | 0.3 | 0.195 |
| Связность | 78% | 0.2 | 0.156 |
| Актуальность | 70% | 0.2 | 0.140 |
| Соответствие | 76% | 0.3 | 0.228 |

## Матрица заполненности

### Ядро A: Automobile

|           | Meaning | Architecture | Operations |
|-----------|---------|--------------|------------|
| A1.Taxi | 🟢 3 док. | 🟡 1 док. | 🔴 0 док. |
| A2.Automobile | 🟢 5 док. | 🟢 4 док. | 🟡 2 док. |
| A3.Assembly-Line | 🔴 0 док. | 🔴 0 док. | 🟡 1 док. |

**Заполненность ядра A:** 44% (4/9 семейств)

### Ядро B: Engine

|           | Meaning | Architecture | Operations |
|-----------|---------|--------------|------------|
| B1.Automobile | 🟡 1 док. | 🔴 0 док. | 🔴 0 док. |
| B2.Engine | 🟢 3 док. | 🟢 4 док. | 🟡 2 док. |
| B3.Engine-Shop | 🔴 0 док. | 🔴 0 док. | 🔴 0 док. |

**Заполненность ядра B:** 33% (3/9 семейств)

## Топ-5 приоритетных задач

| # | Приоритет | Задача | Семейство |
|---|-----------|--------|-----------|
| 1 | 🔴 Критический | Создать документы в A3.Assembly-Line/A3.1.Meaning/ | FA7 |
| 2 | 🔴 Критический | Описать конструктора в B3.Engine-Shop/ | FB7-FB9 |
| 3 | 🟠 Высокий | Добавить архитектуру окружения в A1.Taxi/A1.2.Architecture/ | FA2 |
| 4 | 🟠 Высокий | Обновить market-analysis.md (устарел 185 дней) | FA1 |
| 5 | 🟡 Средний | Добавить связи между A2 и B2 | — |

## Рекомендации

### Документы для создания

1. **A3.Assembly-Line/A3.1.Meaning/principles.md**
   - Содержание: Принципы и ценности команды производства
   - Шаблон: См. [01-project-description-template.md]

2. **A1.Taxi/A1.3.Operations/partnerships.md**
   - Содержание: Партнёрства и экосистема такси-сервисов
   - Шаблон: —

### Документы для обновления

1. **A1.Taxi/A1.1.Meaning/market-analysis.md**
   - Последнее обновление: 185 дней назад
   - Причина: Данные о рынке могли измениться

### Связи для добавления

1. A2.Automobile/A2.2.Architecture/components.md ↔ B2.Engine/B2.2.Architecture/api.md
   - Причина: Engine — компонент Automobile

## Тренды

| Период | Полнота | Связность | Здоровье |
|--------|---------|-----------|----------|
| Месяц назад | 58% | 72% | 0.65 |
| Текущий | 65% | 78% | 0.72 |
| Изменение | +7% | +6% | +0.07 |
```

---

## См. также

- [01-formal-checks.md](01-formal-checks.md) — формальные проверки
- [02-content-checks.md](02-content-checks.md) — содержательные проверки
- [../../0.1.Knowledge-Logic/02-document-families.md](../../0.1.Knowledge-Logic/02-document-families.md) — семейства документов


# SOURCE_FILE: 0.OPS/0.6.Repository-Processes/01-project-description-template.md
---
# Описание проекта: [Название вашего проекта]

> **Инструкция:** Заполните этот шаблон для вашего проекта. После заполнения переименуйте файл в `PROJECT_DESCRIPTION.md` и поместите в корень репозитория.
>
> **Важно:** Для правильного определения трёх систем (целевой, надсистемы, создателя) изучите [Модель ядер](../0.1.Knowledge-Logic/01-kernels-model.md).

---

## 1. Общее описание

### 1.1. Идентификация

**Название проекта:** [Рабочее название проекта]

**Краткое описание (1-2 предложения):**
[Что это за проект и какую проблему решает. Должно быть понятно человеку "с улицы".]

**Тип продукта:**
- [ ] Программное обеспечение (веб/мобильное/десктоп)
- [ ] Физическое устройство
- [ ] Сервис/Услуга
- [ ] Методология/Процесс
- [ ] Контент/Знания
- [ ] Другое: ___________

**Дата создания описания:** [YYYY-MM-DD]

### 1.2. Команда

**Автор/Владелец проекта:** [Имя или псевдоним]

**Контакт:** [Email / Telegram / другое]

**Команда (если есть):**
| Роль | Кто | Статус |
|------|-----|--------|
| [Роль 1] | [Имя] | Активен / Ищем |
| [Роль 2] | [Имя] | Активен / Ищем |

---

## 2. System-of-Interest (Целевая система)

> **FPF-связь:** Паттерн A.1 (Holonic Foundation) — определяем границы системы
> **Вопрос:** ЧТО создаём?
>
> **Важно:** Целевая система — это **результат**, а не процесс. Если слово можно понять как процесс («доставка заняла 2 дня») и как результат («доставка пришла»), описывайте результат.

### 2.1. Что создаём?

**Формулировка в одном предложении:**
[Мы создаём {тип продукта}, который {основная функция} для {целевой аудитории}]

**Пример:** *Мы создаём мобильное приложение, которое помогает вести учёт личных финансов для молодых специалистов.*

### 2.2. Для кого? (Целевая аудитория)

**Основной пользователь (Primary Persona):**
- **Кто:** [Демография, профессия, контекст]
- **Боль:** [Какую проблему испытывает]
- **Цель:** [Чего хочет достичь]
- **Контекст использования:** [Когда/где будет использовать продукт]

**Дополнительные пользователи (если есть):**
| Группа | Описание | Важность |
|--------|----------|----------|
| [Группа 1] | [Кто и зачем] | Высокая / Средняя / Низкая |
| [Группа 2] | [Кто и зачем] | Высокая / Средняя / Низкая |

### 2.3. Какую проблему решает?

**Текущая ситуация (AS-IS):**
[Опишите, как пользователь решает проблему сейчас. Что плохо/неудобно?]

**Желаемая ситуация (TO-BE):**
[Опишите, как будет после внедрения вашего продукта]

**Ценностное предложение:**
> [Одно предложение: "{Продукт} позволяет {кому} {делать что} благодаря {уникальная особенность}"]

### 2.4. Основные функции (MVP)

Минимальный набор функций для первой версии:

1. **[Функция 1]:** [Краткое описание]
2. **[Функция 2]:** [Краткое описание]
3. **[Функция 3]:** [Краткое описание]

**Что НЕ входит в MVP:**
- [Функция, которую отложим]
- [Другая функция на потом]

### 2.5. Критерии успеха

Как поймём, что продукт успешен?

| Метрика | Целевое значение | Срок |
|---------|------------------|------|
| [Метрика 1] | [Значение] | [Когда] |
| [Метрика 2] | [Значение] | [Когда] |

---

## 3. Suprasystem (Надсистема)

> **FPF-связь:** Паттерн A.1.1 (Bounded Context) — определяем контекст
> **Вопрос:** В какую систему **встроится** целевая система? Какую функцию будет выполнять?
>
> **Важно:** Надсистема — это система, **частью которой** становится целевая система. Это НЕ рынок, НЕ все пользователи, НЕ окружение в общем смысле. Это конкретная система пользователя/клиента.

### 3.1. Система пользователя (истинная надсистема)

**В какую систему пользователя встроится ваш продукт?**
[Опишите систему пользователя. Пример: «Система управления личными финансами пользователя, где наше приложение — центральный компонент координации финансовых потоков»]

**С чем будет соприкасаться целевая система?**
[Какие другие компоненты надсистемы есть? Пример: банковские счета, наличные, привычки пользователя]

**Какую функцию/роль выполняет целевая система в надсистеме?**
[Пример: координация и визуализация всех финансовых операций]

### 3.2. Контекст надсистемы (рынок, среда)

> **Примечание:** Это НЕ надсистема, а контекст, в котором надсистема существует.

**Рынок/Домен:**
[В какой области работает продукт. Размер рынка, тренды.]

**Географический охват:**
- [ ] Локальный (город/регион): ___________
- [ ] Национальный: ___________
- [ ] Международный: ___________

### 3.2. Конкуренты и аналоги

| Конкурент | Что хорошо | Что плохо | Наше отличие |
|-----------|------------|-----------|--------------|
| [Конкурент 1] | [Плюсы] | [Минусы] | [Чем мы лучше] |
| [Конкурент 2] | [Плюсы] | [Минусы] | [Чем мы лучше] |
| [Аналог/Замена] | [Плюсы] | [Минусы] | [Чем мы лучше] |

### 3.3. Внешние проектные роли

Кто заинтересован в проекте (кроме пользователей)?

| Проектная роль | Интерес | Влияние | Стратегия работы |
|----------------|---------|---------|------------------|
| [Инвесторы] | [Чего хотят] | Высокое | [Как взаимодействуем] |
| [Регуляторы] | [Чего хотят] | Высокое | [Как взаимодействуем] |
| [Партнёры] | [Чего хотят] | Среднее | [Как взаимодействуем] |

### 3.4. Ограничения среды

**Технические ограничения:**
- [ ] Требуется интеграция с: ___________
- [ ] Должно работать на платформе: ___________
- [ ] Ограничения по производительности: ___________

**Регуляторные/Юридические:**
- [ ] GDPR / Персональные данные
- [ ] Отраслевые стандарты: ___________
- [ ] Лицензирование: ___________

**Ресурсные ограничения:**
- Бюджет: [Сумма или "Без бюджета"]
- Срок до MVP: [X месяцев]
- Доступные специалисты: [Кто есть / кого не хватает]

---

## 4. Constructor (Система создания)

> **FPF-связь:** Паттерн A.3 (Transformer Constitution) — кто/что создаёт систему
> **Вопрос:** КТО и КАК создаёт продукт?
>
> **Важно:** Система создания = Команда + Инструменты + Методы. Часто это не один создатель, а **граф создателей** (создатели создателей).

### 4.1. Команда

**Текущий состав:**

| Роль | Человек | Компетенции | Загрузка |
|------|---------|-------------|----------|
| [Product Owner] | [Имя] | [Навыки] | [%] |
| [Developer] | [Имя] | [Навыки] | [%] |
| [Designer] | [Имя/TBD] | [Навыки] | [%] |

**Нехватка (кого ищем):**
- [ ] [Роль]: [Требования]

### 4.2. Инструменты и технологии

**Разработка:**
| Категория | Инструмент | Обоснование выбора |
|-----------|------------|-------------------|
| Язык | [Python/JS/...] | [Почему] |
| Фреймворк | [React/Django/...] | [Почему] |
| БД | [PostgreSQL/...] | [Почему] |
| Инфраструктура | [AWS/Vercel/...] | [Почему] |

**Коммуникация:**
| Назначение | Инструмент |
|------------|------------|
| Чат | [Telegram/Slack/...] |
| Задачи | [Notion/Jira/...] |
| Документация | [Этот репозиторий] |
| Код | [GitHub] |

### 4.3. Методология

**Подход к разработке:**
- [ ] Agile/Scrum (спринты по X недель)
- [ ] Kanban (непрерывный поток)
- [ ] Waterfall (последовательные фазы)
- [ ] Другое: ___________

**Цикл релизов:**
[Как часто планируете выпускать обновления]

**Практики качества:**
- [ ] Code Review
- [ ] Автотесты
- [ ] CI/CD
- [ ] Другое: ___________

---

## 5. Первичные названия систем

> **Важно:** Это предложения. После экспертизы вы примете окончательное решение.

| Система | Текущее название | Предлагаемое название | Обоснование |
|---------|-----------------|----------------------|-------------|
| System-of-Interest | [Продукт] | [Ваше предложение] | [Почему такое название] |
| Suprasystem | [Среда] | [Ваше предложение] | [Почему такое название] |
| Constructor | [Команда] | [Ваше предложение] | [Почему такое название] |

**Варианты для System-of-Interest:**
- Вариант A: [Название] — [обоснование]
- Вариант B: [Название] — [обоснование]

---

## 6. Самопроверка перед экспертизой

Ответьте честно:

### Чёткость целевой системы
- [ ] Могу в одном предложении объяснить, ЧТО создаю
- [ ] Целевая система — это **результат** (не процесс)
- [ ] Можно «потрогать» или измерить
- [ ] Понятно, для КОГО это
- [ ] Ясно, какую ПРОБЛЕМУ решает
- [ ] Определены функции MVP

### Понимание надсистемы
- [ ] Определена система пользователя, куда **встроится** целевая система
- [ ] Понятно, с чем будет соприкасаться целевая система
- [ ] Описана функция целевой системы в надсистеме
- [ ] НЕ путаю надсистему с рынком/контекстом
- [ ] Знаю конкурентов/аналоги (контекст)
- [ ] Определил ключевые внешние проектные роли

### Реалистичность системы создания
- [ ] Есть команда или план её формирования
- [ ] Выбраны инструменты
- [ ] Оценены ресурсы (время, деньги, люди)

### Готовность к экспертизе
- [ ] Все разделы заполнены
- [ ] Нет откровенных пробелов
- [ ] Готов к критике и корректировкам

---

## 7. Следующий шаг

После заполнения этого документа:

1. **Переименуйте файл** в `PROJECT_DESCRIPTION.md`
2. **Переместите в корень** репозитория
3. **Запустите экспертизу** с Claude Code:

```
Прочитай PROJECT_DESCRIPTION.md и проведи экспертизу на основе FPF и S2R:
1. Проверь чёткость определения целевой системы (A.1, A.7)
2. Проверь полноту описания надсистемы (A.1.1)
3. Проверь реалистичность системы создания
4. Оцени предложенные названия систем
5. Дай рекомендации по улучшению
```

4. **Доработайте** по результатам критики
5. **Примите решение** о финальных названиях систем
6. **Запустите разворачивание** хранилища

---

*Шаблон версии 1.1 | S2R Template | 2026-01-08*


# SOURCE_FILE: 0.OPS/0.6.Repository-Processes/02-standards.md
---
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Стандарты оформления (Standards)

## Формат документа

Все документы в формате **Markdown** с **YAML frontmatter**.

```markdown
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: FA4
kernel: A
system: System-of-Interest
role: Meaning
---

# Заголовок документа

Содержимое...
```

## Обязательные поля frontmatter

| Поле | Тип | Описание |
|------|-----|----------|
| `type` | string | doc, spec, process, report, template |
| `status` | string | stub, draft, active, archived |
| `created` | date | Дата создания (ISO 8601) |
| `updated` | date | Дата обновления (ISO 8601) |

## Рекомендуемые поля frontmatter

| Поле | Тип | Описание |
|------|-----|----------|
| `family` | string | Код семейства (FA1, FB5...) |
| `kernel` | string | Буква ядра (A, B, C...) |
| `system` | string | Suprasystem, System-of-Interest, Constructor |
| `role` | string | Meaning, Architecture, Operations |
| `scope` | string | local-edge, project, ecosystem |
| `related` | list | Связанные документы |
| `fpf_patterns` | list | Коды паттернов FPF |

## Форматирование Markdown

### Заголовки

```markdown
# H1 — только один на документ (название)
## H2 — основные разделы
### H3 — подразделы
#### H4 — детали (редко)
```

### Списки

```markdown
- Маркированный список
- Второй пункт

1. Нумерованный список
2. Второй пункт
```

### Таблицы

```markdown
| Заголовок 1 | Заголовок 2 |
|-------------|-------------|
| Значение 1  | Значение 2  |
```

### Код

```markdown
Инлайн: `code`

Блок:
\`\`\`language
code block
\`\`\`
```

### Ссылки

```markdown
[Текст ссылки](path/to/document.md)
[Внешняя ссылка](https://example.com)
```

## Правила контента

1. **Один документ — одна тема** (SSOT)
2. **Заголовок = имя файла** (по возможности)
3. **Начинай с сути** — не с вводных слов
4. **Используй таблицы** для структурированных данных
5. **Ссылайся на другие документы** через `related` и inline-ссылки

## Язык документов

- **Папки:** только английский
- **Файлы:** могут быть на русском
- **Содержимое:** на языке команды (обычно русский)

## Именование файлов

| Тип файла | Правило | Пример |
|-----------|---------|--------|
| README | Без номера: `README.md` | `README.md` |
| Содержательные файлы | С номером по значимости: `NN-name.md` | `01-kernels-model.md` |

**Важно:** README файлы никогда не имеют номеров. Номера отражают порядок значимости/приоритет чтения.

## Обязательная синхронизация при изменении структуры

> **КРИТИЧЕСКИ ВАЖНО:** При изменении названия файла, папки или структуры репозитория необходимо обновить связанные документы.

### Файлы, требующие синхронизации

| Файл | Когда обновлять |
|------|-----------------|
| `03-structure.md` | При любом изменении структуры |
| `CLAUDE.md` | При изменении структуры 0.OPS/ |
| `README.md` (корневой) | При изменении ядер или основной структуры |
| `03-our-systems-map.md` | При добавлении/изменении ядер |
| `01-value-chain.md` | При добавлении/изменении ядер |
| `02-kernels-relations.md` | При изменении связей между ядрами |
| `03-systems-relations.md` | При изменении связей систем |
| `08-deployment-guide.md` | При изменении файлов в 0.OPS/ |

> **Подробнее:** [08-deployment-guide.md](08-deployment-guide.md#обязательная-синхронизация-при-изменении-структуры)

## См. также

- [frontmatter-spec.md](frontmatter-spec.md) — детали метаданных
- [document-creation.md](document-creation.md) — процесс создания


# SOURCE_FILE: 0.OPS/0.6.Repository-Processes/03-structure.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Структура репозитория (Structure)

## Верхнеуровневая структура

```
s2r/
├── 0.OPS/                       # F0: Метаэпистема хранилища
├── A.SOI-Name/                  # Ядро A: Целевая система
├── B.Our-System-Name/           # Ядро B: Наша система
├── C.../                        # Ядра C, D... (по необходимости)
├── CLAUDE.md                    # ⭐ Инструкции для AI
├── README.md                    # Описание проекта
└── CONTRIBUTING.md              # Правила участия
```

## Структура F0 (Repository Management)

```
0.OPS/
├── README.md
├── 0.1.Knowledge-Logic/         # Онтология и модель
│   ├── README.md
│   ├── 01-kernels-model.md
│   ├── 02-document-families.md
│   ├── 03-our-systems-map.md
│   ├── 04-ontology.md
│   ├── 05-glossary.md
│   ├── 06-taxonomy.md
│   ├── 07-naming.md
│   ├── 08-anti-patterns.md
│   └── 09-examples-library.md
├── 0.2.Kernels-Bridge/          # Связи между ядрами
│   ├── README.md
│   ├── 01-value-chain.md
│   ├── 02-kernels-relations.md
│   └── 03-systems-relations.md  # Структура связанности систем
├── 0.3.Roles-Matrix-3x3/        # Матрица ролей 3×3
│   ├── roles-matrix.md          # Полная версия
│   └── roles-matrix-brief.md    # Краткая версия
├── 0.4.FPF-Integration/         # Интеграция с FPF
│   ├── fpf/                     # Копия спецификации FPF
│   ├── fpf-integration.md
│   └── fpf-patterns-map.md
├── 0.5.AI-Reports/              # AI-проверки и отчёты
│   ├── README.md
│   ├── Validation-Specs/        # ТЗ на проверки
│   │   ├── README.md
│   │   ├── 01-formal-checks.md
│   │   ├── 02-content-checks.md
│   │   └── 03-development-analysis.md
│   └── Validation-Results/      # Результаты проверок
├── 0.6.Repository-Processes/    # Процессы и стандарты
│   ├── README.md
│   ├── 01-project-description-template.md
│   ├── 02-standards.md
│   ├── 03-structure.md
│   ├── 04-document-creation.md
│   ├── 05-frontmatter-spec.md
│   ├── 06-workflows.md
│   ├── 07-roles.md
│   └── 08-deployment-guide.md   # ⭐ Руководство по развёртыванию
├── 0.7.Plans-and-Meetings/      # Планирование и совещания
├── 0.9.Inbox/                   # Входящие идеи и предложения
└── 0.99.Archive/                # Архив
```

## Структура ядра (Kernel)

> **Важно:** Папки именуются по именам систем, не по ролям.

```
X.{System-Name}/
├── README.md                        # Описание ядра
├── X0.{System-Name}-Management/     # FX0: Управление (опционально)
│   ├── README.md
│   └── local-ontology.md
├── X1.{Suprasystem-Name}/           # Надсистема
│   ├── X1.1.Meaning/                # FX1
│   │   └── README.md
│   ├── X1.2.Architecture/           # FX2
│   │   └── README.md
│   └── X1.3.Operations/             # FX3
│       └── README.md
├── X2.{System-Name}/                # Целевая система (SoI)
│   ├── X2.1.Meaning/                # FX4
│   │   └── README.md
│   ├── X2.2.Architecture/           # FX5
│   │   └── README.md
│   └── X2.3.Operations/             # FX6
│       └── README.md
└── X3.{Constructor-Name}/           # Система создания
    ├── X3.1.Meaning/                # FX7
    │   └── README.md
    ├── X3.2.Architecture/           # FX8
    │   └── README.md
    └── X3.3.Operations/             # FX9
        └── README.md
```

где `X` = A, B, C... (буква ядра)

## Внешние данные и первичка

> **Принцип:** Хранилище содержит **знания о системах**, а не первичные данные.

### Что хранится ВНЕ этого репозитория

| Тип данных | Где хранится | В репозитории указываем |
|------------|--------------|-------------------------|
| **Первичка** (документы, счета) | 1С, ERP, DMS | Ссылку и краткое описание |
| **Финансовые показатели** | BI-система, таблицы | Ссылку и структуру метрик |
| **Базы данных** | СУБД, хранилища | Схему и назначение |
| **Код** | Git-репозитории | Ссылку и описание |
| **Медиа-файлы** | CDN, хранилища | Ссылку и описание |

### Как указывать внешние данные

В документах хранилища указывайте:

```markdown
## Внешние источники данных

| Источник | Тип | Расположение | Описание |
|----------|-----|--------------|----------|
| CRM | База данных | `db.company.com/crm` | Клиентская база |
| 1С | ERP | `1c.company.com` | Финансовая первичка |
| Analytics | BI | `bi.company.com/dashboard` | Метрики продукта |
```

### Шаблон описания внешнего источника

```markdown
### [Название источника]

**Тип:** База данных / ERP / BI / Файловое хранилище
**Расположение:** [URL или путь]
**Владелец:** [@username]
**Доступ:** [описание прав доступа]

**Содержимое:**
- [Что хранится]
- [Структура данных]

**Связь с хранилищем:**
- Используется в: [ссылки на документы]
- Для: [назначение]
```

## Навигационная таблица

| Путь | Семейство | Содержимое |
|------|-----------|------------|
| `0.OPS/` | F0 | Метаэпистема хранилища |
| `X.../X1.{Supra}/X1.1.Meaning/` | FX1 | Контекст, рынок |
| `X.../X1.{Supra}/X1.2.Architecture/` | FX2 | Окружение, интерфейсы |
| `X.../X1.{Supra}/X1.3.Operations/` | FX3 | Партнёрства |
| `X.../X2.{SoI}/X2.1.Meaning/` | FX4 | Требования, ценность |
| `X.../X2.{SoI}/X2.2.Architecture/` | FX5 | Архитектура |
| `X.../X2.{SoI}/X2.3.Operations/` | FX6 | Реализация |
| `X.../X3.{Constr}/X3.1.Meaning/` | FX7 | Принципы команды |
| `X.../X3.{Constr}/X3.2.Architecture/` | FX8 | Платформа |
| `X.../X3.{Constr}/X3.3.Operations/` | FX9 | Команда, методология |

## См. также

- [../0.1.Knowledge-Logic/01-kernels-model.md](../0.1.Knowledge-Logic/01-kernels-model.md) — модель ядер
- [../0.1.Knowledge-Logic/07-naming.md](../0.1.Knowledge-Logic/07-naming.md) — именование


# SOURCE_FILE: 0.OPS/0.6.Repository-Processes/04-document-creation.md
---
---
type: process
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Процесс создания документов (Document Creation)

## Алгоритм создания

```
1. Определи ЯДРО
   └── О какой системе документ?

2. Определи СЕМЕЙСТВО (F1-F9)
   ├── Система: Suprasystem / SoI / Constructor
   └── Роль: Meaning / Architecture / Operations

3. Проверь СУЩЕСТВУЮЩИЕ документы
   └── Возможно, нужно дополнить, а не создавать

4. Создай документ
   ├── Правильный путь
   ├── Правильный frontmatter
   └── Содержимое

5. Обнови СВЯЗИ
   └── Добавь в related связанных документов
```

## Шаг 1: Определи ядро

| Вопрос | Ответ |
|--------|-------|
| О главной целевой системе? | Ядро A |
| О нашей подсистеме/сервисе? | Ядро B, C... |
| О команде создания? | Зависит от чьей команды |

## Шаг 2: Определи семейство

### По системе

| Документ о... | Система |
|---------------|---------|
| Рынке, контексте, окружении | X1.Suprasystem |
| Самом продукте/системе | X2.System-of-Interest |
| Команде, инструментах | X3.Constructor |

### По роли

| Документ о... | Роль |
|---------------|------|
| Ценности, требованиях, зачем | X.1.Meaning |
| Структуре, архитектуре, компонентах | X.2.Architecture |
| Процессах, операциях, как работает | X.3.Operations |

## Шаг 3: Проверь существующие

```bash
# Посмотри содержимое целевой папки
ls -la X.Kernel/X2.System-of-Interest/X2.1.Meaning/

# Поищи похожие документы
grep -r "ключевое слово" .
```

## Шаг 4: Создай документ

### Шаблон

```markdown
---
type: doc
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
family: FXN
kernel: X
system: System-of-Interest
role: Meaning
---

# Название документа

## Назначение

[Зачем этот документ?]

## Содержимое

[Основной контент]

## См. также

- [related-doc.md](path/to/related-doc.md)
```

## Шаг 5: Обнови связи

1. Добавь `related` в frontmatter нового документа
2. Обнови `related` в связанных документах
3. При необходимости обнови README папки

## Чеклист

- [ ] Определено ядро (A, B, C...)
- [ ] Определено семейство (FX1-FX9)
- [ ] Проверены существующие документы
- [ ] Создан файл в правильной папке
- [ ] Заполнен frontmatter
- [ ] Написано содержимое
- [ ] Обновлены связи

## Типичные ошибки

| Ошибка | Правильно |
|--------|-----------|
| Документ не в том ядре | Сначала определи о какой системе речь |
| Путаница система/роль | Система = уровень, роль = угол зрения |
| Дублирование | Проверь существующие документы |
| Нет frontmatter | Всегда добавляй метаданные |

## См. также

- [02-standards.md](02-standards.md) — стандарты оформления
- [05-frontmatter-spec.md](05-frontmatter-spec.md) — спецификация метаданных
- [../0.1.Knowledge-Logic/02-document-families.md](../0.1.Knowledge-Logic/02-document-families.md) — модель семейств


# SOURCE_FILE: 0.OPS/0.6.Repository-Processes/05-frontmatter-spec.md
---
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Спецификация Frontmatter

## Формат

YAML-блок в начале документа, ограниченный `---`:

```yaml
---
field: value
list:
  - item1
  - item2
---
```

## Обязательные поля

### type

Тип документа.

```yaml
type: doc | spec | process | report | template
```

| Значение | Описание |
|----------|----------|
| `doc` | Описательный документ |
| `spec` | Спецификация, требования |
| `process` | Описание процесса |
| `report` | Отчёт, результат |
| `template` | Шаблон |

### status

Статус зрелости.

```yaml
status: stub | draft | active | archived
```

| Значение | Описание |
|----------|----------|
| `stub` | Заглушка, только заголовок |
| `draft` | Черновик, в работе |
| `active` | Актуальный, используется |
| `archived` | Архивный |

### created

Дата создания в формате ISO 8601.

```yaml
created: 2026-01-14
```

### updated

Дата последнего обновления.

```yaml
updated: 2026-01-14
```

## Рекомендуемые поля

### family

Код семейства документа.

```yaml
family: FA4    # Ядро A, семейство 4
family: FB9    # Ядро B, семейство 9
family: F0     # Управление хранилищем
```

### kernel

Буква ядра.

```yaml
kernel: A | B | C | ...
```

### system

Система в рамках ядра.

```yaml
system: Suprasystem | System-of-Interest | Constructor
```

### role

Роль (угол зрения).

```yaml
role: Meaning | Architecture | Operations
```

### scope

Область применимости.

```yaml
scope: local-edge | project | ecosystem | universal
```

### layer

Слой знаний.

```yaml
layer: methodology | architecture | operations | data
```

### related

Связанные документы.

```yaml
related:
  - ../path/to/doc1.md
  - ../path/to/doc2.md
```

### fpf_patterns

Связанные паттерны FPF.

```yaml
fpf_patterns:
  - A.1       # Holonic Foundation
  - A.1.1     # Bounded Context
  - B.3       # Trust Calculus
```

### target_audience

Целевая аудитория.

```yaml
target_audience:
  - developers
  - managers
  - ai-agents
```

### tags

Свободные теги для поиска.

```yaml
tags:
  - architecture
  - api
  - security
```

## Полный пример

```yaml
---
type: spec
status: active
created: 2026-01-14
updated: 2026-01-14
family: FA5
kernel: A
system: System-of-Interest
role: Architecture
scope: project
layer: architecture
related:
  - ../A2.1.Meaning/requirements.md
  - ../A2.3.Operations/deployment.md
fpf_patterns:
  - A.1
  - A.7
target_audience:
  - developers
  - architects
tags:
  - api
  - design
---
```

## Валидация

Frontmatter должен:
1. Начинаться с `---`
2. Заканчиваться `---`
3. Быть валидным YAML
4. Содержать все обязательные поля

## См. также

- [02-standards.md](02-standards.md) — стандарты оформления
- [04-document-creation.md](04-document-creation.md) — процесс создания


# SOURCE_FILE: 0.OPS/0.6.Repository-Processes/06-workflows.md
---
---
type: process
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Рабочие процессы (Workflows)

## Жизненный цикл документа

```
stub → draft → active → archived
  │      │       │         │
  │      │       │         └── Устарел, сохранён для истории
  │      │       └── Актуален, используется
  │      └── В работе, не финализирован
  └── Заглушка, только заголовок
```

## Процесс добавления нового ядра

```
1. Определи позицию в карте систем
   └── Прочитай 0.1.Knowledge-Logic/our-systems-map.md

2. Выбери букву ядра (B, C, D...)

3. Создай структуру папок
   └── Используй шаблон из templates/

4. Создай README.md ядра

5. Обнови карту систем
   └── 0.1.Knowledge-Logic/our-systems-map.md

6. Обнови цепочку ценности
   └── 0.2.Kernels-Bridge/value-chain.md
```

## Процесс ревью документа

```
1. Проверь frontmatter
   └── Все обязательные поля заполнены?

2. Проверь размещение
   └── Документ в правильном семействе?

3. Проверь связи
   └── related актуальны?

4. Проверь содержимое
   └── Соответствует назначению семейства?

5. Обнови статус
   └── draft → active (если готов)
```

## Процесс архивации

```
1. Измени статус на archived
   └── status: archived

2. Добавь причину архивации
   └── В начале документа или в комментарии

3. Обнови связи
   └── Удали из related других документов или пометь

4. При необходимости перенеси в 0.99.Archive/
```

## Регулярные процессы

### Еженедельно

- [ ] Проверка Inbox (0.9.Inbox/)
- [ ] Распределение новых идей по семействам

### Ежемесячно

- [ ] Проверка актуальности документов
- [ ] Архивация устаревших
- [ ] Обновление карты систем

### Ежеквартально

- [ ] Ревью структуры ядер
- [ ] Проверка связей между ядрами
- [ ] Обновление онтологии при необходимости

## См. также

- [document-creation.md](document-creation.md) — создание документов
- [roles.md](roles.md) — роли и ответственность


# SOURCE_FILE: 0.OPS/0.6.Repository-Processes/07-roles.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Роли и ответственность (Roles)

## Роли в хранилище

### Администратор хранилища

**Ответственность:**
- Структура и целостность репозитория
- Управление F0 (Repository Management)
- Координация между ядрами
- Поддержка онтологии

**Права:**
- Полный доступ ко всем ядрам
- Создание/удаление ядер
- Изменение общей онтологии

### Владелец ядра (Kernel Owner)

**Ответственность:**
- Целостность своего ядра (A, B, C...)
- Актуальность документов ядра
- Локальная онтология (X0.Kernel-Management)
- Координация контрибьюторов ядра

**Права:**
- Полный доступ к своему ядру
- Назначение ответственных за семейства

### Ответственный за семейство

**Ответственность:**
- Актуальность документов семейства (FX1-FX9)
- Ревью изменений в семействе
- Связи с другими семействами

**Права:**
- Доступ к своему семейству
- Аппрув изменений

### Контрибьютор

**Ответственность:**
- Создание и обновление документов
- Соблюдение стандартов
- Поддержание связей (related)

**Права:**
- Создание документов (через PR)
- Предложение изменений

## Матрица ответственности

```
                    Админ   Владелец   Отв. семейства   Контрибьютор
                    хран.   ядра
F0 (управление)     RACI    I          -                C
Создание ядра       RA      CI         -                I
X0 (управление яд.) I       RA         C                I
FX1-FX9             I       A          R                C
Документы           I       I          A                R

R = Responsible (исполняет)
A = Accountable (отвечает)
C = Consulted (консультирует)
I = Informed (информируют)
```

## Назначение ролей

### Формат записи

```markdown
## Ядро X: [Название]

**Владелец:** @username

**Ответственные за семейства:**
| Семейство | Ответственный |
|-----------|---------------|
| FX1-FX3   | @user1        |
| FX4-FX6   | @user2        |
| FX7-FX9   | @user3        |
```

### Где записывать

- Общее: в этом документе
- По ядрам: в `X0.Kernel-Management/README.md`

## Текущие назначения

> **TODO:** Заполните при инициализации проекта.

### Администратор хранилища

- [ ] Назначить администратора

### Ядро A

- [ ] Назначить владельца
- [ ] Назначить ответственных за семейства

### Ядро B

- [ ] Назначить владельца
- [ ] Назначить ответственных за семейства

## См. также

- [workflows.md](workflows.md) — рабочие процессы
- [../0.1.Knowledge-Logic/ontology.md](../0.1.Knowledge-Logic/ontology.md) — определение ролей


# SOURCE_FILE: 0.OPS/0.6.Repository-Processes/08-deployment-guide.md
---
---
type: doc
status: active
created: 2026-01-14
updated: 2026-01-14
family: F0
scope: repository
---

# Руководство по развёртыванию S2R (Deployment Guide)

> **Для новых пользователей:** Этот документ описывает **пошаговые действия** для развёртывания шаблона S2R под ваш проект.

## Обзор процесса

```
1. Клонировать репозиторий
2. Заполнить описание проекта
3. Переименовать ядра и папки
4. Скопировать методологические файлы (без изменений)
5. Удалить шаблонные папки (если не нужны)
6. Обновить карту систем и цепочку ценности
```

---

## Действия с каждой папкой и файлом

### Корневой уровень

| Элемент | Действие | Описание |
|---------|----------|----------|
| `0.OPS/` | **Оставить** | Метаэпистема хранилища (F0) |
| `A.SOI-Name/` | **Переименовать** | → `A.{Ваша-Целевая-Система}/` |
| `B.Our-System-Name/` | **Переименовать или удалить** | → `B.{Ваша-Система}/` или удалить, если только одно ядро |
| `README.md` | **Заменить** | Заменить на описание вашего проекта |
| `CONTRIBUTING.md` | **Оставить или адаптировать** | Правила участия |
| `.gitignore` | **Оставить** | Без изменений |

---

### Папка 0.OPS/ (Метаэпистема)

#### 0.1.Knowledge-Logic/ — **ОСТАВИТЬ БЕЗ ИЗМЕНЕНИЙ**

Эти файлы определяют методологию S2R и не требуют изменений:

| Файл | Действие | Назначение |
|------|----------|------------|
| `README.md` | Оставить | Индекс папки |
| `01-kernels-model.md` | Оставить | Модель ядер (методология) |
| `02-document-families.md` | Оставить | Семейства F1-F9 (методология) |
| `03-our-systems-map.md` | **ЗАПОЛНИТЬ** | Карта систем вашего проекта |
| `04-ontology.md` | Оставить | Общая онтология |
| `05-glossary.md` | **ДОПОЛНИТЬ** | Добавить термины вашего проекта |
| `06-taxonomy.md` | Оставить | Классификация документов |
| `07-naming.md` | Оставить | Соглашения об именовании |
| `08-anti-patterns.md` | Оставить | Анти-паттерны |
| `09-examples-library.md` | Оставить | Библиотека примеров |

#### 0.2.Kernels-Bridge/ — **ЗАПОЛНИТЬ**

| Файл | Действие | Назначение |
|------|----------|------------|
| `README.md` | Оставить | Индекс папки |
| `01-value-chain.md` | **ЗАПОЛНИТЬ** | Цепочка ценности вашего проекта |
| `02-kernels-relations.md` | **ЗАПОЛНИТЬ** | Связи между ядрами |
| `03-systems-relations.md` | **ЗАПОЛНИТЬ** | Структура связанности систем |

#### 0.3.Roles-Matrix-3x3/ — **ОСТАВИТЬ БЕЗ ИЗМЕНЕНИЙ**

Методологические файлы, не требуют изменений:

| Файл | Действие | Назначение |
|------|----------|------------|
| `roles-matrix.md` | Оставить | Полная матрица ролей 3×3 |
| `roles-matrix-brief.md` | Оставить | Краткая версия матрицы |

#### 0.4.FPF-Integration/ — **ОСТАВИТЬ БЕЗ ИЗМЕНЕНИЙ**

Интеграция с First Principles Framework:

| Файл | Действие | Назначение |
|------|----------|------------|
| `fpf/` | Оставить | Спецификация FPF |
| `fpf-integration.md` | Оставить | Связь S2R и FPF |
| `fpf-patterns-map.md` | Оставить | Маппинг паттернов |

#### 0.5.AI-Reports/ — **ОСТАВИТЬ БЕЗ ИЗМЕНЕНИЙ**

AI-проверки и автоматические отчёты:

| Папка/Файл | Действие | Назначение |
|------------|----------|------------|
| `README.md` | Оставить | Описание системы проверок |
| `Validation-Specs/` | Оставить | ТЗ на автоматические проверки |
| `Validation-Results/` | Оставить (пустая) | Сюда AI будет складывать результаты |

Спецификации проверок (`Validation-Specs/`):

| Файл | Назначение |
|------|------------|
| `01-formal-checks.md` | Формальные проверки структуры и ссылок |
| `02-content-checks.md` | Содержательные проверки методологии |
| `03-development-analysis.md` | Анализ полноты и предложения по развитию |

#### 0.6.Repository-Processes/ — **ЧАСТИЧНО ЗАПОЛНИТЬ**

| Файл | Действие | Назначение |
|------|----------|------------|
| `README.md` | Оставить | Индекс папки |
| `01-project-description-template.md` | **ЗАПОЛНИТЬ ПЕРВЫМ** | Описание вашего проекта |
| `02-standards.md` | Оставить или адаптировать | Стандарты оформления |
| `03-structure.md` | Оставить | Структура репозитория |
| `04-document-creation.md` | Оставить | Как создавать документы |
| `05-frontmatter-spec.md` | Оставить | Спецификация метаданных |
| `06-workflows.md` | **АДАПТИРОВАТЬ** | Рабочие процессы вашей команды |
| `07-roles.md` | **АДАПТИРОВАТЬ** | Роли в вашей команде |
| `08-deployment-guide.md` | Оставить (этот файл) | Руководство по развёртыванию |

#### 0.7.Plans-and-Meetings/ — **ОСТАВИТЬ (ПУСТАЯ)**

| Действие | Назначение |
|----------|------------|
| Оставить пустой | Для планов и протоколов совещаний |

#### 0.9.Inbox/ — **ОСТАВИТЬ (ПУСТАЯ)**

| Действие | Назначение |
|----------|------------|
| Оставить пустой | Для входящих идей и заметок |

#### 0.99.Archive/ — **ОСТАВИТЬ (ПУСТАЯ)**

| Действие | Назначение |
|----------|------------|
| Оставить пустой | Архив устаревших документов |

#### CLAUDE.md — **ОСТАВИТЬ БЕЗ ИЗМЕНЕНИЙ**

| Действие | Назначение |
|----------|------------|
| Оставить | Инструкции для AI-агентов |

---

### Ядро A (Целевая система)

**Папка:** `A.SOI-Name/` → **Переименовать** в `A.{Ваша-Целевая-Система}/`

| Элемент | Действие | Пример |
|---------|----------|--------|
| `A.SOI-Name/` | Переименовать | `A.Automobile/` |
| `A0.SOI-Name-Management/` | Переименовать | `A0.Automobile-Management/` |
| `A1.Suprasystem-Name/` | Переименовать | `A1.Taxi/` (физическая надсистема!) |
| `A2.SOI-Name/` | Переименовать | `A2.Automobile/` |
| `A3.Constructor-Name/` | Переименовать | `A3.Assembly-Line/` |
| `README.md` | **ЗАПОЛНИТЬ** | Описание ядра A |

> **Важно:** A1 должна быть **физической системой**, в которую входит целевая система. Не "рынок", не "отрасль", не "повседневная жизнь"!

**Подпапки ролей** (X.1.Meaning/, X.2.Architecture/, X.3.Operations/) — оставить структуру, заполнять документами по мере необходимости.

---

### Ядро B (Наша система)

**Папка:** `B.Our-System-Name/` → **Переименовать или удалить**

| Сценарий | Действие |
|----------|----------|
| Есть вторая значимая система | Переименовать в `B.{Имя-Системы}/` |
| Только одна система (Ядро A) | Удалить папку B |
| Несколько систем | Создать C./, D./ по аналогии |

---

## Создание дополнительных ядер (C, D, E...)

Если в проекте несколько "наших систем", создайте дополнительные ядра:

### Шаг 1: Скопируйте структуру

```bash
# Скопировать ядро B как шаблон для C
cp -r B.Our-System-Name C.{Имя-Системы}
```

### Шаг 2: Переименуйте папки

```bash
# Переименовать все подпапки
mv C.{Имя-Системы}/B0.Our-System-Name-Management C.{Имя-Системы}/C0.{Имя-Системы}-Management
mv C.{Имя-Системы}/B1.Suprasystem-Name C.{Имя-Системы}/C1.{Надсистема-C}
mv C.{Имя-Системы}/B2.Our-System-Name C.{Имя-Системы}/C2.{Имя-Системы}
mv C.{Имя-Системы}/B3.Constructor-Name C.{Имя-Системы}/C3.{Создатель-C}
```

### Шаг 3: Обновите внутренние папки

```bash
# Переименовать папки ролей (замените B на C)
for dir in C.{Имя-Системы}/C*/; do
  for subdir in "$dir"B*; do
    newname=$(echo "$subdir" | sed 's/B/C/')
    mv "$subdir" "$newname"
  done
done
```

### Шаг 4: Обновите связи

1. Добавьте ядро в `0.1.Knowledge-Logic/03-our-systems-map.md`
2. Добавьте в `0.2.Kernels-Bridge/01-value-chain.md`
3. Обновите `0.2.Kernels-Bridge/02-kernels-relations.md`

---

## Чек-лист развёртывания

### Этап 1: Подготовка

- [ ] Клонировать репозиторий
- [ ] Удалить `.git/` и инициализировать новый репозиторий
- [ ] Заполнить `0.6.Repository-Processes/01-project-description-template.md`

### Этап 2: Определение систем

- [ ] Определить целевую систему (Ядро A)
- [ ] Определить надсистему (A1) — физическая система!
- [ ] Определить конструктора (A3)
- [ ] Определить "наши системы" (Ядра B, C, D...)

### Этап 3: Переименование

- [ ] Переименовать `A.SOI-Name/` → `A.{Целевая-Система}/`
- [ ] Переименовать все подпапки A с реальными именами
- [ ] Переименовать или удалить `B.Our-System-Name/`
- [ ] Создать дополнительные ядра (C, D...) при необходимости

### Этап 4: Заполнение

- [ ] Заполнить README.md ядра A
- [ ] Заполнить `03-our-systems-map.md`
- [ ] Заполнить `01-value-chain.md`
- [ ] Заполнить `02-kernels-relations.md`
- [ ] Обновить корневой README.md

### Этап 5: Проверка

- [ ] Все папки ядер имеют конкретные имена (не "Target-System")
- [ ] A1 — физическая система (не "рынок", не "отрасль")
- [ ] Все ссылки в документах работают
- [ ] CLAUDE.md остаётся без изменений

---

## Примеры переименования

### Пример 1: Автомобильное производство

```bash
# Ядро A
mv A.SOI-Name A.Automobile
mv A.Automobile/A0.SOI-Name-Management A.Automobile/A0.Automobile-Management
mv A.Automobile/A1.Suprasystem-Name A.Automobile/A1.Taxi
mv A.Automobile/A2.SOI-Name A.Automobile/A2.Automobile
mv A.Automobile/A3.Constructor-Name A.Automobile/A3.Assembly-Line

# Ядро B (подсистема)
mv B.Our-System-Name B.Engine
mv B.Engine/B1.Suprasystem-Name B.Engine/B1.Automobile
mv B.Engine/B2.Our-System-Name B.Engine/B2.Engine
mv B.Engine/B3.Constructor-Name B.Engine/B3.Engine-Shop
```

### Пример 2: Мобильное приложение

```bash
# Ядро A
mv A.SOI-Name A.Mobile-App
mv A.Mobile-App/A1.Suprasystem-Name A.Mobile-App/A1.User-Smartphone
mv A.Mobile-App/A2.SOI-Name A.Mobile-App/A2.Mobile-App
mv A.Mobile-App/A3.Constructor-Name A.Mobile-App/A3.Dev-Team

# Удалить ядро B (если не нужно)
rm -rf B.Our-System-Name
```

### Пример 3: E-commerce с несколькими системами

```bash
# Ядро A — платформа
mv A.SOI-Name A.Marketplace
mv A.Marketplace/A1.Suprasystem-Name A.Marketplace/A1.User-Device
mv A.Marketplace/A2.SOI-Name A.Marketplace/A2.Marketplace
mv A.Marketplace/A3.Constructor-Name A.Marketplace/A3.Platform-Team

# Ядро B — каталог
mv B.Our-System-Name B.Catalog-Service
mv B.Catalog-Service/B1.Suprasystem-Name B.Catalog-Service/B1.Marketplace
mv B.Catalog-Service/B2.Our-System-Name B.Catalog-Service/B2.Catalog-Service
mv B.Catalog-Service/B3.Constructor-Name B.Catalog-Service/B3.Catalog-Team

# Ядро C — платёжный шлюз (создать копированием)
cp -r B.Our-System-Name C.Payment-Gateway
# ... переименовать подпапки ...
```

---

## Обязательная синхронизация при изменении структуры

> **КРИТИЧЕСКИ ВАЖНО:** При любом изменении структуры репозитория необходимо обновить связанные файлы.

### Триггеры синхронизации

| Событие | Что обновить |
|---------|--------------|
| Переименование файла | Ссылки во всех документах, `03-structure.md` |
| Переименование папки | Все ссылки, `03-structure.md`, `README.md` корневой |
| Добавление файла | `03-structure.md`, README папки (если есть) |
| Удаление файла | Ссылки во всех документах, `03-structure.md` |
| Добавление ядра | `03-our-systems-map.md`, `01-value-chain.md`, `02-kernels-relations.md`, `03-systems-relations.md` |
| Переименование ядра | Все вышеперечисленные + корневой `README.md` |

### Файлы, требующие синхронизации

При изменении структуры **ОБЯЗАТЕЛЬНО** проверьте и обновите:

| Файл | Что содержит |
|------|--------------|
| `0.OPS/0.6.Repository-Processes/03-structure.md` | Полная структура репозитория |
| `CLAUDE.md` (корневой) | Инструкции для AI-агентов |
| `README.md` (корневой) | Обзор структуры проекта |
| `0.OPS/0.1.Knowledge-Logic/03-our-systems-map.md` | Карта всех систем |
| `0.OPS/0.2.Kernels-Bridge/01-value-chain.md` | Цепочка ценности |
| `0.OPS/0.2.Kernels-Bridge/02-kernels-relations.md` | Матрица связей ядер |
| `0.OPS/0.2.Kernels-Bridge/03-systems-relations.md` | Структура связанности |
| `0.OPS/0.6.Repository-Processes/08-deployment-guide.md` | Этот файл — таблицы файлов |

### Правило именования файлов

| Тип файла | Правило именования | Пример |
|-----------|-------------------|--------|
| README | Без номера: `README.md` | `README.md` |
| Содержательные файлы | С номером по значимости: `NN-name.md` | `01-kernels-model.md` |

> **Важно:** README файлы **никогда** не имеют номеров в названии. Нумеруются только содержательные документы в порядке их значимости/приоритета чтения.

---

## Частые ошибки при развёртывании

| Ошибка | Правильно |
|--------|-----------|
| A1.Market/ | A1.User-Device/ (физическая система) |
| A1.Industry/ | A1.Taxi/ (конкретная система) |
| A.Target-System/ | A.Automobile/ (конкретное имя) |
| Оставить B.Our-System-Name/ | Переименовать или удалить |
| Изменить CLAUDE.md | Оставить без изменений |
| Изменить roles-matrix.md | Оставить без изменений |

---

## См. также

- [01-project-description-template.md](01-project-description-template.md) — шаблон описания проекта
- [03-structure.md](03-structure.md) — структура репозитория
- [../0.1.Knowledge-Logic/07-naming.md](../0.1.Knowledge-Logic/07-naming.md) — соглашения об именовании
- [../0.1.Knowledge-Logic/01-kernels-model.md](../0.1.Knowledge-Logic/01-kernels-model.md) — модель ядер


# SOURCE_FILE: 0.OPS/0.9.Inbox/s2r-orchestrator-concept.md
---
---
type: doc
status: draft
created: 2026-01-15
updated: 2026-01-15
family: F0
scope: repository
---

# Концепция: S2R Orchestrator — ассистент, который превращает знания и правила в рабочие документы

**S2R Orchestrator** — это система, которая отвечает на запросы пользователя не "из головы", а через управляемую сборку контекста из репозиториев и профиля пользователя, затем применяет набор инструкций (правил работы) и производит **выходные документы** (артефакты). Эти выходные документы далее могут становиться **новыми входными данными**: попадать в репозиторий, индекс знаний и профиль пользователя.

Смысл: превратить работу с ИИ из "чата" в **производственную линию документов**, где:

* **данные** (контент) отделены от **действий** (инструкций),
* сбор контекста воспроизводим и проверяем,
* результаты версионируются и переиспользуются.

---

## Чёткое разделение: данные vs действия

| Слой                               | Что это                                                                                                | Примеры                                                                                                                                                                          | Что отдаём на вход/выход                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **ДАННЫЕ (входной контекст)**      | Информация, из которой ИИ может извлечь смысл и факты                                                  | репозиторий S2R (семейства/ядра/шаблоны), репозиторий "индекса знаний" пользователя, артефакты прошлых работ, выдержки из источников, профиль/цифровой двойник (если разрешено)  | **Вход:** "пакет контекста" (подборка выдержек + ссылки/идентификаторы)                    |
| **ДЕЙСТВИЯ (инструкции)**          | Правила, по которым система интерпретирует запрос, собирает контекст, рассуждает и оформляет результат | распознавание роли/намерения, маршрутизация по S2R, поиск+переранжирование, сжатие контекста, проверка согласий на личные данные, шаблоны выходных документов, критерии качества | **Выход:** документ(ы) по шаблону + метаданные (почему так, что использовано)              |
| **ВЫХОДНЫЕ ДОКУМЕНТЫ (артефакты)** | Результат работы, который может стать новым знанием                                                    | ТЗ, спецификация, план, критика/улучшения, чеклист, "name card", политика/регламент, кусок репозитория                                                                           | **Выход:** файл/док + карта контекста; **потом:** индексирование и повторное использование |

---

## Почему это опирается на SoTA

Ваша задумка соответствует современным устойчивым паттернам построения LLM-систем:

1. **Retrieval-Augmented Generation (RAG):** связка "генерация + внешняя память", чтобы ответы опирались на обновляемые источники, а не только на параметры модели. Это базовая парадигма в knowledge-intensive задачах. ([arXiv](https://arxiv.org/abs/2005.11401))

2. **Dense retrieval (двухэнкодерные ретриверы):** практичный способ находить релевантные фрагменты по смыслу в больших корпусах (в т.ч. внутренних). ([arXiv](https://arxiv.org/abs/2004.04906))

3. **Reranking (cross-encoder):** стандартный SoTA-приём: сначала быстро достать кандидатов, затем более "умной" моделью переранжировать топ-N, чтобы резко поднять точность контекста. ([arXiv](https://arxiv.org/abs/1901.04085))

4. **HyDE / query expansion через генерацию:** улучшение поиска, когда запрос пользователя короткий/смутный: сначала генерируется "гипотетический документ", затем по нему ищем. ([arXiv](https://arxiv.org/abs/2212.10496))

5. **Agentic pattern "Reason + Act":** разделение рассуждений и действий (поиск, извлечение, выбор инструментов) — один из ключевых современных подходов к сложным задачам. ([arXiv](https://arxiv.org/abs/2210.03629))

6. **Уплотнение/нормализация инструкций для инструментов и документации:** отдельная линия исследований показывает, что качество tool-use растёт, когда документация преобразована в короткие, унифицированные инструкции. Это напрямую применимо к вашему S2R как "инструкции для поведения". ([aclanthology.org](https://aclanthology.org/2025.naacl-long.44.pdf))

---

## Концепция использования (как команда это будет применять)

**Кто пользователь:** человек приходит с вопросом, но всегда в некотором "режиме" (роль) и с фокусом на некоторый объект/систему интереса.

**Что делает система:**

1. понимает, *какого типа результат* нужен (совет, план, документ, критика, ТЗ),
2. собирает контекст из S2R + (по необходимости) базы знаний пользователя,
3. применяет инструкции рассуждения (в т.ч. внутренние правила анализа),
4. выпускает **рабочий артефакт** в заданной форме,
5. сохраняет артефакт как новое знание.

**Два режима эксплуатации:**

* **Режим "быстрый":** минимум уточнений, компактный контекст, быстрый артефакт (черновик).
* **Режим "строгий":** уточнение цели/формата, явный "пакет контекста", проверки качества, сохранение в репозиторий как версия.

---

## Процесс работы системы (pipeline)

### 0) Вход

* Запрос пользователя.
* Контекст диалога.
* (Опционально) разрешение на использование личных данных/цифрового двойника.

### 1) Интерпретация запроса

* Определить тип выхода: **ответ / план / ТЗ / критика / спецификация / чеклист / пост / инструкция**.
* Сформировать 2–3 гипотезы "режима пользователя" и "объекта интереса" с уверенностью.
* Если уверенность низкая — задать **один** уточняющий вопрос про формат результата (не про внутренние термины).

### 2) План сборки контекста (Context Plan)

* Определить, какие части S2R наиболее релевантны (семейства/перспективы/шаблоны).
* Определить, нужен ли индекс знаний пользователя.
* Определить, нужен ли цифровой профиль (и только если есть согласие).

### 3) Сбор данных (Retrieval)

* Поиск кандидатов по S2R и по индексу знаний (lexical + semantic).
* Опционально: HyDE/расширение запроса, если запрос короткий/смутный.

### 4) Отбор и сжатие (Rerank + Compress)

* Переранжировать топ-N кандидатов cross-encoder'ом.
* Сжать в **пакет контекста**:
  * 6–15 коротких выдержек,
  * идентификаторы/ссылки на первоисточники,
  * список "что намеренно не использовано" (если важно).

### 5) Рассуждение (внутренняя логика)

* Применить внутреннюю методологию рассуждений (в т.ч. "рассуждения по FPF") как **движок анализа**, но:
  * для пользователя показывать только то, что полезно,
  * избегать "метаязыка" в выдаче, если это не внутренний документ.

### 6) Генерация артефакта

* Выбрать шаблон документа (из S2R или заданный пользователем).
* Сформировать результат:
  * основной текст,
  * допущения/ограничения,
  * критерии качества / риски / next steps.

### 7) Контроль качества

* Проверка на:
  * соответствие формату,
  * полноту (обязательные секции),
  * непротиворечивость,
  * корректное использование личных данных (если были).
* Если нужно — вернуть "версия 0.9" и список вопросов/дыр.

### 8) Сохранение (выход становится входом)

* Сохранить артефакт в репозиторий/хранилище:
  * документ,
  * метаданные (тип, объект, режим, использованные источники),
  * связь с задачей/проектом.
* Обновить индекс знаний.
* Обновить цифровой профиль (только допустимые агрегаты/сигналы и только при разрешении).

---

## Политика использования цифрового двойника (минимально необходимая)

**Три режима:**

1. **По умолчанию:** не использовать личные данные.
2. **Только из текущего диалога.**
3. **Полный профиль/индекс знаний:** только после явного подтверждения, с перечислением, какие разделы будут задействованы.

---

## Минимальная дорожная карта (MVP → Production)

### Этап 1 — MVP "ручная маршрутизация"

* Шаблоны выходных документов (минимум 5: критика, план, ТЗ, спецификация, чеклист).
* "Пакет контекста" как объект (структура + лимиты).
* Ручной выбор релевантных разделов S2R (без авто-раутера).
* Логи: что использовано, какой шаблон, какой выход.

**Критерий успеха:** команда стабильно получает качественные артефакты из S2R без хаоса.

### Этап 2 — Auto-routing + RAG-пайплайн

* Реестр (YAML/JSON) для разделов S2R: назначение, типы запросов, выходные артефакты.
* Dense retrieval + reranking.
* HyDE как опция для "плохих" запросов.
* Автоматическая сборка "пакета контекста".

**Критерий успеха:** качество не хуже ручного, а скорость выше.

### Этап 3 — Профиль/цифровой двойник и права доступа

* Механизм согласий и режимов.
* Подключение индекса знаний пользователя как отдельного источника.
* Политики хранения и аудит использования личных данных.

**Критерий успеха:** персонализация без потери доверия и без утечек.

### Этап 4 — Качество и эксплуатация

* Набор эталонных сценариев (evaluation set).
* Метрики: точность контекста, доля "принято без правок", число итераций, время до полезного артефакта.
* Регламент обновления S2R и шаблонов (versioning, changelog).

---

## Что команде нужно "сделать вместе" (краткий список работ)

1. Определить **набор типов выходных артефактов** (и формат каждого).
2. Зафиксировать **структуру "пакета контекста"** (схема + лимиты).
3. Описать **реестр S2R** (машинно-читаемая маршрутизация).
4. Реализовать **retrieval + rerank + compress**.
5. Ввести **режимы использования личных данных** и логи аудита.
6. Сделать **pipeline сохранения**: выход → репозиторий → индекс → повторное использование.
7. Собрать **набор эталонных задач** для оценки качества.

---

## См. также

- [CLAUDE.md](../../CLAUDE.md) — текущие инструкции для AI
- [02-document-families.md](../0.1.Knowledge-Logic/02-document-families.md) — семейства документов
- [roles-matrix.md](../0.3.Roles-Matrix-3x3/roles-matrix.md) — матрица ролей


# SOURCE_FILE: A.SOI-Name/A0.SOI-Name-Management/local-ontology.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: A
family: FA0
---

# Локальная онтология ядра A

## Назначение

Здесь определяются термины, специфичные для ядра A, которые:
- Отличаются от общей онтологии
- Имеют особое значение в контексте целевой системы
- Требуют уточнения для команды

## Локальные термины

> **TODO:** Добавьте термины по мере необходимости.

| Термин | Определение | Отличие от общего |
|--------|-------------|-------------------|
| *[термин]* | *[определение]* | *[чем отличается от общей онтологии]* |

## Связь с общей онтологией

Общая онтология: [../../0.OPS/0.1.Knowledge-Logic/ontology.md](../../0.OPS/0.1.Knowledge-Logic/ontology.md)

**Правило:** Если термин не определён здесь, используется определение из общей онтологии.


# SOURCE_FILE: B.Our-System-Name/B0.Our-System-Name-Management/local-ontology.md
---
---
type: doc
status: stub
created: 2026-01-14
updated: 2026-01-14
kernel: B
family: FB0
---

# Локальная онтология ядра B

## Назначение

Здесь определяются термины, специфичные для ядра B.

## Локальные термины

> **TODO:** Добавьте термины по мере необходимости.

| Термин | Определение | Отличие от общего |
|--------|-------------|-------------------|
| *[термин]* | *[определение]* | *[чем отличается]* |

## Связь с общей онтологией

Общая онтология: [../../0.OPS/0.1.Knowledge-Logic/ontology.md](../../0.OPS/0.1.Knowledge-Logic/ontology.md)

**Правило:** Если термин не определён здесь, используется определение из общей онтологии.


# SOURCE_FILE: CLAUDE.md
---
# CLAUDE.md — S2R (Structured Second-level Repository)

> **Общие инструкции:** см. `/Users/tserentserenov/IWE/CLAUDE.md`
>
> Этот файл содержит только специфику данного репозитория.

---

## 1. Тип репозитория

**Format** — спецификация протокола оформления downstream-репозиториев.

**Source-of-truth:** Да (для формата S2R).

---

## 1.1. Fallback Chain

```
1. Этот репо (спецификация S2R)
2. SPF (форма и процесс) → ~/IWE/SPF/
3. FPF (первые принципы) → ~/IWE/FPF/ (только если нет в SPF)
```

**Правило:** Если чего-то нет на текущем уровне — смотри выше.

---

## 2. Что такое S2R

**S2R** = Structured Second-level Repository = Systems–Roles Repository (SRR)

Это **шаблон/протокол** для организации downstream-репозиториев (особенно governance).

---

## 3. Структура S2R

### 3.1. Ядра (Kernels)

```
X.Kernel-Name/
├── X0.Kernel-Management/     # Локальная онтология ядра
├── X1.Suprasystem/           # Надсистема
│   ├── X1.1.Meaning/
│   ├── X1.2.Architecture/
│   └── X1.3.Operations/
├── X2.System-of-Interest/    # Целевая система
│   ├── X2.1.Meaning/
│   ├── X2.2.Architecture/
│   └── X2.3.Operations/
└── X3.Constructor/           # Система создания
    ├── X3.1.Meaning/
    ├── X3.2.Architecture/
    └── X3.3.Operations/
```

### 3.2. Метауровень (0.OPS/)

```
0.OPS/
├── 0.1.Knowledge-Logic/      # Онтология
├── 0.2.Kernels-Bridge/       # Связи между ядрами
├── 0.3.Roles-Matrix-3x3/     # Матрица ролей
├── 0.4.FPF-Integration/      # Интеграция с FPF
├── 0.6.Repository-Processes/ # Процессы
└── 0.99.Archive/
```

---

## 4. Матрица 3×3 (F1-F9)

| Роль ↓ / Система → | Надсистема (1) | SoI (2) | Создание (3) |
|--------------------|----------------|---------|--------------|
| **Предприниматель (.1)** | F1 | F2 | F3 |
| **Инженер (.2)** | F4 | F5 | F6 |
| **Менеджер (.3)** | F7 | F8 | F9 |

---

## 5. Критические правила

### 5.1. Система ≠ Эпистема

| Концепт | Может быть ядром? |
|---------|-------------------|
| **Система** (физическая сущность) | ✅ Да |
| **Эпистема** (область знания) | ❌ Нет |

**ЗАПРЕЩЕНО:** `E.Экономика/`, `G.Продвижение/`, `H.Монетизация/`

### 5.2. Фиксированная нумерация

```
X1 = Надсистема (∋ SoI)
X2 = SoI
X3 = Система создания (→ SoI)
```

**НЕЛЬЗЯ** менять нумерацию.

### 5.3. Чеклист создания ядра

Новое ядро можно создать **только если ВСЕ пункты выполнены**:

- [ ] Есть **владелец/роль**
- [ ] Есть **вход/выход**
- [ ] Есть **граница**
- [ ] Есть **цикл изменений**
- [ ] Это **НЕ эпистема**

---

## 6. Именование

### 6.1. Файлы

Format: `<номер>-<название>.md`

- Номер с ведущим нулём: `01-`, `02-`
- Название через дефисы: `mission-statement`
- Только латиница

### 6.2. Frontmatter

```yaml
---
family: F5
kernel: A
system: A2
role: Architecture
status: draft
target_audience: []
depends_on: []
---
```

---

## 7. Ключевые документы

| Документ | Путь |
|----------|------|
| Модель ядер | `0.1.Knowledge-Logic/01-kernels-model.md` |
| Семейства | `0.1.Knowledge-Logic/02-document-families.md` |
| Матрица ролей | `0.3.Roles-Matrix-3x3/roles-matrix.md` |
| Анти-паттерны | `0.1.Knowledge-Logic/08-anti-patterns.md` |
| Примеры | `0.1.Knowledge-Logic/09-examples-library.md` |


# SOURCE_FILE: CONTRIBUTING.md
---
# Как участвовать в проекте

## Лучший способ участия

**Разверните это хранилище для своего проекта** и попробуйте его в деле.

Инструкции по развёртыванию описаны в [README.md](README.md) — шаги 1-7.

По итогам работы с хранилищем напишите ваши замечания и предложения:

**Церен Церенов**
- Telegram: [@tserentserenov](https://t.me/tserentserenov)

---

## Стандартный способ

Вы также можете отправить свои поправки в этот репозиторий стандартным способом:

1. Fork репозитория
2. Внесите изменения
3. Создайте Pull Request

---

## Лицензия

MIT License — используйте свободно.


# SOURCE_FILE: REPO-TYPE.md
---
# Тип репозитория

**Тип**: `Base/Форматы`

**Source-of-truth**: yes (для формата оформления downstream-репозиториев)

## Что это

**S2R (Structured Second-level Repository)** — спецификация формата/протокола оформления downstream-репозиториев, особенно управленческих (governance).

## Upstream dependencies

- [TserenTserenov/SPF](https://github.com/TserenTserenov/SPF) — принципы организации знаний
- [ailev/FPF](https://github.com/ailev/FPF) — базовые различения

## Downstream outputs

- [aisystant/ecosystem-development](https://github.com/aisystant/ecosystem-development) — инстанс s2r
- Другие governance-репозитории

## Non-goals

- НЕ является pack'ом (не описывает предметную область)
- НЕ является конкретной реализацией (это формат)
- НЕ содержит кода
- НЕ определяет «что истинно в области» — только «как оформлять downstream»

## Что содержит

- Структура ядер (A/B/C/D...)
- Матрица 3×3 (система × роль)
- Семейства документов (F1-F9)
- Правила именования и навигации
- Обязательные документы
- Правила трассировки на pack
- Правила статусов/решений

---

*Последнее обновление: 2026-02-06*
