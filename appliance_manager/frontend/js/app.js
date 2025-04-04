// API base URL - change this to your backend API URL when deployed
const API_BASE_URL = 'http://localhost:8000/api';

// DOM Elements
let replacementTable;
let modalOverlay;
let selectedReplacementOption = null;
let selectedDate = null;
let selectedHour = 10;
let selectedMinute = 30;

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    replacementTable = document.getElementById('replacement-table-body');
    modalOverlay = document.getElementById('modal-overlay');
    
    // Load replacement options
    loadReplacementOptions();
    
    // Set up event listeners
    setupEventListeners();
});

// Load replacement options from the API
async function loadReplacementOptions() {
    try {
        // In a real application, you would fetch this from the API
        // const response = await fetch(`${API_BASE_URL}/appliances/1/replacement-options/`);
        // const data = await response.json();
        
        // For demo purposes, we'll use hardcoded data that matches our mockup
        const data = [
            {
                id: 1,
                appliance_type: 'washing_machine',
                brand: 'Bosch',
                model: '95I/LPQ',
                price: 3456.00,
                efficiency: 'moderate',
                efficiency_display: 'Moderate',
                matching_score: 100,
                image_url: 'https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcReSzpRzF7VdK2gcKl8MS76x0CCu0WEWyGIEFTxQ74ltm-tSm7Q6eez9Scm3vOHrMg-rGnr54f9K-Z7uhv3Dbw0Jcs2oF_BTmFtaMsb-8JyJZk1HU07Nbph-fK3u87ZCDU9&usqp=CAc'
            },
            {
                id: 2,
                appliance_type: 'washing_machine',
                brand: 'Samsung',
                model: 'LIK889',
                price: 4078.00,
                efficiency: 'very_high',
                efficiency_display: 'Very High',
                matching_score: 98,
                image_url: 'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcQvBQzZ_2D1YdMwxM_SwKjYMJuOudNuT8WgWLfKho7NPg4CmUzP2ofnUBCWyxTF4SaLOSOOYGuQFghuZIw39SafMB7betgpcyAve1EF50IfZtNrxUJn&usqp=CAc'
            },
            {
                id: 3,
                appliance_type: 'washing_machine',
                brand: 'IFB',
                model: 'IF778',
                price: 4431.00,
                efficiency: 'high',
                efficiency_display: 'High',
                matching_score: 70,
                image_url: 'https://encrypted-tbn2.gstatic.com/shopping?q=tbn:ANd9GcSdVHGrx_sjMvZ2kJSU7Cqd0rnNpm36LBn61jSVGZS6k1wfQ2yeOw7-PeFx1Yn7I2wdl8hnxUNZQxVvY08Tl-ENNMLaafTIloV-ue1OZ_FWLd80FFoV-p6bHkDh0IXv3U2M&usqp=CAc'
            },
            {
                id: 4,
                appliance_type: 'washing_machine',
                brand: 'LG',
                model: 'LG5677',
                price: 3549.00,
                efficiency: 'good',
                efficiency_display: 'Good',
                matching_score: 90,
                image_url: 'https://encrypted-tbn0.gstatic.com/shopping?q=tbn:ANd9GcQL-cLtk64kemtK74C9AmUptld_PyapT-gQWyGUEW9ZiSIFLFqogTCL22_ym7qr-ctY6dTTCOr8mOgD5K5TeZhBGVoG3QmWMlY8M7nvzxZhK1DY93HYnETx3eLDcWHiSXPO1Q&usqp=CAc'
            }
        ];
        
        renderReplacementOptions(data);
    } catch (error) {
        console.error('Error loading replacement options:', error);
    }
}

// Render replacement options in the table
function renderReplacementOptions(options) {
    replacementTable.innerHTML = '';
    
    options.forEach(option => {
        const row = document.createElement('tr');
        
        row.innerHTML = `
            <td>Washing machine</td>
            <td>${option.brand}</td>
            <td>${option.model}</td>
            <td>$${option.price.toFixed(2)}</td>
            <td>${option.efficiency_display}</td>
            <td>${option.matching_score}%</td>
            <td><img src="${option.image_url}" alt="${option.brand} ${option.model}" class="appliance-image"></td>
            <td><button class="order-button" data-id="${option.id}">Order</button></td>
        `;
        
        replacementTable.appendChild(row);
    });
    
    // Add event listeners to order buttons
    document.querySelectorAll('.order-button').forEach(button => {
        button.addEventListener('click', handleOrderButtonClick);
    });
}

// Handle order button click
function handleOrderButtonClick(event) {
    const optionId = event.target.getAttribute('data-id');
    selectedReplacementOption = parseInt(optionId);
    
    // Update the modal with the selected option details
    updateModalWithOptionDetails(selectedReplacementOption);
    
    // Show the modal
    modalOverlay.style.display = 'flex';
}

