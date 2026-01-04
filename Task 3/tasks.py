DATA_FILE = 'tasks.txt'
def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split('|')
                if len(parts) < 3:
                    continue
                try:
                    tid = int(parts[0])
                except ValueError:
                    continue
                title = parts[1]
                done = parts[2] == '1'
                tasks.append({'id': tid, 'title': title, 'done': done})
    except FileNotFoundError:
        return []
    except Exception as e:
        print('Error loading tasks:', e)
        return []
    return tasks

def save_tasks(filename, tasks):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for t in tasks:
                title = t['title'].replace('|', ' ')
                done_flag = '1' if t.get('done') else '0'
                f.write(f"{t['id']}|{title}|{done_flag}\n")
    except Exception as e:
        print('Error saving tasks:', e)

def next_id(tasks):
    if not tasks:
        return 1
    highest = max(t['id'] for t in tasks)
    return highest + 1

def list_tasks(tasks):
    if not tasks:
        print('\nNo tasks found.\n')
        return
    print('\nTasks:')
    for t in tasks:
        mark = 'x' if t.get('done') else ' '
        print(f"{t['id']}: [{mark}] {t['title']}")
    print('')

def add_task(tasks):
    title = input('Enter task title: ').strip()
    if not title:
        print('Empty title, task not added.')
        return
    tid = next_id(tasks)
    tasks.append({'id': tid, 'title': title, 'done': False})
    save_tasks(DATA_FILE, tasks)
    print('Task added.')

def update_task(tasks):
    try:
        tid = int(input('Enter task id to update: ').strip())
    except ValueError:
        print('Invalid id.')
        return
    for t in tasks:
        if t['id'] == tid:
            new_title = input(f"New title (leave empty to keep: '{t['title']}'): ").strip()
            if new_title:
                t['title'] = new_title
            done_input = input("Mark done? (y/n, leave empty to keep current): ").strip().lower()
            if done_input == 'y':
                t['done'] = True
            elif done_input == 'n':
                t['done'] = False
            save_tasks(DATA_FILE, tasks)
            print('Task updated.')
            return
    print('Task id not found.')

def delete_task(tasks):
    try:
        tid = int(input('Enter task id to delete: ').strip())
    except ValueError:
        print('Invalid id.')
        return
    for i, t in enumerate(tasks):
        if t['id'] == tid:
            confirm = input(f"Delete '{t['title']}'? (y/n): ").strip().lower()
            if confirm == 'y':
                tasks.pop(i)
                save_tasks(DATA_FILE, tasks)
                print('Task deleted.')
            else:
                print('Delete cancelled.')
            return
    print('Task id not found.')

def main():
    tasks = load_tasks(DATA_FILE)
    while True:
        print('''\nSimple Tasks Manager
1) List tasks
2) Add task
3) Update task
4) Delete task
5) Exit
''')
        choice = input('Choose an option: ').strip()
        if choice == '1':
            list_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            update_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print('Goodbye.')
            break
        else:
            print('Invalid option, please choose 1-5.')

if __name__ == '__main__':
    main()