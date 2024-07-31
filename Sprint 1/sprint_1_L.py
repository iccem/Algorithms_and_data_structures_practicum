from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    shorter = sorted(shorter)
    shorter.append('0')
    longer = sorted(longer)
    for i in range(len(longer)):
        if longer[i] != shorter[i]:
            return longer[i]

def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))