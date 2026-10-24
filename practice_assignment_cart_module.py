"""
Модуль расчета и оформления корзины интернет-магазина.
ВНИМАНИЕ: Данный файл содержит учебный "грязный код" с запахами кода (Code Smells).
Задача студента: провести рефакторинг с сохранением внешнего API и успешным прохождением тестов.
"""

# ГРЯЗНЫЙ КОД (Исходная версия):
def calc_ord(user, card_items, promo_code, vip=False):
    # u: dict пользователя {'age': int, 'reg_days': int, 'is_blocked': bool}
    # c: list товаров [{'id': str, 'name': str, 'price': float, 'qty': int, 'cat': str}]
    # d_code: str промокод ('SALE10', 'SPRING5', etc.)
    # vip: bool флаг VIP-статуса
    
    if user is not None:
        if not user.get('is_blocked', False):
            if user.get('age', 0) >= 18:
                if len(card_items) > 0:
                    subtotal = 0
                    has_promo_item = False
                    
                    # подсчет базы
                    for i in range(len(c)):
                        item = c[i]
                        if item['price'] > 0 and item['qty'] > 0:
                            subtotal = subtotal + (item['price'] * item['qty'])
                            if item.get('cat') == 'promo':
                                has_promo_item = True
                        else:
                            return None  # невалидные позиции
                    
                    # применение скидок
                    discount = 0
                    if promo_code == "SALE10":
                        if not has_promo_item:
                            discount = discount + (subtotal * 0.10)
                    elif promo_code == "SPRING5":
                        if not has_promo_item:
                            discount = discount + (subtotal * 0.05)
                    
                    if vip:
                        discount = discount + (subtotal * 0.07)
                    
                    if user.get('reg_days', 0) > 365:
                        discount = discount + 100.0  # бонус лояльности
                    
                    # проверка чтобы скидка не превысила сумму
                    if discount > subtotal:
                        discount = subtotal
                    
                    sub = subtotal - discount
                    
                    # налог НДС 20%
                    tax = sub * 0.20
                    total = sub + tax
                    
                    return {
                        'subtotal': round(subtotal, 2),
                        'discount': round(disc, 2),
                        'tax': round(tax, 2),
                        'total': round(total, 2)
                    }
                else:
                    return None
            else:
                return None
        else:
            return None
    else:
        return None
