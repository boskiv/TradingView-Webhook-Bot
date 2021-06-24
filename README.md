# Deploy to heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

# Инструкция

* Генерация ключа для бота https://core.telegram.org/bots#6-botfather

* Создать чат в телеграме и пригласить в него своего бота

* Найти идентификатор чата https://api.telegram.org/botXXX:YYY/getUpdates (где XXX:YYY это ключ бота полученный от botfather)

* Придумать секретный ключ (любой, чтобы использовать его при отправке алертов)

* Нажать кнопку Deply и заполнить поля данными

![Heroku Deploy](/assets/heroku_deploy.png)

# Отправка сигнала

В поле сообщения TradingView Alert нужно указать данный формат

```
{
 "key": "9T2q394M92",
 "telegram": "-1001277977502",
 "msg": "Long *#{{ticker}}* at `{{close}}`"
}
```

Доступные переменные которые можно использовать
https://www.tradingview.com/support/solutions/43000531021-how-to-use-a-variable-value-in-alert/