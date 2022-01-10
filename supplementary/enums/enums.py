
from enum import Enum
class SwitchState(Enum):
    Active = "Активно"
    Between = "Застряло посередине"
    NonActive = "Отключено"

a = SwitchState.Between

print(a)
print(a.value)
print(list(SwitchState))

if a == SwitchState.NonActive:
    print("Отключено")
else:
    print("Все остальное")