customer_service_tickets = {
    "Ticket001": {"Customer": "Alex", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Vitoria", "Issue": "Payment issue", "Status": "closed"},
    "Ticket003": {"Customer": "Claudia", "Issue": "Check out problem", "Status": "open"},
    "Ticket004": {"Customer": "Nick", "Issue": "Adding to cart problem", "Status": "closed"},
    "Ticket005": {"Customer": "Gabriela", "Issue": "Promo code problem", "Status": "open"}
}

# user input on if and what ticket they would like to update
# the function updates that specific ticket with the user input


# update status of existing ticket

def update_ticket():
    user_update = input('Would you like to update a ticket? (y/n): ').lower()
    
    if user_update == 'y':
        ticket_number = input("Please enter the ticket number to update: ")
        
        if ticket_number in customer_service_tickets:
            print(f"Current ticket info: {customer_service_tickets[ticket_number]}")
            
            update_field = input("Which field would you like to update? (Issue/Status): ").capitalize()
            
            if update_field in ["Issue", "Status"]:
                new_value = input(f"Enter the new {update_field}: ")
                
                customer_service_tickets[ticket_number][update_field] = new_value
                print(f"Ticket {ticket_number} updated successfully!")
            else:
                print("Invalid field. Only 'Issue' or 'Status' can be updated.")
        else:
            print(f"Ticket {ticket_number} not found.")
    else:
        print("No update will be made.")

update_ticket()


def get_next_ticket_number():
    # Extract current ticket numbers, convert the number part to an integer
    highest_ticket_number = max(int(ticket[6:]) for ticket in customer_service_tickets.keys())
    # Increment the highest ticket number to get the new one
    next_ticket_number = f"Ticket{highest_ticket_number + 1:03d}"
    return next_ticket_number

# open new service ticket (add)
#  - asking for user input to initiate a new ticket


# display all tickets

def display_tickets():
    user_display = input('Would you like to display the tickets? (y/n): ')
    if user_display == 'y':
        print(customer_service_tickets)
    else:
        print('Invalid input')

display_tickets()

def adding_ticket():
    user_name = input("Please provide your name: ")
    user_issue = input("Please provide a brief description of your issue: ")
    
    next_ticket = get_next_ticket_number()

    customer_service_tickets[next_ticket] = {"Customer": user_name, "Issue": user_issue, "Status": "open"}

adding_ticket()
print(customer_service_tickets)