## ЗАДАНИЕ MIDLE Python

#16. **Реализация мини-фреймворка:**
# - Напишите небольшой веб-сервер на основе библиотеки `http.server`, который обрабатывает запросы GET и POST, 
# а также возвращает динамически сгенерированный HTML.

import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

# Обработчик запросов
class MyHandler(BaseHTTPRequestHandler):

    # Обработка GET-запроса
    def do_GET(self):
        # Устанавливаем код ответа (200 OK)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        
        # Отправляем простой HTML с формой для POST-запроса
        self.wfile.write("<html><body>".encode('utf-8'))
        self.wfile.write("<h1>Погода</h1>".encode('utf-8'))
        self.wfile.write("<form id='weatherForm'>".encode('utf-8'))
        self.wfile.write("Введите город: <input type='text' name='city' id='city'><br>".encode('utf-8'))
        self.wfile.write("Введите ед-цу измерения (m или i): <input type='text' name='units' id='units'><br>".encode('utf-8'))
        self.wfile.write("Введите язык: <input type='text' name='lang' id='lang'><br>".encode('utf-8'))
        self.wfile.write("Введите кол-во дней: <input type='text' name='count_day' id='count_day'><br>".encode('utf-8'))
        self.wfile.write("<input type='submit' value='Отправить'>".encode('utf-8'))
        self.wfile.write("</form><br>".encode('utf-8'))

        # Место для отображения результата
        self.wfile.write("<div id='response'></div>".encode('utf-8'))

        # Добавим JavaScript для асинхронного отправления данных и отображения ответа
        self.wfile.write("""
        <script>
        document.getElementById('weatherForm').addEventListener('submit', function(event) {
            event.preventDefault();  // Предотвращаем обычную отправку формы

            // Сбор данных с формы
            const formData = new FormData(document.getElementById('weatherForm'));
            const data = new URLSearchParams(formData);

            // Создаем запрос
            fetch('/submit', {
                method: 'POST',
                body: data
            })
            .then(response => response.text())  // Получаем текстовый ответ
            .then(responseData => {
                // Отображаем результат в div с id='response'
                document.getElementById('response').innerHTML = '<pre>' + responseData + '</pre>';
            })
            .catch(error => {
                document.getElementById('response').innerHTML = 'Произошла ошибка: ' + error;
            });
        });
        </script>
        </body></html>
        """.encode('utf-8'))

    # Вызов функции для получения данных погоды
    def api_call_weather(self, city, units, lang, count_day):
        script_path = "./bash_api_call_weather/main_wether.sh"
        result = subprocess.run(['bash', script_path, city, units, lang, count_day], capture_output=True, text=True)
        return result.stdout

    # Обработка POST-запроса
    def do_POST(self):
        # Получаем размер данных
        content_length = int(self.headers['Content-Length'])
        
        # Получаем данные запроса
        post_data = self.rfile.read(content_length)
        
        # Преобразуем байты в строку
        data = parse_qs(post_data.decode('utf-8'))
        
        # Получаем значение из данных формы
        user_city = data.get('city', [''])[0]
        user_units = data.get('units', [''])[0]
        user_lang = data.get('lang', [''])[0]
        user_count_day = data.get('count_day', [''])[0]
        
        # Вызываем функцию для получения данных погоды
        result = self.api_call_weather(user_city, user_units, user_lang, user_count_day)
        
        # Формируем текстовый ответ
        response = f'Вы отправили:\n\n'
        response += f'Город: {user_city}\n'
        response += f'Единица измерения: {user_units}\n'
        response += f'Язык: {user_lang}\n'
        response += f'Количество дней: {user_count_day}\n\n'
        response += f'Результат погоды:\n{result}'

        # Отправляем текстовый ответ
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))

# Настроим сервер
def run(server_class=HTTPServer, handler_class=MyHandler, port=8080):
    server_address = ('', port)  # Сервер будет слушать на порту 8080
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()

if __name__ == '__main__':
    run()
