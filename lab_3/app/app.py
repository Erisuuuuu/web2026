import random
from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_login import UserMixin, login_user, logout_user, LoginManager, current_user, login_required
from faker import Faker

fake = Faker()

app = Flask(__name__)
app.secret_key = 'Checkname'
application = app

images_ids = ['7d4e9175-95ea-4c5f-8be5-92a6b708bb3c',
              '2d2ab7df-cdbc-48a8-a936-35bba702def5',
              '6e12f3de-d5fd-4ebb-855b-8cbc485278b7',
              'afc2cfe7-5cac-4b80-9b9a-d5c65ef0c728',
              'cab5b7f2-774e-4884-a200-0c0180fa777f']

def generate_comments(replies=True):
    comments = []
    for i in range(random.randint(1, 3)):
        comment = { 'author': fake.name(), 'text': fake.text() }
        if replies:
            comment['replies'] = generate_comments(replies=False)
        comments.append(comment)
    return comments

def generate_post(i):
    return {
        'title': 'Заголовок поста',
        'text': fake.paragraph(nb_sentences=100),
        'author': fake.name(),
        'date': fake.date_time_between(start_date='-2y', end_date='now'),
        'image_id': f'{images_ids[i]}.jpg',
        'comments': generate_comments()
    }

posts_list = sorted([generate_post(i) for i in range(5)], key=lambda p: p['date'], reverse=True)

# Класс для пользователя
class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Для доступа к запрашиваемой странице необходимо пройти аутентификацию.'
login_manager.login_message_category = 'warning'

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

USERS = {'user': 'qwerty'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', title='Посты', posts=posts_list)

@app.route('/posts/<int:index>')
def post(index):
    p = posts_list[index]
    return render_template('post.html', title=p['title'], post=p)

@app.route('/about')
def about():
    return render_template('about.html', title='Об авторе')

@app.route('/request_info')
def request_info():
    cookies = list(request.cookies.items())
    url_params = list(request.args.items())
    headers = list(request.headers.items()) 
    return render_template('request_info.html', title='Информация о запросе', cookies=cookies, url_params=url_params, headers=headers)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_fields = []
    if request.method == 'POST':
        form_fields = list(request.form.items())    
        username = request.form.get('login')
        password = request.form.get('password')
        next_url = request.form.get('next') or request.args.get('next')
        if username in USERS and USERS[username] == password:
            user = User(username)
            remember = bool(request.form.get('remember'))
            login_user(user, remember=remember)
            flash('Вы успешно вошли в систему')

            return redirect(next_url or url_for('index'))
        else:
            flash('Неверный логин или пароль')
            return redirect(url_for('login', next=next_url))

    return render_template('login.html', title='Вход', form_fields=form_fields, next=request.args.get('next'))

ERR_PHONE_DIGITS = 'Недопустимый ввод. Неверное количество цифр.'
ERR_PHONE_CHARS = (
    'Недопустимый ввод. В номере телефона встречаются недопустимые символы.'
)

ALLOWED_PHONE_SYMBOLS = set('0123456789 ()-.+')


@app.route('/check_phone', methods=['GET', 'POST'])
def check_phone():
    if request.method == 'GET':
        return render_template(
            'check_phone.html',
            title='Проверка телефона',
            phone='',
            error=None,
            formatted=None,
        )

    raw = request.form.get('phone') or ''

    if any(ch not in ALLOWED_PHONE_SYMBOLS for ch in raw):
        return render_template(
            'check_phone.html',
            title='Проверка телефона',
            phone=raw,
            error=ERR_PHONE_CHARS,
            formatted=None,
        )

    digits = ''.join(ch for ch in raw if ch.isdigit())
    stripped = raw.strip()
    expected_digits = 11 if stripped.startswith('+7') or stripped.startswith('8') else 10

    if len(digits) != expected_digits:
        return render_template(
            'check_phone.html',
            title='Проверка телефона',
            phone=raw,
            error=ERR_PHONE_DIGITS,
            formatted=None,
        )

    if len(digits) == 10:
        norm = '8' + digits
    elif digits[0] == '7':
        norm = '8' + digits[1:]
    else:
        norm = digits

    formatted = (
        f'{norm[0]}-{norm[1:4]}-{norm[4:7]}-{norm[7:9]}-{norm[9:11]}'
    )
    return render_template(
        'check_phone.html',
        title='Проверка телефона',
        phone=raw,
        error=None,
        formatted=formatted,
    )

@app.route('/counter')
def counter():
    if 'visits' not in session:
        session['visits'] = 0
    session['visits'] += 1
    return render_template('counter.html', title='Счётчик посещений', visits=session['visits'])

@app.route('/secret_page')
@login_required
def secret_page():
    return render_template('secret_page.html', title='Секретная страница')
