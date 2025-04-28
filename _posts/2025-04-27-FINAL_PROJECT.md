---
layout: post
title: World Builder
description: Final PPR Project – World Builder
type: post
comments: true
permalink: Final
categories: [Final Project]
---

<html lang="en">
    <title>World Builder</title>
    <style>
        body {
            font-family: 'Orbitron', sans-serif;
            background: linear-gradient(135deg, #5ee7df, #b490ca);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            color: white;
            transition: background 1s ease;
            position: relative;
        }
        body::before {
            content: '';
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background: url('https://www.transparenttextures.com/patterns/stardust.png');
            animation: moveBg 30s linear infinite;
            z-index: -1;
        }
        @keyframes moveBg {
            0% { background-position: 0 0; }
            100% { background-position: 1000px 1000px; }
        }
        .container {
            background: rgba(0, 0, 0, 0.7);
            padding: 2rem;
            border-radius: 20px;
            width: 90%;
            max-width: 800px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
            opacity: 0;
            transform: translateY(-20px);
            animation: fadeIn 1s ease forwards;
        }
        @keyframes fadeIn {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        .inputs-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 1rem;
            width: 100%;
            margin: auto;
        }
        .input-wrapper {
            position: relative;
            width: 100%;
        }
        .input-wrapper i {
            position: absolute;
            top: 50%;
            left: 10px;
            transform: translateY(-50%);
            color: #ccc;
        }
        .input-wrapper input, .input-wrapper select {
            padding: 10px 10px 10px 35px;
            margin: 10px 0;
            width: 100%;
            border-radius: 5px;
            border: none;
            font-size: 1rem;
        }
        button {
            background: #5ee7df;
            color: black;
            border: none;
            padding: 10px 20px;
            margin: 10px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            transition: background 0.3s, transform 0.3s;
            box-shadow: 0 0 10px #5ee7df, 0 0 20px #b490ca;
        }
        button:hover {
            background: #4dd0e1;
            transform: scale(1.05);
            animation: pulse 1s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        .world-stats, #history-log {
            margin-top: 20px;
            text-align: left;
        }
        .bar {
            height: 20px;
            background: #4caf50;
            margin: 10px 0;
            border-radius: 5px;
            transition: width 0.5s ease, background 0.5s ease;
        }
        .night {
            background: linear-gradient(135deg, #2c3e50, #4ca1af) !important;
        }
        #notification {
            transition: opacity 0.5s ease, transform 0.5s ease;
            transform: translateY(0);
        }
        #notification.show {
            transform: translateY(-10px);
        }
    </style>
<body>
    <div id="notification" style="display:none; position:fixed; bottom:20px; right:20px; background:rgba(0,0,0,0.8); color:white; padding:15px 20px; border-radius:10px; font-family:Orbitron, sans-serif; box-shadow:0 0 15px rgba(0,0,0,0.5); z-index:9999; max-width:300px;"></div>
    <div class="container">
        <h1>World Builder 🌍</h1>
        <div class="inputs-grid">
            <div class="input-wrapper">
                <i class="fas fa-mountain"></i>
                <input type="number" id="land-input" min="1" max="10" placeholder="Land Amount">
            </div>
            <div class="input-wrapper">
                <i class="fas fa-water"></i>
                <input type="number" id="water-input" min="1" max="10" placeholder="Water Amount">
            </div>
            <div class="input-wrapper">
                <i class="fas fa-leaf"></i>
                <input type="number" id="plants-input" min="1" max="10" placeholder="Plant Amount">
            </div>
            <div class="input-wrapper">
                <i class="fas fa-paw"></i>
                <input type="number" id="animals-input" min="0" max="20" placeholder="Number of Animals">
            </div>
            <div class="input-wrapper">
                <i class="fas fa-thermometer-half"></i>
                <input type="number" id="temp-input" min="-10" max="40" placeholder="Temperature (C)">
            </div>
            <div class="input-wrapper">
                <i class="fas fa-cloud-sun"></i>
                <select id="weather-select">
                    <option value="Sunny">Sunny</option>
                    <option value="Rainy">Rainy</option>
                    <option value="Stormy">Stormy</option>
                </select>
            </div>
        </div>
        <button id="build-world-btn">Build World</button>
        <div class="world-stats" id="world-stats"></div>
        <div id="balance-bar" class="bar"></div>
        <button id="next-day-btn" class="hidden">Next Day</button>
        <button id="intervene-btn" class="hidden">Take Action</button>
        <div id="history-log"></div>
        <audio id="build-sound" src="build.mp3"></audio>
        <audio id="disaster-sound" src="disaster.mp3"></audio>
        <button id="reset-world-btn">Reset World</button>
    </div>

