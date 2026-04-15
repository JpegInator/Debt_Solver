from django.db import models


class CreditCard(models.Model):

    """Модель кредитной карты"""

    name = models.CharField(max_length=100, verbose_name="Название карты")
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Кредитный лимит")
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Годовая ставка (%)")
    current_debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Текущая задолженность")
    min_payment_percent = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Мин. платёж (% от долга)")

    def __str__(self):
        return f"{self.name} (долг: {self.current_debt})"

    class Meta:
        verbose_name = "Кредитная карта"
        verbose_name_plural = "Кредитные карты"


class PaymentSchedule(models.Model):

    """График платежей по карте"""

    card = models.ForeignKey(CreditCard, on_delete=models.CASCADE, related_name="payments", verbose_name="Карта")
    month = models.IntegerField(verbose_name="Номер месяца")
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма платежа")
    interest_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Проценты за месяц")
    remaining_debt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Остаток долга")

    def __str__(self):
        return f"{self.card.name} - месяц {self.month}"

    class Meta:
        verbose_name = "График платежа"
        verbose_name_plural = "Графики платежей"
        ordering = ['card', 'month']


class CalculationHistory(models.Model):

    """История расчётов"""

    session_id = models.CharField(max_length=100, blank=True, verbose_name="ID сессии")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата расчёта")
    cards_snapshot = models.JSONField(verbose_name="Снимок данных карт")
    total_overpayment = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Общая переплата")
    payoff_months = models.IntegerField(default=0, verbose_name="Месяцев до погашения")
    recommended_strategy = models.TextField(blank=True, verbose_name="Рекомендуемая стратегия")

    def __str__(self):
        return f"Расчёт от {self.created_at}"

    class Meta:
        verbose_name = "История расчёта"
        verbose_name_plural = "История расчётов"
        ordering = ['-created_at']