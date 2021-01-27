class Worker:
  def __init__(self, name, surname, position, income):
      self.name=name
      self.surname=surname
      self.position=position
      wage = int(input("Введите оклад сотрудника"))
      bonus = int(input("Введите бонус сотрудника"))
      income_dict = {"wage": wage, "bonus": bonus}
      self._income=income_dict


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)
    def get_full_name(self, name, surname):
        print(name, surname)
    def get_total_income(self, wage, bonus):
        total_income=wage+bonus
        print(total_income)

new_worker=Position('Иван', 'Иванов', 'директор', 'lkjlkj')
new_worker.get_full_name()