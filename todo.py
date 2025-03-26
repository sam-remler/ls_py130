class Todo:
    IS_DONE = 'X'
    IS_UNDONE = ' '

    def __init__(self, title):
        self._title = title
        self._done = False

    @property
    def title(self):
        return self._title

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, done):
        self._done = done

    def __str__(self):
        marker = Todo.IS_DONE if self.done else Todo.IS_UNDONE
        return f'[{marker}] {self.title}'

    def __eq__(self, other):
        if isinstance(other, Todo):
            return self.title == other.title and self.done == other.done

        return NotImplemented



class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []
    
    @property
    def title(self):
        return self._title
    
    def add(self, todo):
        if not isinstance(todo, Todo):
            return TypeError("Can only add Todo objects")
        else:
            self._todos.append(todo)
    
    def __str__(self):
        output_lines = [f'----- {self.title} -----']
        output_lines += [str(todo) for todo in self._todos]
        return '\n'.join(output_lines)
    
    def __len__(self):
        return len(self._todos)
    
    def first(self):
        return self._todos[0]
    
    def last(self):
        return self._todos[-1]
    
    def todo_at(self, index):
        return self._todos[index]
    
    def mark_done_at(self, index):
        todo = self.todo_at(index)
        todo.done = True
    
    def mark_undone_at(self, index):
        todo = self.todo_at(index)
        todo.done = False
    
    def mark_all_done(self):
        def mark_done(todo):
            todo.done = True
        self.each(mark_done)
    
    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False
        self.each(mark_undone)

    def all_done(self):
        return all([todo.done for todo in self._todos])
    
    def remove_at(self, index):
        del self._todos[index]
    
    
    def to_list(self):
        return self._todos.copy()    
    
    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        new_todolist = TodoList(self.title)
        for todo in filter(callback, self._todos):
                new_todolist.add(todo)
        return new_todolist
    
    def find_by_title(self,title):
        found = self.select(lambda todo: todo.title == title)
        return found.todo_at(0)
    
    def done_todos(self):
        return self.select(lambda todo: todo.done)
    
    def undone_todos(self):
        return self.select(lambda todo: not todo.done)
    
    def mark_done(self, title):
        todo = self.find_by_title(title)
        todo.done = True
