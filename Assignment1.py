class Guest:
    def __init__(self, first_name, last_name, email, phone_number, guest_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__guest_id = guest_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_phone_number(self):
        return self.__phone_number

    def set_guest_id(self, guest_id):
        self.__guest_id = guest_id

    def get_guest_id(self):
        return self.__guest_id

    def __str__(self):
        return f"First Name: {self.get_first_name()} Last Name: {self.get_last_name()} Email: {self.get_email()} Phone Number: {self.get_phone_number()} Guest ID: {self.get_guest_id()}"

    def make_reservation(self):
        print(self.get_first_name(), self.get_last_name(), "has made a reservation.")

    def cancel_reservation(self):
        print(self.get_first_name(), self.get_last_name(), "has canceled the reservation.")

    def modify_reservation(self):
        print(self.get_first_name(), self.get_last_name(), "has modified the reservation.")

    def add_special_request(self):
        print(self.get_first_name(), self.get_last_name(), "has added a special request.")


class Reservation:
    def __init__(self, reservation_id, room_type, check_in_date, check_out_date, special_request):
        self.__reservation_id = reservation_id
        self.__room_type = room_type
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__special_request = special_request

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def get_reservation_id(self):
        return self.__reservation_id

    def set_room_type(self, room_type):
        self.__room_type = room_type

    def get_room_type(self):
        return self.__room_type

    def set_check_in_date(self, check_in_date):
        self.__check_in_date = check_in_date

    def get_check_in_date(self):
        return self.__check_in_date

    def set_check_out_date(self, check_out_date):
        self.__check_out_date = check_out_date

    def get_check_out_date(self):
        return self.__check_out_date

    def set_special_request(self, special_request):
        self.__special_request = special_request

    def get_special_request(self):
        return self.__special_request

    def __str__(self):
        return f"Reservation ID: {self.get_reservation_id()} Room Type: {self.get_room_type()} Check-in Date: {self.get_check_in_date()} Check-out Date {self.get_check_out_date()} Special Request: {self.get_special_request()} "

    def create_reservation(self):
        print("Reservation ", self.get_reservation_id(), "for room type ", self.get_room_type(), "has been created.")

    def cancel_reservation(self):
        print("Reservation ", self.get_reservation_id(), "has been canceled.")

    def modify_reservation(self):
        print("Reservation ", self.get_reservation_id(), "has been modified.")

    def confirm_reservation(self):
        print("Reservation ", self.get_reservation_id(), "has been confirmed.")


class Payment:
    def __init__(self, payment_id, amount, payment_method, payment_status, reservation_id):
        self.__payment_id = payment_id
        self.__amount = amount
        self.__payment_method = payment_method
        self.__payment_status = payment_status
        self.__reservation_id = reservation_id

    def set_payment_id(self, payment_id):
        self.__payment_id = payment_id

    def get_payment_id(self):
        return self.__payment_id

    def set_amount(self, amount):
        self.__amount = amount

    def get_amount(self):
        return self.__amount

    def set_payment_method(self, payment_method):
        self.__payment_method = payment_method

    def get_payment_method(self):
        return self.__payment_method

    def set_payment_status(self, payment_status):
        self.__payment_status = payment_status

    def get_payment_status(self):
        return self.__payment_status

    def set_reservation_id(self, reservation_id):
        self.__reservation_id = reservation_id

    def get_reservation_id(self):
        return self.__reservation_id

    def __str__(self):
        return f"Payment ID: {self.get_payment_id()} Amount: {self.get_amount()} Payment Method: {self.get_payment_method()} Payment Status: {self.get_payment_status()} Reservation ID: {self.get_reservation_id()}"

    def process_payment(self):
        print("Payment ", self.get_payment_id(), "of amount $", self.get_amount(), "has been processed using ",
              self.get_payment_method())

    def verify_payment(self):
        print("Payment ", self.get_payment_id(), "has been verified. Status: ", self.get_payment_status())


class Receptionist:
    def __init__(self, employee_id, first_name, last_name, role, contact_number):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__role = role
        self.__contact_number = contact_number

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_employee_id(self):
        return self.__employee_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_role(self, role):
        self.__role = role

    def get_role(self):
        return self.__role

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def get_contact_number(self):
        return self.__contact_number

    def __str__(self):
        return f"Receptionist ID: {self.get_employee_id()} First Name: {self.get_first_name()} Last Name: {self.get_last_name()} Role: {self.get_role()} Contact Number: {self.get_contact_number()}"

    def check_in_guest(self):
        print("Receptionist: ", self.get_first_name(), self.get_last_name(), "has checked in the guest.")

    def check_out_guest(self):
        print("Receptionist: ", self.get_first_name(), self.get_last_name(), "has checked out the guest.")

    def verify_guest_details(self):
        print("Receptionist: ", self.get_first_name(), self.get_last_name(), "has verified the guest details.")


guest1 = Guest("Ted", "Vera", "Tedver@mac.com", "0509999999", "GUEST001")
print(guest1)
guest1.make_reservation()

reservation1 = Reservation("RES321", "2 Queen Beds/ No Smoking/ Desk/ Safe/ Coffee Maker/ Hair Dryer", "22-AUG-2010",
                           "24-AUG-2010", "Early check-in")
print(reservation1)
reservation1.confirm_reservation()

payment1 = Payment("PAY745", "201.48", "Master Card", "Completed", "RES321")
print(payment1)
payment1.process_payment()

receptionist1 = Receptionist("EMP222", "Ahmed", "Khalid", "Manager", "505-661-1110")
print(receptionist1)
receptionist1.check_in_guest()