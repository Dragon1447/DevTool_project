function render(page, id=null){
  const addPatient = document.getElementById('add-patient');
  const editPatient = document.getElementById('edit-patient');
  addPatient.classList.add('hidden');
  editPatient.classList.add('hidden');

  switch(page){
    case 'add_patient':
      addPatient.classList.remove('hidden');
      break;
    case 'edit_patient':
      editPatient.classList.remove('hidden');

      const patientCard = document.querySelector(`[data-id="${id}"]`);

      // Access dataset values
      const patientId = patientCard.dataset.id;
      const firstName = patientCard.dataset.firstName;
      const lastName = patientCard.dataset.lastName;
      const contactNumber = patientCard.dataset.contactNumber;

      // Set form field values
      document.getElementById('patient-id').value = patientId || '';
      document.getElementById('first-name').value = firstName || '';
      document.getElementById('last-name').value = lastName || '';
      document.getElementById('contact-number').value = contactNumber || '';
      break;
  }
}

function medicine() {
  // Get form data
  const id = document.getElementById('patient-id').value;

  fetch('/treatment/medicine/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
    },
    body: JSON.stringify({ id: id })
    })
    .then(response => response.json())
    .then(data => {
        // Handle response (e.g., redirect to another page or update UI)
        window.location.href = `/treatment/medicine/`; // Example of redirect
    })
    .catch(error => console.error('Error:', error));
}


document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('search').addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    document.querySelectorAll('.patient-item').forEach(item => {
      const name = item.querySelector('h3').textContent.toLowerCase();
      console.log(name);
      if (name.includes(searchTerm)) {
        item.style.display = 'block'; // Show item
      } else {
        item.style.display = 'none'; // Hide item
      }
    });
  });
});
