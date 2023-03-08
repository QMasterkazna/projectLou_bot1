# API_TOKEN = '5962999120:AAEO3YAT1hIBckQPRZjYoZtnJGETv_6Fq30'
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

logging.basicConfig(level=logging.INFO)

button_start_python = KeyboardButton('Python')
button_start_c = KeyboardButton('C')
button_start_cpp = KeyboardButton('C++')
button_start_js = KeyboardButton('Javascript')
start = ReplyKeyboardMarkup()
start.add(button_start_python).add(button_start_js).add(button_start_c).add(button_start_cpp)
start1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_start_python).add(
    button_start_js).add(button_start_c).add(button_start_cpp)

button_python_history = KeyboardButton('О Python')
python = ReplyKeyboardMarkup()
python.add(button_python_history)
python1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_python_history)

button_c_history = KeyboardButton('О C(Си)')
C = ReplyKeyboardMarkup()
C.add(button_c_history)
C1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_c_history)

button_javascript_history = KeyboardButton('О Javascript')
javascript = ReplyKeyboardMarkup()
javascript.add(button_javascript_history)
javascript1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_javascript_history)

button_cpp_history = KeyboardButton('О C++')
cpp = ReplyKeyboardMarkup()
cpp.add(button_cpp_history)
cpp1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_cpp_history)
python_history = (
        "Python был создан в конце 1980-х годов Гвидо ван Россумом, голландским программистом. Он начал разрабатывать язык программирования, когда работал в крупной компании по производству систем управления операционными системами. Python получил свое имя в честь популярного комедийного телешоу 'Monty Python's Flying Circus', любимого Гвидо ван Россума.\n" +
        "Python быстро стал популярным среди программистов благодаря своей простоте, лаконичности и универсальности. В начале 1990-х годов Гвидо ван Россум выпустил первую версию Python под открытой лицензией, что позволило другим разработчикам использовать язык и вносить свои вклады в его развитие.\n" +
        "В 2000-х годах Python получил еще большую популярность благодаря своей применяемости во многих областях, таких как веб-разработка, научные исследования, анализ данных, искусственный интеллект и многое другое. В настоящее время Python является одним из самых популярных языков программирования в мире.\n" +
        "Python имеет большое сообщество разработчиков, которые вносят свои вклады в его развитие и поддержку. Кроме того, Python является свободно распространяемым и доступным для использования на различных платформах и операционных системах." +
        "Язык программирования Python подойдет для новичка, вот пример кода:\n")
python_code = ("""def greet(name):
    print("Hello, " + name + "!")

# вызов функции greet() с аргументом "Alice"
greet("Alice")

# вызов функции greet() с аргументом "Bob"
greet("Bob")""")

