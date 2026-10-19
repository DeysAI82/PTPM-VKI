from Delivery import calculate_delivery_cost


class Controller:
    def __init__(self, database, user_interface, external_service):
        self.database = database
        self.user_interface = user_interface
        self.external_service = external_service

    def run(self):
        weight, distance, package_type, is_express = self.user_interface.get_data()

        result = self.database.get(weight, distance, package_type, is_express)

        if result is None:
            cost, delivery_date = calculate_delivery_cost(
                weight, distance, package_type, is_express
            )

            self.database.add(
                weight, distance, package_type, is_express,
                cost, delivery_date
            )
        else:
            cost, delivery_date = result

        if cost == -1:
            message = "Некорректные параметры доставки"
        else:
            message = f"Стоимость доставки: {cost} руб. Дата доставки: {delivery_date}"

        sent = self.external_service.send(message)

        return cost, delivery_date, sent
