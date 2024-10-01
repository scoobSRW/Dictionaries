service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

nxt_ticket_num = 3

def add_ticket(service_tickets, customer_name, issue, status="open"):
    global nxt_ticket_num
    ticket_id = f"Ticket{str(nxt_ticket_num).zfill(3)}"
    service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue, "Status": status}
    nxt_ticket_num += 1

def update_status(service_tickets, ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Status for {ticket_id} updated to {new_status}")
    else:
        print(f"{ticket_id} not found in service tickets.")

def list_service_tickets():
    for k, v in service_tickets.items():
        print(k, v)


def user_interface():
    while True:
        print("\n--- Service Ticket System ---")
        print("1. Add a new ticket")
        print("2. Update ticket status")
        print("3. List all tickets")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            customer_name = input("Enter customer name: ")
            issue = input("Describe the issue: ")
            status = input("Enter status (default is 'open'): ") or "open"
            add_ticket(service_tickets, customer_name, issue, status)

        elif choice == "2":
            ticket_id = input("Enter the ticket ID to update: ")
            new_status = input("Enter the new status: ")
            update_status(service_tickets, ticket_id, new_status)

        elif choice == "3":
            list_service_tickets()

        elif choice == "4":
            print("Exiting system. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

user_interface()