C_History = ("""Язык программирования C был разработан в 1972 году в лаборатории Bell Labs в США. Его создателями являются Деннис Ритчи и Кен Томпсон. В начале своего развития C использовался в основном для разработки операционных систем Unix, которые были также созданы в Bell Labs.

C быстро стал популярным среди программистов благодаря своей эффективности и портируемости. В отличие от других языков программирования того времени, C позволял разрабатывать низкоуровневый код, который мог быть скомпилирован в машинный код для разных архитектур процессоров. Кроме того, C был достаточно простым для изучения и использования, что сделало его популярным среди начинающих программистов.

В 1980-х годах C стал стандартом де-факто для разработки операционных систем, системных приложений, компиляторов и других программных продуктов. Стандарт языка C был формализован в 1989 году в стандарте ANSI C, который включал основные конструкции языка и библиотеки функций. В 1990 году этот стандарт был утвержден ISO как международный стандарт.

В настоящее время C остается одним из самых популярных языков программирования в мире и широко используется для разработки программного обеспечения в различных областях, таких как системное программирование, встраиваемые системы, игровая индустрия, научные исследования и многое другое.\n вот пример кода на С:\n""")
C_Code = ("""#include <iostream>

class Person {
  private:
    std::string name;
    int age;
  
  public:
    Person(std::string name, int age) {
        this->name = name;
        this->age = age;
    }
  
    void greet() {
        std::cout << "Hello, my name is " << name << "." << std::endl;
    }
  
    void celebrate_birthday() {
        age++;
        std::cout << "It's my birthday! I am now " << age << " years old." << std::endl;
    }
};

int main() {
    Person person("Alice", 25);
    person.greet();
    person.celebrate_birthday();
    return 0;
}""")
CPP_History = ("""C++ был разработан в 1979 году Бьёрном Страуструпом в Bell Labs как расширение языка C. Имя C++ происходит от инкрементной операции в языке C, которая увеличивает значение на 1.

Первая версия C++ была выпущена в 1985 году. В следующем году была выпущена первая книга, посвященная языку C++, написанная самим Страуструпом.

Сначала C++ был скорее эволюционным, чем новым языком, который включал некоторые новые функции, такие как классы и наследование, но постепенно он стал все более и более мощным и современным языком.

C++ стал одним из самых популярных языков программирования в мире благодаря своей мощности и гибкости, а также своей способности быть использованным для разработки широкого спектра программного обеспечения - от системных приложений до игр и мобильных приложений.

На сегодняшний день C++ остается одним из наиболее популярных языков программирования и продолжает эволюционировать с выпуском новых стандартов, таких как C++11, C++14, C++17 и C++20. Вот пример кода на С++: \n""")
CPP_Code = ("""#include <iostream>
#include <string>

class Person {
    private:
        std::string name;
        int age;
    public:
        // Конструктор класса
        Person(std::string name, int age) {
            this->name = name;
            this->age = age;
        }
        // Методы для получения и установки имени
        std::string getName() {
            return name;
        }
        void setName(std::string name) {
            this->name = name;
        }
        // Методы для получения и установки возраста
        int getAge() {
            return age;
        }
        void setAge(int age) {
            this->age = age;
        }
};

int main() {
    // Создаем объект класса Person и устанавливаем имя и возраст
    Person person("John", 25);
    
    // Получаем и выводим имя и возраст на экран
    std::cout << "Name: " << person.getName() << std::endl;
    std::cout << "Age: " << person.getAge() << std::endl;
    
    // Устанавливаем новое имя и возраст для объекта person
    person.setName("Jane");
    person.setAge(30);
    
    // Получаем и выводим новое имя и возраст на экран
    std::cout << "New Name: " << person.getName() << std::endl;
    std::cout << "New Age: " << person.getAge() << std::endl;
    
    return 0;
}""")
Javascript_History = (
            "JavaScript был создан Бренданом Айком (Brendan Eich) в 1995 году, когда он работал в компании Netscape. Вначале язык назывался Mocha, затем переименовали в LiveScript, а затем в JavaScript. Название JavaScript было выбрано для связи с языком программирования Java, который был очень популярен в то время. Однако JavaScript не имеет ничего общего с Java, за исключением синтаксиса, который был вдохновлен Java.\n" +
            "JavaScript был создан как язык программирования для веб-страниц. Он позволяет создавать динамические и интерактивные веб-страницы, которые могут реагировать на действия пользователя, такие как щелчки мыши, нажатия клавиш и т.д. JavaScript быстро стал очень популярным среди веб-разработчиков и постепенно расширял свои возможности. В настоящее время JavaScript используется не только для веб-разработки, но и для создания настольных приложений, мобильных приложений, игр и т.д.\n" +
            "Сегодня JavaScript является одним из самых популярных языков программирования в мире. Он постоянно развивается и улучшается, появляются новые фреймворки и библиотеки, которые облегчают разработку веб-приложений. Вот пример кода:\n")

Javascript_Code = ("""// определение объекта
let person = {
  firstName: "John",
  lastName: "Doe",
  age: 30,
  
  // метод для вывода полного имени
  fullName: function() {
    return this.firstName + " " + this.lastName;
  },
  
  // метод для увеличения возраста на 1
  increaseAge: function() {
    this.age++;
  }
};

// вызов методов объекта
console.log("Full name: " + person.fullName());
console.log("Age before: " + person.age);
person.increaseAge();
console.log("Age after: " + person.age);""")
# Инициализируем бота и диспетчер
bot = Bot(token="5962999120:AAEO3YAT1hIBckQPRZjYoZtnJGETv_6Fq30")
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Привет, Я бот , который поможет вам с определением первого языка программирования. \n "
                         "Выберите любой язык, а я постараюсь вам помочь определится подходит ли он вам или нет.",
                         reply_markup=start1)


@dp.message_handler()
async def language(msg: types.Message):
    if msg.text == "Python":
        text = "Python — высокоуровневый язык программирования общего назначения."
        await msg.answer(text, reply_markup=python1)
    if msg.text == "Javascript":
        text = "JavaScript — динамический язык программирования, применяемый в браузерах для создания интерактивных веб-страниц и пользовательских интерфейсов."
        await msg.answer(text, reply_markup=javascript1)
    if msg.text == "C++":
        text = "C++ — компилируемый язык программирования общего назначения."
        await msg.answer(text, reply_markup=cpp1)
    if msg.text == "C":
        text = "C — компилируемый язык программирования, используемый для системного программирования и написания приложений, работающих в режиме реального времени."
        await msg.answer(text, reply_markup=C1)
    if msg.text == "О Python":
        text = python_history
        await msg.answer(text + python_code, reply_markup=start1)
    if msg.text == "О C(Си)":
        text = C_History
        await msg.answer(text + C_Code, reply_markup=start1)
    if msg.text == "О C++":
        text = CPP_History
        await msg.answer(text + CPP_Code, reply_markup=start1)
    if msg.text == "О Javascript":
        text = Javascript_History
        await msg.answer(text + Javascript_Code, reply_markup=start1)


# Запускаем бота
if __name__ == '__main__':
    executor.start_polling(dp)

