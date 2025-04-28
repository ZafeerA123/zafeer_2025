---
layout: post
title: Energy Tracker 💪
description: Final PPR Project – Energy Tracker 
type: post
comments: true
permalink: Final
categories: [Final Project]
---

<html lang="en">
<head>
    <title>Fitness Tracker Simulator</title>
    <style>
        body {
            font-family: 'Orbitron', sans-serif;
            background: linear-gradient(135deg, #5ee7df, #b490ca);
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
            color: white;
        }
        .main-content {
            display: flex;
            justify-content: center;
            align-items: flex-start;
            flex: 1;
            padding: 20px;
        }
        h1 {
            font-size: 2.5rem;
            margin-bottom: 20px;
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 10px;
            border-radius: 10px;
        }
        .container {
            background: rgba(0,0,0,0.7);
            padding: 2rem;
            border-radius: 20px;
            width: 500px;
            max-width: 100%;
            text-align: center;
            margin: 20px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
        }
        .inputs-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            margin-bottom: 1rem;
        }
        input, select {
            padding: 10px;
            width: 100%;
            border-radius: 5px;
            border: none;
            font-size: 1rem;
            margin: 5px 0;
        }
        button {
            background: #5ee7df;
            color: black;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            margin: 5px;
            transition: background 0.3s ease;
        }
        button:hover {
            background: #3dcfc1;
        }
        .bar {
            height: 25px;
            background: #4caf50;
            margin: 20px auto;
            border-radius: 5px;
            transition: width 0.5s ease;
            box-shadow: inset 0 0 5px rgba(0,0,0,0.5);
            width: 80%;
        }
        .history {
            display: flex;
            overflow-x: auto;
            margin: 20px 0;
            background: rgba(255,255,255,0.1);
            padding: 10px;
            border-radius: 10px;
        }
        .history div {
            min-width: 100px;
            margin: 0 5px;
            background: rgba(0,0,0,0.5);
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            box-shadow: 0 0 5px rgba(0,0,0,0.2);
        }
        .sidebar {
            background: rgba(0,0,0,0.85);
            padding: 1.5rem;
            border-radius: 20px;
            width: 300px;
            margin: 20px;
            box-shadow: 0 0 15px rgba(0,0,0,0.3);
        }
        .sidebar h2 {
            font-size: 1.5rem;
            margin-bottom: 10px;
            text-align: center;
        }
        .action-list {
            margin-top: 10px;
            max-height: 400px;
            overflow-y: auto;
        }
        .action-item {
            margin: 8px 0;
            background: rgba(255,255,255,0.1);
            padding: 8px;
            border-radius: 5px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .action-item span {
            flex: 1;
        }
        footer {
            text-align: center;
            padding: 10px;
            font-size: 0.9rem;
            background: rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <div class="main-content">
        <div class="container">
            <div class="inputs-grid" id="inputsGrid">
                <input type="number" id="exercise" placeholder="Exercise Hours (0-5)">
                <input type="number" id="sleep" placeholder="Sleep Hours (0-12)">
                <input type="number" id="water" placeholder="Water (cups)">
                <input type="number" id="calories" placeholder="Calories Eaten">
                <select id="mood">
                    <option>Happy</option>
                    <option>Neutral</option>
                    <option>Stressed</option>
                </select>
            </div>
            <button id="completeDay" style="display:none;">Complete Day</button>
            <button id="start">Start Day</button>
            <div id="stats"></div>
            <div id="bar" class="bar"></div>
            <button id="nextDay" style="display:none;">Next Day</button>
            <button id="reset">Reset</button>
            <div class="history" id="historyView"></div>
        </div>
        <div class="sidebar">
            <h2>Additional Actions ⚡</h2>
            <button id="addAction">Add Action</button>
            <div class="action-list" id="actionList"></div>
        </div>
    </div>
</body>
</html>


<script type="module">
// Data structure for tracking fitness stats
let fitness = { exercise: 0, sleep: 0, water: 0, calories: 0, mood: '', day: 0, energy: 100 };
let energyHistory = []; // List to track daily energy values
let customActions = []; // List to store custom user-defined actions

// Student-Developed Procedure
function calculateEnergyChange(exercise, sleep, water, calories, mood) {
    let change = 0;
    if (sleep >= 7 && sleep <= 12) change += 15; // Sleep logic
    else if (sleep < 5) change -= 15;

   if (exercise >= 1 && exercise <= 5) {
        change += 10;
    } else if (exercise > 5 || exercise < 1) {
        change -= 10;
    }

    if (water >= 6) change += 10;
    else change -= 10;

    if (calories < 1500) {
        change -= 10; 
    } else if (calories > 3000) {
        change -= 10; 
    } else {
        change += 10; 
    }


    if (mood === "Happy") change += 10;
    if (mood === "Stressed") change -= 10;
    if (mood === "Neutral") change -= 0;

    // Iterate through custom actions to boost energy
    customActions.forEach(action => {
        if (action.autoApply) {
            change += action.boost;
        }
    });

    return change;
}

// Apply calculated energy change and update stats
function applyDailyUpdate() {
    const change = calculateEnergyChange(fitness.exercise, fitness.sleep, fitness.water, fitness.calories, fitness.mood);
    fitness.energy = Math.max(0, Math.min(100, fitness.energy + change));
    fitness.day++;
    energyHistory.push(fitness.energy);
    updateStats();
}

// Update UI Stats
function updateStats() {
    stats.innerHTML = `Day ${fitness.day}<br>Energy: ${fitness.energy}%`;
    bar.style.width = fitness.energy + '%';
    bar.style.background = fitness.energy > 70 ? '#4caf50' : fitness.energy > 40 ? '#ff9800' : '#f44336';
    renderHistory();
}

// Render History from energyHistory list
function renderHistory() {
    historyView.innerHTML = '';
    energyHistory.forEach((val, idx) => {
        let d = document.createElement('div');
        d.innerText = `Day ${idx + 1}: ${val}%`;
        historyView.appendChild(d);
    });
}

// Render Custom Actions
function renderActions() {
    actionList.innerHTML = '';
    customActions.forEach((act, idx) => {
        let div = document.createElement('div');
        div.className = 'action-item';
        div.innerHTML = `
            <span>${act.name} (+${act.boost}%)</span> 
            <button onclick="applyAction(${idx})">Use</button> 
            <button onclick="editAction(${idx})">✎</button> 
            <button onclick="deleteAction(${idx})">🗑</button>
        `;
        actionList.appendChild(div);
    });
}

function startDay() {
    start.style.display = 'none';
    inputsGrid.style.display = 'grid';
    completeDay.style.display = 'inline';
}

// Complete Day: gather input, update energy, show Next Day
function completeDayFunc() {
    let e = +exercise.value, s = +sleep.value, w = +water.value, c = +calories.value, m = mood.value;
    if ([e, s, w, c].some(isNaN) || !m) return alert("Fill all fields correctly!");

    fitness = { exercise: e, sleep: s, water: w, calories: c, mood: m, day: 1, energy: 100 };
    energyHistory = [100];

    applyDailyUpdate();

    inputsGrid.style.display = 'none';
    completeDay.style.display = 'none';
    nextDay.style.display = 'inline';
}

// Move to next day and update stats using procedure
function nextDayFunc() {
    let e = +prompt("Exercise Hours (0-5):", fitness.exercise);
    let s = +prompt("Sleep Hours (0-12):", fitness.sleep);
    let w = +prompt("Water (cups):", fitness.water);
    let c = +prompt("Calories Eaten:", fitness.calories);
    let m = prompt("Mood (Happy/Neutral/Stressed):", fitness.mood);

    if ([e, s, w, c].some(isNaN) || !["Happy", "Neutral", "Stressed"].includes(m)) {
        alert("Invalid input! Keeping previous values.");
    } else {
        fitness.exercise = e;
        fitness.sleep = s;
        fitness.water = w;
        fitness.calories = c;
        fitness.mood = m;
    }

    applyDailyUpdate();
}

// Event Listeners
start.onclick = startDay;
completeDay.onclick = completeDayFunc;
nextDay.onclick = nextDayFunc;
reset.onclick = () => { location.reload(); };


// Apply a custom action and use the list
window.applyAction = function (idx) {
    let boost = customActions[idx].boost;
    fitness.energy = Math.min(100, fitness.energy + boost);
    fitness.day++;
    energyHistory.push(fitness.energy);
    updateStats();
}

// Edit an action from the list
window.editAction = function (idx) {
    let name = prompt("Edit action name:", customActions[idx].name);
    let boost = parseInt(prompt("Edit energy boost %:", customActions[idx].boost));
    let autoApply = confirm("Should this action auto-apply daily?");
    if (!name || isNaN(boost)) return;
    customActions[idx] = { name, boost, autoApply };
    renderActions();
}

// Delete an action from the list
window.deleteAction = function (idx) {
    customActions.splice(idx, 1);
    renderActions();
}

// Add new custom actions to the list
addAction.onclick = () => {
    let name = prompt("Enter action name:");
    let boost = parseInt(prompt("Enter energy boost %:"));
    let autoApply = confirm("Should this action auto-apply daily?");
    if (!name || isNaN(boost)) return;
    customActions.push({ name, boost, autoApply }); // Store data in list
    renderActions();
}

</script>
