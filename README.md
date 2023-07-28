## Проект автотестов  UI + API 

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Requests" src="images/logo/requests.png"></code>
  <code><img width="5%" title="Docker" src="images/logo/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="images/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>


<!-- Тест кейсы -->

## Покрытый функционал

1. [DemoWebShop](https://demowebshop.tricentis.com/) - UI
    - Регистрация пользователя
    - Авторизация пользователя
    - Поиск товара
    - Удаление товара из корзины
    - Добавление товара в корзину
2. [reqres](https://reqres.in/) - API
   - Регистрация пользователя 
   - Регистрация пользователя с невалидными данными
   - Авторизация пользователя
   - Авторизация пользователя с невалидными данными
   - Обновление данных пользователя
   - Обновление данных пользователя частично
   - Создание пользователя
   - Удаление пользователя
   - Получение списка пользователей с задержкой

## Запуск тестов

### [Запуск проекта в Jenkins](https://jenkins.autotests.cloud/job/qa_gugru_maxaten_graduate_work_web_and_api/)

Для запуска тестов выбрать "Собрать с параметрами"

![Jenkins](/images/screenshot/jenkins_1.png)

Выбрать набор тестов и нажать "Собрать"

![Jenkins](/images/screenshot/jenkins_3.png)

Отчет о прохождении тестов отправляется в телеграм, со ссылкой на Allure отчет.

![Telegram](/images/screenshot/telegramm_report.png)

### __Примеры Allure отчётов:__ 

### [Allure Report](https://jenkins.autotests.cloud/job/qa_gugru_maxaten_graduate_work_web_and_api/17/allure/)

UI и API тесты

![Allure Diagram](/images/screenshot/allure_report_diagramm.png)

![Allure UI and Api](/images/screenshot/allure_report_tests.png)

Пример видео прохождения теста

![Allure vid](/images/screenshot/test_video.mp4)

### __Интеграции с другими сервисами:__ 
[Allure TestOps](https://allure.autotests.cloud/launch/27918/tree?search=W3siaWQiOiJzdGF0dXMiLCJ0eXBlIjoidGVzdFN0YXR1c0FycmF5IiwidmFsdWUiOlsicGFzc2VkIl19XQ%3D%3D&treeId=6973)

![Allure TestOps](/images/screenshot/allure_testops_report.png)

[Jira](https://jira.autotests.cloud/browse/HOMEWORK-825)

![Allure TestOps](/images/screenshot/jire_report.png)
