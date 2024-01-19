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
        specialties.textContent = 'Specialties: ' + (result.specialties || 'None');

        // Create and add the location paragraph
        var location = document.createElement('p');
        location.textContent = 'Location: ' + result.location;

        // Create and add the languages paragraph
        var languages = document.createElement('p');
        var languagesSpoken = Array.isArray(result.languages) ? result.languages.join(', ') : 'None';
        languages.textContent = 'Languages Spoken: ' + languagesSpoken;

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
        document.getElementById('details-provider-specialities').textContent = provider.speciality || 'N/A';
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


    });
}

        
        /*if (provider.profile_picture) {
            document.getElementById('details-provider-profile_picture').src = provider.profile_picture;
            document.getElementById('details-provider-profile_picture').alt = 'Profile picture of ' + provider.name;
        } else {
            document.getElementById('details-provider-profile_picture').src = 'path/to/default_profile_picture.jpg'; // Path to a default image
            document.getElementById('details-provider-profile_picture').alt = 'Default profile picture';
        }

        // Make sure to handle any buttons or links that need to be updated with dynamic data
        // For example:
        // document.getElementById('email-button').href = `mailto:${provider.email}`;
        // document.getElementById('phone-button').href = `tel:${provider.phone_number}`;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to load provider details.');
    });
}*/