import streamlit as st
from datetime import datetime, date
import time

st.set_page_config(page_title="Date & Time Utility App", page_icon="📅")

st.title("📅 Date & Time Utility Application")

menu = st.sidebar.selectbox(
    "Choose an option",
    [
        "Find Day for a Date",
        "Today's Day",
        "Greeting & Birthday",
        "Age Calculator",
        "Event Countdown"
    ]
)

# ---------------------------------------------------
# 1. FIND DAY FOR A DATE
# ---------------------------------------------------
if menu == "Find Day for a Date":
    st.header("🗓 Find Day for a Given Date")

    date_input = st.text_input("Enter date (DD-MM-YYYY)")

    if st.button("Find Day"):
        try:
            date_obj = datetime.strptime(date_input, "%d-%m-%Y")
            st.success(f"Day of the week: **{date_obj.strftime('%A')}**")
        except ValueError:
            st.error("Invalid date format. Use DD-MM-YYYY.")

# ---------------------------------------------------
# 2. TODAY'S DAY
# ---------------------------------------------------
elif menu == "Today's Day":
    st.header("📆 Today's Date & Day")

    today = datetime.today()
    st.info(f"Date: {today.strftime('%d-%m-%Y')}")
    st.info(f"Day: {today.strftime('%A')}")

# ---------------------------------------------------
# 3. GREETING & BIRTHDAY
# ---------------------------------------------------
elif menu == "Greeting & Birthday":
    st.header("🎉 Greeting & Birthday Checker")

    name = st.text_input("Enter your name")
    dob = st.date_input("Select your date of birth")

    if st.button("Greet Me"):
        now = datetime.now()
        hour = now.hour
        today = date.today()

        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 17:
            greeting = "Good afternoon"
        elif 17 <= hour < 21:
            greeting = "Good evening"
        else:
            greeting = "Good night"

        if today.day == dob.day and today.month == dob.month:
            st.success(f"{greeting}, {name}! 🎂 Happy Birthday!")
        else:
            st.success(f"{greeting}, {name}!")

# ---------------------------------------------------
# 4. AGE CALCULATOR
# ---------------------------------------------------
elif menu == "Age Calculator":
    st.header("🎯 Age Calculator")

    name = st.text_input("Enter your name")
    dob = st.date_input("Select your date of birth")

    if st.button("Calculate Age"):
        today = date.today()

        years = today.year - dob.year
        months = today.month - dob.month
        days = today.day - dob.day

        if days < 0:
            months -= 1
            days += 30  # approximate

        if months < 0:
            years -= 1
            months += 12

        st.info(f"Hello {name}")
        st.success(f"Your age is {years} years, {months} months and {days} days")

# ---------------------------------------------------
# 5. COUNTDOWN TIMER
# ---------------------------------------------------
elif menu == "Event Countdown":
    st.header("⏳ Countdown to Future Event")

    event_name = st.text_input("Event name")
    event_datetime = st.datetime_input("Event date and time")

    if st.button("Start Countdown"):
        placeholder = st.empty()

        while True:
            now = datetime.now()
            remaining = event_datetime - now

            if remaining.total_seconds() <= 0:
                placeholder.success(f"🎉 {event_name} has arrived!")
                break

            days = remaining.days
            hours, rem = divmod(remaining.seconds, 3600)
            minutes, seconds = divmod(rem, 60)

            placeholder.info(
                f"Time left: {days}d {hours}h {minutes}m {seconds}s"
            )
            time.sleep(1)

