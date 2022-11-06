import json
from datetime import datetime, date
import uuid

ADVANCE_PRICE = 0.6
STUDENT_PRICE = 0.5
LATE_PRICE = 1.1


class Ticket:
    def __init__(self, price):
        self._price = price
        self._id = uuid.uuid4()

    @property
    def get_price(self):
        return self._price

    @property
    def get_info(self):
        return self._price, self._id

    def __str__(self):
        return f"Price is: {self._price}$\nTicket id is: {self._id}\n"

class AdvanceTicket(Ticket):
    def __init__(self, price):
        super().__init__(price)
        self._price = round(self._price * ADVANCE_PRICE)

class StudentTicket(Ticket):
    def __init__(self, price):
        super().__init__(price)
        self._price = round(self._price * STUDENT_PRICE)

class LateTicket(Ticket):
    def __init__(self, price):
        super().__init__(price)
        self._price = round(self._price / LATE_PRICE)

class TicketManage:
    def __init__(self):
        self._event_chosen = ""
        self._ticket = ""

    def sel_event(self):
        with open("Events.json") as file:
            events_data = json.load(file)
        choice = input("Enter event name: ")
        if not any(x["name"] == choice for x in events_data["Events"]):
            raise ValueError("Invalid input")
        for i in events_data["Events"]:
            if choice == i["name"]:
                if i["amount"] <= 0:
                    raise ValueError("Tickets sold")
                i["amount"] -= 1
                json.dump(events_data, open("Events.json", "w"), indent=4)
                self._event_chosen = i.copy()

    @staticmethod
    def gett_diff(event_date):
        data = datetime.now()
        current_date = (data.year, data.month, data.day)
        event_date = tuple(int(i) for i in reversed(event_date.split(".")))
        if current_date > event_date:
            raise TimeoutError("Event ended")
        return (date(data.year, data.month, data.day) - date(event_date[0], event_date[1], event_date[2])).days

    def make_order(self):
        ticket_type = input("\nSelect ticket type: standart, student, advanced, late\n Enter: ")
        days_difference = abs(TicketManage.gett_diff(self._event_chosen["date"]))

        if not (ticket_type in ("standart", "student", "advanced", "late")):
            TicketManage.make_order(self)
        elif ticket_type == "standart":
            self._ticket = Ticket(self._event_chosen["price"])
        elif ticket_type == "student":
            self._ticket = StudentTicket(self._event_chosen["price"])
        if ticket_type == "advanced":
            if days_difference >= 60:
                self._ticket = AdvanceTicket(int(self._event_chosen["price"]))
            else:
                raise TimeoutError("This ticket isnt available")
        elif ticket_type == "late":
            if 0 <= days_difference < 10:
                self._ticket = LateTicket(self._event_chosen["price"])
            else:
                raise TimeoutError(f"This ticket will be available in {days_difference - 10} days")

        with open("Log.json") as file:
            database = json.load(file)
        if "Data" not in database:
            database["Data"] = {}
        ticket_id = str(self._ticket.get_info[1])
        if not (ticket_id in database["Data"]):
            database["Data"][ticket_id] = {
                "event": self._event_chosen["name"],
                "location": self._event_chosen["location"],
                "date": self._event_chosen["date"],
                "ticket_type": ticket_type,
                "price": self._ticket.get_price,
                "purchase_date": str(datetime.now())
            }
            json.dump(database, open("Log.json", "w"), indent=4)

    @property
    def get_ev(self):
        events_data = json.load(open("Events.json"))
        return "\n".join([f'Name: {event["name"]}\nLocation: {event["location"]}\nDate: {event["date"]} '
                          f'\nPrice: {event["price"]}$\n' for event in events_data["Events"]])

    @property
    def get_price(self):
        return self._ticket.get_price

    def __str__(self):
        return f'\nYour tiket:\n------------------------------------------------------\nTicket info:\nName of event: {self._event_chosen["name"]}\t'\
               f'\nLocation: {self._event_chosen["location"]}\t'\
               f'Date: {self._event_chosen["date"]}\t'\
               f'\n\n{self._ticket}------------------------------------------------------'
               

create_ticket = TicketManage()
print(create_ticket.get_ev)
create_ticket.sel_event()
create_ticket.make_order()
result = input("Would you like to check ticket? (yes/no): ")
if result.lower() == "yes":
    print(create_ticket)
elif result.lower() == "":
    raise ValueError("Invalid input")