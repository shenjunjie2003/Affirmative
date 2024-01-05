// Sample function to simulate applying filters
function applyFilters() {
    alert('Filters applied!');
}

// Function to close the center column
function closeCenterColumn() {
    document.getElementById('center-column').style.display = 'none';
}

// Sample function to simulate displaying details on result click
function showResultDetails(providerID) {
    document.getElementById('right-column').style.display = 'block';
    // Make an AJAX request to get the result details
    fetch(`/get_result_details/${providerID}`)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(provider => {
        // Update the HTML elements in the right column dynamically
        // ... (your code to update the provider details)
    })
    .catch(error => console.error('Error:', error));
}