<script type="module">
        let world = { land: 0, water: 0, plants: 0, animals: 0, temperature: 20, weather: '', day: 0, health: 100, events: [] };
        let worldHistory = [];

        let dailyHealthHistory = [];
        dailyHealthHistory.push(world.health);

        if (dailyHealthHistory.length >= 3) {
                let last3 = dailyHealthHistory.slice(-3);
                let avg = last3.reduce((a, b) => a + b, 0) / 3;
                if (avg < 40) {
                    world.health += 5;
                    events.push("Recent recovery efforts have slightly boosted health.");
                }
            }


        const landInput = document.getElementById('land-input');
        const waterInput = document.getElementById('water-input');
        const plantsInput = document.getElementById('plants-input');
        const animalsInput = document.getElementById('animals-input');
        const tempInput = document.getElementById('temp-input');
        const weatherSelect = document.getElementById('weather-select');
        const buildWorldBtn = document.getElementById('build-world-btn');
        const worldStats = document.getElementById('world-stats');
        const balanceBar = document.getElementById('balance-bar');
        const nextDayBtn = document.getElementById('next-day-btn');
        const interveneBtn = document.getElementById('intervene-btn');
        const historyLog = document.getElementById('history-log');
        const buildSound = document.getElementById('build-sound');
        const disasterSound = document.getElementById('disaster-sound');

        buildWorldBtn.addEventListener('click', () => {
            const land = parseInt(landInput.value);
            const water = parseInt(waterInput.value);
            const plants = parseInt(plantsInput.value);
            const animals = parseInt(animalsInput.value);
            const temp = parseInt(tempInput.value);
            const weather = weatherSelect.value;


            if ([land, water, plants, animals, temp].some(isNaN)) {
                alert("Please fill all fields correctly!");
                return;
            }

            initializeWorld(land, water, plants, animals, temp, weather);
        });

        nextDayBtn.addEventListener('click', () => {
            simulateDay();
        });

        interveneBtn.addEventListener('click', () => {
            takeAction();
        });

        function initializeWorld(land, water, plants, animals, temp, weather) {
            world = { land, water, plants, animals, temperature: temp, weather, day: 1, health: 100 };
            worldHistory = [{...world}];
            displayWorld();
            updateBalanceBar();
            nextDayBtn.classList.remove('hidden');
            interveneBtn.classList.remove('hidden');
            historyLog.innerHTML = '';
        }

        function displayWorld() {
            worldStats.innerHTML = `
                <h2>Day ${world.day}</h2>
                <p>Land: ${world.land}</p>
                <p>Water: ${world.water}</p>
                <p>Plants: ${world.plants}</p>
                <p>Animals: ${world.animals}</p>
                <p>Temperature: ${world.temperature}°C</p>
                <p>Weather: ${world.weather}</p>
                <p>World Health: ${world.health}%</p>
            `;
        }

        function updateBalanceBar() {
            balanceBar.style.width = `${world.health}%`;
            if (world.health > 70) {
                balanceBar.style.background = '#4caf50';
            } else if (world.health > 40) {
                balanceBar.style.background = '#ff9800';
            } else {
                balanceBar.style.background = '#f44336';
            }
            updateBackground();
        }

        function updateBackground() {
            if (world.health > 70) {
                document.body.style.background = 'linear-gradient(135deg, #5ee7df, #b490ca)';
            } else if (world.health > 40) {
                document.body.style.background = 'linear-gradient(135deg, #ffb347, #ffcc33)';
            } else {
                document.body.style.background = 'linear-gradient(135deg, #ff6e7f, #bfe9ff)';
            }
        }

        const disasters = [
            { name: "Wildfire", healthImpact: -15, effect: (world) => { world.plants = Math.max(0, world.plants - 2); } },
            { name: "Flood", healthImpact: -10, effect: (world) => { world.water += 2; world.land = Math.max(0, world.land - 2); } },
            { name: "Drought", healthImpact: -12, effect: (world) => { world.plants = Math.max(0, world.plants - 3); world.water = Math.max(0, world.water - 1); } },
            { name: "Cold Snap", healthImpact: -8, effect: (world) => { world.temperature -= 5; } },
            { name: "Heat Wave", healthImpact: -10, effect: (world) => { world.temperature += 5; world.water = Math.max(0, world.water - 2); } }
        ];

        function simulateDay() {
            let events = [];
            world.day++;

            // Random weather/temperature change
            const oldTemp = world.temperature;
            world.temperature += Math.floor(Math.random() * 3 - 1);
            if (world.temperature !== oldTemp) {
                events.push(`Temperature changed from ${oldTemp}°C to ${world.temperature}°C`);
            }

            const oldWeather = world.weather;
            const weathers = ["Sunny", "Rainy", "Stormy"];
            if (Math.random() < 0.2) {
                world.weather = weathers[Math.floor(Math.random() * weathers.length)];
                if (world.weather !== oldWeather) {
                    events.push(`Weather changed to ${world.weather}`);
                }
            }

            let healthChange = 0;

            // Random Disaster
            if (Math.random() < 0.3) {
                let disaster = disasters[Math.floor(Math.random() * disasters.length)];
                processDisaster(disaster, world);
                events.push(`${disaster.name} affected the world`);
            }

            // Plant vs Animal ratio
            let plantAnimalRatio = world.plants / (world.animals || 1);
            if (plantAnimalRatio < 0.5) {
                healthChange -= 8;
                events.push("Too many animals and not enough plants caused stress.");
            } else if (plantAnimalRatio > 2) {
                healthChange += 5;
                events.push("Plenty of plants supported the ecosystem.");
            }

            // Temperature effect
            if (world.temperature >= 15 && world.temperature <= 25) {
                adjustWorldHealth(5, "Ideal temperature");
            } else if (world.temperature < 10 || world.temperature > 30) {
                healthChange -= 7;
                events.push("Extreme temperature harmed life.");
            }

            // Water effects
            if (world.water < 2) {
                healthChange -= 7;
                events.push("Low water levels caused drought stress.");
            } else if (world.water > 9) {
                healthChange -= 5;
                events.push("Too much water led to flooding.");
            } else if (world.weather === "Rainy") {
                world.plants += 1;
                healthChange += 3;
                events.push("Rain helped plants grow.");
            }

            // Random Positive Event
            if (Math.random() < 0.2) {
                healthChange += 5;
                world.plants += 1;
                showNotification("🌸 Natural bloom! Plants are thriving.");
            }

            // Animal Disease Example
            if (Math.random() < 0.1 && world.animals > 0) {
                const deadAnimals = Math.min(2, world.animals);
                world.animals -= deadAnimals;
                healthChange -= 5;
                events.push(`${deadAnimals} animals died from disease.`);
            }

            // Clamp health
            world.health += healthChange;
            world.health = Math.max(0, Math.min(100, world.health));

            document.body.classList.toggle('night', world.day % 2 === 0);

            world.events.push({ day: world.day, summary: events });


            worldHistory.push({...world});
            displayWorld();
            updateBalanceBar();
            displayDailySummary(healthChange, events);

            if (world.day > 10) {
                nextDayBtn.disabled = true;
                interveneBtn.disabled = true;
                calculateScore();
            }

            let balanceResult = evaluatePlantAnimalBalance(world.plants, world.animals);
            healthChange += balanceResult.healthImpact;
            events = events.concat(balanceResult.events);

            updateHistoryLog();  
        }




        function processDisaster(disaster, world) {
            if (disaster && disaster.effect) {
                world.health += disaster.healthImpact;
                disaster.effect(world);
                showNotification(`${disaster.name} occurred! Health and resources adjusted.`);
            }

            worldHistory.slice(-3).forEach((entry) => {
                console.log(`Log - Day ${entry.day}: Health=${entry.health}%, Plants=${entry.plants}`);
            });
        }



        function takeAction() {
            if (world.health < 50) {
                world.health += 10;
                world.plants += 1;
                world.animals = Math.max(0, world.animals - 1);
                showNotification("🌳 You planted trees and moved animals. Balance improved!");
                displayWorld();
                updateBalanceBar();
            } else {
                alert("World is stable, no action needed now.");
            }
        }

        function evaluatePlantAnimalBalance(plants, animals) {
            let healthImpact = 0;
            let events = [];

            let ratio = plants / (animals || 1);
            if (ratio < 0.5) {
                healthImpact -= 8;
                events.push("Too many animals and not enough plants caused stress.");
            } else if (ratio > 2) {
                healthImpact += 5;
                events.push("Plenty of plants supported the ecosystem.");
            }

            if (dailyHealthHistory.length >= 3) {
                let stressDays = 0;
                world.events.slice(-3).forEach(event => {
                    if (event.summary.includes("Too many animals and not enough plants caused stress.")) {
                        stressDays++;
                    }
                });
                if (stressDays >= 2) {
                    adjustWorldHealth(-5, "Ongoing stress");
                }
            }

            return { healthImpact, events };
        }



        function displayDailySummary(healthChange, events) {
            let summary = `<h3>Day ${world.day} Summary:</h3>`;
            summary += `<p>Health Change: ${healthChange > 0 ? '+' : ''}${healthChange}%</p>`;
            events.forEach(event => {
                summary += `<p>${event}</p>`;
            });
            historyLog.innerHTML = summary + historyLog.innerHTML; // show newest first
        }


        function updateHistoryLog() {
            let logHTML = "<h3>Last 3 Days:</h3>";
            world.events.slice(-3).forEach((entry) => {
                logHTML += `<p>Day ${entry.day}: ${entry.summary.join(", ")}</p>`;
            });
            historyLog.innerHTML = logHTML;
        }


        function calculateScore() {
            let avgHealth = worldHistory.reduce((sum, day) => sum + day.health, 0) / worldHistory.length;
            alert(`Simulation Complete! Your World Balance Score: ${Math.round(avgHealth)}%`);
        }
    
        const resetWorldBtn = document.getElementById('reset-world-btn');

    resetWorldBtn.addEventListener('click', () => {
        // Reset world state
        world = { land: 0, water: 0, plants: 0, animals: 0, temperature: 20, weather: '', day: 0, health: 100 };
        worldHistory = [];
        
        // Clear inputs
        landInput.value = '';
        waterInput.value = '';
        plantsInput.value = '';
        animalsInput.value = '';
        tempInput.value = '';
        weatherSelect.selectedIndex = 0;

        // Reset UI elements
        worldStats.innerHTML = '';
        balanceBar.style.width = '0%';
        balanceBar.style.background = '#4caf50';
        historyLog.innerHTML = '';
        nextDayBtn.classList.add('hidden');
        interveneBtn.classList.add('hidden');
        nextDayBtn.disabled = false;
        interveneBtn.disabled = false;

        // Reset background
        document.body.style.background = 'linear-gradient(135deg, #5ee7df, #b490ca)';
        document.body.classList.remove('night');
    });

    function showNotification(message) {
            const notification = document.getElementById('notification');
            notification.innerHTML = message;
            notification.style.display = 'block';
            notification.classList.add('show');
            notification.style.opacity = '1';

            setTimeout(() => {
                notification.style.opacity = '0';
                notification.classList.remove('show');
                setTimeout(() => { notification.style.display = 'none'; }, 1000);
            }, 3000);
        }
    
    function adjustWorldHealth(amount, cause) {
        world.health += amount;
        world.health = Math.max(0, Math.min(100, world.health)); // Clamp
        showNotification(`🌿 ${cause}: Health ${amount > 0 ? 'increased' : 'decreased'} by ${Math.abs(amount)}%`);
    }



    </script>
</body>
</html>