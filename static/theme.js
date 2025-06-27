// Управление темами галереи изображений

document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('theme-toggle');
    const html = document.documentElement;
    
    // Получаем сохранённую тему или используем светлую по умолчанию
    const savedTheme = localStorage.getItem('gallery-theme') || 'light';
    
    // Применяем сохранённую тему
    if (savedTheme === 'dark') {
        html.setAttribute('data-theme', 'dark');
        updateToggleIcon('dark');
    } else {
        html.removeAttribute('data-theme');
        updateToggleIcon('light');
    }
    
    // Обработчик клика по переключателю темы
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const currentTheme = html.getAttribute('data-theme');
            
            if (currentTheme === 'dark') {
                // Переключаемся на светлую тему
                html.removeAttribute('data-theme');
                localStorage.setItem('gallery-theme', 'light');
                updateToggleIcon('light');
            } else {
                // Переключаемся на тёмную тему
                html.setAttribute('data-theme', 'dark');
                localStorage.setItem('gallery-theme', 'dark');
                updateToggleIcon('dark');
            }
        });
    }
    
    // Функция для обновления иконки переключателя
    function updateToggleIcon(theme) {
        if (theme === 'dark') {
            themeToggle.innerHTML = '☀️'; // Солнце для переключения на светлую тему
            themeToggle.title = 'Переключить на светлую тему';
        } else {
            themeToggle.innerHTML = '🌙'; // Луна для переключения на тёмную тему
            themeToggle.title = 'Переключить на тёмную тему';
        }
    }
    
    // Плавная анимация при переключении темы
    html.style.transition = 'background-color 0.3s ease, color 0.3s ease';
}); 