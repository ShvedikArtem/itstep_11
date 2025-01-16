import random
import logging

logging.basicConfig(
    filename="simulation.log", 
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        logging.info(f"{self.name} створений з початковими параметрами")

    def get_home(self):
        self.home = House()
        logging.info(f"{self.name} оселився в будинку")

    def get_car(self):
        self.car = Auto(brands_of_car)
        logging.info(f"{self.name} купив машину {self.car.brand}")

    def get_job(self):
        if self.car.drive():
            self.job = Job(job_list)
            logging.info(f"{self.name} отримав роботу {self.job.job} з зарплатою {self.job.salary}")
        else:
            self.to_repair()

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
            logging.info(f"{self.name} поїв. Ситість: {self.satiety}")

    def work(self):
        if self.car.drive():
            self.money += self.job.salary
            self.gladness -= self.job.gladness_less
            self.satiety -= 4
            logging.info(f"{self.name} працював. Гроші: {self.money}, Щастя: {self.gladness}, Ситість: {self.satiety}")
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
            else:
                self.to_repair()

    def shopping(self, manage):
        if self.car.drive():
            if manage == "fuel":
                self.money -= 100
                self.car.fuel += 100
                logging.info(f"{self.name} купив паливо. Залишок грошей: {self.money}, Паливо: {self.car.fuel}")
            elif manage == "food":
                self.money -= 50
                self.home.food += 50
                logging.info(f"{self.name} купив їжу. Залишок грошей: {self.money}, Їжа: {self.home.food}")
            elif manage == "delicacies":
                self.money -= 15
                self.gladness += 10
                self.satiety += 2
                logging.info(f"{self.name} купив делікатеси. Щастя: {self.gladness}, Ситість: {self.satiety}, Гроші: {self.money}")
        else:
            self.to_repair()

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        logging.info(f"{self.name} відпочивав. Щастя: {self.gladness}, Безлад у домі: {self.home.mess}")

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        logging.info(f"{self.name} прибрав дім. Щастя: {self.gladness}")

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
        logging.info(f"{self.name} відремонтував машину {self.car.brand}. Залишок грошей: {self.money}, Стан машини: {self.car.strength}")

    def days_indexes(self, day):
        logging.info(f"День {day} у житті {self.name}. Гроші: {self.money}, Щастя: {self.gladness}, Ситість: {self.satiety}")

    def is_alive(self):
        if self.gladness < 0:
            logging.warning(f"{self.name} впав у депресію")
            return False
        if self.satiety < 0:
            logging.warning(f"{self.name} помер від голоду")
            return False
        if self.money < -500:
            logging.warning(f"{self.name} збанкрутував")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()
        self.days_indexes(day)

        dice = random.randint(1, 4)
        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()
        elif dice == 1:
            self.chill()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.clean_home()
        elif dice == 4:
            self.shopping(manage="delicacies")

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            logging.warning(f"Машина {self.brand} не може рухатися")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1},
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14},
}

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]

nick = Human(name="Nick")
for day in range(1, 8):
    if not nick.live(day):
        break