// Update modal with selected option details
function updateModalWithOptionDetails(optionId) {
    // In a real application, you would fetch the details from your data
    // For demo purposes, we'll use hardcoded data
    const options = [
        {
            id: 1,
            brand: 'Bosch',
            model: '95I/LPQ',
            price: 3456.00,
            efficiency: 'Moderate',
            matching_score: 100
        },
        {
            id: 2,
            brand: 'Samsung',
            model: 'LIK889',
            price: 4078.00,
            efficiency: 'Very High',
            matching_score: 98
        },
        {
            id: 3,
            brand: 'IFB',
            model: 'IF778',
            price: 4431.00,
            efficiency: 'High',
            matching_score: 70
        },
        {
            id: 4,
            brand: 'LG',
            model: 'LG5677',
            price: 3549.00,
            efficiency: 'Good',
            matching_score: 90
        }
    ];
    
    const selectedOption = options.find(option => option.id === optionId);
    
    if (selectedOption) {
        document.getElementById('modal-appliance').textContent = 'Washing machine';
        document.getElementById('modal-brand').textContent = selectedOption.brand;
        document.getElementById('modal-model').textContent = selectedOption.model;
        document.getElementById('modal-cost').textContent = `$${selectedOption.price.toFixed(2)}`;
        document.getElementById('modal-efficiency').textContent = selectedOption.efficiency;
        document.getElementById('modal-matching').textContent = `${selectedOption.matching_score}%`;
    }
}

// Set up event listeners
function setupEventListeners() {
    // Close modal when clicking outside or on cancel button
    modalOverlay.addEventListener('click', event => {
        if (event.target === modalOverlay) {
            closeModal();
        }
    });
    
    document.getElementById('cancel-button').addEventListener('click', closeModal);
    
    // Handle date selection
    document.querySelectorAll('.date-option').forEach(option => {
        option.addEventListener('click', handleDateSelection);
    });
    
    // Handle time selection
    document.getElementById('hour-select').addEventListener('change', event => {
        selectedHour = parseInt(event.target.value);
    });
    
    document.getElementById('minute-select').addEventListener('change', event => {
        selectedMinute = parseInt(event.target.value);
    });
    
    // Handle form submission
    document.getElementById('confirm-button').addEventListener('click', handleOrderConfirmation);
}

// Handle date selection
function handleDateSelection(event) {
    // Remove selected class from all date options
    document.querySelectorAll('.date-option').forEach(option => {
        option.classList.remove('selected');
    });
    
    // Add selected class to clicked option
    event.currentTarget.classList.add('selected');
    
    // Store selected date
    selectedDate = event.currentTarget.getAttribute('data-date');
}

// Handle order confirmation
async function handleOrderConfirmation() {
    if (!selectedDate) {
        alert('Please select a delivery date');
        return;
    }
    
    try {
        // In a real application, you would send this data to your API
        const orderData = {
            flat: 1, // Assuming Flat 101 has ID 1
            old_appliance: 1, // Assuming the current washing machine has ID 1
            replacement_option: selectedReplacementOption,
            delivery_date: selectedDate,
            delivery_time_hour: selectedHour,
            delivery_time_minute: selectedMinute,
            notification_email: document.getElementById('notification-toggle').checked ? 'user@example.com' : null,
            notification_phone: document.getElementById('notification-toggle').checked ? '+1234567890' : null
        };
        
        console.log('Order data:', orderData);
        
        // For demo purposes, we'll just log the data and close the modal
        // In a real application, you would send this to your API
        // const response = await fetch(`${API_BASE_URL}/orders/`, {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify(orderData)
        // });
        // const data = await response.json();
        
        // Show success message
        alert('Order placed successfully!');
        
        // Close the modal
        closeModal();
    } catch (error) {
        console.error('Error placing order:', error);
        alert('Error placing order. Please try again.');
    }
}

// Close the modal
function closeModal() {
    modalOverlay.style.display = 'none';
    selectedReplacementOption = null;
    selectedDate = null;
    
    // Reset date selection
    document.querySelectorAll('.date-option').forEach(option => {
        option.classList.remove('selected');
    });
}

// Helper function to format date
function formatDate(date) {
    const options = { weekday: 'short', month: 'short', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}

// Generate dates for the next few days
function generateDates() {
    const today = new Date();
    const dates = [];
    
    for (let i = 0; i < 3; i++) {
        const date = new Date(today);
        date.setDate(today.getDate() + i + 1);
        dates.push({
            date: date.toISOString().split('T')[0],
            display: formatDate(date)
        });
    }
    
    return dates;
}