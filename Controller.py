import web
from Models import RegisterModel

urls = (
    '/', 'Home',
    '/register', 'Register',
    '/postregistration', 'PostRegistration'
)


render = web.template.render("Views/Templates", base="MainLayout")
app = web.application(urls, globals())

# classes/routes


class Home:
    def GET(self):
        return render.Home()


class Register:
    def GET(self):
        return render.Register()


class PostRegistration:
    def POST(self):
        data = web.input()

        reg_model = RegisterModel.RegisterModel()
        reg_model.insert_user(data)

        return data.username


if __name__ == "__main__":
    app.run()
