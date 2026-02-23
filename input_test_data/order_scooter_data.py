from dataclasses import dataclass
from enum import Enum, auto


class OrderStartButton(Enum):
    NAVIGATION_BUTTON = auto()
    ROADMAP_FINISH_BUTTON = auto()


@dataclass
class OrderData:
    start_button: OrderStartButton
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
        start_button=OrderStartButton.NAVIGATION_BUTTON,
        name="Иван",
        surname="Иванов",
        address="Москва, Ленина 1",
        subway="Раменки",
        phone="79991234567",
        delivery_date="01.03.2026",
        rent_period="двое суток",
        colors=["black", "grey"],
        comment="Позвонить заранее",
    ),
    OrderData(
        start_button=OrderStartButton.ROADMAP_FINISH_BUTTON,
        name="Петр",
        surname="Петров",
        address="Москва, Кутузовский 10",
        subway="Киевская",
        phone="79997654321",
        delivery_date="05.03.2026",
        rent_period="сутки",
        colors=["black"],
    ),
]
