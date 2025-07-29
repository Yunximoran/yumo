from django.dispatch import receiver
from django.dispatch import Signal


first = Signal()

@receiver(first)
def firstemit(sender, **kwargs):
    print("first signal tirgger")
    print(kwargs)


__all__ = [
    "first"
]