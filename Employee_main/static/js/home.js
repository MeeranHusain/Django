document.addEventListener('DOMContentLoaded', function () {

        const modal = document.getElementById('deleteModal');
        const employeeName = document.getElementById('employeeName');
        const cancelBtn = document.getElementById('cancelDelete');
        const confirmBtn = document.getElementById('confirmDelete');

        let selectedUrl = null;
        let selectedRow = null;

        const csrfToken = document.querySelector(
            '#csrf-form [name=csrfmiddlewaretoken]'
        ).value;

        // Open modal
        document.querySelectorAll('.delete-btn').forEach(function (button) {

            button.addEventListener('click', function () {

                selectedUrl = button.dataset.url;
                selectedRow = button.closest('tr');

                employeeName.textContent = button.dataset.name;

                modal.style.display = 'flex';
            });

        });

        // Cancel deletion
        cancelBtn.addEventListener('click', function () {

            modal.style.display = 'none';

            selectedUrl = null;
            selectedRow = null;
        });

        // Close modal when clicking outside the box
        modal.addEventListener('click', function (event) {

            if (event.target === modal) {
                modal.style.display = 'none';
                selectedUrl = null;
                selectedRow = null;
            }

        });

        // Confirm deletion using AJAX
        confirmBtn.addEventListener('click', async function () {

            if (!selectedUrl || !selectedRow) {
                return;
            }

            const url = selectedUrl;
            const row = selectedRow;

            confirmBtn.disabled = true;
            confirmBtn.textContent = 'Deleting...';

            try {

                const response = await fetch(url, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'X-Requested-With': 'XMLHttpRequest',
                        'Accept': 'application/json'
                    },
                    credentials: 'same-origin'
                });

                const data = await response.json();

                if (!response.ok || !data.success) {
                    throw new Error(data.message || 'Unable to delete employee.');
                }

                // Remove employee row without reloading the page
                row.remove();

                // Show empty state if no employees remain
                const tbody = document.querySelector('.employee-table tbody');

                if (tbody && !tbody.querySelector('tr')) {
                    tbody.innerHTML = `
                        <tr>
                            <td colspan="10" class="no-data">
                                No employees found.
                            </td>
                        </tr>
                    `;
                }

                modal.style.display = 'none';

                selectedUrl = null;
                selectedRow = null;

            } catch (error) {

                alert(error.message || 'Something went wrong. Please try again.');

            } finally {

                confirmBtn.disabled = false;
                confirmBtn.textContent = 'Yes, Delete';

            }

        });

    });