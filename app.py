import streamlit as st

st.title("⚡ AI-Based Energy Saving Recommendation System")
st.write("Monitor your appliance usage, estimate energy consumption, calculate electricity cost, and get smart energy-saving recommendations.")
power_values = {
    "LED Bulb": 10,
    "Fan": 75,
    "TV": 100,
    "AC": 1500
}

st.subheader("Appliance Usage")
st.write("Enter the number of hours each aplliance is used per day.")

col1, col2 = st.columns(2)

with col1:
    bulb_hours = st.number_input("LED Bulb - hours/day", 0.0, 24.0)
    fan_hours = st.number_input("Fan - hours/day", 0.0, 24.0)

with col2:
    tv_hours = st.number_input("TV - hours/day", 0.0, 24.0)
    ac_hours = st.number_input("AC - hours/day", 0.0, 24.0)
if st.button("Calculate Total Energy",type="primary"):

    bulb_energy = (power_values["LED Bulb"] * bulb_hours) / 1000
    fan_energy = (power_values["Fan"] * fan_hours) / 1000
    tv_energy = (power_values["TV"] * tv_hours) / 1000
    ac_energy = (power_values["AC"] * ac_hours) / 1000

    total_energy = bulb_energy + fan_energy + tv_energy + ac_energy

    cost_per_unit = 8
    total_cost = total_energy * cost_per_unit
    monthly_cost = total_cost * 30

    col1, col2, col3 = st.columns(3)

    col1.metric("⚡ Daily Energy", f"{total_energy:.2f} kWh")
    col2.metric("💰 Daily Cost", f"Rs. {total_cost:.2f}")
    col3.metric("📅 Monthly Cost", f"Rs. {monthly_cost:.2f}")

    st.subheader(" Appliance-wise Energy Consumption")

    energy_data = {
        "LED Bulb": bulb_energy,
        "Fan": fan_energy,
        "TV": tv_energy,
        "AC": ac_energy
    }

    st.bar_chart(energy_data)

    st.subheader(" Smart Energy Recommendation")

    if ac_hours > 2:
        st.info(
            "💡 AC usage is high. Try reducing AC usage or increasing the temperature setting to save energy."
        )

    elif fan_hours > 8:
        st.info(
            "🌀 Fan usage is high. Switch off the fan when the room is not in use."
        )

    elif tv_hours > 6:
        st.info(
            "📺 TV usage is high. Try reducing TV usage by 1–2 hours per day."
        )

    elif total_energy < 5:
        st.success(
            "✅ Your energy usage is efficient. Keep using appliances wisely."
        )

    elif total_energy < 10:
        st.warning(
            "⚡ Moderate energy usage detected. Try reducing appliance usage to save electricity."
        )

    else:
        st.error(
            "🚨 High energy usage detected. Focus on reducing high-power appliance usage, especially AC."
        )