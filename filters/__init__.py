from loader import dp
from .admin import IsAdmin

if __name__ == "filters":
    dp.bind_filter(IsAdmin)
