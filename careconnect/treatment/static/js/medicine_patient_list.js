function displayCartTable() {
    const savedCart = localStorage.getItem('cart');

    // Check if there is any data in localStorage
    if (savedCart) {
        const items = JSON.parse(savedCart); // Parse JSON data
        const tableBody = document.getElementById('cart-table-body'); // Reference to table body

        tableBody.innerHTML = ''; // Clear any existing rows

        // Loop through items and create table rows with form elements
        items.forEach((item, index) => {
            const row = document.createElement('tr');

            row.innerHTML = `
        <tr class="border border-black">
            <td class="pb-4">
                <input type="hidden" name="medicine_id[]" value="${item.id}">
                <input type="text" value="${item.name}" class="border rounded p-2" name="name[]" readonly>
            </td>
            <td class="pb-4">
                <input type="number" value="${item.quantity}" class="border rounded p-2 w-16" name="quantity[]" readonly>
            </td>

            <!-- Input number for dose -->
            <td class="pb-4 ml-4">
                <input type="number" value="${item.dose}" class="border rounded p-2" name="dose[]">
            </td>

            <!-- Select dropdown for time -->
            <td class="pb-4">
                <select class="border rounded p-2" name="time[]">
                    <option value="" disabled selected>Select time</option>
                    <option value="AC_TID">Ante Cibum Three Times a Day</option>
                    <option value="PC_TID">Post Cibum Three Times a Day</option>
                    <option value="AC_BID">Ante Cibum Twice a Day</option>
                    <option value="PC_BID">Post Cibum Twice a Day</option>
                    <option value="AC_Noon">Ante Cibum at Noon</option>
                    <option value="PC_Noon">Post Cibum at Noon</option>
                    <option value="HS">Hora Somni</option>
                </select>
            </td>

            <!-- Input text for details -->
            <td class="pb-4">
                <input type="text" value="" class="border rounded p-2" name="details[]">
            </td>

            <!-- Select dropdown for notification -->
            <td class="pb-4">
                <select class="border rounded p-2" name="notification[]">
                    <option value="true" ${item.notification ? 'selected' : ''}>Yes</option>
                    <option value="false" ${!item.notification ? 'selected' : ''}>No</option>
                </select>
            </td>
        </tr>

            `;

            tableBody.appendChild(row);
        });
    } else {
        console.log('No items in cart.');
    }
}

function toggleForm() {
    const form = document.getElementById('appointment-form');
    const notification = document.getElementById('appointment_notification');

    form.classList.toggle('hidden');

    if (form.classList.contains('hidden')) {
        notification.value = 'false';
    } else {
        notification.value = 'true';
    }
}

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    form.addEventListener('submit', function () {
        localStorage.clear()
    });
});
