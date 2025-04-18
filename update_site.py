import os

# Папка с проектом
project_dir = "C:/my-website/my_proj"

# Файл стилей
styles_css = """/* Современный стиль Сбера + анимация */
body {
    margin: 0;
    font-family: 'Inter', sans-serif;
    background-color: #f4f8f7;
    color: #1c1c1e;
}

.hero {
    position: relative;
    background: linear-gradient(135deg, #21a038 0%, #bfffae 100%);
    color: white;
    text-align: center;
    padding: 80px 20px;
    overflow: hidden;
}

.background-animation::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle at center, rgba(255,255,255,0.1) 0%, transparent 70%);
    animation: rotate 20s linear infinite;
    z-index: 0;
}

@keyframes rotate {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}

.container {
    position: relative;
    z-index: 1;
    max-width: 900px;
    margin: 0 auto;
}

.cat-image {
    width: 120px;
    border-radius: 20px;
    box-shadow: 0 0 20px rgba(255, 255, 255, 0.4);
    animation: float 4s ease-in-out infinite;
    margin-bottom: 20px;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-10px); }
}

h1 {
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 10px;
}

p {
    font-size: 18px;
    font-weight: 400;
}

.btn {
    display: inline-block;
    margin-top: 20px;
    padding: 12px 28px;
    background-color: #ffffff;
    color: #21a038;
    font-weight: 600;
    text-decoration: none;
    border-radius: 8px;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.btn:hover {
    background-color: #e2fbe6;
    transform: scale(1.05);
}

.info-section {
    background-color: #ffffff;
    padding: 60px 20px;
    text-align: center;
}

footer {
    background-color: #1c1c1e;
    color: white;
    padding: 20px 0;
    text-align: center;
    font-size: 14px;
}
"""

# Обновим файл styles.css
with open(os.path.join(project_dir, "styles.css"), "w", encoding="utf-8") as f:
    f.write(styles_css)

# Пример HTML-файла (index.html)
index_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Добро пожаловать</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header class="hero background-animation">
        <div class="container">
            <img src="https://i.ibb.co/wzYqPY2/cat-sber.gif" class="cat-image" alt="Анимированный котик">
            <h1>Добро пожаловать на инновационный сайт</h1>
            <p>Здесь технологии встречаются с удобством.</p>
            <a href="quiz.html" class="btn">Пройти опросник</a>
        </div>
    </header>

    <section class="info-section">
        <div class="container">
            <h2>О проекте</h2>
            <p>Это сайт, оформленный в стиле Сбера, с современными визуальными эффектами, анимацией и ярким дизайном.</p>
        </div>
    </section>

    <footer>
        <p>&copy; 2025 Инновационный Сайт. Все права защищены.</p>
    </footer>
</body>
</html>
"""

with open(os.path.join(project_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_html)

print("✅ Файлы успешно обновлены!")

