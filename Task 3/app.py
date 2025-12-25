from tasks import TaskManager
def main() -> None:
    m = TaskManager()
    while True:
        print("\nOptions: 1) Create  2) List  3) Update  4) Delete  0) Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            desc = input("Description (optional): ").strip()
            try:
                t = m.create_task(title, desc)
                print(f"Created #{t.id}: {t.title}")
            except ValueError as e:
                print("Error:", e)
        elif choice == "2":
            tasks = m.list_tasks()
            if not tasks:
                print("No tasks.")
            else:
                for t in tasks:
                    status = "Done" if t.completed else "Pending"
                    print(f"#{t.id} {t.title} [{status}]")
                    if t.description:
                        print("  ", t.description)
        elif choice == "3":
            try:
                tid = int(input("Task id: "))
            except ValueError:
                print("Invalid id")
                continue
            t = m.get_task(tid)
            if not t:
                print("Not found")
                continue
            nt = input(f"Title ({t.title}): ").strip()
            nd = input(f"Desc ({t.description}): ").strip()
            nc = input("Completed? (y/n, leave blank to keep): ").strip().lower()
            try:
                m.update_task(tid, title=nt or None, description=nd or None,
                              completed=(True if nc == "y" else False) if nc in ("y", "n") else None)
                print("Updated.")
            except Exception as e:
                print("Error:", e)
        elif choice == "4":
            try:
                tid = int(input("Task id to delete: "))
            except ValueError:
                print("Invalid id")
                continue
            if input("Confirm delete? (y/n): ").strip().lower() != "y":
                print("Canceled")
                continue
            try:
                d = m.delete_task(tid)
                print("Deleted:", d.title)
            except KeyError as e:
                print("Error:", e)
        elif choice == "0":
            print("Bye")
            break
        else:
            print("Unknown option")

if __name__ == "__main__":
    main()