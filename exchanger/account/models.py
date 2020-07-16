from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    wallet = models.ForeignKey('Wallet', on_delete=models.CASCADE)
    list_of_transaction = []


class Wallet(models.Model):  # Кошелек со всеми видами валют и их количеством у юзера
    rubles = models.FloatField()
    dollars = models.FloatField()
    euros = models.FloatField()


class Transaction(models.Model):
    date = models.DateField(auto_now_add=True)
    type = models.ForeignKey('TypeTransaction', on_delete=models.CASCADE)  # тип транзакции
    first_currency_on_action = models.ForeignKey('Currency', on_delete=models.CASCADE)  # валюта над которой дейтвие
    amount_first_currency = models.FloatField()  # количество валюты над которой действие типа транзакци
    second_currency_for_action = models.ForeignKey('Currency', on_delete=models.CASCADE)  # валюта за которую действие
    amount_second_currency = models.FloatField()  # количество валюты за которую действие типа транзакции


class TypeTransaction(models.Model):  # типы транзакци ( покупка, продажа)
    name = models.CharField(max_length=7)


class Currency(models.Model):  # названия валют ( рубли, доллары и т.д.)
    name = models.CharField(max_length=10)
