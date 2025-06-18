class CircularListNode:
    """Узел кольцевого списка"""
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node if next_node is not None else self

    def __repr__(self):
        return f"Node({self.value})"


class CircularLinkedList:
    """Кольцевой список"""
    def __init__(self, data_string):
        if not data_string:
            raise ValueError("Input string cannot be empty")
        if not data_string.isdigit():
            raise ValueError("Input string must contain only digits")
        
        self.head = None
        self.length = 0
        self._build_list(data_string)

    def _build_list(self, data_string):
        """Строит кольцевой список из строки цифр"""
        prev_node = None
        first_node = None
        
        for char in data_string:
            node = CircularListNode(int(char))
            self.length += 1
            
            if prev_node is not None:
                prev_node.next = node
            else:
                first_node = node
                
            prev_node = node
        
        if prev_node is not None:
            prev_node.next = first_node
            self.head = first_node

    def get_numbers_starting_from(self, start_node, lengths):
        """
        Получает числа из кольца, начиная с start_node, с заданными длинами
        Возвращает кортеж (число1, число2, число3, следующий узел)
        """
        numbers = []
        current_node = start_node
        
        for length in lengths:
            if length == 0:
                numbers.append(0)
                continue
                
            num_str = ""
            for _ in range(length):
                num_str += str(current_node.value)
                current_node = current_node.next
            numbers.append(int(num_str))
        
        return (*numbers, current_node)

    def find_equation(self):
        """Ищет уравнение вида A+B=C в кольце"""
        max_length = min(30, self.length // 3)  # Ограничиваем максимальную длину числа
        
        for a_len in range(1, max_length + 1):
            for b_len in range(1, max_length + 1):
                c_len_max = min(a_len, b_len) + 1
                for c_len in range(max(1, max(a_len, b_len) - 1), c_len_max + 1):
                    if a_len + b_len + c_len > self.length:
                        continue
                    
                    current_node = self.head
                    for _ in range(self.length):
                        a, b, c, next_node = self.get_numbers_starting_from(
                            current_node, [a_len, b_len, c_len]
                        )
                        
                        if a + b == c:
                            return f"{a}+{b}={c}"
                        
                        current_node = current_node.next
        
        return "No"


def main():
    """Основная функция программы"""
    print("Программа для поиска уравнения A+B=C в числовом кольце")
    print("Введите строку цифр (без пробелов):")
    
    try:
        input_data = input().strip()
        if not input_data:
            raise ValueError("Введена пустая строка")
        
        ring = CircularLinkedList(input_data)
        result = ring.find_equation()
        print("\nРезультат:")
        print(result)
    except ValueError as e:
        print(f"\nОшибка ввода: {e}")
    except Exception as e:
        print(f"\nПроизошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
