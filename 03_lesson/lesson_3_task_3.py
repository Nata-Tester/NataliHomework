from address import Address
from mailing import Mailing

to_addr = Address('123456', 'Москва', 'Кирова', '1', '2')
from_addr = Address('654321', 'Санкт-Петербург', 'Ленина', '3', '4')

mail = Mailing(to_addr, from_addr, "150", "155-155-155")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.city}, "
      f"{mail.from_address.str}, {mail.from_address.building} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, {mail.to_address.str}, "
      f"{mail.to_address.building} - {mail.to_address.apartment}. "
      f"Стоимость {mail.cost} рублей.")
