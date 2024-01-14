function applyFilters() {
    // Collect filter values
    var procedureElement = document.getElementById('procedure-title');
    var procedure = procedureElement.textContent || procedureElement.innerText;

    // Collect the rest of the filter values
    var distance = document.getElementById('sort-distance').value;
    var gender = document.getElementById('gender').value;
    var meetingForm = document.getElementById('meeting-form').value;
    var language = document.getElementById('languages-dropdown').value;
    var insurance = document.getElementById('insurance-dropdown').value;

    // Construct the query parameters
    var queryParams = new URLSearchParams({
        procedure: procedure,
        distance: distance,
        gender: gender,
        meetingForm: meetingForm,
        language: language,
        insurance: insurance
    });

    // Make an AJAX request to apply filters and update results
    fetch(`/apply_filters?${queryParams}`, {
        method: 'GET', // or 'POST' if you're sending a lot of data
        // Additional options like headers, credentials, etc. may be needed depending on your setup
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // Assuming 'data' is an array of provider objects
        updateResults(data);
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to apply filters.');
    });
}

function updateResults(data) {
    var resultsContainer = document.querySelector('.results-container');
    resultsContainer.innerHTML = ''; // Clear current results

    // Update the count of results
    var resultsCount = data.length; // Get the count of results
    var headerElement = document.querySelector('.center_header');
    headerElement.innerHTML = 'RESULTS (' + resultsCount + ')'; // Update the header with the new count


    // Iterate over each result and append it to the results container
    data.forEach(result => {
        // Create result block
        var resultBlock = document.createElement('div');
        resultBlock.className = 'result-block';

        // Check if languages is defined and is an array, then join; otherwise, use 'None'
        var languagesSpoken = Array.isArray(result.languages) ? result.languages.join(', ') : 'None';

        // Populate the result block with provider data
        resultBlock.innerHTML = `
            <h3>${result.name}</h3>
            <p>Specialties: ${result.specialties || 'None'}</p>
            <p>Location: ${result.location}</p>
            <p>Languages Spoken: ${languagesSpoken}</p>
            <button onclick="showResultDetails('${result.provider_ID}')">View Details</button>
        `;

        // Append the result block to the results container
        resultsContainer.appendChild(resultBlock);
    });
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