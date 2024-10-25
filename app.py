import random
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy data
flights = [
    {"id": 1, "name": "Flight A", "from": "City A", "to": "City B", "date": "2024-09-25", "time": "2 hrs", "price": 100},
    {"id": 2, "name": "Flight B", "from": "City C", "to": "City D", "date": "2024-09-26", "time": "3 hrs", "price": 200},
]

bookings = []

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin' and password == 'admin123':
        return redirect(url_for('admin_dashboard'))
    elif username == 'user' and password == 'user123':
        return redirect(url_for('user_dashboard'))
    
    return "Invalid credentials"

@app.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html', flights=flights)

@app.route('/submit_booking', methods=['POST'])
def submit_booking():
    booking_id = random.randint(100000, 999999)
    username = request.form['username']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    email = request.form['email']
    phone = request.form['phone']
    num_tickets = request.form['num_tickets']
    passport_no = request.form['passport_no']

    # Add booking logic here (save to bookings list or database)
    bookings.append({
        "id": booking_id,
        "username": username,
        "address": address,
        "city": city,
        "state": state,
        "email": email,
        "phone": phone,
        "num_tickets": num_tickets,
        "passport_no": passport_no,
        "status": "not paid"
    })

    return redirect(url_for('user_dashboard'))

@app.route('/cancel_ticket', methods=['POST'])
def cancel_ticket():
    booking_id = request.form['booking_id']
    # Logic to delete ticket from bookings
    return redirect(url_for('user_dashboard'))

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
