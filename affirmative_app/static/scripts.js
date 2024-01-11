// Sample function to simulate applying filters
function applyFilters() {
    alert('Filters applied!');
}
// Function to close the center column
function closeCenterColumn() {
    document.getElementById('center-column').style.display = 'none';
}

function closeRightColumn() {
    document.getElementById('right-column').style.display = 'none';
}

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
    document.getElementById('details-provider-name').innerHTML = `
        <h2>${provider.name}</h2>
    `;
    document.getElementById('details-provider-pronoun').innerHTML = `
        <h2>${provider.pronoun}</h2>
    `;
    document.getElementById('details-provider-location').innerHTML = `
        <h2>${provider.location}</h2>
    `;
    document.getElementById('details-provider-email').innerHTML = `
        <h2>${provider.email}</h2>
    `;
    document.getElementById('details-provider-phone_number').innerHTML = `
        <h2>${provider.phone_number}</h2>
    `;
    /*document.getElementById('details-provider-profile_picture').innerHTML = `
        <h2>${provider.profile_picture}</h2>
    `;*/



    /*
        <p id="details-provider-insurance">${provider.insurance}</p>
        <p id="details-provider-website">${provider.website}</p>
        <p id="details-provider-zip_code">${provider.zip_code}</p>
        <p id="details-provider-finances">${provider.finances}</p>
        <p id="details-provider-qualifications">${provider.qualifications}</p>
        <p id = "details-provider-category">${provider.category}</p>
        <p id = "details-provider-education">${provider.education}</p>
        <p id = "details-provider-hospital">${provider.hospital}</p>
        <p id = "details-provider-languages">${provider.languages}</p>*/
})
.catch(error => console.error('Error:', error));
}