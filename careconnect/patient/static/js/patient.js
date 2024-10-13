function openAppointmentForm(date, time, detail) {
    // Display the hidden form by removing the 'hidden' class
    document.getElementById("appointment-form").classList.remove("hidden");
    const dateInput = document.getElementById("date");
    dateInput.value = date;

    // Populate the time input field and set it to readonly
    const timeInput = document.getElementById("time");
    timeInput.value = time;

    // Populate the detail textarea and set it to readonly
    const detailInput = document.getElementById("detail");
    detailInput.value = detail;
}

function closeAppointmentForm() {
    // Hide the form by adding the 'hidden' class
    document.getElementById("appointment-form").classList.add("hidden");
}

