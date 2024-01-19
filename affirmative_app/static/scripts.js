var currentProviderId = null;

document.addEventListener('DOMContentLoaded', (event) => {
    var bookmarkButton = document.getElementById('bookmark-button');
    var saveBookmarkButton = document.getElementById('save-bookmark');

    if (bookmarkButton) {
        bookmarkButton.addEventListener('click', function() {
            var dropdown = document.getElementById('bookmark-dropdown');
            dropdown.style.display = dropdown.style.display === 'none' ? 'block' : 'none';
        });
    }

    if (saveBookmarkButton) {
        saveBookmarkButton.addEventListener('click', function() {
            handleSaveBookmark(currentProviderId);
        });
    }

    // Add any other DOMContentLoaded functionalities here
});


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

    data.forEach(result => {
        // Create the container for each result
        var resultBlock = document.createElement('div');
        resultBlock.className = 'result-block';

        // Create and style the label
        var label = document.createElement('p');
        label.className = 'label'; // Make sure this matches your CSS class for styling the label
        label.textContent = result.label // Or any other text or result property

        // Create and add the name heading
        var name = document.createElement('h3');
        name.textContent = result.name;

        // Create and add the specialties paragraph
        var specialties = document.createElement('p');
        specialties.textContent = 'Specialties: ' + (result.category || 'None');

        // Create and add the location paragraph
        var location = document.createElement('p');
        location.textContent = 'Location: ' + result.address + ', ' + result.city + ', ' + result.state + ', ' + result.zip_code;

        // Create and add the languages paragraph
        var languages = document.createElement('p');
        languages.textContent = 'Languages Spoken: ' + result.languages;

        // Create and style the view details button
        var viewDetailsButton = document.createElement('button');
        viewDetailsButton.textContent = 'View Details';
        viewDetailsButton.addEventListener('click', function() {
            showResultDetails(result.provider_ID);
        });

        // Append all the elements to the result block
        resultBlock.appendChild(label);
        resultBlock.appendChild(name);
        resultBlock.appendChild(specialties);
        resultBlock.appendChild(location);
        resultBlock.appendChild(languages);
        resultBlock.appendChild(viewDetailsButton);

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
    document.getElementById('right-column').style.display = 'flex';
    currentProviderId = providerID;

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
        document.getElementById('details-provider-name').textContent = provider.name || 'N/A';
        document.getElementById('details-provider-pronoun').textContent = provider.pronoun || 'N/A';
        document.getElementById('details-provider-zip_code').textContent = provider.zip_code || 'N/A';
        document.getElementById('details-provider-email').textContent = provider.email || 'N/A';
        document.getElementById('details-provider-phone_number').textContent = provider.phone_number || 'N/A';
        document.getElementById('details-provider-specialities').textContent = provider.specialties || 'N/A';
        document.getElementById('details-provider-gender').textContent = provider.gender|| 'N/A';
        document.getElementById('details-provider-hospital').textContent = provider.hospital || 'N/A';
        document.getElementById('details-provider-languages').textContent = provider.languages || 'N/A';
        document.getElementById('details-provider-insurance').textContent = provider.insurance || 'N/A';
        document.getElementById('details-provider-address').textContent = provider.address || 'N/A';

        var city = provider.city || 'N/A';
        var state = provider.state || 'N/A';
        var location = city + ', ' + state;
        document.getElementById('details-provider-cityandstate').textContent = location;

        var qualifications = provider.qualifications || 'N/A';
        var edu = provider.education || 'N/A';
        document.getElementById('details-provider-education').textContent = qualifications + ', ' + edu;
        //console.log(qualifications + ',' + edu);

        return fetch(`/bookmarked_patients/${currentProviderId}`);
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(bookmarkedPatientIds => {
        // Get all patient checkboxes and update their checked state based on the bookmarked patients
        var patientCheckboxes = document.querySelectorAll('.patient-checkbox');
        patientCheckboxes.forEach(checkbox => {
            checkbox.checked = bookmarkedPatientIds.includes(parseInt(checkbox.value));
        });
        
        // Display the right column after updating the provider details and the bookmarked state
        document.getElementById('right-column').style.display = 'flex';
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred while fetching the details. Please try again.');
    });
    // Now check if the save bookmark event listener has been attached
    var saveBookmarkButton = document.getElementById('save-bookmark');
    if (!isSaveBookmarkEventAttached) {
        saveBookmarkButton.addEventListener('click', saveBookmarkEventHandler);
        isSaveBookmarkEventAttached = true; // Set the flag to true after attaching the event
    }
}

function saveBookmarkEventHandler() {
    handleSaveBookmark(currentProviderId);
}


function handleSaveBookmark(providerId) {
    var checkedPatients = Array.from(document.querySelectorAll('.patient-checkbox:checked')).map(cb => cb.value);
    var uncheckedPatients = Array.from(document.querySelectorAll('.patient-checkbox:not(:checked)')).map(cb => cb.value);

    // Perform the AJAX request with providerId
    fetch('/update_bookmarks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            provider_id: providerId,
            checked_patients: checkedPatients,
            unchecked_patients: uncheckedPatients
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            document.getElementById('bookmark-dropdown').style.display = 'none';
            alert('Your changes have been saved successfully.');
        } else {
            alert('An error occurred while saving your changes. Please try again.');
        }
    })
    .catch(error => {
        alert('An error occurred while saving your changes. Please try again.');
    });
}