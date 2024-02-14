from flask import Flask
from flask import url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def bage():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '''
Человечество вырастает из детства.</br>
Человечеству мала одна планета.</br>
Мы сделаем обитаемыми безжизненные пока планеты.</br>
И начнем с Марса!</br>
Присоединяйся!</br>
'''


@app.route('/promotion_image')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" background-color: brown>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  </body>
                    <img src="{url_for('static', filename='img/mars.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1><center>Анкета претендента</center></h1>
                           <body>
                            <h3><center>на участие в миссии</center></h3>
                            <div>
                             </br>
                                <form class="login_form" method="post">
                                    <input type="name" class="form-control" id="name" aria-describedby="emailHelp" placeholder="Введите фамилию" name="name">
                                    <input type="family" class="form-control" id="family" placeholder="Введите имя" name="family">
                                    </br>
                                    <input type="email" class="form-control" id="email" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образоване?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Начальное</option>
                                          <option>Основное</option>
                                          <option>Среднее</option>
                                          <option>Среднее профессиональное</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                        <label for="checkbox">Какие у вас есть профессии?</label></br>
                                            <label class="form-check-label" for="p">
                                            <input class="form-check-label" type="checkbox" name="sex" id="p" value="p">
                                          инженер-исследователь

                                          <label class="form-check-label" for="z">
                                            <input class="form-check-input" type="checkbox" name="sex" id="z" value="z">
                                          пилот

                                          <label class="form-check-label" for="k">
                                            <input class="form-check-input" type="checkbox" name="sex" id="k" value="k">
                                          строитель

                                          <label class="form-check-label" for="y">
                                            <input class="form-check-input" type="checkbox" name="sex" id="y" value="y">
                                         экзобиолог 

                                          <label class="form-check-label" for="r">
                                            <input class="form-check-input" type="checkbox" name="sex" id="r" value="r">
                                         врач

                                          <label class="form-check-label" for="e">
                                            <input class="form-check-input" type="checkbox" name="sex" id="e" value="e">
                                          инженер по терраформированию

                                          <label class="form-check-label" for="f">
                                            <input class="form-check-input" type="checkbox" name="sex" id="f" value="f">
                                          климатолог

                                          <label class="form-check-label" for="w">
                                         <input class="form-check-input" type="checkbox" name="sex" id="w" value="w">
                                            специалист по радиационной защите
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male">
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    <div class="form-group">
                                        <label for="about">Почему вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    </br>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
