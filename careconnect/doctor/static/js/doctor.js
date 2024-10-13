function render(page, id=null){
  const addDoctor = document.getElementById('add-doctor');
  const editDoctor = document.getElementById('edit-doctor');
  addDoctor.classList.add('hidden');
  editDoctor.classList.add('hidden');

  switch(page){
    case 'add_doctor':
      addDoctor.classList.remove('hidden');
      break;
    case 'edit_doctor':
      editDoctor.classList.remove('hidden');

      const doctorCard = document.querySelector(`[data-id="${id}"]`);

      const doctorId = doctorCard.dataset.id;
      const firstName = doctorCard.dataset.firstName;
      const lastName = doctorCard.dataset.lastName;
      const contactNumber = doctorCard.dataset.contactNumber;

      document.getElementById('doctor-id').value = doctorId || '';
      document.getElementById('first-name').value = firstName || '';
      document.getElementById('last-name').value = lastName || '';
      document.getElementById('contact-number').value = contactNumber || '';
      break;
  }
}


function updateDoctor() {
  // Get form data
  const id = document.getElementById('doctor-id').value;
  const firstName = document.getElementById('first-name').value;
  const lastName = document.getElementById('last-name').value;
  const contactNumber = document.getElementById('contact-number').value;

  console.log(id, firstName, lastName, contactNumber);

  // Send a PUT request
  fetch(`/doctor/update/${id}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
    },
    body: JSON.stringify({
      'first_name': firstName,
      'last_name': lastName,
      'contact_number': contactNumber,
    })
  })
  .then(response => response.json())
  .then(data => {
    window.location.href = '/doctor/';
  })
  .catch(error => console.error('Error:', error));
}


function deleteDoctor() {
  // Get doctor ID
  const id = document.getElementById('doctor-id').value;

  // Send a DELETE request
  fetch(`/doctor/delete/${id}/`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
    }
  })
  .then(response => response.json())
  .then(data => {
    window.location.href = '/doctor/';
  })
  .catch(error => console.error('Error:', error));
}


document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('search').addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    document.querySelectorAll('.doctor-item').forEach(item => {
      const name = item.querySelector('h3').textContent.toLowerCase();
      if (name.includes(searchTerm)) {
        item.style.display = ''; // Show item
      } else {
        item.style.display = 'none'; // Hide item
      }
    });
  });
});
