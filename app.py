from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Получаем данные от пользователя
        email = request.form.get("email")
        review = request.form.get("review")  # Отзыв
        user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

        # Сохраняем отзыв в файл
        try:
            with open("feedback.txt", "a", encoding="utf-8") as file:
                file.write(f"Email: {email}\n")
                file.write(f"Отзыв: {review}\n")
                file.write(f"IP: {user_ip}\n\n")

            print("Отзыв успешно записан в файл.")
        except Exception as e:
            print(f"Ошибка при записи в файл: {e}")

        # Перенаправление после обработки запроса POST
        return redirect(url_for('index'))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
