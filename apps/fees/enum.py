from django.db import models

# tuition, transport, library, sports, exam, hostel, misc

class FeeType(models.TextChoices):
    TUITION = "tuition", "Tuition"
    TRANSPORT = "transport", "Transport"
    LIBRARY = "library", "Library"
    SPORTS = "sports", "Sports"
    EXAM = "exam", "Exam"
    HOSTEL = "hostel", "Hostel"
    MISC = "misc", "Miscellaneous"

# cash, card, upi, neft, cheque
class PaymentMethod(models.TextChoices):
    CASH = "cash", "Cash"
    CARD = "card", "Card"
    UPI = "upi", "UPI"
    NEFT = "neft", "NEFT"
    CHEQUE = "cheque", "Cheque"

# paid, partial, pending, overdue

class PaymentStatus(models.TextChoices):
    PAID = "paid", "Paid"
    PARTIAL = "partial", "Partial"
    PENDING = "pending", "Pending"
    OVERDUE = "overdue", "Overdue"