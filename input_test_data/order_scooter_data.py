from dataclasses import dataclass


@dataclass
class OrderData:
    name: str
    surname: str
    address: str
    subway: str
    phone: str
    delivery_date: str
    rent_period: str
    colors: list[str]
    comment: str = ""


ORDER_DATA = [
    OrderData(
        name = "Иван",
        surname = "Иванов",
        address = "Москва, Ленина 1",
        subway = "Раменки",
        phone = "79991234567",
        delivery_date = "01.03.2026",
        rent_period = "двое суток",
        colors = ["black", "grey"],
        comment = "Позвонить заранее",
    ),
    OrderData(
        name = "Петр",
        surname = "Петров",
        address = "Москва, Кутузовский 10",
        subway = "Киевская",
        phone = "79997654321",
        delivery_date = "05.03.2026",
        rent_period = "сутки",
        colors=["black"],
    ),
]
