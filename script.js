// Dynamic Surveillance Intelligence Logic

document.addEventListener('DOMContentLoaded', () => {
    initDashboard();
});

function initDashboard() {
    updateDateTime();
    startSimulation();
    animateDetectionBoxes();
    
    // Refresh date every minute
    setInterval(updateDateTime, 60000);
}

// 1. Live Clock Logic
function updateDateTime() {
    const now = new Date();
    const options = { month: 'long', day: 'numeric', year: 'numeric' };
    const dateText = now.toLocaleDateString('en-US', options);
    const timeText = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
    
    document.getElementById('current-date').innerHTML = `${dateText} • ${timeText}`;
}

// 2. Simulated Data Stream
function startSimulation() {
    let vehicleCount = 1428;
    let violationCount = 42;
    
    // Update counters randomly
    setInterval(() => {
        // Vehicles go up consistently
        if (Math.random() > 0.3) {
            vehicleCount += Math.floor(Math.random() * 3) + 1;
            document.getElementById('count-vehicles').innerText = vehicleCount.toLocaleString();
            
            // Sometimes a violation happens
            if (Math.random() > 0.85) {
                violationCount++;
                document.getElementById('count-violations').innerText = violationCount;
                addViolationAlert();
            }
        }
    }, 2000);
}

// 3. Animated Detection Overlay Logic
function animateDetectionBoxes() {
    const detectionLayer = document.getElementById('detection-layer');
    const container = document.getElementById('video-placeholder');
    
    // Create extra boxes
    const boxes = [
        { el: null, x: 200, y: 150, type: 'CAR [82%]', color: '#00f2fe' },
        { el: null, x: 500, y: 300, type: 'BIKE [94%]', color: '#9d50bb' },
        { el: null, x: 100, y: 400, type: 'TRUCK [76%]', color: '#00f2fe' }
    ];

    boxes.forEach(box => {
        const div = document.createElement('div');
        div.className = 'detection-box';
        div.style.borderColor = box.color;
        div.innerHTML = `<div class="detection-label" style="background: ${box.color}">${box.type}</div>`;
        detectionLayer.appendChild(div);
        box.el = div;
    });

    // Move boxes to simulate tracking
    setInterval(() => {
        boxes.forEach(box => {
            box.x += (Math.random() - 0.5) * 40; // Horizontal jitter
            box.y += (Math.random() - 0.5) * 10; // Slight vertical jitter
            
            // Keep boxes in bounds
            if (box.x < 50) box.x = 50;
            if (box.x > 700) box.x = 700;
            if (box.y < 100) box.y = 100;
            if (box.y > 450) box.y = 450;

            box.el.style.left = box.x + 'px';
            box.el.style.top = box.y + 'px';
            box.el.style.width = (100 + Math.random() * 20) + 'px';
            box.el.style.height = (70 + Math.random() * 10) + 'px';
        });
    }, 200);
}

// 4. Dynamic Alert Feed
function addViolationAlert() {
    const list = document.getElementById('violation-list');
    const types = ['Red Light', 'Overspeeding', 'No Helmet', 'Wrong Lane'];
    const plates = ['XY-300', 'MN-442', 'BZ-109', 'LP-772'];
    
    const type = types[Math.floor(Math.random() * types.length)];
    const plate = plates[Math.floor(Math.random() * plates.length)];
    const time = new Date().toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit' });

    const item = document.createElement('div');
    item.className = 'v-item';
    item.style.opacity = '0';
    item.style.transform = 'translateY(-10px)';
    item.style.transition = 'all 0.5s ease';
    
    item.innerHTML = `
        <div class="v-info">
            <h4 style="color: var(--danger);">${type} Alert</h4>
            <p>Vehicle: ${plate} • ${time}</p>
        </div>
        <span class="v-tag">NEW EVENT</span>
    `;

    list.prepend(item);
    
    // Animation in
    setTimeout(() => {
        item.style.opacity = '1';
        item.style.transform = 'translateY(0)';
    }, 50);

    // Remove oldest if too many
    if (list.children.length > 5) {
        list.removeChild(list.lastElementChild);
    }
}
