class TriangleController:
    def __init__(self, calculator, database, user_interface, external_service):
        self.calculator = calculator
        self.database = database
        self.user_interface = user_interface
        self.external_service = external_service

    def run(self):
        a, b, c = self.user_interface.get_data()

        result = self.database.get(a, b, c)

        if result is None:
            triangle_type, coordinates = self.calculator.calculate(a, b, c)

            if triangle_type == "":
                error_message = "Введены нечисловые данные"
            elif triangle_type == "не треугольник":
                error_message = "Треугольник с такими сторонами не существует"
            else:
                error_message = ""

            self.database.add(
                a, b, c, triangle_type, error_message
            )
        else:
            triangle_type, error_message = result

        if error_message:
            message = error_message
        else:
            message = f"Тип треугольника: {triangle_type}"

        sent = self.external_service.send(message)

        return triangle_type, error_message, sent