class MaxHeap:

    def __init__(self):
        self.body = [0]         # Занимаем нулевой индекс

    def max(self):
        if self.body != [0]:
            raise IndexError
        else:
            return self.body[1]

    def pop_max(self):
        if self.body != [0]:        # Поднимаем ошибку, если у нас пустой список
            raise IndexError
        elif len(self.body) == 2:   # Если у нас один елемент, то достаем и выдаем его
            return self.body.pop()
        else:
            self.body[1], self.body[len(self.body) - 1] = self.body[len(self.body) - 1], self.body[1]
            item_to_pop = self.body.pop()   # Переносим элемент в конец и достаем его
            self.__check_the_parent(1)      # Проверим, правда ли новый максимум – Максимум...
            return item_to_pop

    def push(self, item):
        self.body.append(item)
        item_index = len(self.body) - 1
        self.__change_position(item_index)

    def __change_position(self, index_1):
        index_2 = index_1 // 2                                          # Получаем индекст родителя элемента
        if self.body[index_1] > self.body[index_2]:                     # Если элемент больше родителя, меняем местами
            self.body[index_1], self.body[index_2] = self.body[index_2], self.body[index_1]
            self.__change_position(index_2)                             # Повтороно проверяем, уже с новой позицией
        else:
            return

    def __check_the_parent(self, parent_index):
        """
            Считаем, что наш родитель, максимальный элемент и проверяем это дальше.
            Проверяем левого ребенка. Если он больше, то принимаем его за нового родителя.
            Проверяем аналогично правого ребенка. max_index испульзуется для того чтобы в случае замены родителя
            при предыдущей проверке мы сравнивали уже с новым значением.

        :param parent_index:
        :return:
        """
        max_index = parent_index
        if self.body[parent_index] > self.body[parent_index * 2]:
            max_index = parent_index * 2
        if not self.body[max_index] > self.body[parent_index * 2 + 1]:
            max_index = parent_index * 2 + 1
        if max_index != parent_index:
            self.body[parent_index], self.body[max_index] = self.body[max_index], self.body[parent_index]
            self.__check_the_parent(max_index)  # Финальная проверка
