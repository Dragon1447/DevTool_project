function render(page, id=null){
  const addMedicine = document.getElementById('add-medicine');
  const editMedicine = document.getElementById('edit-medicine');
  addMedicine.classList.add('hidden');
  editMedicine.classList.add('hidden');

  switch(page){
    case 'add_medicine':
      addMedicine.classList.remove('hidden');
      break;
    case 'edit_medicine':
      editMedicine.classList.remove('hidden');

      const medicineCard = document.querySelector(`[data-id="${id}"]`);

      const medicineId = medicineCard.dataset.id;
      const name = medicineCard.dataset.name;
      const quantity = medicineCard.dataset.quantity;
      const detail = medicineCard.dataset.detail;

      document.getElementById('medicine-id').value = medicineId || '';
      document.getElementById('name').value = name || '';
      document.getElementById('quantity').value = quantity || '';
      document.getElementById('detail').value = detail || '';
      break;
  }
}


function updateMedicine() {
  // Get form data
  const id = document.getElementById('medicine-id').value;
  const name = document.getElementById('name').value;
  const quantity = document.getElementById('quantity').value;
  const detail = document.getElementById('detail').value;

  // Send a PUT request
  fetch(`/medicine/update/${id}/`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
    },
    body: JSON.stringify({
      'name': name,
      'quantity': quantity,
      'detail': detail
    })
  })
  .then(response => response.json())
  .then(data => {
    window.location.href = '/medicine/';
  })
  .catch(error => console.error('Error:', error));
}


function deleteMedicine() {
  // Get medicine ID
  const id = document.getElementById('medicine-id').value;

  // Send a DELETE request
  fetch(`/medicine/delete/${id}/`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
    }
  })
  .then(response => response.json())
  .then(data => {
    window.location.href = '/medicine/';
  })
  .catch(error => console.error('Error:', error));
}

document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('search').addEventListener('input', function() {
    const searchTerm = this.value.toLowerCase();
    document.querySelectorAll('.medicine-item').forEach(item => {
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
