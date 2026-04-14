# 💳 Debt Solver — Оптимизация погашения задолженности по кредитным картам

![Python](https://img.shields.io/badge/Python-3.12-light?logo=python)
![Django](https://img.shields.io/badge/Django-5.0-gold?logo=django)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-magenta?logo=bootstrap)

## 📝 О проекте

Веб-сервис для физических лиц с 2–5 кредитными картами. Помогает рассчитать **реальную переплату** и построить **оптимальный график платежей**, чтобы погасить долги быстрее и с меньшими процентами.

### 🎯 Основные возможности
- Добавление до 5 кредитных карт с разными ставками и лимитами
- Расчёт минимальных платежей и процентов
- Построение графика погашения по месяцам
- Визуализация снижения долга (интерактивные графики Plotly)
- Расчёт общей переплаты за весь период

## 🛠 Технологии

| Технология | Назначение |
|------------|------------|
| Django 5.0 | Веб-фреймворк |
| SQLite | База данных (разработка) |
| Bootstrap 5 | Адаптивный интерфейс |
| Plotly | Графики и визуализация |
| Django ORM | Работа с моделями |

## 🚀 Быстрый старт

### Требования
- Python 3.10+
- Git

### Установка и запуск

```bash
# 1. Клонировать репозиторий
git clone https://github.com/ВАШ_НИК/Debt_Solver.git
cd Debt_Solver

# 2. Создать виртуальное окружение
python -m venv .venv

# 3. Активировать окружение (Windows)
.venv\Scripts\activate

# 4. Установить зависимости
pip install -r requirements.txt

# 5. Выполнить миграции
python manage.py migrate

# 6. Запустить сервер
python manage.py runserver